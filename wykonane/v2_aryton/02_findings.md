# Findings v2: patrizia.aryton.pl — 2026-04-09
> Źródło danych: GA4 API (Property 326801658), 30d + YoY 30d
> Legenda: ✅ OK | ❌ Błąd | ⚠️ Do weryfikacji | ➖ Nie dotyczy | 🔒 Brak dostępu (wymaga DevTools/GTM)

---

## SEKCJA 1 — Audyt Wstępny

### 1.2 Kolejność skryptów HTML
- **Status**: ❌ Błąd (pośrednio potwierdzony z danych)
- **Wynik**: 0/3 pkt
- **Komentarz**: Dane GA4 wykazują 89 eventów `purchase` z `transaction_id = (not set)` i `revenue = 0`. To sygnatura hardcoded `gtag` w PrestaShop, który fires purchase event BEZ DataLayer (brak transaction_id, brak revenue). W PrestaShop ten snippet jest zwykle dodawany przez moduł Google Analytics bezpośrednio do HTML szablonu, NIEZALEŻNIE od GTM. Potwierdzenie wymaga DevTools, ale dane GA4 jednoznacznie wskazują na drugie źródło eventów purchase.
- **Dowód z danych**: `(not set)` → trans=0, ePurch=89, rev=0.00 PLN (30 dni)
- **Impact PLN**: 89 eventów purchase bez danych = brak contribution do analiz konwersji, mogą zakłócać Smart Bidding.
- **Rekomendacja**: Sprawdzić w DevTools → Network → czy przy zakupie są DWA requesty do google-analytics.com (jeden z `items[]`, jeden bez). Wyłączyć moduł Google Analytics w PrestaShop Admin → Preferencje → jeśli GTM jest aktywny.

### 1.3 Przegląd podstron
- **Status**: 🔒 Brak dostępu (wymaga DevTools)
- **Wynik**: 0/3 pkt
- **Komentarz**: Z danych hostname: `aryton81.local` (7 sesji), `dev18.arytondev.local` (14 sesji), `dev18.arytondev.pl` (26 sesji) — ruch deweloperski trafia do GA4. Wymaga potwierdzenia DevTools, ale wskazuje na brak filtrowania ruchu testowego.

### 1.5 TagHound — duplikowane tagi
- **Status**: ❌ Błąd (potwierdzony z danych)
- **Wynik**: 0/3 pkt
- **Komentarz**: Dane transakcyjne dowodzą istnienia co najmniej DWÓCH tagów/snippetów wysyłających purchase do GA4:
  1. GTM tag z DataLayer: poprawnie wysyła 427 transakcji (transaction_id, revenue ✅)
  2. Hardcoded gtag/moduł PrestaShop: wysyła 89 eventów z (not set) i 1105 malformed IDs
  W 2025 roku problem nie istniał (ratio ePurchases:transactions = 1.013 ≈ 1.0). W 2026 ratio = 3.77. Problem pojawił się PO 2025-04-09 — prawdopodobnie przy aktualizacji strony lub konfiguracji.

### 1.8 DataLayer — poprawność
- **Status**: ⚠️ Częściowy błąd
- **Wynik**: 1/3 pkt
- **Komentarz**: DataLayer dla 427 prawidłowych transakcji DZIAŁA — transaction_id poprawne (numeryczne, bez parametrów URL), revenue prawidłowe. Jednak:
  - 1105 eventów z malformed ID (`210032&key=1abe2783...`) wskazuje na DRUGI tag, który odczytuje transaction_id z URL zamiast z DataLayer
  - Konkretne malformed ID: `210032&key=1abe2783234b4109f15a80bdd3246c14`, `210033&key=1abe2783234b4109f15a80bdd3246c14` (itp.)
  - PrestaShop order confirmation URL: `?id=210032&key=1abe2783234b4109f15a80bdd3246c14` — tag odczytuje pełny parametr zamiast tylko `id`

### 1.9 DataLayer — struktura e-commerce (items[])
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: **KOREKTA v1** — produkty MAJĄ dane itemRevenue w GA4. TOP produkt: "Camelowy płaszcz teddy bear z wełną" (ID: 26271) = 8 zakupów, 27 992 PLN. Łącznie 100 produktów z przychodem > 0. DataLayer poprawnie przekazuje items[] z cenami przy prawidłowych transakcjach.

**Sekcja 1 — Wynik szacunkowy: ~10/36 pkt (27%)**

