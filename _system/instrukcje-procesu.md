# Instrukcje procesu — Audyt MarTech
> Wersja: 1.1 | Autor: Adrian Andrzejczyk | Aktualizacja: 2026-04
>
> **Ten plik czyta agent-orkiestrator na początku każdej sesji audytu.**
> Pliki z kryteriami per sekcja → `AUDYT/MarTech/_wytyczne/`
> Szablony raportów → `AUDYT/MarTech/_system/szablon-audyt.md` i `szablon-podsumowanie.md`
> Repo GitHub: `https://github.com/andrzejczyk-adrian/MarTech_Audyt`

---

## 0. INICJALIZACJA — wykonaj przed każdym audytem

```
1. Uruchom sync wytycznych z Google Sheets:
   cd "C:\Users\adria\Documents\AI\AUDYT\MarTech"
   "C:/Program Files/Python310/python.exe" _system/sync_sheets.py

2. Przeczytaj ten plik (instrukcje-procesu.md)

3. Zapytaj o nazwę klienta → zacznij od ETAP 1
```

---

## 0B. GITHUB — OBOWIĄZKOWE po każdej zmianie pliku

**Każda zmiana (zapis MD, DOCX, PDF, wytycznych) = commit + push:**

```cmd
cd "C:\Users\adria\Documents\AI\AUDYT\MarTech"
git add .
git commit -m "{opis: np. 'invette etap 3 findings'}"
git push
```

Repo: `https://github.com/andrzejczyk-adrian/MarTech_Audyt`
Branch: `main`

Jeśli git nie skonfigurowany → uruchom `_system/setup_git.bat`

---

## 1. Cel systemu

System przeprowadza kompleksowy audyt MarTech klienta: od zebrania danych wejściowych (brief), przez analizę techniczną (GA4, GTM, Google Ads, kod strony), aż do finalnych raportów (szczegółowy + biznesowy) w formatach MD i DOCX.

**Efekt końcowy każdego audytu:**
```
AUDYT/MarTech/wykonane/{klient}/
  00_brief.md                          ← dane wejściowe
  01_raw-data.md                       ← surowe dane z API
  02_findings.md                       ← wnioski audytu (per sekcja)
  {RRRRMMDD}_{klient}_audyt.md         ← finalny raport szczegółowy
  {RRRRMMDD}_{klient}_audyt.docx
  {RRRRMMDD}_{klient}_audyt.pdf
  {RRRRMMDD}_{klient}_podsumowanie.md  ← podsumowanie biznesowe
  {RRRRMMDD}_{klient}_podsumowanie.docx
  {RRRRMMDD}_{klient}_podsumowanie.pdf
  generate_docs.py
  dane/                                ← pliki źródłowe od klienta
```

---

## 2. Pipeline — 6 etapów

Każdy etap kończy się zapisem konkretnego pliku i **zatrzymaniem**. Agent czeka na zatwierdzenie przez użytkownika przed przejściem do kolejnego etapu.

```
ETAP 1: BRIEF         → 00_brief.md
ETAP 2: DANE          → 01_raw-data.md
ETAP 3: AUDYT         → 02_findings.md   [+ Manager Review A]
ETAP 4: RAPORT        → {klient}_audyt.md [+ Manager Review B]
ETAP 5: PODSUMOWANIE  → {klient}_podsumowanie.md
ETAP 6: DOCX          → DOCX + PDF (oba pliki)
```

---

## 3. Szczegóły etapów

### ETAP 1 — BRIEF

**Cel:** Zebranie wszystkich danych potrzebnych do audytu.

**Jak:** Zapytaj użytkownika o każdy element. Nie zakładaj domyślnych wartości bez pytania.

**Zapisz:** `AUDYT/MarTech/wykonane/{klient}/00_brief.md`

