"""
sync_sheets.py — Synchronizacja Google Sheets → _wytyczne/ MD files
Uruchom: python _system/sync_sheets.py [--dry-run] [--sekcja N]

Zasada działania:
  1. Połącz się z Google Sheets (service account)
  2. Odczytaj każdy arkusz (Sekcja 1–10)
  3. Porównaj z lokalnym plikiem MD
  4. Jeśli są zmiany → zaktualizuj plik MD
  5. Wypisz raport zmian

Konfiguracja:
  - Service account: keys/ai-andrzejczyk-ga4.json
  - Spreadsheet: https://docs.google.com/spreadsheets/d/1n_MRlIMZpPc2MJsLMPqbb3DgMiB97pTTmjmizQh07c8
  - Uwaga: Udostępnij Sheets dla emaila service account (Viewer lub Editor)

Wymagania:
  pip install gspread google-auth
"""

import sys
import os
import argparse
from datetime import datetime
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# ── Konfiguracja ─────────────────────────────────────────────────────────────

SPREADSHEET_ID = "1n_MRlIMZpPc2MJsLMPqbb3DgMiB97pTTmjmizQh07c8"
SERVICE_ACCOUNT_FILE = str(Path(__file__).parent.parent.parent.parent / "keys" / "ai-andrzejczyk-ga4.json")
WYTYCZNE_DIR = Path(__file__).parent.parent / "_wytyczne"
WYKONANE_DIR = Path(__file__).parent.parent / "wykonane"

# Mapowanie: nazwa arkusza Sheets → plik MD
SHEET_TO_FILE = {
    "Infrastruktura śledzenia": "01_audyt-wstepny.md",
    "RODO i Consent Mode": "02_eprivacy.md",
    "Konfiguracja GTM i GA4": "03_konfiguracja.md",
    "Jakość danych": "04_data-quality.md",
    "Oznaczenia UTM": "05_utm.md",
    "Analiza produktów (BCG)": "06_bcg.md",
    "Lejki zakupowe": "07_lejki.md",
    "GA4 i Google Ads": "08_ga4-ads.md",
    "Analiza wyników": "09_analiza.md",
    "Google Ads": "10_google-ads.md",
}

# Kolumny wymagane w Sheets (kolejność musi się zgadzać)
REQUIRED_COLUMNS = ["id", "kryterium", "priorytet", "dotyczy",
                    "jak_sprawdzic", "warunek_ok", "czerwona_flaga", "max_pkt", "uwagi"]


# ── Google Sheets połączenie ──────────────────────────────────────────────────

def get_spreadsheet():
    """Połącz się z Google Sheets przez service account."""
    try:
        import gspread
        from google.oauth2.service_account import Credentials
    except ImportError:
        print("ERROR: Brak bibliotek. Zainstaluj: pip install gspread google-auth")
        sys.exit(1)

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly"
    ]

    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        print(f"ERROR: Brak pliku service account: {SERVICE_ACCOUNT_FILE}")
        print("  Opcja 1: Sprawdź czy plik istnieje")
        print("  Opcja 2: Użyj OAuth: zmień get_spreadsheet() na gspread.oauth()")
        sys.exit(1)

    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=scopes)
    client = gspread.authorize(creds)

    try:
        return client.open_by_key(SPREADSHEET_ID)
    except Exception as e:
        print(f"ERROR: Nie można otworzyć Sheets: {e}")
        print(f"  Upewnij się, że arkusz jest udostępniony dla: {creds.service_account_email}")
        sys.exit(1)


# ── Parser danych z Sheets ────────────────────────────────────────────────────

def parse_sheet(worksheet) -> list[dict]:
    """Parsuj arkusz Google Sheets → lista wierszy (słowniki)."""
    all_values = worksheet.get_all_values()
    if not all_values:
        return []

    # Pierwsza niepusta linia = nagłówki
    header_row = None
    data_start = 0
    for i, row in enumerate(all_values):
        if any(cell.strip() for cell in row):
            header_row = [h.strip().lower() for h in row]
            data_start = i + 1
            break

    if not header_row:
        return []

    # Sprawdź czy kolumny się zgadzają
    missing = [col for col in REQUIRED_COLUMNS if col not in header_row]
    if missing:
        print(f"  UWAGA: Brakujące kolumny: {missing}")
        print(f"  Dostępne: {header_row}")

    rows = []
    for row in all_values[data_start:]:
        if not any(cell.strip() for cell in row):
            continue  # pomiń puste wiersze
        # Dopasuj wartości do nagłówków
        row_dict = {}
        for col in REQUIRED_COLUMNS:
            idx = header_row.index(col) if col in header_row else -1
            row_dict[col] = row[idx].strip() if idx >= 0 and idx < len(row) else ""
        if row_dict.get("id"):  # tylko wiersze z ID
            rows.append(row_dict)

    return rows


# ── Generator MD ──────────────────────────────────────────────────────────────