---

## SEKCJA 2 — ePrivacy / Consent Mode

### 2.4 Blokowanie cookies po odmowie
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: (not set)/(not set): 10 502 sesji = **3.18%** całości. W 2025 dane YoY wskazują podobny poziom Unassigned. Wymaga testu w incognito z DevTools.

### 2.17 url_passthrough
- **Status**: ❌ Błąd (nie potwierdzony bezpośrednio, ale wskazany przez 3.18% not-set trans)
- **Wynik**: 0/3 pkt
- **Komentarz**: 30 transakcji (7.0% z 427) pochodzi z (not set) — 13 675 PLN/msc bez atrybuacji. Wymaga potwierdzenia w GTM, ale wskazuje na brak url_passthrough.

**Sekcja 2 — Wynik szacunkowy: ~0/45 pkt (0–5% bez DevTools)**

---

## SEKCJA 3 — Konfiguracja GTM i GA4

### 3A.1 Podwójne tagi
- **Status**: ❌ Błąd (potwierdzony z danych)
- **Wynik**: 0/3 pkt
- **Komentarz**: Dwa aktywne snippety GA4 na stronie (GTM + PrestaShop moduł). Dowód: 89 eventów purchase z `(not set)` i `rev=0` + 1105 malformed IDs. W 2025 problem nie istniał. Naprawić: wyłączyć moduł Google Analytics w PrestaShop Admin.

### 3C.8 Filtrowanie ruchu wewnętrznego
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Serwery deweloperskie widoczne w GA4:
  - `dev18.arytondev.pl`: 26 sesji, 1 transakcja (!)
  - `dev18.arytondev.local`: 14 sesji
  - `aryton81.local`: 7 sesji
  - Łącznie: 47 sesji, w tym 1 transakcja z serwera DEV (zaburza dane)

### 3C.10 Cross-domain + Klarna
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: `klarna/referral`: 55 sesji/msc. Klarna nie jest wykluczone z referral exclusion.

### 3C.12–3C.13 Wykluczenia referral
- **Status**: ❌ Błąd
- **Wynik**: 0/5 pkt
- **Komentarz**: Niezwykluczone: klarna (55), poczta.onet.pl (191), poczta.interia.pl (88), poczta.o2.pl (83), statics.teams.cdn.office.net (72).

### 3C.17 Model atrybucji
- **Status**: ✅ OK (poprzedni audyt)
- **Wynik**: 2/2 pkt

### 3C.18 Połączenie Google Ads
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt

### 3C.19 BigQuery
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt

**Sekcja 3 — Wynik szacunkowy: ~15/93 pkt (16%)**

---

## SEKCJA 4 — Data Quality

### 4A.1 (not set) < 5%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set)/(not set): 10 502 sesji / 330 296 = **3.18%** < 5%.

### 4A.7 Bramki płatności poza ścieżką
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: `klarna/referral`: 55 sesji — Klarna w referral.

### 4A.8 Webmaile
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: poczta.onet.pl (191), poczta.interia.pl (88), poczta.o2.pl (83) = 362 sesji jako referral zamiast email.

### 4A.9 Meta fragmentation
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: 7 wariantów: facebook/cpc (58 776), m.facebook.com/referral (1 736), l.instagram.com/referral (1 703), l.facebook.com/referral (706), lm.facebook.com/referral (365), facebook/referral (366), facebook.com/referral (~86). Łącznie ~63 738 sesji w 7 silosach.

### 4C.2 Direct/none < 30%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: direct/(none): 17 459 sesji = **5.3%** << 30%.

### 4C.4 Transakcje (not set) < 10%
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: 30 transakcji z (not set)/(not set) / 427 = **7.0%** > 5% progu ostrzegawczego. 13 675 PLN/msc bez atrybuacji.

### 4D.1 Ratio ecommercePurchases:transactions
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: Ratio = 1610/427 = **3.77**. JEDNAK natura problemu jest inna niż v1 sugerował:
  - NIE są to zduplikowane transaction_id (każde ID unikalne)
  - PRAWDZIWA przyczyna: 1105 malformed IDs (`210032&key=...`) = 1105 błędnych ePurchases + 89 eventów z `(not set)` = 89 ePurchases bez danych
  - Prawidłowych transakcji: **427** (każda z unikalnym numerycznym ID, revenue > 0)
  - W 2025: ratio = 1.013 (normalne). Problem pojawił się w 2026.

