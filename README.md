# 📊 MarTech Audyt — System audytu GA4 i Google Ads

> **Autor:** Adrian Andrzejczyk  
> **Wersja:** 1.1 | Aktualizacja: 2026-04  
> **Repo:** `andrzejczyk-adrian/MarTech_Audyt`

System wieloagentowy do przeprowadzania kompleksowych audytów MarTech: GA4, GTM, Google Ads, ePrivacy, Data Quality, UTM, BCG i więcej. Zarządzany przez tryb Roo Code `📊 MarTech Audyt`.

---

## Spis treści

1. [Jak uruchomić audyt](#1-jak-uruchomić-audyt)
2. [Architektura systemu](#2-architektura-systemu)
3. [Struktura katalogów](#3-struktura-katalogów)
4. [Pipeline — 6 etapów](#4-pipeline--6-etapów)
5. [Wytyczne audytu (kryteria)](#5-wytyczne-audytu-kryteria)
6. [Google Sheets — zarządzanie kryteriami](#6-google-sheets--zarządzanie-kryteriami)
7. [GitHub — workflow zmian](#7-github--workflow-zmian)
8. [Skrypty systemowe](#8-skrypty-systemowe)
9. [Dodawanie nowych kryteriów](#9-dodawanie-nowych-kryteriów)
10. [Przykładowe audyty](#10-przykładowe-audyty)

---

## 1. Jak uruchomić audyt

### W Roo Code (VS Code)

1. Kliknij selektor trybu (lewy dolny róg) → wybierz **`📊 MarTech Audyt`**
2. Wpisz:
   ```
   /martech-audit
   ```
   lub od razu podaj klienta:
   ```
   Nowy audyt: tableforu, https://tableforu.pl, e-commerce, GA4: 123456789
   ```
3. Agent:
   - Zsynchronizuje kryteria z Google Sheets
   - Przeprowadzi przez 6 etapów z zatrzymaniem na każdym
   - Po każdym etapie wykona `git commit + push`

### Wymagane dostępy do pełnego audytu

| Dostęp | Jak uzyskać |
|--------|-------------|
| GA4 Property ID | GA4 → Admin → Właściwość → ID |
| Google Ads Customer ID | Google Ads → format `123-456-7890` |
| GTM Container ID | GTM → format `GTM-XXXXXX` |
| BigQuery dataset | GCP → format `projekt.dataset` (opcjonalne) |
| BDOS alias | Agencyjny system dostępu do kont Ads |

---

## 2. Architektura systemu

```
Google Sheets (wytyczne)           .roomodes (tryb Roo Code)
       ↓ sync_sheets.py                    ↓
_wytyczne/01-10 MD          →    📊 MarTech Audyt
       ↓                              ↓
GA4 API (mcp__ga4-analytics)      Pipeline 6 etapów
BDOS (Google Ads)                     ↓
BigQuery                     wykonane/{klient}/
       ↓                              ↓
02_findings.md               GitHub (auto push)
       ↓
_audyt.md + _podsumowanie.md
       ↓
generate_docs.py
       ↓
DOCX + PDF (2 pliki)
```

---

## 3. Struktura katalogów

```
AUDYT/MarTech/
│
├── README.md                        ← Ten plik
├── .gitignore
│
├── _system/                         ← Pliki systemowe (agent czyta)
│   ├── instrukcje-procesu.md        ← Główne instrukcje pipeline'u
│   ├── szablon-podsumowanie.md      ← Szablon raportu 2-3 str.
│   ├── wytyczne-format.md           ← Spec. formatu dla Google Sheets
│   ├── sync_sheets.py               ← Sheets → MD sync
│   ├── upload_to_sheets.py          ← MD → Sheets upload
│   └── setup_git.bat                ← Helper konfiguracji git
│
├── _wytyczne/                       ← Kryteria audytu per sekcja
│   ├── 01_audyt-wstepny.md          ← Sekcja 1: infrastruktura śledzenia
│   ├── 02_eprivacy.md               ← Sekcja 2: RODO / Consent Mode
│   ├── 03_konfiguracja.md           ← Sekcja 3: GTM + GA4 admin + BQ
│   ├── 04_data-quality.md           ← Sekcja 4: jakość danych
│   ├── 05_utm.md                    ← Sekcja 5: UTM
│   ├── 06_bcg.md                    ← Sekcja 6: macierz BCG
│   ├── 07_lejki.md                  ← Sekcja 7: lejki per kampania
│   ├── 08_ga4-ads.md                ← Sekcja 8: GA4 ↔ Google Ads
│   ├── 09_analiza.md                ← Sekcja 9: analiza danych
│   └── 10_google-ads.md             ← Sekcja 10: audyt Google Ads
│
├── wykonane/                        ← Gotowe audyty klientów
│   ├── invette/                     ← Przykładowy kompletny audyt
│   ├── aryton/
│   └── modnakiecka/
│
├── martech-audit-szablon.md         ← Szablon raportu szczegółowego
└── generate_docx.py                 ← Konwerter MD → DOCX (master)
```

---

## 4. Pipeline — 6 etapów

Każdy etap kończy się zapisem pliku i zatrzymaniem. Agent czeka na zatwierdzenie przed przejściem dalej.

| Etap | Nazwa | Output | Co robi |
|------|-------|--------|---------|
| 1 | Brief | `00_brief.md` | Zbiera dane klienta: GA4 ID, URL, typ, dostępy |
| 2 | Dane | `01_raw-data.md` | GA4 API + BDOS: zdarzenia, źródła, transakcje, kampanie |
| 3 | Audyt | `02_findings.md` | Ocena per sekcja wg kryteriów z `_wytyczne/` |
| — | Manager Review A | — | Auto-weryfikacja kompletności findings |
| 4 | Raport | `{klient}_audyt.md` | Pełny raport szczegółowy (bez ograniczeń obj.) |
| — | Manager Review B | — | Auto-weryfikacja jakości raportu |
| 5 | Podsumowanie | `{klient}_podsumowanie.md` | 2–3 str. A4 dla właściciela/dyrektora |
| 6 | DOCX | `*.docx + *.pdf` | Python: MD → DOCX + PDF (2 pliki) |

**Pliki klienta trafiają do:** `wykonane/{klient}/`

---

## 5. Wytyczne audytu (kryteria)

Każdy plik `_wytyczne/0N_*.md` zawiera tabelę kryteriów w formacie:

```
id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi
```

### Kolumna `dotyczy` — filtrowanie per klient

| Wartość | Kiedy stosować |
|---------|----------------|
| `all` | Zawsze — każdy typ biznesu |
| `ecommerce` | Tylko sklepy internetowe |
| `ads` | Tylko konta z Google Ads |
| `sgtm` | Tylko jeśli GTM Server Side wdrożony |
| `bq` | Tylko jeśli BigQuery aktywny |
| `ecommerce+ads` | E-commerce z Google Ads |

Agent automatycznie pomija kryteria gdzie `dotyczy` nie pasuje do klienta → oznacza ➖ Nie dotyczy.

### Sekcje i liczba kryteriów (łącznie: 193)

| Sekcja | Opis | Kryteria |
|--------|------|---------|
| 1 | Audyt Wstępny (GTM, DL, Clarity, integracje) | 29 |
| 2 | ePrivacy / Consent Mode | 20 |
| 3 | Konfiguracja GTM + GA4 Admin + BQ | 46 |
| 4 | Data Quality | 28 |
| 5 | UTM | 10 |
| 6 | Macierz BCG | 5 |
| 7 | Lejki per kampania | 4 |
| 8 | GA4 ↔ Google Ads | 10 |
| 9 | Analiza danych | 10 |
| 10 | Audyt Google Ads | 31 |

### System punktacji

| Priorytet | Punkty |
|-----------|--------|
| Wysoki | 3 pkt |
| Średni | 2 pkt |
| Niski | 1 pkt |
| Nie dotyczy / Brak dostępu | 0 (pomijane w mianowniku) |

Wynik sekcji = uzyskane pkt / max pkt × 100%

- **>80%** ✅ Zadowalający
- **49–80%** ⚠️ Wymaga poprawy
- **<49%** ❌ Krytyczny

---

## 6. Google Sheets — zarządzanie kryteriami

**Arkusz:** https://docs.google.com/spreadsheets/d/1n_MRlIMZpPc2MJsLMPqbb3DgMiB97pTTmjmizQh07c8

Każdy arkusz (Sekcja 1–10) odpowiada jednemu plikowi `_wytyczne/`.

### Jak dodać nowe kryterium w Sheets

1. Otwórz odpowiedni arkusz (np. Sekcja 1)
2. Dodaj nowy wiersz z **wypełnionym polem `id`** (np. `1.25`)
3. Wypełnij pozostałe kolumny
4. Przy następnym starcie audytu agent automatycznie pobierze zmianę

### Sync Sheets → MD (ręcznie)

```cmd
cd "C:\Users\adria\Documents\AI\AUDYT\MarTech"
"C:/Program Files/Python310/python.exe" _system/sync_sheets.py
```

### Upload MD → Sheets (gdy potrzebujesz nadpisać Sheets z MD)

```cmd
"C:/Program Files/Python310/python.exe" _system/upload_to_sheets.py
```

---

## 7. GitHub — workflow zmian

**Każda zmiana = commit + push (obowiązkowe)**

```cmd
cd "C:\Users\adria\Documents\AI\AUDYT\MarTech"
git add .
git commit -m "opis zmiany"
git push
```

### Przykłady dobrych commit messages

```
feat: audyt tableforu etap 3 findings
fix: poprawka kryteriow Clarity w sekcji 1
feat: nowy audyt zielony-parapet podsumowanie
update: sync wytycznych z Sheets (nowe kryteria)
docs: aktualizacja README
```

---

## 8. Skrypty systemowe

| Skrypt | Opis | Uruchomienie |
|--------|------|--------------|
| `_system/sync_sheets.py` | Sheets → MD sync (agent uruchamia auto) | `python _system/sync_sheets.py` |
| `_system/upload_to_sheets.py` | MD → Sheets upload | `python _system/upload_to_sheets.py` |
| `_system/setup_git.bat` | Konfiguracja git (pierwsze uruchomienie) | Kliknij dwukrotnie |
| `generate_docx.py` | MD → DOCX + PDF | Kopiuj do katalogu klienta, uruchom |

### Wymagania Python

```cmd
pip install gspread google-auth google-api-python-client python-docx
```

### Konfiguracja service account (Google Sheets API)

- Plik klucza: `keys/ai-andrzejczyk-ga4.json`
- Service account: `ai-agents@ai-andrzejczyk.iam.gserviceaccount.com`
- Sheets API: włączone w projekcie `ai-andrzejczyk` (GCP #1056271345313)

---

## 9. Dodawanie nowych kryteriów

### Do istniejącej sekcji

1. Edytuj plik `_wytyczne/0N_*.md` lub dodaj wiersz w Google Sheets
2. Uruchom sync: `python _system/sync_sheets.py`
3. Commit + push

### Nowa sekcja (np. Sekcja 11 — LinkedIn Ads)

1. Utwórz `_wytyczne/11_linkedin-ads.md` wg szablonu z `_system/wytyczne-format.md`
2. Dodaj arkusz `Sekcja 11` w Google Sheets (te same kolumny)
3. Zaktualizuj słowniki `FILE_TO_SHEET` i `SHEET_TO_FILE` w obu skryptach sync
4. Commit + push

---

## 10. Przykładowe audyty

Gotowe audyty w folderze `wykonane/`:

| Klient | Typ | Pliki |
|--------|-----|-------|
| `invette` | e-commerce (PMax, Shopping) | `_audyt.md`, `_podsumowanie.md`, `.docx`, `.pdf` |
| `aryton` | e-commerce | `_audyt.md` |
| `modnakiecka` | e-commerce | `_audyt.md` |

Wzorzec dobrego raportu szczegółowego: [`wykonane/invette/20260403_invette_martech_audyt.md`](wykonane/invette/20260403_invette_martech_audyt.md)

---

## Kontakt

**Adrian Andrzejczyk** — analityka marketingowa, GA4, Google Ads, MarTech  
Roo Code mode: `📊 MarTech Audyt` | Trigger: `/martech-audit`
