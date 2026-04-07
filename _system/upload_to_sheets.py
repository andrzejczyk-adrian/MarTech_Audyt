"""
upload_to_sheets.py — Upload danych z _wytyczne/ MD → Google Sheets
Uzywa: google-api-python-client (nie gspread)

Uruchom: python _system/upload_to_sheets.py
"""

import sys
import re
import os
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

SPREADSHEET_ID = "1n_MRlIMZpPc2MJsLMPqbb3DgMiB97pTTmjmizQh07c8"
SERVICE_ACCOUNT_FILE = str(Path(__file__).parent.parent.parent.parent / "keys" / "ai-andrzejczyk-ga4.json")
WYTYCZNE_DIR = Path(__file__).parent.parent / "_wytyczne"

FILE_TO_SHEET = {
    "01_audyt-wstepny.md": "Infrastruktura śledzenia",
    "02_eprivacy.md": "RODO i Consent Mode",
    "03_konfiguracja.md": "Konfiguracja GTM i GA4",
    "04_data-quality.md": "Jakość danych",
    "05_utm.md": "Oznaczenia UTM",
    "06_bcg.md": "Analiza produktów (BCG)",
    "07_lejki.md": "Lejki zakupowe",
    "08_ga4-ads.md": "GA4 i Google Ads",
    "09_analiza.md": "Analiza wyników",
    "10_google-ads.md": "Google Ads",
}

COLUMNS = ["id", "kryterium", "priorytet", "dotyczy",
           "jak_sprawdzic", "warunek_ok", "czerwona_flaga", "max_pkt", "uwagi"]


def get_service():
    try:
        from google.oauth2.service_account import Credentials
        from googleapiclient.discovery import build
    except ImportError:
        print("ERROR: pip install google-api-python-client google-auth")
        sys.exit(1)

    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    print(f"  Service account: {creds.service_account_email}")
    service = build("sheets", "v4", credentials=creds)
    return service


def get_sheet_ids(service):
    """Pobierz mapowanie nazwa arkusza → sheetId."""
    result = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheets = {}
    for s in result.get("sheets", []):
        title = s["properties"]["title"]
        gid = s["properties"]["sheetId"]
        sheets[title] = gid
    return sheets


def parse_md_tables(md_path: Path) -> list[list[str]]:
    """Parsuj wszystkie tabele kryteriow z pliku MD."""
    content = md_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    all_rows = []
    header_written = False
    in_criteria_table = False

    for line in lines:
        stripped = line.strip()

        if not stripped.startswith("|"):
            in_criteria_table = False
            continue

        # Separator ---
        if re.match(r'^\|[\s\-:]+\|', stripped):
            continue

        cells = [c.strip() for c in stripped.strip("|").split("|")]

        # Naglowek tabeli kryteriow
        if cells and cells[0].lower() == "id" and not in_criteria_table:
            in_criteria_table = True
            if not header_written:
                all_rows.append(COLUMNS)
                header_written = True
            continue

        if in_criteria_table and cells and cells[0]:
            row = []
            for j in range(len(COLUMNS)):
                val = cells[j] if j < len(cells) else ""
                row.append(val.replace("\\|", "|"))
            all_rows.append(row)

    return all_rows


def upload_sheet(service, sheet_name: str, rows: list[list[str]]) -> bool:
    """Wyczysc arkusz i wgraj dane przez Sheets API v4."""
    # 1. Wyczysc zakres
    service.spreadsheets().values().clear(
        spreadsheetId=SPREADSHEET_ID,
        range=f"'{sheet_name}'!A1:Z1000"
    ).execute()

    # 2. Wgraj dane
    body = {"values": rows}
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=f"'{sheet_name}'!A1",
        valueInputOption="RAW",
        body=body
    ).execute()
    return True


def main():
    print("\n" + "="*60)
    print("  Upload _wytyczne/ MD → Google Sheets (API v4)")
    print(f"  Spreadsheet ID: {SPREADSHEET_ID}")
    print("="*60 + "\n")

    service = get_service()

    try:
        sheet_ids = get_sheet_ids(service)
        print(f"  Znaleziono {len(sheet_ids)} arkuszy: {list(sheet_ids.keys())}\n")
    except Exception as e:
        print(f"ERROR połączenia z Sheets: {e}")
        sys.exit(1)

    total = 0
    for md_file, sheet_name in FILE_TO_SHEET.items():
        md_path = WYTYCZNE_DIR / md_file
        print(f"[{sheet_name}] ← {md_file}")

        if not md_path.exists():
            print(f"  SKIP: plik MD nie istnieje\n")
            continue

        if sheet_name not in sheet_ids:
            print(f"  SKIP: arkusz '{sheet_name}' nie istnieje w Sheets")
            print(f"  Utwórz arkusz o tej nazwie i uruchom ponownie\n")
            continue

        try:
            rows = parse_md_tables(md_path)
            if len(rows) <= 1:
                print(f"  WARN: brak wierszy danych\n")
                continue

            upload_sheet(service, sheet_name, rows)
            count = len(rows) - 1
            total += count
            print(f"  ✅ Wgrano {count} kryteriów\n")

        except Exception as e:
            import traceback
            print(f"  ERROR: {e}")
            traceback.print_exc()
            print()

    print("="*60)
    print(f"  GOTOWE: {total} kryteriów wgranych do Sheets")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()