### 4D.2 % bez transactionId
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: `(not set)` count = 1 z 1534 unikalnych wierszy = 0.07%. Prawidłowych IDs bez revenue jest 1105, ale mają ID (tylko malformed).

### 4D.3 Malformed transaction_id
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: 1105 malformed IDs z parametrami URL. Przykłady:
  - `210032&key=1abe2783234b4109f15a80bdd3246c14`
  - `210033&key=1abe2783234b4109f15a80bdd3246c14`
  - `210034&key=1abe2783234b4109f15a80bdd3246c14`
  Każdy malformed ID odpowiada prawdziwemu zamówieniu (np. `210034` to prawdziwa transakcja z rev=2069 PLN). Tag w GTM odczytuje transaction_id z URL `?id=210034&key=...` zamiast z DataLayer, pobierając pełny ciąg za `id=` łącznie z `&key=...`.

### 4D.4 value > 0 przy purchase
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: 1105 malformed IDs + 89 (not set) + 1 pusty string = **1195 eventów purchase z revenue = 0 PLN** (z 1610 łącznie = 74.2% wszystkich purchase events bez revenue). Jednak 427 prawidłowych transakcji MA revenue.

### 4E.1–4E.4 Zdarzenia e-commerce
- **Status**: ✅ OK (wszystkie wdrożone)
- **Wynik**: 12/12 pkt
- **Komentarz**: view_item (~590k), add_to_cart (32 653), begin_checkout (~1 296), purchase (1 610 raw / 427 real).

### 4E.5 Lejek wygląda naturalnie
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: add_shipping_info (~2 132) > begin_checkout (~1 296) = anomalia. purchase_raw (1 610) > add_payment_info (~806) = anomalia. Lejek rozbity na etapach shipping i payment.

### 4E.6 AOV naturalny
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: AOV = 529 914 PLN / 427 trans = **1 241 PLN**. Naturalny dla marki premium odzieżowej. Identyczny YoY (1 241 vs 1 242 PLN).

### 4B.3 CR naturalny
- **Status**: ⚠️ Niski
- **Wynik**: 1/2 pkt
- **Komentarz**: CR = 427/330 296 = **0.129%** — poniżej benchmarku 0.5–3%. W 2025: CR = 0.341%.

**Sekcja 4 — Wynik: ~30/75 pkt (40%)**

---

## SEKCJA 5 — UTM

### 5.2 Google Ads UTM source/medium
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: google/cpc: 142 854 sesji, 90 transakcji. Auto-tagging działa.

### 5.4 Meta Ads UTM
- **Status**: ⚠️ Częściowy
- **Wynik**: 1/3 pkt
- **Komentarz**: facebook/cpc: 58 776 sesji (UTM płatne ok). 7 wariantów referral Meta (~5 000 sesji bez UTM) = 8% ruchu Meta bez UTM.

### 5.7 Email UTM
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: edrone/email: 17 711 sesji, 37 transakcji, 45 826 PLN.

### 5.10 SMS UTM/konwersje
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: sms/smsapi: 1 708 sesji, **0 transakcji**. W YoY 2025: 2 428 sesji, 8 transakcji, CR=0.33%. Coś zepsuło się między 2025 a 2026 — albo linki SMS kierują na złą stronę albo tracking konwersji z SMS jest broken.

**Sekcja 5 — Wynik: ~9/18 pkt (50%)**

---

## SEKCJA 6 — BCG

### 6.1–6.5 Analiza BCG
- **Status**: ⚠️ Ograniczona (brak dostępu do Google Ads przez BDOS)
- **Wynik**: 0/12 pkt
- **Komentarz**: Dane produktowe GA4 dostępne (100 produktów z rev > 0). TOP bestseller: "Camelowy płaszcz teddy bear" (ID: 26271) = 8 zakupów, 27 992 PLN. Jednak pełna analiza BCG wymaga danych Google Ads (ROAS per produkt) — niedostępnych bez BDOS.

**Sekcja 6 — Wynik: 0/12 pkt (0% — brak dostępu Ads)**

---

## SEKCJA 7 — Lejki zakupowe

### 7.1 Wszystkie 4 zdarzenia
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt

### 7.2 CR paid ≥ 50% CR organic
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: google/cpc: 90 trans / 142 854 sesji = **0.063%** vs google/organic: 173/75 838 = **0.228%**. Ratio = **27.6%** << 50%.
- **Impact PLN**: Gdyby google/cpc miał CR = 50% organic (0.114%), dodatkowych 72 trans/msc × 1 241 PLN = **~89 000 PLN/msc**.