```markdown
# Brief: {klient} — {RRRRMMDD}

## Dane podstawowe
- Nazwa klienta:
- URL strony:
- Typ biznesu: e-commerce / lead gen / SaaS / mix
- Tryb audytu: single konto / multi-konto (MCC)

## Dostępy techniczne
- GA4 Property ID: (format: 123456789)
- Google Ads Customer ID: (format: 123-456-7890)
- GTM Container ID: (format: GTM-XXXXXX)
- BigQuery dataset: (format: projekt.dataset lub "brak")
- BDOS alias Google Ads: (alias agencyjny lub "brak")
- CMP (Consent Management Platform): Cookiebot / OneTrust / Usercentrics / własne / brak

## Zakres audytu
- Sekcje: pełny (1–10) / wybrane: [lista]
- Priorytety: GA4 / Google Ads / kod strony / wszystko
- Czy to e-commerce z feedem produktowym: tak / nie

## Informacje dodatkowe
- Platforma sklepu: Shoper / WooCommerce / Shopify / PrestaShop / inne
- Agencja prowadząca: (nazwa lub "klient bezpośredni")
- Uwagi od klienta:
```

**Gate 1:** Pokaż wypełniony brief. Zapytaj: _"Dane kompletne? Zatwierdzasz?"_

---

### ETAP 2 — DANE (zbieranie z API)

**Cel:** Pobranie surowych danych z GA4 API i Google Ads. Bez interpretacji — tylko dane.

**Narzędzia:**
- GA4: `mcp__ga4-analytics` (`get_property_schema`, `get_ga4_data`)
- Google Ads: BDOS (`from bdos import connect`)
- BigQuery: MCP BigQuery (tylko jeśli dataset podany w briefie)

**Kolejność zapytań GA4:**

```python
# 1. Schemat property (sprawdź typ biznesu, custom dims, połączenie z Ads)
get_property_schema(property_id)

# 2. Lista zdarzeń (30d) — co jest wdrożone
get_ga4_data(
    dimensions=["eventName"],
    metrics=["eventCount", "eventCountPerUser"],
    date_from="30daysAgo"
)

# 3. Jakość źródeł ruchu — (not set) check
get_ga4_data(
    dimensions=["sessionSource", "sessionMedium"],
    metrics=["sessions", "transactions", "purchaseRevenue"],
    date_from="30daysAgo"
)

# 4. Transakcje — weryfikacja duplikatów
get_ga4_data(
    dimensions=["transactionId"],
    metrics=["transactions", "ecommercePurchases", "purchaseRevenue"],
    date_from="30daysAgo",
    limit=2000
)

# 5. Lejek zakupowy per kanał
get_ga4_data(
    dimensions=["sessionDefaultChannelGroup"],
    metrics=["sessions", "addToCarts", "checkouts", "ecommercePurchases", "purchaseRevenue"],
    date_from="30daysAgo"
)

# 6. Top 20 miast
get_ga4_data(
    dimensions=["city"],
    metrics=["sessions", "ecommercePurchases", "purchaseRevenue"],
    date_from="30daysAgo",
    limit=20
)

# 7. Produkty (tylko e-commerce)
get_ga4_data(
    dimensions=["itemId", "itemName", "itemCategory"],
    metrics=["itemsViewed", "itemsPurchased", "itemRevenue"],
    date_from="30daysAgo"
)
```

**Kolejność zapytań Google Ads (BDOS):**

```python
from bdos import connect
ctx = connect("{alias}")

# Kampanie — lista bez metryk (widać też nowe/wstrzymane)
all_campaigns = ctx.engine.execute(entity="campaigns", metrics=[], filters=["status = ENABLED"])

# Performance kampanii 30 dni
perf = ctx.engine.execute(entity="campaigns", days=30, filters=["cost > 0"])

# Kampanie z 0 konwersji ale z wydatkami
no_conv = [c for c in perf.data if c.get('conversions', 0) == 0 and c.get('cost', 0) > 300]

# Shopping per produkt
shopping = ctx.engine.execute(entity="shopping_performance", days=30, filters=["metrics.cost_micros > 0"])

# PMax asset groups
pmax = ctx.engine.execute(entity="pmax_assets", metrics=[])
```