def rows_to_md_table(rows: list[dict]) -> str:
    """Generuj tabelę MD z listy wierszy."""
    header = "| " + " | ".join(REQUIRED_COLUMNS) + " |"
    separator = "|" + "|".join(["---"] * len(REQUIRED_COLUMNS)) + "|"
    lines = [header, separator]
    for row in rows:
        values = [row.get(col, "") for col in REQUIRED_COLUMNS]
        # Escapuj pipe w wartościach
        values = [v.replace("|", "\\|") for v in values]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def update_md_file(md_path: Path, new_rows: list[dict], dry_run: bool = False) -> tuple[bool, str]:
    """
    Zaktualizuj tabelę kryteriów w pliku MD.
    Zwraca (zmieniono: bool, raport: str).
    """
    if not md_path.exists():
        print(f"  WARN: Plik nie istnieje: {md_path}")
        return False, "Plik nie istnieje"

    content = md_path.read_text(encoding="utf-8")
    new_table = rows_to_md_table(new_rows)

    # Znajdź istniejącą tabelę kryteriów (od | id | do pustej linii lub nowej sekcji)
    import re
    table_pattern = re.compile(
        r'(\| id \|.*?\n(?:\|[-| ]+\|\n)?(?:\|.*?\|\n)*)',
        re.MULTILINE
    )

    match = table_pattern.search(content)
    if not match:
        print(f"  WARN: Nie znaleziono tabeli w {md_path.name}")
        return False, "Brak tabeli w pliku"

    old_table = match.group(1).rstrip("\n")
    if old_table.strip() == new_table.strip():
        return False, "Brak zmian"

    # Oblicz diff (uproszczony)
    old_lines = set(old_table.strip().split("\n"))
    new_lines = set(new_table.strip().split("\n"))
    added = new_lines - old_lines
    removed = old_lines - new_lines
    # Pomiń linię separatora w diff
    added = {l for l in added if not l.startswith("|---")}
    removed = {l for l in removed if not l.startswith("|---")}

    report_lines = []
    if added:
        report_lines.append(f"  + Dodano/zmieniono {len(added)} wierszy")
    if removed:
        report_lines.append(f"  - Usunięto {len(removed)} wierszy")

    if not dry_run:
        new_content = content[:match.start()] + new_table + "\n" + content[match.end():]
        # Aktualizuj datę w Meta
        new_content = re.sub(
            r'(ostatnia_aktualizacja: )[\d-]+',
            f"ostatnia_aktualizacja: {datetime.now().strftime('%Y-%m')}",
            new_content
        )
        md_path.write_text(new_content, encoding="utf-8")

    return True, "\n".join(report_lines) if report_lines else "Zmieniono"


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sync Google Sheets → _wytyczne/ MD")
    parser.add_argument("--dry-run", action="store_true",
                        help="Pokaż co zostałoby zmienione bez zapisywania")
    parser.add_argument("--sekcja", type=int, metavar="N",
                        help="Synchronizuj tylko sekcję N (1–10)")
    args = parser.parse_args()

    mode = "DRY-RUN" if args.dry_run else "SYNC"
    print(f"\n{'='*60}")
    print(f"  MarTech Sheets → MD Sync ({mode})")
    print(f"  Spreadsheet: {SPREADSHEET_ID}")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")

    spreadsheet = get_spreadsheet()
    available_sheets = {ws.title: ws for ws in spreadsheet.worksheets()}

    changed_count = 0
    skipped_count = 0

    for sheet_name, md_file in SHEET_TO_FILE.items():
        # Filtruj jeśli --sekcja podana
        if args.sekcja:
            sekcja_nr = int(sheet_name.split()[-1])
            if sekcja_nr != args.sekcja:
                continue

        md_path = WYTYCZNE_DIR / md_file

        print(f"[{sheet_name}] → {md_file}")

        if sheet_name not in available_sheets:
            print(f"  SKIP: Arkusz '{sheet_name}' nie istnieje w Sheets\n")
            skipped_count += 1
            continue

        try:
            rows = parse_sheet(available_sheets[sheet_name])
            if not rows:
                print(f"  SKIP: Arkusz pusty\n")
                skipped_count += 1
                continue

            print(f"  Pobrano {len(rows)} kryteriów z Sheets")
            changed, report = update_md_file(md_path, rows, dry_run=args.dry_run)

            if changed:
                changed_count += 1
                status = "✅ ZAKTUALIZOWANO" if not args.dry_run else "📋 DO ZMIANY"
                print(f"  {status}")
            else:
                print(f"  ✓ Bez zmian")

            if report and report != "Brak zmian":
                print(f"{report}")

        except Exception as e:
            print(f"  ERROR: {e}")

        print()

    print(f"{'='*60}")
    print(f"  Podsumowanie: {changed_count} zaktualizowanych, {skipped_count} pominiętych")
    if args.dry_run:
        print(f"  (DRY-RUN — żadne pliki nie zostały zmienione)")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
