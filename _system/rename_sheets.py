"""
rename_sheets.py - Zmien nazwy arkuszy Sekcja 1-10 na przyjazne nazwy.
Uruchom: python _system/rename_sheets.py
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from pathlib import Path
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

SPREADSHEET_ID = "1n_MRlIMZpPc2MJsLMPqbb3DgMiB97pTTmjmizQh07c8"
SERVICE_ACCOUNT_FILE = str(Path(__file__).parent.parent.parent.parent / "keys" / "ai-andrzejczyk-ga4.json")

# Mapowanie stara -> nowa nazwa
RENAMES = {
    "Sekcja 1":  "Infrastruktura sledzenia",
    "Sekcja 2":  "RODO i Consent Mode",
    "Sekcja 3":  "Konfiguracja GTM i GA4",
    "Sekcja 4":  "Jakosc danych",
    "Sekcja 5":  "Oznaczenia UTM",
    "Sekcja 6":  "Analiza produktow BCG",
    "Sekcja 7":  "Lejki zakupowe",
    "Sekcja 8":  "GA4 i Google Ads",
    "Sekcja 9":  "Analiza wynikow",
    "Sekcja 10": "Google Ads",
}

creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
svc = build("sheets", "v4", credentials=creds)

info = svc.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheets = {s["properties"]["title"]: s["properties"]["sheetId"]
          for s in info.get("sheets", [])}

print("Arkusze przed zmiana:", list(sheets.keys()))

reqs = []
for old, new in RENAMES.items():
    if old in sheets:
        reqs.append({
            "updateSheetProperties": {
                "properties": {"sheetId": sheets[old], "title": new},
                "fields": "title"
            }
        })
        print(f"  -> {old} => {new}")

if reqs:
    svc.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={"requests": reqs}
    ).execute()
    print(f"OK! Zmieniono {len(reqs)} nazw arkuszy.")
else:
    print("Brak arkuszy do zmiany (moze juz przemianowane).")