**Zapisz:** `AUDYT/MarTech/wykonane/{klient}/01_raw-data.md`

Format pliku `01_raw-data.md`:
```markdown
# Dane surowe: {klient} — {data}

## GA4 — Schema i typ biznesu
[wyniki get_property_schema — typ: e-comm/lead gen, custom dims, połączenie z Ads]

## GA4 — Zdarzenia (30d) — TOP 30
| Zdarzenie | Liczba | Liczba/użytkownik |
|-----------|--------|-------------------|

## GA4 — Źródła ruchu (30d)
| source | medium | sessions | transactions | revenue |
|--------|--------|----------|--------------|---------|
[% (not set): ___]

## GA4 — Transakcje (weryfikacja duplikatów)
| transactionId | transactions | ecommercePurchases | revenue |
|---------------|--------------|---------------------|---------|
[Ratio ecommercePurchases:transactions: ___]
[% bez transactionId: ___]
[Przykłady malformed ID: ...]

## GA4 — Lejek zakupowy (30d)
| Kanał | sessions | addToCarts | checkouts | purchases | CR |
|-------|----------|------------|-----------|-----------|-----|

## GA4 — Top 20 miast
| Miasto | sessions | purchases | CR | AOV |
|--------|----------|-----------|-----|-----|

## GA4 — Produkty (e-commerce)
| itemId | itemName | itemCategory | viewed | purchased | revenue |
|--------|----------|--------------|--------|-----------|---------|

## Google Ads — Podsumowanie konta (30d)
[metryki zbiorcze: wydatki, kliknięcia, konwersje, ROAS]

## Google Ads — Kampanie (30d)
| Kampania | Typ | Wydatki | Konwersje | ROAS | Budżet/d | Strategia |
|----------|-----|---------|-----------|------|---------|-----------|

## Google Ads — Kampanie bez konwersji (>300 PLN, 0 konw.)
| Kampania | Typ | Wydatki 30d | Drenaż/msc |
|----------|-----|-------------|------------|

## Google Ads — Shopping per produkt (TOP 15)
| Produkt | Wydatki | ROAS | Konwersje |
|---------|---------|------|-----------|

## Notatki — pierwsze obserwacje
[Co rzuca się w oczy w surowych danych — bez interpretacji, tylko fakty]
```

**Gate 2:** Pokaż podsumowanie pobranych danych. Zapytaj: _"Dane pobrane. Przejrzeć i zatwierdzić?"_

---

### ETAP 3 — AUDYT TECHNICZNY

**Cel:** Ocena każdego kryterium z checklisty. Surowe wnioski per sekcja — bez "ozdabiania".

**Jak:**
1. Przeczytaj plik wytycznych dla danej sekcji z `AUDYT/MarTech/_wytyczne/`
2. Oceń każdy punkt na podstawie `01_raw-data.md` i wiedzy technicznej
3. Dla każdego punktu: status + wynik pkt + KONKRETNY komentarz + rekomendacja

**Zasada przykładów (KRYTYCZNA):**
- ❌ ZŁE: _"Wykryto problem z UTM"_
- ✅ DOBRE: _"Wykryto 5 wariantów źródła Meta: `facebook` (184 372 sesji), `facebook.com` (38 291), `m.facebook.com` (19 440) — łącznie 251 537 sesji podzielonych na 5 wierszy"_

**Zapisz:** `AUDYT/MarTech/wykonane/{klient}/02_findings.md`

Format wpisu per punkt:
```markdown
### {ID} {Nazwa punktu}
- **Status**: ✅ OK / ❌ Błąd / ⚠️ Do weryfikacji / ➖ Nie dotyczy / 🔒 Brak dostępu
- **Wynik**: {uzyskane}/{max} pkt
- **Komentarz**: [konkretne dane, przykłady, liczby — minimum 2 zdania]
- **Impact PLN**: [szacowany koszt błędu jeśli dotyczy]
- **Rekomendacja**: [co, kto, kiedy]
```