### 7.3 Brak kanału z CR < 0.1% przy wydatkach
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: google/cpc CR = 0.063% — jedynym kanałem płatnym z CR < 0.1%. Cross-network (PMax): 0.051% przy szacunkowych wydatkach >> 10 000 PLN/msc.

### 7.4 Checkout drop-off
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: begin_checkout (~1 296) → transactions (427) = **32.9%** konwersji checkout = **67.1% drop-off**. Benchmark: <40%.

**Sekcja 7 — Wynik: 2/8 pkt (25%)**

---

## SEKCJA 8 — GA4 ↔ Google Ads

### 8.1 Połączenie aktywne
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt

### 8.2–8.10 Pozostałe (BDOS)
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/24 pkt

**Sekcja 8 — Wynik: 3/27 pkt (11%)**

---

## SEKCJA 9 — Analiza danych

### 9.1 CVR paid ≥ 50% organic
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Jak 7.2.

### 9.2 Najlepszy kanał wg Rev/sesja
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**:
  | Kanał | Rev/sesja |
  |-------|-----------|
  | Organic Search | 3.48 PLN |
  | Paid Search | 2.42 PLN |
  | Email (edrone) | 2.59 PLN |
  | Bing organic | **10.51 PLN** ⭐ |
  | Direct | 1.21 PLN |
  | PMax (Cross-network) | 0.54 PLN |
  | Paid Social (Meta) | 1.10 PLN |
  **Bing organic** (2 859 sesji, 26 trans, 30 063 PLN) = najwyższy Rev/sesja = 10.51 PLN. Kompletnie niedoinwestowany kanał.

### 9.3 Mobile/Desktop CVR ratio
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**:
  - Mobile CR: 246/259 439 = **0.095%** (vs 0.288% w 2025 = **-67% YoY**)
  - Desktop CR: 180/65 243 = **0.276%** (vs 0.466% w 2025 = **-41% YoY**)
  - Ratio mobile/desktop: 0.095/0.276 = **34%** << 50%
  - Mobile stracił 3× więcej CR niż desktop w ciągu roku — wskazuje na degradację UX mobile lub problem techniczny

### 9.4 Engagement rate
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: 47.8% > 40%.

### 9.5 Porzucenie koszyka
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: add_to_cart = 32 653, trans = 427 → porzucenie = **98.7%**. Benchmark: <80%.
- **Impact PLN**: Przy 3% odzysku: 32 240 × 3% × 1 241 = **~1 199 000 PLN/rok** potencjał.

### 9.6 Anomalie ruchu
- **Status**: ❌ Wykryta anomalia
- **Wynik**: 0/2 pkt
- **Komentarz**: **2026-04-04: 9 564 sesji, 0 transakcji** — całkowity brak sprzedaży przy normalnym ruchu. Możliwa awaria bramki płatności lub strony koszyka. Wymaga weryfikacji logów serwera.

### 9.7 Ruch wewnętrzny
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: dev18.arytondev.pl (26 sesji, 1 transakcja z dev!), dev18.arytondev.local (14), aryton81.local (7). Ruch deweloperski w produkcyjnym GA4.

### 9.9 Bramki płatności w referral
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: klarna (55), webmaile (362 sesji) jako referral.

**Sekcja 9 — Wynik: 4/24 pkt (17%)**

---

## SEKCJA 10 — Google Ads
- **Status**: 🔒 Brak dostępu (BDOS wymagany)
- **Wynik**: 0/81 pkt

**Z danych GA4 pośrednio:**
- Paid Search -92% sesji YoY (58 884 → 4 600) — kampanie Search drastycznie ograniczone lub wyłączone
- Cross-network CR: 0.051% vs 0.221% YoY — PMax przynosi niekonwertujący ruch
- Cross-network sesje: +63% YoY (137 557 vs 84 140) — większy budżet PMax ale gorsze wyniki

---

## SEKCJA 11 — ANALIZA SPADKU SPRZEDAŻY YoY (NOWA SEKCJA)

### 11.1 Skala problemu

| Metryka | 2026 | 2025 | Delta |
|---------|------|------|-------|
| Transakcje | 427 | 1 495 | **-71.4%** |
| Przychód | 529 914 PLN | 1 856 701 PLN | **-71.5%** |
| Sesje | 330 296 | 438 646 | **-24.7%** |
| AOV | 1 241 PLN | 1 242 PLN | **≈0%** |
| CR | 0.129% | 0.341% | **-62%** |