**Tabela punktacji na końcu pliku:**
```markdown
## Punktacja
| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | | | | ✅/⚠️/❌ |
| 2. ePrivacy | | | | |
| 3. Konfiguracja | | | | |
| 3K. BigQuery | | | | |
| 4. Data Quality | | | | |
| 5. UTM | | | | |
| 6. BCG | | | | |
| 7. Lejki | | | | |
| 8. GA4↔Ads | | | | |
| 9. Analiza danych | | | | |
| 10. Google Ads | | | | |
| **ŁĄCZNIE** | | | **%** | |

## Impact finansowy (podsumowanie)
| Problem | Szacunek PLN/msc | Priorytet |
|---------|-----------------|-----------|

## Top 5 problemów
1. [najważniejszy — z kwotą strat]
2.
3.
4.
5.
```

**Manager Review A** (wykonaj automatycznie po zapisie findings):

Sprawdź `02_findings.md`:
- [ ] Czy każdy punkt z wytycznych dla sprawdzanych sekcji jest wypełniony lub oznaczony ➖?
- [ ] Czy każdy ❌ i ⚠️ ma konkretny przykład (liczby, ID, wartości)?
- [ ] Czy ROAS podany jako mnożnik Xx (nie % z BDOS)?
- [ ] Czy kampanie bez konwersji mają wyliczony drenaż PLN/msc?
- [ ] Czy impact finansowy jest wyliczony dla top problemów?
- [ ] Czy brakuje danych, które można jeszcze pobrać z API?

Jeśli są luki: **uzupełnij przed zamknięciem etapu** (pobierz dodatkowe dane jeśli potrzeba).

**Gate 3:** Pokaż wyniki review A i podsumowanie punktacji. Zapytaj: _"Audyt techniczny gotowy. Zatwierdzasz przejście do pisania raportu?"_

---

### ETAP 4 — RAPORT SZCZEGÓŁOWY

**Cel:** Przekształcenie suchych wyników audytu w pełny, obszerny raport.

**Jak:**
1. Przeczytaj `02_findings.md` + `_system/szablon-audyt.md`
2. Pisz obszernie — każdy punkt = min. ¼ strony A4
3. Dla dyrektora/właściciela: wyjaśnij CZYM JEST każde zagadnienie zanim podasz wynik
4. Konkretne dane, przykłady, wyceny w PLN

**Zapisz:** `AUDYT/MarTech/wykonane/{klient}/{RRRRMMDD}_{klient}_audyt.md`

**Manager Review B** (wykonaj automatycznie po zapisie raportu):

Sprawdź raport:
- [ ] Czy każda sekcja ma opis "czym jest i dlaczego sprawdzamy" (dla właściciela)?
- [ ] Czy komentarze zawierają konkretne dane, nie ogólniki?
- [ ] Czy CZĘŚĆ III — Rekomendacje ma 3 horyzonty (0-7 dni / Miesiąc 1 / Miesiąc 2-3)?
- [ ] Czy CZĘŚĆ II.B — Impact finansowy jest wypełniony (PLN/msc i PLN/rok)?
- [ ] Czy punktacja w raporcie zgadza się z punktacją w findings?
- [ ] Czy raport jest logicznie spójny?

Jeśli są problemy: **popraw przed zamknięciem etapu**.

**Gate 4:** Pokaż wyniki review B. Zapytaj: _"Raport szczegółowy gotowy. Zatwierdzasz?"_

---

### ETAP 5 — PODSUMOWANIE BIZNESOWE

**Cel:** Skrót raportu szczegółowego dla właściciela/dyrektora. 2–3 strony A4 max.

**Jak:**
1. Przeczytaj `{klient}_audyt.md` + `_system/szablon-podsumowanie.md`
2. Zero żargonu technicznego — zamiast "DataLayer push" → "system przekazywania danych"
3. Kwantyfikuj problemy w PLN (utracone konwersje, przepalony budżet)
4. Action plan: co KONKRETNIE zrobić i kiedy

**Zapisz:** `AUDYT/MarTech/wykonane/{klient}/{RRRRMMDD}_{klient}_podsumowanie.md`