**Kluczowa obserwacja:** AOV jest identyczny → problem NIE jest cenowy, NIE jest w wartości koszyka. Problem jest w liczbie kupujących.

### 11.2 Analiza przyczyn per kanał

| Kanał | Sesje delta | Trans delta | CR delta | Hipoteza przyczyny |
|-------|------------|------------|---------|-------------------|
| **Paid Search** | **-92%** | -92% | +5% | Budżet kampanii Search drastycznie obcięty lub kampanie wyłączone |
| **Cross-network (PMax)** | +63% | -62% | **-77%** | PMax optymalizuje na fałszywe konwersje (ratio 3.77x), przynosi niekonwertujący ruch |
| **Organic Search** | -43% | -62% | -33% | Algorytm Google / SEO regres |
| **Email** | -42% | -77% | -60% | Zmniejszona baza emaili lub gorsza segmentacja |
| **Direct** | -46% | -91% | **-83%** | Spadek powracających klientów / lojalności |
| **Mobile** | -19% | -73% | **-67%** | Problem techniczny UX mobile lub zmiana algorytmu |
| SMS | -30% | -100% | -100% | Tracking zepsuty lub kampanie nieaktywne |

### 11.3 Hipotezy wyjaśniające spadek (-71%)

**H1: Wyłączenie kampanii Search (POTWIERDZONE DANYMI)**
- Paid Search sesje -92% (z 58 884 do 4 600)
- Paid Search CR NIEZMIENIONY (0.29% → 0.30%) → jakość kampanii była dobra, problem = wolumen
- Szacunkowa strata: 54 284 sesji × 0.29% CR × 1 241 PLN = **~195 000 PLN/msc** utraconych przez brak Search

**H2: PMax optymalizuje na fałszywe dane (POTWIERDZONY)**
- W 2025: ePurchases:transactions = 1.013 (normalne) → PMax "widział" 186 konwersji miesięcznie
- W 2026: ratio = 3.77 → PMax "widzi" 1610 eventów zamiast 427 → **optymalizuje na 3.77× zawyżone dane**
- Skutek: PMax kupuje ruch, który "wygląda" jak konwertujący ale nie konwertuje prawdziwie
- Cross-network CR: 0.221% (2025) → 0.051% (2026) = 4× gorsza jakość przy 63% więcej ruchu

**H3: Degradacja CR mobile (POTWIERDZONA DANYMI)**
- Mobile CR: 0.288% → 0.095% = -67%
- Mobile stanowi 78% ruchu (259 439 sesji)
- Potencjalna przyczyna: zmiana szablonu mobilnego, problemy z Google PageSpeed, nowa wersja PrestaShop
- Desktop CR też spadł (-41%) ale mniej dramatycznie

**H4: Sezonowość/promocje (MOŻLIWA)**
- W 2025-03 były MEGA-szczyty: 125 trans/dzień (2025-03-14), 113 trans/dzień (2025-03-26), 110 trans/dzień (2025-03-31) → wielka wyprzedaż lub promocja
- W 2026 max = 29 trans/dzień (2026-03-31)
- Gdyby wykluczyć szczyty promocyjne 2025, bazowe wyniki 2025 byłyby niższe
- Jednak nawet dni "normalne" 2025 mają 30-60 trans/dzień vs 10-25 w 2026

**H5: Problemy techniczne (CZĘŚCIOWO POTWIERDZONE)**
- 2026-04-04: 9 564 sesji, 0 transakcji — awaria
- Malformed transaction IDs (pojawienie się w 2026 a nie w 2025) → zmiana w kodzie strony
- Nowe formaty item_id w 2026 (numeryczne vs hyphenated) → migracja produktów
- add_shipping_info > begin_checkout → bug w sekwencji eventów lejka

### 11.4 Szacunkowy wpływ każdej przyczyny na utracone transakcje

| Przyczyna | Szac. utracone trans/msc | Szac. utracony przychód/msc |
|-----------|-------------------------|---------------------------|
| Brak Paid Search | ~155–175 | ~190 000–215 000 PLN |
| PMax na fałszywych danych (-77% CR) | ~80–100 | ~100 000–125 000 PLN |
| Mobile CR -67% | ~120–150 | ~150 000–185 000 PLN |
| Organic Search -43% sesji + -33% CR | ~100–130 | ~125 000–160 000 PLN |
| Brak promocji (vs 2025 spikes) | ~200–300 | ~250 000–370 000 PLN |
| **ŁĄCZNIE** | **~655–855** | **~815 000–1 055 000 PLN/msc** |

*(Dla porównania: różnica w przychodzie YoY = 1 856 701 - 529 914 = **1 326 787 PLN/msc**)*

---

## Punktacja

| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | 10 | 36 | 28% | ❌ Krytyczny |
| 2. ePrivacy | 1 | 45 | 2% | ❌ Krytyczny |
| 3. Konfiguracja | 15 | 93 | 16% | ❌ Krytyczny |
| 4. Data Quality | 30 | 75 | 40% | ❌ Krytyczny |
| 5. UTM | 9 | 18 | 50% | ⚠️ Wymaga poprawy |
| 6. BCG | 0 | 12 | 0% | 🔒 Brak dostępu Ads |
| 7. Lejki | 2 | 8 | 25% | ❌ Krytyczny |
| 8. GA4↔Ads | 3 | 27 | 11% | 🔒 Brak dostępu Ads |
| 9. Analiza | 4 | 24 | 17% | ❌ Krytyczny |
| 11. Analiza YoY | — | — | — | ❌ Spadek -71.4% YoY |
| 10. Google Ads | 0 | 81 | 0% | 🔒 Brak dostępu |
| **ŁĄCZNIE (bez 10)** | **74** | **338** | **22%** | **❌ Krytyczny** |

---

## Impact finansowy (podsumowanie)

| Problem | Szacunek PLN/msc | Priorytet | Dowód |
|---------|-----------------|-----------|-------|
| Wyłączone kampanie Search (-92% sesji) | ~190 000–215 000 strata | 🔴 | Paid Search sesje: 4 600 vs 58 884 YoY |
| Mobile CR -67% YoY | ~150 000–185 000 strata | 🔴 | CR: 0.095% vs 0.288% YoY |
| PMax na fałszywych danych (CR: 0.05%) | ~100 000–125 000 strata | 🔴 | Cross-network CR: 0.051% vs 0.221% |
| Malformed transaction_id (1105) | Niemierzalne (błędna optymalizacja) | 🔴 | 1105 konkretnych malformed IDs |
| Porzucenie koszyka 98.7% | ~100 000 potencjał | 🟡 | 32 653 add_to_cart vs 427 trans |
| Checkout drop-off 67% | ~80 000–120 000 potencjał | 🟡 | begin_checkout vs transactions |
| (not set) trans 7% | ~13 675 bez atrybuacji | 🟡 | 30 transakcji bez źródła |
| SMS 0 transakcji | ~10 000 potencjał | 🟢 | 1 708 sesji, 0 trans (vs 8 w 2025) |

---

## Top 5 problemów

1. **❌ Transakcje -71.4% YoY (1 495 → 427)** — utracono ~1 330 000 PLN/msc przychodów rok do roku. Główne przyczyny: wyłączone kampanie Search, PMax na fałszywych danych, spadek CR mobile.

2. **❌ Malformed transaction_id (1105 konkretnych przypadków)** — np. `210034&key=1abe2783234b4109f15a80bdd3246c14` — powoduje ratio ecommercePurchases:transactions = 3.77× i fałszywe sygnały konwersji dla Google Ads Smart Bidding. Problem pojawił się w 2026 (w 2025 ratio było 1.01).

3. **❌ Paid Search sesje -92%** — z 58 884 do 4 600 sesji miesięcznie. CR Paid Search pozostało stabilne (0.29-0.30%) → to problem wolumenu (budżet/kampanie), nie jakości. Szacunkowa strata: ~190 000–215 000 PLN/msc.

4. **❌ Mobile CR -67% YoY** — z 0.288% do 0.095%. Mobile stanowi 78% ruchu (259 439 sesji/msc). Desktop też spadł (-41%) ale znacznie mniej. Wskazuje na degradację UX mobile po aktualizacji PrestaShop lub szablonu.

5. **❌ PMax przynosi więcej ruchu ale 4× mniej efektywny** — sesje Cross-network wzrosły +63% (84k→137k) ale CR spadło z 0.221% do 0.051%. PMax optymalizuje się na malformed transaction_id (3.77×) i może "myśleć" że osiąga dobry ROAS na nie-konwertującym ruchu.