Struktura:
```
1. Nagłówek (klient, data, okres, audytor)
2. Tabela KPI / tabela przestawna (tryb multi-konto)
3. Ocena ogólna (1 zdanie) + wynik % łączny
4. Top 3–5 problemów (każdy z kwotą strat/szans PLN)
5. Action plan — 3 horyzonty:
   🔴 Natychmiast (0–7 dni) — zatamowanie strat
   🟡 Miesiąc 1 — optymalizacja i naprawa
   🟢 Miesiąc 2–3 — skalowanie i strategia
```

**Gate 5:** Zapytaj: _"Podsumowanie gotowe. Zatwierdzasz generowanie DOCX?"_

---

### ETAP 6 — GENEROWANIE DOCX/PDF

**Jak:**
1. Sprawdź czy `generate_docs.py` jest w katalogu klienta. Jeśli nie — skopiuj z `_system/generate_docs.py`
2. Uruchom:
```cmd
cd "C:\Users\adria\Documents\AI\AUDYT\MarTech\wykonane\{klient}" && "C:/Program Files/Python310/python.exe" generate_docs.py
```
3. Podaj ścieżki do 4 wygenerowanych plików (2x DOCX + 2x PDF)

---

## 4. Zasady krytyczne

| Zasada | Opis |
|--------|------|
| **Ścieżka** | `C:\Users\adria\Documents\AI\AUDYT\MarTech\wykonane\{klient}\` |
| **Nazwy klientów** | Małe litery, bez PL znaków, myślnik: `invette`, `aryton`, `modnakiecka` |
| **ROAS** | Zawsze mnożnik `9x`, `12x` — NIGDY procent z BDOS (BDOS "9%" = 9x ROAS) |
| **Przykłady** | Każdy ❌/⚠️ MUSI mieć konkretne liczby / ID / wartości PLN |
| **Język** | Polski. Terminy techniczne (GTM, GA4, ROAS, CPA) mogą zostać po angielsku |
| **Jeden GA4 tag** | Zawsze rekomenduj wyłącznie jeden aktywny tag GA4 na stronie |
| **2 pliki** | Zawsze generuj oba: `_audyt` (szczegółowy) i `_podsumowanie` (biznesowy) |

---

## 5. Struktura wytycznych

Kryteria audytu per sekcja są w plikach:

| Plik | Sekcja | Zawartość |
|------|--------|-----------|
| `_wytyczne/01_audyt-wstepny.md` | Sekcja 1 | Kryterium + priorytet + jak sprawdzić + czerwone flagi |
| `_wytyczne/02_eprivacy.md` | Sekcja 2 | j.w. |
| `_wytyczne/03_konfiguracja.md` | Sekcja 3 | j.w. |
| `_wytyczne/04_data-quality.md` | Sekcja 4 | j.w. |
| `_wytyczne/05_utm.md` | Sekcja 5 | j.w. |
| `_wytyczne/06_bcg.md` | Sekcja 6 | j.w. |
| `_wytyczne/07_lejki.md` | Sekcja 7 | j.w. |
| `_wytyczne/08_ga4-ads.md` | Sekcja 8 | j.w. |
| `_wytyczne/09_analiza.md` | Sekcja 9 | j.w. |
| `_wytyczne/10_google-ads.md` | Sekcja 10 | j.w. |

> **Uwaga dla przyszłości:** Docelowo wytyczne będą zarządzane w Google Sheets i eksportowane do tych plików MD. Format tabeli w plikach wytycznych jest celowo przyjazny dla eksportu z arkuszy.

---

## 6. Przykłady gotowych audytów

Wzorcowe audyty do weryfikacji jakości:
- Szczegółowy: `AUDYT/MarTech/invette/20260403_invette_martech_audyt.md`
- Podsumowanie: `AUDYT/MarTech/invette/20260403_invette_martech_podsumowanie.md`
- Multi-konto: `AUDYT/MarTech/Aryton/20260403_Aryton_audyt.md`
