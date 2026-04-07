# Skill: Audyt GA4 / MarTech

## Lokalizacja plików — OBOWIĄZKOWE

**Wszystkie audyty MarTech zapisujesz WYŁĄCZNIE w:**
```
C:\Users\adria\Documents\AI\AUDYT\MarTech\
```

**Struktura katalogów:**
```
C:\Users\adria\Documents\AI\AUDYT\MarTech\
  {nazwa_klienta}\
    {RRRRMMDD}_{nazwa_klienta}_podsumowanie.md       ← Plik 1 źródłowy
    {RRRRMMDD}_{nazwa_klienta}_podsumowanie.docx     ← Plik 1 Word
    {RRRRMMDD}_{nazwa_klienta}_podsumowanie.pdf      ← Plik 1 PDF
    {RRRRMMDD}_{nazwa_klienta}_audyt.md              ← Plik 2 źródłowy
    {RRRRMMDD}_{nazwa_klienta}_audyt.docx            ← Plik 2 Word
    {RRRRMMDD}_{nazwa_klienta}_audyt.pdf             ← Plik 2 PDF
    generate_docs.py                                  ← Konwerter MD→DOCX+PDF
    dane\                                             ← Pliki źródłowe
      *.json, *.csv (eksporty BDOS, GA4)
```

**Konwencja nazw klientów:** małe litery, bez polskich znaków, myślnik jako separator
- `invette`, `tableforu`, `ideashirt`, `zielony-parapet`, `optimum-bhp`

**Przykłady pełnych ścieżek:**
```
C:\Users\adria\Documents\AI\AUDYT\MarTech\invette\20260403_invette_audyt.md
C:\Users\adria\Documents\AI\AUDYT\MarTech\tableforu\20260415_tableforu_podsumowanie.docx
```

**Python do generowania DOCX/PDF:**
```
"C:/Program Files/Python310/python.exe" generate_docs.py
```

**NIGDY** nie zapisuj audytów w innych lokalizacjach. NIGDY w Documents bezpośrednio ani folderach tymczasowych.

---

## Jak uruchomić
Użytkownik pisze `/martech-audit` lub prosi o audyt GA4/MarTech.

---

## KROK 0 — Ustal zakres audytu (ZAWSZE jako pierwszy krok)

Zanim zapytasz o dane klienta, ustal zakres:

### Pytania wstępne

1. **Ile kont GA4 / Google Ads podlega audytowi?**
   - Jedno konto → tryb standardowy (jeden audyt)
   - Więcej niż jedno → **tryb multi-konto** (każde konto jako osobny akapit)

2. **Czy to konto agencji / MCC (Manager Account)?**
   - Jeśli TAK → aktywuj tryb MCC: tabela przestawna na początku + sekcja 0 + BCG cross-account
   - Jeśli NIE → standardowy audyt jednego konta

3. **Jakie pliki wyjściowe generujemy?**
   - **ZAWSZE generuj 2 pliki:**
     - `{nazwa}_{data}_podsumowanie.docx` — krótki raport (2–3 strony A4), tabela przestawna, kluczowe problemy, action plan
     - `{nazwa}_{data}_audyt.docx` — szczegółowy raport, pełna analiza per sekcja i per konto

### Tryb multi-konto — zasady i struktura dokumentów

Gdy audytujesz więcej niż 1 konto GA4 lub Google Ads, raporty mają inną strukturę niż dla 1 konta:

#### PLIK 1 — Podsumowanie (krótki, 2–4 strony)

```
CZĘŚĆ 0 — Tabela przestawna wszystkich kont
  0.1 Dane portfela
  0.2 Tabela przestawna (Konto | Wydatki | ROAS | Konwersje | Brak konw. | Niski ROAS | Wysoki CPA | Niski QS | GA4 | Status)
  0.3 Wyniki kampanii per konto
  0.4 Segmentacja portfela + Top 5 problemów

CZĘŚĆ 0B — Analiza błędów powtarzalnych (cross-account patterns)  ← KLUCZOWE
  → Które błędy i problemy powtarzają się u >1 klientów
  → Macierz powtarzalności błędów

CZĘŚĆ I — Wyniki i wnioski zbiorcze
  → Tabela wyników sekcji (zagregowana)
  → Kluczowe wnioski

CZĘŚĆ III — Action Plan (3 horyzonty)
  → Rekomendacje per klient (z oznaczeniem priorytetu)
```

#### PLIK 2 — Raport szczegółowy (długi, bez ograniczeń)

```
CZĘŚĆ 0 — Tabela przestawna (kopiuj z Pliku 1)
CZĘŚĆ 0B — Analiza błędów powtarzalnych (rozszerzona)

--- ROZDZIAŁ PER KLIENT ---
Dla każdego audytowanego konta:

## KLIENT [N] — [Nazwa klienta]
[Pełny audyt MarTech — IDENTYCZNY jak dla 1 konta, Sekcje 1–10:]
  Sekcja 1 — Audyt Wstępny
  Sekcja 2 — ePrivacy / Consent Mode
  Sekcja 3 — Konfiguracja (GTM, GA4 admin)
  Sekcja 3K — BigQuery Export (jeśli dostępny)
  Sekcja 4 — Data Quality
  Sekcja 5 — UTM
  Sekcja 6 — Macierz BCG (e-commerce)
  Sekcja 7 — Lejki per kampania (e-commerce)
  Sekcja 8 — Spójność GA4 ↔ Google Ads
  Sekcja 9 — Analiza danych
  Sekcja 10 — Audyt Google Ads

## KLIENT [N+1] — [Nazwa klienta]
[to samo co wyżej]

--- ZAKOŃCZENIE ---
CZĘŚĆ 3 — Konta nieaktywne (tabela: Nr | Nazwa | ID konta | Status | Rekomendacja)
CZĘŚĆ 4 — Podsumowanie wykonawcze MCC (globalne statystyki + TOP 5 kont + priorytety)
CZĘŚĆ KOŃCOWA — Rekomendacje zbiorcze
```

**Kluczowa zasada:** każdy klient = pełny audyt MarTech. Nie skracaj sekcji 1–9 tylko dlatego, że to tryb multi-konto. Każdy klient ma być przeanalizowany tak jakby był jedynym klientem w audycie.

**REGUŁA KOMPLETNOŚCI (tryb MCC z >10 kont):** Plik 2 musi zawierać sekcję per konto dla KAŻDEGO aktywnego konta z wydatkami — nie tylko top N kont. Nawet konto z 200 PLN wydatków/msc dostaje pełną sekcję: metryki, tabela kampanii, GA4, błędy, tracking, sugestie, ocena. NIE stosuj "tabeli skróconej" zamiast sekcji per konto — to ogranicza głębokość raportu do ~20% możliwości. Wzorzec: Invette_audit_v2.md — 94 aktywne konta, każde = pełna strona opisu.

**NOTACJA ROAS:** BDOS v2 wyświetla ROAS jako "X%" gdzie X to faktyczny mnożnik (np. "9%" = 9x ROAS, "105%" = 105x ROAS, "1%" = 1x ROAS). W raportach ZAWSZE używaj notacji z mnożnikiem: 9x, 105x, 1x — NIGDY nie przepisuj "%" z BDOS dosłownie. Weryfikacja: conv_value / cost = ROAS-mnożnik (np. 577 791 / 66 325 = 8.7x ≈ "9%" w BDOS).

**REGUŁA KONT NIEAKTYWNYCH:** Plik 2 musi zawierać sekcję kont nieaktywnych (CZĘŚĆ 3) — tabelę wszystkich kont w MCC z zerowym wydatkiem w ostatnich 30 dniach. Format: Nr | Nazwa | ID | Status | Rekomendacja. Minimalnie: zarchiwizuj / przerwa sezonowa / wymaga weryfikacji z klientem.

---

#### Analiza błędów powtarzalnych — jak ją przeprowadzić

Po zebraniu danych dla wszystkich klientów, przed pisaniem rozdziałów per klient, wykonaj analizę cross-account:

**Krok A — zidentyfikuj błędy wspólne:**

Dla każdego z poniższych błędów/problemów, policz ile klientów go ma:

| Obszar | Błąd / Problem | Klienci z tym błędem | % klientów |
|--------|---------------|---------------------|------------|
| GA4 | Brak połączenia GA4 ↔ Ads | N | % |
| GA4 | Brak GA4 lub brak dostępu | N | % |
| ePrivacy | Brak Consent Mode v2 | N | % |
| GTM | Duplikacja tagów GA4 | N | % |
| Data Quality | Udział (not set) > 20% | N | % |
| UTM | Nieoznaczone źródła ruchu | N | % |
| Google Ads | Niski QS (< 5.0) | N | % |
| Google Ads | Kampanie bez konwersji | N | % |
| Google Ads | Brak Enhanced Conversions | N | % |
| Google Ads | Błędy w konfiguracji konwersji | N | % |
| Google Ads | Brak Customer Match | N | % |
| Google Ads | Manual CPC zamiast smart bidding | N | % |
| Google Ads | Brak brand campaign | N | % |
| Feed | Brak GTIN w feedzie | N | % |
| Feed | Niezoptymalizowane tytuły | N | % |

**Krok B — macierz powtarzalności:**

Wygeneruj tabelę: Błąd × Klient — zaznacz który klient ma który błąd:

```
| Błąd/problem         | Klient1 | Klient2 | Klient3 | ... | Razem |
|----------------------|---------|---------|---------|-----|-------|
| Brak GA4↔Ads         | ❌      | ✅      | ❌      |     | 2/N   |
| Brak Consent Mode v2 | ❌      | ❌      | ✅      |     | 2/N   |
| Niski QS             | ✅      | ❌      | ❌      |     | 1/N   |
```

**Krok C — wnioski z powtarzalności:**

Błędy u >50% klientów = problem systemowy agencji / wspólna przyczyna (np. ten sam szablon GTM, ten sam CMP, ta sama agencja deweloperska)

Błędy u 1 klienta = problem indywidualny, dedykowana rekomendacja

---

### Tryb pojedynczy (1 konto)

Standardowy przebieg KROK 1–6. Sekcja 0 → pomiń (jest zbędna dla 1 konta). Generuj 2 pliki (podsumowanie + szczegółowy).

---

## Twoja rola

Jesteś ekspertem od analityki marketingowej, implementacji GA4 i architektury pomiaru. Przeprowadzasz kompleksowy audyt techniczny i jakościowy konta GA4. Piszesz raport w języku polskim, zrozumiałym dla dyrektora lub właściciela firmy — nie tylko dla osoby technicznej.

---

## KROK 1 — Zbierz informacje wejściowe

Zanim zaczniesz audyt, zapytaj o:

1. **Nazwa klienta / agencji** (do nazwy pliku)
2. **Liczba kont do audytu** — jedno czy wiele (MCC/multi-konto)?
   - Jeśli wiele → zbierz dane dla każdego: ID konta Google Ads + GA4 Property ID
3. **GA4 Property ID** (format: `123456789`) — dla każdego konta osobno
4. **Google Ads Customer ID** (format: `123-456-7890`) — dla każdego konta osobno; jeśli MCC — podaj MCC ID
5. **URL strony** (lub URL sklepów) — do manualnej weryfikacji; jeśli wiele kont → URL per konto
6. **Typ biznesu per konto**: e-commerce / lead gen / SaaS / inne
   - Jeśli mix (np. kilka kont e-commerce + kilka lead gen) → oznacz typ przy każdym koncie
7. **Dostęp do GA4 API**: Czy masz service account lub OAuth token? (tak/nie)
8. **Dostęp do GTM**: Czy masz dostęp do kontenera GTM? Jeśli tak, podaj Container ID
9. **BigQuery dataset ID**: Czy masz dostęp do BigQuery z eksportem GA4? Jeśli tak, podaj project GCP i dataset ID (np. `projekt-123.analytics_456789`)
10. **Platforma CMP**: Jaki system zarządzania zgodami? (Cookiebot / OneTrust / Usercentrics / Piwik PRO / własne / brak?)

Jeśli użytkownik jawnie napisze, że nie ma danego dostępu — **pomijasz ten obszar** i zaznaczasz to w raporcie jako "Nie zweryfikowano — brak dostępu".

---

## KROK 2 — Wykryj typ biznesu

Na podstawie zdarzeń w GA4 i URL strony oceń typ biznesu:

- **E-commerce**: są zdarzenia `purchase`, `add_to_cart`, `view_item` → pełny audyt e-commerce
- **Lead gen**: są zdarzenia `generate_lead`, `form_submit`, lub konwersje na strony /kontakt, /dziekujemy → pomijasz zdarzenia e-commerce, sprawdzasz zdarzenia leadowe
- **SaaS**: rejestracja, trial, upgrade → dostosuj sekcję zdarzeń

Zaznacz w raporcie rozpoznany typ i czy to wpłynęło na zakres audytu.

---

## KROK 2.5 — Automatyczna weryfikacja przez GA4 API

Przed audytem manualnym użyj narzędzia `mcp__ga4-analytics` aby zebrać dane automatycznie. Wyniki zachowaj — posłużą jako dowody w raporcie.

### Połączenia i konfiguracja (sprawdź przez API — nie pytaj użytkownika)

```
get_property_schema(property_id) → sprawdź dostępne wymiary i metryki
```
Na tej podstawie:
- Zidentyfikuj czy property jest e-commerce (obecność `itemId`, `itemRevenue`, `transactionId`)
- Sprawdź czy jest User-ID (wymiar `userId` w schemacie)
- Zidentyfikuj niestandardowe wymiary (custom dimensions)

### Dane do pobrania automatycznie

```
# 1. Zdarzenia — jakie są wdrożone (ostatnie 30 dni)
get_ga4_data(
  dimensions=["eventName"],
  metrics=["eventCount", "eventCountPerUser"],
  date_from="30daysAgo"
)
→ Wynik: lista wszystkich zdarzeń + ich częstotliwość

# 2. Jakość źródeł ruchu — (not set) check
get_ga4_data(
  dimensions=["sessionSource", "sessionMedium"],
  metrics=["sessions", "transactions", "purchaseRevenue"],
  date_from="30daysAgo"
)
→ Wynik: udział (not set), dominant direct, anomalie

# 3. Produkty — jakość danych e-commerce
get_ga4_data(
  dimensions=["itemId", "itemName", "itemCategory"],
  metrics=["itemsViewed", "itemsPurchased", "itemRevenue"],
  date_from="30daysAgo"
)
→ Wynik: % (not set) w itemId, item_name — weryfikacja DataLayer

# 4. Kanały → lejek zakupowy
get_ga4_data(
  dimensions=["sessionDefaultChannelGroup"],
  metrics=["sessions", "addToCarts", "checkouts", "ecommercePurchases", "purchaseRevenue"],
  date_from="30daysAgo"
)
→ Wynik: lejek per kanał dla Sekcji 7

# 5. Transakcje — weryfikacja duplikacji (metodologia 3-krokowa)

## Krok 1 — Pobierz surową liczbę purchase events
get_ga4_data(
  dimensions=["sessionDefaultChannelGroup"],
  metrics=["ecommercePurchases"],
  date_from="30daysAgo"
)
→ Zsumuj ecommercePurchases across all channels = total_raw
→ To jest RAW liczba zdarzeń purchase (bez deduplicacji)

## Krok 2 — Pobierz unikalne transaction IDs
get_ga4_data(
  dimensions=["transactionId"],
  metrics=["transactions", "ecommercePurchases", "purchaseRevenue"],
  date_from="30daysAgo",
  limit=2000
)
→ total_rows_in_source = liczba unikalnych transactionId w bazie
→ Podziel wiersze na:
    - ecommercePurchases=1, revenue>0 → zakupy z ważnym transactionId (count_valid)
    - ecommercePurchases=0, revenue<0 → zwroty/refundy (count_refunds)
    - ecommercePurchases=0, revenue=0 → transakcje zerowe lub anulowania
→ Zidentyfikuj konkretne przykłady transactionId z problemami:
    - Malformed ID (zawiera &, =, spacje w stringu)
    - ID z ujemnym revenue = zwroty
    - Wzorzec numeryczny (czy ID są czyste liczbowo?)

## Krok 3 — Oblicz wskaźniki i zweryfikuj deduplicację GA4
- % transakcji bez transactionId = (total_raw - count_valid) / total_raw × 100%
- Sprawdź czy GA4 deduplicuje: jeśli wszystkie wiersze w kroku 2 mają transactions=1 → GA4 deduplicuje metryke
- Stosunek zwrotów = count_refunds / (count_valid + count_refunds) × 100%
- Jeśli stosunek zwrotów > 20% → nieprawidłowe śledzenie refundów lub Shoper wysyła zdarzenia dla anulowań

## Przykłady do raportu (zawsze podawaj)
- min. 5 konkretnych transactionId z ujemnym revenue (zwroty)
- Szacowana wartość straconych/niezidentyfikowanych zakupów (count_not_set × avg_AOV)
- Wyraźne stwierdzenie czy GA4 deduplicuje (tak/nie) na podstawie transactions=1 per row
```

# 6. Analiza geograficzna — Top cities
get_ga4_data(
  dimensions=["city"],
  metrics=["sessions", "ecommercePurchases", "purchaseRevenue"],
  date_from="30daysAgo",
  limit=20,
  proceed_with_large_dataset=True
)
→ Top 15-20 miast po sesjach
→ Oblicz CR per miasto = ecommercePurchases / sessions
→ Oblicz AOV per miasto = purchaseRevenue / ecommercePurchases
→ Szukaj anomalii: miasto z CR >>2× średniej konta, miasto z AOV <<50% średniej
→ Sprawdź czy miasto siedziby firmy/agencji generuje wysoki ruch (wewnętrzny ruch niezfiltrowany)
```

### Połączenie GA4 ↔ Google Ads — weryfikacja automatyczna

Sprawdź przez `get_property_schema` lub dedykowane narzędzie:
- Czy `sessionGoogleAdsAdGroupName` jest dostępnym wymiarem → potwierdza aktywne połączenie GA4↔Ads
- Czy `sessionCampaignId` jest dostępny → potwierdza import danych z Ads
- Jeśli wymiary Google Ads NIE są dostępne → zaznacz błąd 3.68 (brak połączenia) bez pytania użytkownika

---

## KROK 3 — Weryfikacja warunkowa (przed audytem)

### GTM Server Side
Sprawdź w tagu GA4 Configuration w GTM czy jest ustawione pole `server_container_url`. Jeśli NIE ma — **pomiń całą sekcję GTM Server Side**. Jeśli jest — sprawdź czy masz dostęp do kontenera serwera. Jeśli nie masz dostępu — zaznacz "Nie zweryfikowano" i przejdź dalej.

### BigQuery Export
Weryfikuj automatycznie przez API (nie pytaj użytkownika): GA4 → Admin → Połączone usługi → BigQuery. Jeśli eksport jest aktywny — przeprowadź pełną **Sekcję 3K** (BigQuery Audit). Jeśli brak eksportu → zaznacz 3.70 jako ❌ i pomiń sekcję 3K.

### Integracje opcjonalne (LinkedIn, Pinterest, Meta, YM, Clarity, TikTok)
Nie zakładaj z góry co jest wdrożone. Podczas audytu manualnego sprawdź w DevTools → Network jakie requesty wychodzą ze strony. Zidentyfikuj wdrożone narzędzia i zaraportuj co znalazłeś. Punkty dotyczące narzędzi, których nie wykryłeś na stronie — pomijasz lub oznaczasz ➖ Nie dotyczy.

---

## KROK 4 — Przeprowadź audyt

Przejdź przez każdą sekcję. Dla każdego punktu:
- Oceń: **✅ OK** / **❌ Błąd** / **⚠️ Do weryfikacji** / **➖ Nie dotyczy** / **🔒 Brak dostępu**
- Napisz krótki komentarz przy każdym odchyleniu
- Policz punkty na bieżąco

### ZASADA: Jeden kod GA4 na stronie

**Zawsze rekomenduj, żeby na stronie był tylko jeden aktywny tag GA4.** Więcej niż jeden tag GA4 (np. przez dwa kontenery GTM, lub GTM + hardcoded snippet) powoduje:
- Podwójne lub wielokrotne wysyłanie zdarzeń (purchase, page_view, add_to_cart)
- Fałszywe zawyżenie wszystkich metryk (sesje, konwersje, przychód)
- Błędną optymalizację Smart Bidding w Google Ads (jeśli importuje konwersje z GA4)
- Trudności z debugowaniem (nie wiadomo który tag strzela)

Szczególnie uważaj na platformy e-commerce (Shoper, WooCommerce, Shopify, PrestaShop) — wiele z nich wstrzykuje własny kontener GTM lub własny snippet GA4 niezależnie od kontenera właściciela sklepu. Weryfikuj liczbę aktywnych tagów GA4 przez analizę HTML strony i porównanie ID kontenerów GTM.

---

### ZASADA: Zawsze podawaj konkretne przykłady

**Komentarz bez przykładu jest niepełny.** Dla każdego wykrytego problemu lub potwierdzenia obowiązuje:

| Typ problemu | Wymagany przykład |
|---|---|
| Duplikacja transakcji | (1) ecommercePurchases raw vs count distinct transactionId — czy GA4 deduplicuje (transactions=1 per row?); (2) % zakupów bez transactionId = (raw - count_valid_TID) / raw; (3) min. 5 przykładów transactionId z ujemnym revenue (zwroty); (4) stosunek refundów do zakupów |
| Fragmentacja UTM | Lista wszystkich wariantów źródeł (np. `facebook`, `facebook.com`, `m.facebook.com`) z liczbą sesji każdego |
| Referral — bramki pocztowe / płatności | Lista domen z liczbą sesji i transakcji np. `poczta.onet.pl (637 sesji, 0 transakcji)` |
| (not set) w wymiarach | % i liczba bezwzględna dla każdego wymiaru z problemem |
| Błąd DataLayer | Faktyczna struktura z błędem: np. `{event: "purchase", ecommerce: {transaction_id: "210035&key=abc"}}` |
| Błędna kolejność skryptów | Wypisz kolejność 1/2/3 jak faktycznie wygląda w HTML `<head>` |
| Nieoznaczone konwersje | Lista brakujących zdarzeń z uzasadnieniem biznesowym |
| Kanały/integracje | Wymień konkretne narzędzia z ID i statusem, nie "wykryto narzędzia" |
| Anomalia w lejku | Konkretne liczby: `purchase (7 616) > begin_checkout (5 874) = 129.7%` |
| AOV/przychód | Konkretne wartości: `AOV (not set) = 749 PLN vs średnia konta = 1 264 PLN` |

**Przykładowe złe vs dobre sformułowanie:**
- ❌ ZŁE: *"Wykryto duplikację transaction ID"*
- ✅ DOBRE: *"Ratio ecommercePurchases:transactions = 3.53 — każda transakcja wyzwala zdarzenie purchase średnio 3.5 razy. Transakcje z (not set) jako transaction_id: 452 eventów (6% całości). Przykłady malformed ID: `210035&key=1abe2783234b4109f15a80bdd3246c14` — parametr URL wchodzi w skład transaction_id"*

- ❌ ZŁE: *"Meta ma niejednorodne UTM"*
- ✅ DOBRE: *"Wykryto 5 wariantów źródła dla Meta: `facebook` (184 372 sesji), `facebook.com` (38 291), `m.facebook.com` (19 440), `l.facebook.com` (8 218), `lm.facebook.com` (1 216). Razem 251 537 sesji rozbitych na 5 wierszy — GA4 traktuje je jako osobne źródła"*

---

## KROK 5 — Briefing końcowy

Po zakończeniu weryfikacji wszystkich sekcji:
1. Przedstaw listę pytań doprecyzowujących (rzeczy, których nie udało się zweryfikować automatycznie lub które wymagają kontekstu od klienta)
2. Poczekaj na odpowiedzi
3. Uzupełnij audyt o informacje z briefingu
4. Dopiero WTEDY generuj finalny raport

---

## KROK 6.5 — Analiza BCG i lejków _(tylko e-commerce z feedem i GA4)_

> Wykonaj ten krok PRZED generowaniem raportu DOCX. Warunek wejścia: typ biznesu = e-commerce + kampanie Shopping lub PMax z feedem + dostęp do GA4.

---

### SEKCJA 6 — Macierz BCG

**Cel:** Ocenić czy struktura kampanii (podział budżetów, wykluczenia, asset groups) jest zgodna z potencjałem sprzedażowym produktów.

**Dane wejściowe:**
- Google Ads: `shopping_performance` per `product_item_id`, 30d — metryki: `cost`, `conv_value`, `conversions`, `clicks`, `impressions`
- GA4: `run_report(dimensions=["itemId","itemName"], metrics=["itemsViewed","itemsAddedToCart","itemsPurchased","itemRevenue"], date_from="30daysAgo")` — dwa wywołania: wszystkie kanały + filtr `sessionMedium = cpc`

**Klasyfikacja BCG:**
1. Oblicz `revenue_share` każdego produktu = jego conv_value / total_conv_value konta × 100%
2. Oblicz `roas` każdego produktu = conv_value / cost
3. Wyznacz mediany obu wskaźników dla konta
4. Przypisz kwadrant:
   - revenue_share ≥ mediana + roas ≥ mediana → **⭐ Gwiazda**
   - revenue_share ≥ mediana + roas < mediana → **🐄 Dojna Krowa**
   - revenue_share < mediana + roas ≥ mediana → **❓ Znak Zapytania**
   - revenue_share < mediana + roas < mediana → **🐕 Pies**
   - brak transakcji → **⚫ Nieaktywny**

**Mapowanie GA4 → BCG:**
- Klucz łączący: `itemId` (GA4) ↔ `product_item_id` (Google Ads). Normalizuj: `str(id).lower().rstrip('_').strip()`
- Agreguj metryki GA4 per kwadrant BCG: `purchase_rate = purchased / max(viewed, 1) × 100`, `cart_rate = added_to_cart / max(viewed, 1) × 100`

**Delta Ads vs GA4:**
- `delta_pct = (ads_revenue_segment - ga4_cpc_revenue_segment) / ads_revenue_segment × 100`
- Progi: ≤15% ✅ dane spójne | 15–30% ⚠️ sprawdź okno atrybucji | >30% 🔴 problem z konfiguracją e-commerce tracking lub konwersji
- Typowe przyczyny dużej delty: GA4 Cross-network nie jest w filtrze CPC, różne okna atrybucji (Google Ads 30d klik vs GA4 7d), brak `items[]` array w zdarzeniu `purchase`

**Psy organiczne:**
- Produkt = Dog w Google Ads (niski ROAS) + GA4 all-channels revenue > 50 PLN
- Interpretacja: produkt sprzedaje się organicznie, ale Ads nie dowozi — możliwy błąd w strukturze kampanii (np. produkt wykluczony z właściwej grupy) lub po prostu nie wymaga wsparcia płatnego

**Punktacja (max 9 pkt):**
- Gwiazdy w osobnych kampaniach lub asset groups z wyższym target ROAS: 3 pkt
- Dojne Krowy z ograniczonym target ROAS lub CPC cap (nie palą budżetu bez sensu): 2 pkt
- Psy wykluczone lub stanowią < 5% budżetu kampanii feedowych: 2 pkt
- Znaki Zapytania w wydzielonym teście (osobna kampania / asset group / niższy budżet): 2 pkt

---

### SEKCJA 7 — Lejki zachowań per typ kampanii

**Cel:** Zidentyfikować na którym etapie ścieżki zakupowej odpada ruch z poszczególnych typów kampanii — i ocenić jakość tego ruchu.

**Warunek:** GA4 musi mieć wdrożone 4 zdarzenia: `view_item`, `add_to_cart`, `begin_checkout`, `purchase`. Sprawdź wcześniej w SEKCJI 4 (Data Quality → zdarzenia e-commerce).

**Jak zbierać dane:**
1. Per kanał (sessionDefaultChannelGroup): `run_report(dimensions=["sessionDefaultChannelGroup"], metrics=["itemsViewed","itemsAddedToCart","itemsPurchased","itemRevenue","ecommercePurchases"])`
2. Begin_checkout per kanał: osobne wywołanie z `eventName = begin_checkout` + `sessionDefaultChannelGroup` — lub szacuj z `begin_checkout` event count
3. Paid Search = filtr `sessionMedium = cpc` lub kanał "Paid Search"
4. Shopping = kanał "Paid Shopping"
5. Performance Max = kanał "Cross-network" lub "Paid Shopping" + "Paid Search" łącznie (PMax jest w wielu kanałach GA4)

**Oblicz przejścia lejka per kanał:**
- `view→cart` = add_to_cart / view_item × 100%
- `cart→checkout` = begin_checkout / add_to_cart × 100%
- `checkout→purchase` = purchase / begin_checkout × 100%
- `CR całkowity` = purchase / view_item × 100%

**Benchmarki e-commerce PL:**
| Przejście | Benchmark |
|-----------|-----------|
| view_item → add_to_cart | 5–20% (wyższy = lepszy) |
| add_to_cart → begin_checkout | 30–60% |
| begin_checkout → purchase | 50–80% |
| CR całkowity (view→purchase) | 0,3–2% |

**Interpretacja:**
- Niski `view→cart` dla kanału płatnego: reklamy przyciągają ruch niedopasowany do intencji zakupowej — problem z targetowaniem lub landing page
- Niski `cart→checkout`: problem UX koszyka lub nadmiarowe kroki przed kasą
- Niski `checkout→purchase`: problem z bramką płatności, brak metod płatności, zbyt wysoki koszt dostawy
- CR paid < 50% CR organic: ruch płatny jest słabej jakości lub strona docelowa jest niedopasowana

**Punktacja (max 8 pkt):**
- Wszystkie 4 zdarzenia e-commerce wdrożone i spójne: 2 pkt
- CR paid ≥ 50% CR organic: 2 pkt
- Brak kanału z CR < 0,1% przy wydatkach > 1000 PLN/mies.: 2 pkt
- Checkout drop-off ≤ 40% (begin_checkout → purchase ≥ 60%): 2 pkt

---

## KROK 6.8 — Audyt Google Ads _(jeśli klient ma konto Google Ads w BDOS)_

> Wykonaj ten krok PRZED generowaniem raportu DOCX. Warunek wejścia: klient ma konto Google Ads w rejestrze BDOS i audytor ma dostęp.

**Jak pobrać dane przez BDOS:**

```python
import sys; sys.stdout.reconfigure(encoding='utf-8')
from bdos import connect
ctx = connect("alias")

# 1. Lista kampanii (bez metryk — widzisz też zerowe/nowe)
all_campaigns = ctx.engine.execute(entity="campaigns", metrics=[], filters=["status = ENABLED"])
print(f"Kampanii aktywnych: {len(all_campaigns.data)}")

# 2. Performance kampanii 30 dni
perf = ctx.engine.execute(entity="campaigns", days=30, filters=["cost > 0"])
for c in sorted(perf.data, key=lambda x: -x.get('cost', 0))[:20]:
    print(f"{c['name'][:50]:50} | {c.get('cost',0):8.0f} PLN | ROAS {c.get('roas',0):.1f}x | conv {c.get('conversions',0):.0f}")

# 3. Kampanie z 0 konwersji ale z wydatkami
no_conv = [c for c in perf.data if c.get('conversions', 0) == 0 and c.get('cost', 0) > 500]
for c in no_conv:
    print(f"BRAK KONWERSJI: {c['name']} | {c.get('cost',0):.0f} PLN wydatków")

# 4. PMax asset groups
pmax = ctx.engine.execute(entity="pmax_assets", metrics=[])

# 5. Shopping performance per produkt
shopping = ctx.engine.execute(entity="shopping_performance", days=30, filters=["metrics.cost_micros > 0"])
print(f"Produkty z wydatkami: {len(shopping.data)}")
for p in sorted(shopping.data, key=lambda x: -x.get('cost', 0))[:15]:
    print(f"  {p.get('product_title','')[:40]:40} | {p.get('cost',0):.0f} PLN | ROAS {p.get('roas',0):.1f}x | bcg?")

# 6. Geo targeting
geo = ctx.engine.execute(entity="geo_settings", metrics=[])

# 7. Konwersje — przez GAQL bezpośredni
from bdos.core.client import GoogleAdsClient
# Sprawdź konwersje przez dedicated query — szczegóły w SEKCJI 10B
```

**Checklist KROK 6.8 — co sprawdzić per punkt:**

| # | Punkt | Jak sprawdzić | Czerwona flaga |
|---|-------|---------------|----------------|
| 1 | Konwersje Primary/Secondary | Panel Google Ads → Konwersje | Brak Primary; stała wartość "1" |
| 2 | Duplikacja śledzenia | Lista konwersji: tag Ads + import GA4 tej samej akcji | Dwie konwersje "purchase" z różnych źródeł |
| 3 | Enhanced Conversions | Panel → Ustawienia konwersji | Wyłączone = strata danych after cookies |
| 4 | Learning period | `perf.data` → `status` / panel | >3 kampanie w Learning >14 dni |
| 5 | Target ROAS vs osiągany | ROAS target w campaign settings vs ROAS z perf | Target 2× wyższy niż osiągany = blokada |
| 6 | Brand IS | Panel → Search campaigns → IS columns | Brand IS < 70% = ochrona marki za słaba |
| 7 | PMax typ | `pmax_assets` + listing group structure | Mixed PMax = trudny do audytu per segment |
| 8 | Geo | `geo_settings` → location_type | PRESENCE_OR_INTEREST = nieprecyzyjne |
| 9 | Auto-apply | Panel → Rekomendacje → Auto-apply | Włączone = Google sam zmienia kampanie |
| 10 | ROAS < 1× | `perf.data` → roas < 1 i cost > 500 | Kampania kosztuje więcej niż zarabia |

**Zasada podawania przykładów (tak samo jak w GA4):**
- ❌ ZŁE: *"Kampanie mają niski ROAS"*
- ✅ DOBRE: *"3 kampanie poniżej progu rentowności: [PMax] Wszystkie produkty — ROAS 0.8x (wydatki 4 230 PLN, conv_value 3 380 PLN); [Search] Generic — ROAS 0.6x (wydatki 1 180 PLN, conv_value 712 PLN). Razem 5 410 PLN wydatków generuje 4 092 PLN przychodów — strata ~1 318 PLN/mies."*

---

## KROK 6.9 — Konta nieaktywne i statystyki globalne MCC _(tylko tryb MCC)_

> Wykonaj po zakończeniu analizy per konto. Wymagany w każdym audycie MCC.

### Konta nieaktywne (0 wydatków w ostatnich 30 dniach)

Utwórz tabelę wszystkich kont z zerowym budżetem. Źródło: BDOS MCC — lista kont z `cost = 0` w ostatnich 30 dniach.

```
| # | Nazwa konta | ID konta | Status | Rekomendacja |
|---|------------|---------|--------|--------------|
| 1 | | | ⛔ Brak aktywności | Zarchiwizuj / Przerwa sezonowa / Wymaga weryfikacji |
| 2 | | | | |
```

**Rekomendacje per typ:**
- Konto z wydatkami historycznie → przerwa sezonowa lub wstrzymane przez klienta
- Konto bez historii wydatków → nigdy nie uruchomione, weryfikacja kontraktu
- Konto starsze niż 6 miesięcy bez aktywności → zarchiwizuj w BDOS

### Globalne statystyki MCC (executive summary)

Agreguj dane ze wszystkich aktywnych kont — umieść w CZĘŚCI 4 raportu:

| Metryka | Wartość |
|---------|---------|
| Łączne wydatki 30d (wszystkie aktywne) | PLN |
| Łączne kliknięcia | |
| Łączne konwersje | |
| Łączna wartość konwersji | PLN |
| Średni ROAS portfela (konta e-comm) | x |
| Kont aktywnych (z wydatkami) | |
| Kont nieaktywnych | |
| Kont z problemami krytycznymi (ROAS < 2x lub 0 konwersji) | |
| Kont bez problemów | |

**TOP 5 kont wg wydatków:**

| # | Konto | Wydatki | ROAS | Konwersje |
|---|-------|---------|------|-----------|
| 1 | | PLN | x | |
| 2 | | PLN | x | |

**Priorytety działań pilnych (do tygodnia):**
- Format: `[Konto]: problem — zalecane działanie`
- Kryterium: konta z 0 konwersjami > 500 PLN wydatków + konta z ROAS < 1x

---

## KROK 6 — Wygeneruj raporty DOCX (ZAWSZE DWA PLIKI)

**Każdy audyt generuje dwa oddzielne pliki DOCX + PDF każdy:**

### Plik 1 — Podsumowanie (krótki)
**Nazwa:** `{RRRRMMDD}_{nazwa_klienta}_podsumowanie.docx`
**Objętość:** 2–3 strony A4
**Zawartość:**
1. Nagłówek: klient, data, okres, audytor
2. **Tabela przestawna kont** (tryb multi-konto) lub tabela KPI (tryb pojedynczy):
   - Kolumny: Konto | Wydatki | ROAS | Konwersje | Brak konw. | Niski ROAS | Wysoki CPA | Niski QS | Status
   - Każda flaga: ✅/⚠️/🔴
3. **Segmentacja problemów** — lista problemów posortowana od najpoważniejszego:
   - 🔴 Krytyczne (niski ROAS e-commerce, zero konwersji)
   - ⚠️ Uwaga (kampanie bez konwersji, niski QS, anomalie GA4)
   - ℹ️ Do omówienia (lead gen bez wartości, nieaktywne konta)
4. **Wyniki sekcji** — tabela procentowa (tylko sumy, bez detali)
5. **Action plan** — 3 fazy: Natychmiast (0–7 dni) / Miesiąc 1 / Miesiąc 2–3

### Plik 2 — Raport szczegółowy (długi)
**Nazwa:** `{RRRRMMDD}_{nazwa_klienta}_audyt.docx`
**Objętość:** bez ograniczeń — pełna analiza
**Zawartość:**
1. Nagłówek + streszczenie (jak Plik 1)
2. **CZĘŚĆ 0 — Tabela przestawna** (tryb multi-konto)
3. **CZĘŚĆ I — Sekcje GA4** (1–9): pełna analiza per punkt
4. **CZĘŚĆ II — Google Ads per konto** (Sekcja 10):
   - Każde konto = osobna sekcja `### KONTO N — [nazwa konta]`
   - Per konto: metryki → kampanie → GA4 → błędy → śledzenie → ocena specjalisty
5. **CZĘŚĆ III — Rekomendacje** posortowane per priorytet

**Ścieżka zapisu:** `AI/audyt/{nazwa_klienta}/{RRRRMMDD}_{nazwa_klienta}_podsumowanie.docx` i `..._audyt.docx`

Raport jest zawsze w języku polskim, chyba że audytor wyraźnie zdecyduje inaczej.

Użyj narzędzia do tworzenia pliku DOCX (Python `python-docx` lub markdown → DOCX). Jeśli narzędzie nie jest dostępne — zapisz jako MD i poinformuj użytkownika.

---

## System punktacji

| Priorytet | Punkty |
|-----------|--------|
| Wysoki | 3 pkt |
| Średni | 2 pkt |
| Niski | 1 pkt |
| Nie dotyczy / Brak dostępu | 0/0 (pomijasz w mianowniku) |

**Wynik sekcji** = Σ uzyskanych pkt / Σ max pkt × 100%

| Wynik | Ocena |
|-------|-------|
| > 80% | ✅ Zadowalający |
| 49–80% | ⚠️ Wymaga poprawy |
| < 49% | ❌ Krytyczny |

---

## Struktura raportu DOCX

### PLIK 1 — Podsumowanie (2–3 strony A4)

Pisz językiem zrozumiałym dla właściciela lub dyrektora — bez żargonu technicznego.

**Strona 1 — Nagłówek i tabela przestawna:**
1. Klient, data, okres, audytor, liczba kont
2. **Tabela przestawna wszystkich kont** (multi-konto) lub KPI zbiorcze (1 konto):
   `Konto | Wydatki 30d | ROAS | Konwersje | Kamp. bez konw. | Niski ROAS | Wysoki CPA | Niski QS | GA4 | Status`
3. **Segmentacja portfela** (jeśli multi):
   - ✅ OK (N kont) — brak krytycznych problemów
   - ⚠️ Uwaga (N kont) — wymagają obserwacji
   - 🔴 Problem (N kont) — wymagają natychmiastowej interwencji
   - ℹ️ Lead gen (N kont) — brak wartości konwersji, wymaga weryfikacji

**Strona 2 — Wyniki i wnioski:**
4. **Tabela wyników sekcji** — wynik % per sekcja
5. **Top 3–5 problemów** — najważniejsze problemy z całego audytu (z kwantyfikacją: "strata X PLN/msc")
6. **Action plan** — trzy horyzonty:
   - 🔴 Natychmiast (0–7 dni): zatamowanie strat
   - 🟡 Miesiąc 1: optymalizacja i naprawa
   - 🟢 Miesiąc 2–3: skalowanie i strategia

**Strona 3 (opcjonalna) — Ocena specjalistów:**
7. Tabela per konto: Konto | Spec. prowadzący | Ocena ⭐/5 | Komentarz

---

### PLIK 2 — Raport szczegółowy (bez ograniczenia objętości)

**CZĘŚĆ 0 — Tabela przestawna** (tryb multi-konto, jeśli dotyczy — kopiuj z Pliku 1)

**CZĘŚĆ I — Audyt GA4 i infrastruktury:**
Dla każdego punktu audytu (sekcje 1–9):
- Nagłówek punktu
- **Opis** (min. ¼ strony A4): czym jest zagadnienie, dlaczego ważne — dla dyrektora/właściciela
- **Wynik**: ✅/❌/⚠️/➖
- **Komentarz**: konkretne przykłady (patrz ZASADA przykładów)
- **Rekomendacja**: co należy poprawić

**CZĘŚĆ II — Audyt Google Ads per konto (Sekcja 10):**
Dla każdego konta osobny blok:
```
### KONTO [N] — [Nazwa konta]
ID: [customer_id] | GA4: [property_id] | Typ: [e-commerce/lead gen]

#### Wyniki kampanii Google Ads (ostatnie 30 dni)
[tabela metryk konta]

#### Kampanie (ostatnie 30 dni)
[tabela kampanii z ROAS, wydatkami, konwersjami]

#### Analiza GA4
[wyniki lub "brak dostępu"]

#### Błędy w konfiguracji
[lista błędów lub "brak"]

#### Analiza trackingu
[status śledzenia konwersji, Enhanced Conv.]

#### Sugestie i rekomendacje
[1–5 konkretnych działań]

#### Ocena specjalisty prowadzącego konto
⭐⭐⭐ (3/5) — [komentarz]
```

**CZĘŚĆ III — Rekomendacje:**
Lista priorytetowych działań podzielona na:
- 🔴 Pilne (Wysoki priorytet, błędy krytyczne)
- 🟡 Do zaplanowania (Średni priorytet)
- 🟢 Usprawnienia (Niski priorytet)

---

# SEKCJA 0 — Tabela przestawna kont _(tryb multi-konto / MCC)_

> **Warunek:** Wykonaj tę sekcję TYLKO gdy audytujesz więcej niż 1 konto Google Ads lub GA4.
> Dla jednego konta → pomiń Sekcję 0, przejdź do Sekcji 1.

---

## 0.1 — Nagłówek portfela

```
MCC ID / agencja: _______________
Liczba kont łącznie w MCC: ___
Kont z wydatkami (audytowany okres): ___
Kont nieaktywnych: ___
Okres analizy: _______________
```

## 0.2 — Tabela przestawna wszystkich kont (konta aktywne)

**Cel:** Jedno miejsce, gdzie widać cały portfel i gdzie są problemy. Generuj tę tabelę automatycznie z danych Google Ads API przed pisaniem jakiegokolwiek innego komentarza.

```
| # | Konto | Wydatki 30d | ROAS | Konwersje | Kamp. bez konw. | Niski ROAS | Wysoki CPA | Niski QS | GA4 | Status |
|---|-------|------------|------|-----------|-----------------|------------|------------|---------|-----|--------|
| 1 | [nazwa] | PLN | Xx | N | ✅/⚠️ | ✅/🔴 | ✅/🔴 | ✅/🔴 | ✅/❌ | ✅/⚠️/🔴 |
```

**Definicje flag:**
| Flaga | Kolumna | Próg |
|-------|---------|------|
| 🔴 Niski ROAS | Niski ROAS | ROAS < 2x przy e-commerce |
| ⚠️ | Niski ROAS | ROAS 2–3x (akceptowalny ale do poprawy) |
| ✅ | Niski ROAS | ROAS > 3x |
| 🔴 Wysoki CPA | Wysoki CPA | CPA > 2x cel lub brak benchmarku |
| 🔴 Niski QS | Niski QS | Avg QS < 5.0 |
| ⚠️ | Niski QS | Avg QS 5–7 |
| ✅ | Niski QS | Avg QS > 7 |
| ⚠️ | Kamp. bez konw. | ≥ 1 kampania z wydatkami > 300 PLN i 0 konwersji |
| ❌ GA4 | GA4 | Brak połączenia GA4 ↔ Ads lub brak dostępu |

**Legenda statusu konta:**
- ✅ OK — brak krytycznych problemów, ROAS akceptowalny
- ⚠️ Uwaga — 1–2 problemy, wymaga obserwacji
- 🔴 Problem — krytyczny ROAS lub zero konwersji, natychmiastowa interwencja
- ℹ️ Lead gen — brak wartości konwersji (celowe), wymaga weryfikacji z klientem
- 💤 Nieaktywne — zero wydatków w okresie

## 0.3 — Wyniki kampanii — ROAS, CPA, Quality Score (top 50 kont wg wydatków)

```
| # | Konto | Wydatki | Kliknięcia | Konwersje | Wartość konw. | ROAS | CPA | Avg QS | Typy kampanii |
|---|-------|---------|-----------|----------|--------------|------|-----|--------|--------------|
```

## 0.4 — Segmentacja portfela i analiza problemów

Po wygenerowaniu tabeli przestawnej, automatycznie oblicz i przedstaw:

### A) Podział na segmenty

```
✅ OK: N kont (łączne wydatki: PLN)
⚠️ Uwaga: N kont
🔴 Problem: N kont (łączne wydatki na krytycznych: PLN — szacowany koszt strat: PLN)
ℹ️ Lead gen: N kont
💤 Nieaktywne: N kont
```

### B) Lista problemów posortowana od najpoważniejszego

**Wzorzec z Invette — 5 kategorii problemów:**

**1. 🔴 Niski ROAS (<2x) przy wydatkach e-commerce**
```
| Konto | Wydatki | ROAS |
| ...   | PLN     | Xx   |
Łącznie: PLN/msc przy negatywnym lub śladowym zwrocie.
```

**2. ⚠️ Kampanie aktywne bez żadnych konwersji**
```
Lista kont z N kampaniami bez konwersji + łączny koszt drenażu
Rekomendacja: wstrzymaj kampanie z > 300 PLN/msc i 0 konwersji
```

**3. 🔴 Brak jakichkolwiek konwersji na koncie (całkowite)**
```
| Konto | Wydatki | Kampanie aktywne |
```

**4. ℹ️ Brak wartości konwersji (konta lead gen)**
```
Lista kont — weryfikacja czy celowe (usługi) czy błąd konfiguracji
```

**5. 💤 Konta nieaktywne**
```
Lista — weryfikacja kontraktów
```

## 0.5 — Punktacja Sekcji 0

Sekcja 0 nie ma własnych punktów — jest przeglądem diagnostycznym. Wyniki per konto wpływają na Sekcję 10 (Google Ads per konto).

---

---

# SEKCJA 1 — Audyt Wstępny

> Cel: Weryfikacja fundamentów technicznych. To pierwsza linia oceny — sprawdzamy czy podstawowa infrastruktura śledzenia jest zdrowa.

---

### 1.1 Adnotacje w GA4
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Adnotacje to notatki, które analitycy dodają bezpośrednio do osi czasu w Google Analytics, aby zaznaczyć ważne zdarzenia — na przykład: "15 marca wdrożono nową wersję strony", "uruchomiono kampanię Black Friday", "zmieniono strukturę kategorii". Wyobraź sobie, że patrzysz na wykres ruchu i widzisz nagły skok lub spadek. Bez adnotacji nie wiesz, czy to wynik kampanii marketingowej, zmiany technicznej, czy błędu. Adnotacje to "dziennik pokładowy" konta analitycznego. Ich brak oznacza, że firma nie dokumentuje zmian, co dramatycznie utrudnia interpretację danych historycznych i wyciąganie wniosków.

**Jak sprawdzić:** GA4 → Admin → Adnotacje. Sprawdź czy istnieją wpisy i czy są regularnie dodawane.

**Kryterium sukcesu:** Istnieją adnotacje przy kluczowych zmianach technicznych i marketingowych. Brak adnotacji przez ponad 3 miesiące = negatywna ocena.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.2 Kolejność skryptów w kodzie HTML
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Przeglądarka wczytuje kod strony od góry do dołu. Kolejność, w jakiej ładują się skrypty śledzące, ma ogromne znaczenie dla poprawności zbierania danych i zgodności z przepisami. Prawidłowa kolejność to: najpierw zgoda użytkownika na cookies (Consent DataLayer), potem warstwa danych (DataLayer), potem Google Tag Manager, a dopiero po nim inne skrypty. Jeśli piksel reklamowy załaduje się przed pytaniem o zgodę — naruszamy RODO. Jeśli GTM załaduje się po innych tagach — tracimy część danych. To jak kolejność domino: jeden zły krok powoduje błąd w całym łańcuchu.

**Prawidłowa kolejność:**
```
<head>
  1. Consent DataLayer (gtag consent default)
  2. DataLayer push
  3. GTM snippet
  4. Inne tagi (tylko jeśli konieczne hardcoded)
```

**Jak sprawdzić:** Otwórz źródło strony (Ctrl+U). Przeszukaj `<head>`. Sprawdź kolejność pierwszych skryptów.

**Czerwone flagi:** Jakikolwiek skrypt piksela (Meta, Google Ads, LinkedIn) przed GTM lub przed consent. Brak consent DataLayer.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.3 Przegląd wybranych podstron — brak błędów krytycznych
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Ręczny przegląd kluczowych podstron to szybki test zdrowia całego systemu śledzenia. Sprawdzamy czy na stronie nie ma błędów JavaScript (które mogą blokować działanie GTM), błędów sieciowych (kod 404/500 dla plików śledzenia) oraz czy piksele i tagi wywołują się poprawnie. Wiele błędów wdrożeniowych nie jest widocznych z poziomu panelu GA4 — dopiero inspekcja przeglądarki je ujawnia. Minimalny zestaw podstron: strona główna, strona kategorii, strona produktu, koszyk, potwierdzenie zamówienia.

**Jak sprawdzić:** DevTools (F12) → Console (błędy JS) + Network (błędy requestów analitycznych). Sprawdź 5 kluczowych podstron.

**Czerwone flagi:** Czerwone błędy JS w konsoli, requesty do `collect` lub `gtag` ze statusem 4xx/5xx, zduplikowane wywołania page_view.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.4 Google Tag Assistant
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
Tag Assistant to oficjalne narzędzie Google, które analizuje tagi Google (GA4, Google Ads, GTM) i raportuje błędy lub ostrzeżenia. Działa jako rozszerzenie przeglądarki lub przez tagassistant.google.com. Pozwala szybko zobaczyć czy tagi są poprawnie załadowane, czy nie duplikują się i czy działają bez ostrzeżeń. Niski priorytet oznacza, że narzędzie jest pomocnicze — inne metody weryfikacji są ważniejsze, ale brak błędów w Tag Assistant to dobry sygnał.

**Jak sprawdzić:** tagassistant.google.com → Connect → podaj URL strony → sprawdź wyniki dla homepage i 2–3 podstron.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.5 TagHound
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
TagHound (taghound.com) to narzędzie do audytu tagów marketingowych, które skanuje wiele podstron i raportuje: jakie tagi są wdrożone, czy pojawiają się na właściwych podstronach, czy nie ma zduplikowanych tagów. Jest bardziej kompleksowy niż Tag Assistant, bo skanuje całą witrynę, nie tylko jedną stronę. Wysoki priorytet — problemy wykryte przez TagHound często wskazują na systemowe błędy wdrożenia.

**Jak sprawdzić:** Uruchom TagHound dla: homepage, strona kategorii, strona produktu, koszyk. Zwróć uwagę na: tagi pojawiające się na nieoczekiwanych stronach, tagi ładowane wielokrotnie, brakujące tagi na kluczowych stronach.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.6 Consent Mode — wstępna weryfikacja
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Consent Mode to system opracowany przez Google, który pozwala GA4 i Google Ads działać w sposób zgodny z przepisami o ochronie prywatności (RODO/ePrivacy), nawet gdy użytkownik nie wyraził zgody na cookies. Zamiast całkowicie wyłączać śledzenie, Consent Mode wysyła "sygnały zgody" (pings) — anonimowe dane, które Google wykorzystuje do modelowania konwersji. To ważne z dwóch powodów: prawnego (RODO) i biznesowego (bez Consent Mode tracisz do 20-40% danych konwersji). Na tym etapie robimy wstępną weryfikację — pełny audyt jest w Sekcji 2.

**Jak sprawdzić:** Otwórz stronę w trybie incognito. Sprawdź czy pojawia się baner zgody z możliwością personalizacji wyboru.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.7 Brak starych kodów UA na stronie
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
Universal Analytics (UA) — poprzednia wersja Google Analytics — przestała zbierać dane w lipcu 2024 roku. Mimo to, stare kody UA (`UA-XXXXXXXX-X`) lub skrypty `analytics.js` mogą nadal zalegać na stronie. Choć nie zbierają już danych do GA, mogą spowalniać ładowanie strony, generować błędy w konsoli przeglądarki i mylić audytorów. To jak stary alarm, który już nie działa, ale nadal pobiera prąd.

**Jak sprawdzić:** DevTools → Network → filtruj po "analytics.js" lub "UA-". Sprawdź też źródło strony. Upewnij się że jedyne requesty analityczne idą do GA4 (google-analytics.com/g/collect).

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.8 DataLayer — poprawność
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
DataLayer (warstwa danych) to obiekt JavaScript na stronie, który służy jako "przekaźnik informacji" między stroną a GTM. Strona "wrzuca" do DataLayer informacje — np. "użytkownik kliknął przycisk Kup Teraz", "wartość koszyka to 299 zł", "użytkownik ma 25-34 lata" — a GTM odczytuje te dane i przekazuje je do GA4, Google Ads i innych narzędzi. DataLayer jest fundamentem całego systemu śledzenia. Błędy w DataLayer oznaczają, że GA4 dostaje złe lub niekompletne dane — co bezpośrednio wpływa na decyzje marketingowe oparte na tych danych.

**Jak sprawdzić:** DevTools → Console → wpisz `dataLayer` i naciśnij Enter. Sprawdź czy obiekt istnieje i czy push-e mają poprawny format. Sprawdź kilka podstron i akcji (dodanie do koszyka, zakup).

**Czerwone flagi:** `dataLayer is not defined`, puste tablice, push-e bez klucza `event`, błędna struktura obiektów.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.9 DataLayer GA4 — struktura e-commerce
**Priorytet:** Wysoki *(sprawdzaj tylko dla e-commerce)*

**Czym jest i dlaczego sprawdzamy:**
Dane e-commerce w GA4 — takie jak informacje o produktach, wartości zamówień, kategoriach — są przekazywane przez DataLayer w specyficznej strukturze zdefiniowanej przez Google. Każdy produkt w koszyku musi być opisany jako obiekt z polami: `item_id`, `item_name`, `price`, `quantity`, `item_category` itd. Jeśli struktura jest błędna — GA4 nie "rozumie" tych danych i raporty e-commerce będą puste lub błędne. To bezpośrednio uniemożliwia analizę sprzedaży, popularności produktów czy efektywności kampanii.

**Jak sprawdzić:** Na stronie produktu: DevTools → Console → wpisz `dataLayer` → szukaj push z `ecommerce`. Sprawdź czy `items[]` zawiera przynajmniej: `item_id`, `item_name`, `price`. Powtórz na koszyku i potwierdzeniu zamówienia.

**Czerwone flagi:** Brak `ecommerce` w pushu, `items` jest pustą tablicą, brak `price`, brak `item_id`, wartości jako string zamiast number.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 1.10–1.20 Podpięcie innych usług (integracje)

> **Instrukcja dla agenta:** NIE zakładaj z góry co jest wdrożone. Podczas manualnego przeglądu strony w DevTools → Network zidentyfikuj jakie zewnętrzne narzędzia wysyłają requesty. Raportuj tylko to, co wykryłeś. Nieznalezione narzędzia oznacz ➖ Nie dotyczy.

**Czym jest i dlaczego sprawdzamy integracje:**
Strony e-commerce i serwisy marketingowe używają dziesiątek narzędzi śledzących: pikseli reklamowych, narzędzi do nagrywania sesji, platform remarketingowych. Każde z tych narzędzi zbiera dane i musi działać poprawnie, zgodnie ze zgodą użytkownika i bez powielania danych. Naszym zadaniem jest zidentyfikowanie co faktycznie jest wdrożone i sprawdzenie czy działa poprawnie w GTM.

| # | Narzędzie | Priorytet | Jak zidentyfikować | Status | Uwagi |
|---|-----------|-----------|-------------------|--------|-------|
| 1.10 | Google Analytics 360 | Wysoki | GA4 Admin → Połączone usługi → sprawdź licencję 360 | | |
| 1.11 | Google Ads — remarketing | Średni | Network → szukaj `googleadservices.com` lub `googlesyndication.com` | | |
| 1.12 | Konwersje Google Ads w GTM | Wysoki | GTM → Tagi → szukaj "Google Ads Conversion Tracking" | | |
| 1.13 | Meta (Facebook) Pixel | Wysoki | Network → szukaj `facebook.com/tr` lub `connect.facebook.net` | | |
| 1.14 | Meta — API konwersji (CAPI) | Wysoki | GTM → Tagi → szukaj "Facebook Conversions API" lub sGTM client | | |
| 1.15 | LinkedIn Insight Tag | Wysoki | Network → szukaj `snap.licdn.com` | | |
| 1.16 | Pinterest Tag | Wysoki | Network → szukaj `ct.pinterest.com` | | |
| 1.17 | Yandex Metrica | Wysoki | Network → szukaj `mc.yandex.ru` | | |
| 1.18 | Microsoft Clarity | Wysoki | Network → szukaj `clarity.ms` | | |
| 1.19 | Bing/Microsoft Ads | Średni | Network → szukaj `bat.bing.com` | | |
| 1.20 | TikTok Pixel | Wysoki | Network → szukaj `analytics.tiktok.com` lub `tiktok.com/i18n` | | |
| 1.21 | Hotjar | Wysoki | Network → szukaj `static.hotjar.com` lub `hj.js`; sprawdź GTM → szukaj tagu Hotjar | | |
| 1.22 | Criteo | Średni | Network → szukaj `static.criteo.net` lub `dis.criteo.com` lub `bidder.criteo.com` | | |
| 1.23 | RTB House | Średni | Network → szukaj `creativecdn.com` lub `rtbhouse.com` | | |
| 1.24 | Allegro Ads pixel | Średni | Network → szukaj `allegro.pl/biznes/reklama` lub `pixel.allegro.pl` | | |

---

# SEKCJA 2 — ePrivacy / Consent Mode

> Cel: Weryfikacja zgodności z RODO i ePrivacy. Ta sekcja ma wymiar prawny — błędy mogą skutkować karami finansowymi sięgającymi 4% globalnego obrotu firmy. Weryfikujemy zarówno aspekty techniczne jak i biznesowe.

---

### 2.1 Personalizacja wyboru zgód
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
RODO wymaga, aby użytkownik miał możliwość wyboru na jakie kategorie cookies wyraża zgodę. Kategorie to zazwyczaj: niezbędne, analityczne, marketingowe, funkcjonalne. Baner bez kategorii — tylko "Akceptuj wszystkie" i "Odrzuć" — jest niezgodny z duchem RODO, choć formalnie debata prawna trwa. Dobre praktyki branżowe i wytyczne organów ochrony danych w Polsce i UE wskazują na konieczność granularnej zgody.

**Jak sprawdzić:** Odwiedź stronę w incognito → sprawdź baner → czy są kategorie cookies z możliwością indywidualnego wyboru.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.2 Możliwość odrzucenia wszystkich zgód
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
Jeśli istnieje przycisk "Zaakceptuj wszystkie", zgodnie z RODO musi istnieć równoważnie dostępny przycisk "Odrzuć wszystkie". Ukrywanie opcji odrzucenia lub utrudnianie do niej dostępu jest tzw. "dark pattern" — praktyką nielegalną w UE. Brak prostej opcji odmowy to ryzyko prawne i wizerunkowe.

**Jak sprawdzić:** Sprawdź baner — czy przycisk "Odrzuć wszystkie" jest tak samo widoczny jak "Akceptuj wszystkie", czy nie wymaga dodatkowych kliknięć.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.3 Strona domyślnie zablokowana przed wyborem zgody
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Użytkownik powinien móc podjąć decyzję o zgodzie zanim zacznie korzystać ze strony. Jeśli strona jest w pełni dostępna — można ją przeglądać, przewijać, klikać — bez podejmowania decyzji o cookies, to de facto traktujemy brak odpowiedzi jako zgodę. Taka praktyka jest niezgodna z RODO. Strona powinna być "zablokowana" lub przynajmniej wyraźnie ograniczona do czasu wyboru.

**Jak sprawdzić:** Incognito → czy można korzystać ze strony (przewijać, klikać linki) bez kliknięcia czegokolwiek w banerze?

**Czerwona flaga:** Możliwość przeglądania strony bez jakiejkolwiek interakcji z banerem.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.4 Skuteczne blokowanie cookies
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Wiele banerów cookie jest "atrapą" — wizualnie wyglądają poprawnie, ale po kliknięciu "Odrzuć" i tak instalują wszystkie cookies i wysyłają dane do GA4 czy Meta. To jest jeden z najpoważniejszych błędów RODO. Organ ochrony danych (UODO w Polsce, CNIL we Francji) nakłada kary właśnie za tę praktykę. Technicznie: po kliknięciu "Odrzuć" nie powinno być żadnych requestów do usług analitycznych ani reklamowych.

**Jak sprawdzić:** DevTools → Network → wyczyść logi → kliknij "Odrzuć wszystkie" → sprawdź czy pojawią się requesty do GA4 (`google-analytics.com`) lub Meta (`facebook.com/tr`). Sprawdź też DevTools → Application → Cookies → czy cookies `_ga`, `_gid` zostały ustawione.

**Czerwona flaga:** Jakikolwiek request analityczny lub piksel reklamowy po kliknięciu "Odrzuć".

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.5 Możliwość zmiany decyzji
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
RODO gwarantuje użytkownikowi prawo do wycofania zgody w dowolnym momencie. Oznacza to, że strona musi oferować stały, łatwo dostępny sposób zmiany ustawień cookies — najczęściej ikona "cookie" w rogu strony lub link w stopce. Utrudnienie dostępu do zmiany zgody to naruszenie przepisów.

**Jak sprawdzić:** Zaakceptuj cookies → szukaj ikony lub linku do zarządzania zgodami na stronie głównej i w stopce.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.6–2.7 Ustawienia domyślne przy pierwszej wizycie
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Przy pierwszej wizycie użytkownika strona powinna domyślnie działać bez cookies analitycznych i reklamowych (consent denied by default). To wymóg prawny w większości krajów UE. Jeśli GA4 zbiera dane przed podjęciem decyzji przez użytkownika — to naruszenie RODO. Sprawdzamy dwa aspekty: czy użytkownik musi podjąć decyzję oraz czy przed decyzją nie są zbierane żadne dane.

**Jak sprawdzić:**
- Incognito → otwórz DevTools → Network → ładuj stronę → NIE klikaj nic przez 30 sekund → sprawdź czy są requesty GA4
- Sprawdź DevTools → Application → Storage → czy są cookies analityczne przed wyborem

| Status — wymuszony wybór | Status — brak cookies przed decyzją | Komentarz |
|--------------------------|-------------------------------------|-----------|
| | | |

---

### 2.8 Wywołanie consent update w DataLayer
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Consent Mode wymaga specyficznej sekwencji w DataLayer: najpierw `gtag('consent', 'default', {...})` z domyślnie odmową, a po decyzji użytkownika `gtag('consent', 'update', {...})` z jego wyborem. GA4 powinno "czekać" na ten update i dopiero wtedy wysłać dane (lub PING jeśli zgody nie udzielono). Błędna kolejność lub brak update oznacza, że Consent Mode nie działa jak powinien.

**Jak sprawdzić:** DevTools → Console → wpisz `dataLayer` → sprawdź sekwencję eventów: `consent_default` → (wybór użytkownika) → `consent_update` lub zdarzenie CMP.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.9 Brak odświeżania strony po wyborze zgody
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Jeśli po kliknięciu "Akceptuj" strona się przeładowuje (refresh), to nowa sesja zaczyna się od nowa — gubiona jest informacja o źródle ruchu, poprzednich akcjach na stronie, a sam event zgody nie jest przypisany do właściwej sesji. Poprawna implementacja Consent Mode aktualizuje zgody dynamicznie bez przeładowania.

**Jak sprawdzić:** Kliknij "Akceptuj" na banerze → obserwuj czy strona się przeładowuje (pasek postępu w przeglądarce, zmiana URL).

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.10 GA4 i piksele wywołują się po udzieleniu zgody
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Weryfikacja, że system działa jak powinien: po kliknięciu "Akceptuj" tagi analityczne i reklamowe faktycznie się wywołują. To test "odwrotny" do punktu 2.4 — tam sprawdzaliśmy czy blokuje po odmowie, tutaj sprawdzamy czy działa po zgodzie. Brzmi oczywisto, ale zdarzają się implementacje gdzie po akceptacji tagi nadal nie startują.

**Jak sprawdzić:** Incognito → DevTools → Network → wyczyść → kliknij "Akceptuj" → sprawdź czy pojawiają się requesty GA4 i innych wykrytych narzędzi.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.11 Brak podwójnego user_engagement po zgodzie
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
Po kliknięciu "Akceptuj" nie powinno wywoływać się zdarzenie `user_engagement` od razu — to zdarzenie powinno nastąpić naturalnie po czasie spędzonym na stronie. Podwójne liczenie page_view lub natychmiastowe user_engagement zaraz po zgodzie może zawyżać metryki zaangażowania.

**Jak sprawdzić:** Network po kliknięciu "Akceptuj" — sprawdź czy nie ma dwóch `page_view` lub natychmiastowego `user_engagement` w pierwszej sekundzie.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.12–2.16 Konfiguracja Consent Mode w GTM
**Priorytet:** Średni–Wysoki

**Czym jest i dlaczego sprawdzamy:**
GTM jest centralnym punktem zarządzania wszystkimi tagami. Consent Mode w GTM działa na poziomie każdego tagu — każdy tag powinien mieć przypisane "wymagania zgodowe". Jeśli tag GA4 nie ma przypisanego `analytics_storage`, może się wywołać bez zgody. GTM oferuje też mechanizm "Consent Initialization" — specjalną regułę, która ładuje CMP przed wszystkimi innymi tagami.

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 2.12 | Przegląd ustawień zgód w GTM | Średni | GTM → każdy tag → zakładka Consent | | |
| 2.13 | CMP ładuje się z Consent Initialization | Średni | GTM → Tag CMP → reguła: "Consent Initialization — All Pages" | | |
| 2.14 | Consent Mode blokuje tagi bez zgody | Wysoki | GTM Preview → odwiedź stronę bez zgody → sprawdź "Blocked by consent" | | |
| 2.15 | Wszystkie tagi mają ustawiony tryb zgody | Średni | GTM → lista tagów → każdy tag musi mieć consent setting | | |
| 2.16 | PING w Consent Mode | Średni | Network po odmowie → czy są puste requesty (pings) do GA4? | | |

---

### 2.17 url_passthrough
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
`url_passthrough` to parametr konfiguracyjny GA4, który pozwala przekazywać informacje o kliknięciach w reklamy bezpośrednio w URL-u strony docelowej — zamiast w cookies. Dzięki temu, nawet jeśli użytkownik odrzuci cookies, Google może modelować konwersje na podstawie parametrów URL. Bez tego ustawienia, użytkownicy którzy odmawiają cookies nie są w ogóle przypisywani do kampanii reklamowych, co zaniża ROI mierzonych kampanii.

**Jak sprawdzić:** GTM → Tag GA4 Configuration → Pola konfiguracji → szukaj `url_passthrough: true`. Alternatywnie w gtag bezpośrednim: `gtag('set', 'url_passthrough', true)`.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 2.18–2.20 Dane wrażliwe
**Priorytet:** Wysoki (wszystkie)

**Czym jest i dlaczego sprawdzamy:**
GA4 jest usługą zewnętrzną — wszystko co trafi do GA4 (adresy URL, parametry UTM, wartości zdarzeń) jest przesyłane do serwerów Google. Jeśli w tych danych znajdą się dane osobowe lub wrażliwe (adresy email, numery PESEL, dane kart płatniczych, numery telefonów), naruszamy RODO, Warunki Korzystania z Google Analytics oraz potencjalnie wiele innych regulacji. Takie zdarzenia zdarzają się nieintencjonalnie — np. gdy parametr formularza trafia do URL lub gdy developer zapisuje email w nazwie zdarzenia "dla wygody".

**Jak sprawdzić:**
- URL: GA4 → Raporty → Strony i ekrany → szukaj URL z wzorcami: `email=`, `mail=`, `phone=`, `tel=`, ciągi wyglądające jak email/PESEL
- UTM: GA4 → Eksploracje → filtruj source/medium/campaign szukając adresów email
- Zdarzenia: GA4 → DebugView lub BigQuery → sprawdź wartości parametrów zdarzeń

| # | Punkt | Status | Komentarz |
|---|-------|--------|-----------|
| 2.18 | Brak danych wrażliwych w URL | | |
| 2.19 | Brak danych wrażliwych w UTM | | |
| 2.20 | Brak danych wrażliwych w zdarzeniach | | |

---

# SEKCJA 3 — Konfiguracja

> Cel: Weryfikacja kompletności i poprawności konfiguracji GTM oraz GA4. Dobra konfiguracja to fundament wiarygodnych danych.

---

## 3A — Konfiguracja GTM

### 3.1 Walidacja GTM
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Google Tag Manager powinien być zainstalowany jako pierwszy skrypt zaraz po otwarciu tagu `<head>` — jeszcze przed innymi tagami marketingowymi. Nieprawidłowa instalacja (np. GTM na dole strony, w stopce, lub zakomentowany) powoduje, że część wizyt nie jest mierzona (strony ładują się szybciej niż GTM zdąży się zainicjować). Fragment `<noscript>` powinien być umieszczony bezpośrednio po otwarciu `<body>` — to fallback dla przeglądarek bez JavaScript.

**Jak sprawdzić:** Źródło strony — szukaj fragmentu `<!-- Google Tag Manager -->` i zweryfikuj jego pozycję w `<head>`.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.2 Brak błędów i powiadomień w GTM
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
GTM sygnalizuje błędy i ostrzeżenia w panelu administracyjnym — np. tagi z błędnymi konfiguracjami, niepoprawne reguły, brakujące zmienne. Ignorowanie powiadomień GTM to jak ignorowanie lampek ostrzegawczych w samochodzie. Każde powiadomienie może wskazywać na tagi które się nie wywołują lub wywołują się błędnie.

**Jak sprawdzić:** GTM → Workspace → ikona dzwonka w prawym górnym rogu. Sprawdź też zakładkę "Aktywność" w Admin.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.3 Ustawienia Consent dla wszystkich tagów
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
W GTM każdy tag powinien mieć przypisane wymagania dotyczące zgody (Consent Settings). Oznacza to że GTM "wie" czy dany tag może się uruchomić w zależności od decyzji użytkownika. Tag GA4 = `analytics_storage`. Tagi Google Ads i Meta = `ad_storage`, `ad_user_data`, `ad_personalization`. Tag bez consent settings może się wywołać niezależnie od decyzji użytkownika — co jest naruszeniem RODO.

**Jak sprawdzić:** GTM → każdy tag → "Ustawienia zaawansowane" → "Wymagania dotyczące zgody". Każdy tag powinien mieć przynajmniej jeden wymóg.

**Czerwona flaga:** Jakikolwiek tag analityczny lub reklamowy bez ustawionego trybu zgody.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.4 Tag łączący konwersje (Conversion Linker)
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Conversion Linker to specjalny tag GTM wymagany przez Google Ads, który "zapamiętuje" informacje o kliknięciach w reklamy poprzez pliki cookies (first-party). Bez tego tagu, gdy użytkownik kliknie reklamę Google Ads, trafi na stronę i dokona zakupu — Google Ads może nie przypisać tej konwersji do właściwej reklamy. Przekłada się to bezpośrednio na błędną optymalizację kampanii i złe decyzje budżetowe. Conversion Linker powinien mieć regułę "Wszystkie strony" i być jednym z pierwszych tagów do załadowania.

**Jak sprawdzić:** GTM → Tagi → szukaj "Conversion Linker". Sprawdź regułę wyzwalania (All Pages) i czy tag jest opublikowany.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.5 Podsumowanie zasięgu tagu
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
GTM oferuje raport "Podsumowanie zasięgu tagu" który pokazuje jaki procent stron w witrynie jest otagowany przez GTM. Jeśli zasięg wynosi np. 60%, oznacza to że 40% podstron nie jest mierzone — mogą to być podstrony techniczne, subddomeny, strony wygenerowane przez zewnętrzne systemy (np. checkout na zewnętrznej domenie). Każda nieotagowana strona to martwy punkt w danych analitycznych.

**Jak sprawdzić:** GTM → Admin → Podsumowanie zasięgu tagu. Sprawdź procentowe pokrycie i listę nieotagowanych stron.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.6 Wersje kontenerów mają tytuły
**Priorytet:** Niski

Nadawanie opisowych nazw wersjom kontenerów GTM (np. "2024-03-15 Wdrożenie GA4 e-commerce") umożliwia audytowalność zmian i szybki rollback w razie błędu.

**Jak sprawdzić:** GTM → Wersje → sprawdź czy wersje mają opisowe nazwy.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.7 Brak kodów UA w GTM
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Universal Analytics przestał zbierać dane w lipcu 2024 roku. Stare tagi UA w GTM (`UA-XXXXXXXX-X`) są bezużyteczne, ale mogą powodować błędy w konsoli przeglądarki, spowalniać ładowanie strony i mylić deweloperów. Co gorsza — jeśli nikt nie usunął tych tagów, oznacza to brak porządku w kontenerze GTM.

**Jak sprawdzić:** GTM → Tagi → filtruj typ "Universal Analytics" lub szukaj "UA-". Aktywne tagi UA = błąd.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.8 GA4 wdrożone przez GTM
**Priorytet:** Niski

Wdrożenie GA4 przez GTM (jako tag "Google Analytics: GA4 Configuration") zamiast hardcoded w HTML umożliwia łatwą aktualizację konfiguracji bez udziału deweloperów.

**Jak sprawdzić:** GTM → Tagi → szukaj "GA4 Configuration". Sprawdź Measurement ID.

| Status | Komentarz |
|--------|-----------|
| | |

---

## 3A2 — GTM Container Health (Zdrowie kontenera)

> Ocena stanu kontenera GTM jako całości. Zły kontener to: tagi które nie działają, błędne reguły wyzwalania, zaśmiecone zmienne, brak porządku w strukturze. Zdrowy kontener = audytowalny, testowalny, skalowalny.

### Jak pobrać dane do analizy kontenera

```
GTM → Admin → Eksportuj kontener (JSON) → otwórz w edytorze
→ Policz: tagi (tags), reguły (triggers), zmienne (variables)
→ Sprawdź: % tagów bez nazewnictwa, % tagów nieuruchamiających się, duplikaty
```

### 3A2.1 — Liczba i struktura tagów

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| Łączna liczba tagów w kontenerze | | ✅ <30 / ⚠️ 30–60 / ❌ >60 |
| Tagi aktywne (uruchamiane) | | |
| Tagi wstrzymane / wyłączone | | ⚠️ jeśli >5 bez uzasadnienia |
| Tagi bez jednej nazwy konwencji | | ❌ jeśli >20% |
| Zduplikowane tagi (ta sama akcja 2× lub więcej) | | ❌ jeśli jakikolwiek |
| Tagi z regułą "All Pages" które powinny mieć węższą | | ⚠️ |

**Konwencja nazewnictwa tagów (standard):**
```
[Typ narzędzia] - [Akcja/Zdarzenie] - [Wyzwalacz]
Przykłady:
  GA4 - Konfiguracja - All Pages
  GA4 - purchase - Potwierdzenie zamówienia
  Google Ads - Conversion - Zakup
  Meta - Purchase - Potwierdzenie
  Hotjar - Heatmap - All Pages
```

### 3A2.2 — Reguły wyzwalania (Triggers)

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| Łączna liczba reguł | | ✅ <20 / ⚠️ 20–40 / ❌ >40 |
| Reguły bez przypisanego tagu | | ❌ jeśli jakikolwiek (martwe reguły) |
| Reguły z nazwą domyślną ("Trigger 1", "Trigger 2"...) | | ❌ jeśli >0 |
| Reguły bazujące na selektorach CSS (kruchych) | | ⚠️ lepiej dataLayer |
| Reguły oparte na URL text match (zamiast DataLayer) | | ⚠️ ryzyko regresji |

### 3A2.3 — Zmienne (Variables)

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| Łączna liczba zmiennych zdefiniowanych przez użytkownika | | |
| Zmienne DataLayer (preferowane) | | |
| Zmienne JavaScript (potencjalnie niestabilne) | | ⚠️ |
| Zmienne cookie first-party | | |
| Zmienne bez użycia w żadnym tagu | | ❌ usuń |

### 3A2.4 — Workspace i kontrola wersji

| Punkt | Priorytet | Status | Komentarz |
|-------|-----------|--------|-----------|
| Aktualny workspace jest "Default Workspace" lub ma opisową nazwę | Niski | | |
| Historia wersji: wersje mają opisowe nazwy i daty | Niski | | |
| Ostatnia publikacja: data i kto opublikował | Średni | | |
| Brak niezatwierdzonych zmian w workspace (ghost changes) | Wysoki | | |
| GTM jest połączony z repozytorium (GitHub/Bitbucket) jeśli używany workflow | Niski | | |

### 3A2.5 — Preview Mode i testowanie

**Jak sprawdzić:** GTM → Preview → sprawdź czy tagi wywołują się zgodnie z oczekiwaniem.

| Scenariusz testowy | Oczekiwany tag | Faktyczne wywołania | Ocena |
|--------------------|---------------|---------------------|-------|
| Strona główna (page_view) | GA4 Config, Conversion Linker | | |
| Strona produktu (view_item) | GA4 view_item, Meta ViewContent | | |
| Dodanie do koszyka | GA4 add_to_cart, Meta AddToCart | | |
| Checkout (begin_checkout) | GA4 begin_checkout | | |
| Potwierdzenie zamówienia (purchase) | GA4 purchase, Google Ads Conv., Meta Purchase | | |
| Odrzucenie cookies (consent denied) | GA4 ping bez danych, ŻADNE tagi reklamowe | | |

**Czerwone flagi Preview Mode:**
- Tag wywołuje się na stronach gdzie nie powinien (np. GA4 purchase na każdej stronie)
- Brak wywołania purchase na potwierdzeniu zamówienia
- Tagi reklamowe wywołują się po odrzuceniu zgody
- Tag GA4 wywołuje się 2× na tej samej stronie (duplikacja)

### 3A2.6 — GTM Container Health Score

| Obszar | Max pkt | Uzyskane | Komentarz |
|--------|---------|---------|-----------|
| Liczba tagów < 40 | 2 | | |
| Brak zduplikowanych tagów | 3 | | |
| Konwencja nazewnictwa > 80% tagów | 2 | | |
| Brak martwych reguł/zmiennych | 2 | | |
| Wersje mają opisowe nazwy | 1 | | |
| Preview Mode — brak błędów | 3 | | |
| Brak tagów bez consent settings | 3 | | |
| **ŁĄCZNIE** | **16** | | |

---

## 3B — GTM Server Side

> **UWAGA:** Sprawdź najpierw czy GA4 tag w GTM client ma pole `server_container_url`. Jeśli nie ma — **pomiń całą sekcję 3B**. Jeśli jest — sprawdź dostęp i przeprowadź poniższy audyt.

**Czym jest GTM Server Side i dlaczego sprawdzamy:**
GTM Server Side (sGTM) to wersja Google Tag Manager działająca na serwerze w chmurze (Google Cloud Platform) zamiast w przeglądarce użytkownika. Oznacza to, że dane analityczne i reklamowe są najpierw wysyłane na własny serwer firmy (np. analytics.twojadomena.pl), a dopiero stamtąd trafiają do GA4, Google Ads, Meta itp. Korzyści są znaczące: cookies są first-party (żyją dłużej, nie są blokowane przez Safari/ITP), dane są bardziej kompletne (nie blokowane przez ad-blockery), możliwa jest dodatkowa filtracja i wzbogacanie danych przed wysłaniem do zewnętrznych platform. To nowoczesna infrastruktura śledzenia — jej brak nie jest błędem, ale jej obecność powinna być dobrze skonfigurowana.

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 3.9 | sGTM włączony i skonfigurowany | Wysoki | GTM → kontenery → sprawdź czy istnieje kontener Server | | |
| 3.10 | Kontener serwera poprawnie utworzony | Wysoki | GTM Server → sprawdź status kontenera | | |
| 3.11 | GCP skonfigurowane | Wysoki | GCP Console → Cloud Run → serwis gtm-server | | |
| 3.12 | Płatność GCP — brak zaległości | Wysoki | GCP Console → Rozliczenia → sprawdź stan konta | | |
| 3.13 | Połączenie client-side → sGTM | Wysoki | GTM client → Tag GA4 → `server_container_url` = domena 1st party | | |
| 3.14 | Custom domain (1st party) dodana | Wysoki | DNS domeny → sprawdź czy istnieje rekord dla analytics.{domena} | | |
| 3.15 | Walidacja klienta przeszła pomyślnie | Wysoki | GTM Server → Klienci → status "Zweryfikowany" | | |
| 3.16 | DNS AAAA (IPv6) | Wysoki | `nslookup -type=AAAA analytics.{domena}` | | |
| 3.17 | DNS A (IPv4) | Wysoki | `nslookup analytics.{domena}` | | |
| 3.18 | URL kontenera serwera zmieniony | Średni | GTM Server → Ustawienia → URL serwera (nie domyślny GCP) | | |
| 3.19 | Transport URL ustawiony | Wysoki | GTM client → Tag GA4 Config → pole `server_container_url` | | |
| 3.20 | Flexible plan GCP | Średni | GCP → Cloud Run → sprawdź plan rozliczeniowy | | |

### 3B.2 — sGTM: Klienty i tagi serwera

> Gdy sGTM jest aktywny — sprawdź jakie klienty i tagi są skonfigurowane.

**Klienty (Clients) w sGTM:**

| Klient | Status | Komentarz |
|--------|--------|-----------|
| GA4 Client (odbiera requesty z GTM web) | ✅/❌ | Wymagany — bez niego sGTM nie odbiera danych |
| Google Ads Conversion Tracking Client | ✅/❌/➖ | Opcjonalny |
| Floodlight Client | ✅/❌/➖ | Opcjonalny (Campaign Manager 360) |

**Tagi serwera (Server Tags):**

| Tag | Cel | Status | Komentarz |
|-----|-----|--------|-----------|
| GA4 → Google Analytics | Przekazanie danych do GA4 | | |
| Google Ads — konwersje | Przekazanie konwersji do Ads | | |
| Meta CAPI | Conversion API dla Meta | | |
| Inne (Pinterest, TikTok, LinkedIn) | | | |

### 3B.3 — sGTM: Weryfikacja cookie first-party

**Sprawdź w DevTools → Application → Cookies:**

| Cookie | Domena | Expiry | HttpOnly | Secure | Ocena |
|--------|--------|--------|----------|--------|-------|
| `_ga` | `.twojadomena.pl` (first-party) | 2 lata | Nie | Tak | ✅ / ❌ (third-party) |
| `_ga_XXXXXX` | `.twojadomena.pl` | 2 lata | Nie | Tak | ✅ / ❌ |
| `_gcl_aw` (Google Ads click) | `.twojadomena.pl` | 90 dni | Nie | Tak | ✅ / ❌ |

**Cel:** Cookies first-party przez sGTM żyją pełne 2 lata (vs ~7 dni w Safari bez sGTM). To bezpośrednio wpływa na jakość atrybucji długich cykli zakupowych.

### 3B.4 — sGTM: Preview i monitoring

| Punkt | Priorytet | Status | Komentarz |
|-------|-----------|--------|-----------|
| sGTM Preview działa — requesty docierają do kontenera | Wysoki | | |
| Logi GCP Cloud Run — brak błędów 5xx | Wysoki | | |
| Monitoring GCP — alert na niedostępność serwera | Średni | | |
| Skalowanie automatyczne skonfigurowane (min. 1, max. N instancji) | Średni | | |
| Koszty GCP miesięczne są znane i monitorowane | Niski | | |

---

## 3C — Konfiguracja GA4 (Konto i Administracja)

### 3.21 Alerty i powiadomienia w GA4
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Google Analytics wysyła powiadomienia systemowe o potencjalnych problemach: np. "Wykryliśmy anomalię w zbieraniu danych", "Brak danych z jednego ze strumieni", "Wygasły dostęp do połączonej usługi". Te powiadomienia często są ignorowane bo nie wymagają natychmiastowej akcji — ale każde z nich może sygnalizować poważny problem z jakością danych.

**Jak sprawdzić:** GA4 → Admin → ikona dzwonka w prawym górnym rogu. Sprawdź listę powiadomień.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.22–3.23 Preferencje i udostępnianie danych
**Priorytet:** Niski

Ustawienia udostępniania danych z Google (dla benchmarkingu, wsparcia technicznego, modelowania) są zazwyczaj korzystne dla jakości danych. Ich wyłączenie może pogorszyć jakość modelowania konwersji.

| # | Punkt | Status | Komentarz |
|---|-------|--------|-----------|
| 3.22 | Moje preferencje (rekomendacje, pomoc, modelowanie) | | |
| 3.23 | Ustawienia udostępniania danych | | |

---

### 3.24 Weryfikacja uprawnień do konta
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Lista użytkowników mających dostęp do GA4 powinna być regularnie weryfikowana. Nieautoryzowane osoby z uprawnieniami "Edytor" lub "Administrator" mogą zmieniać konfigurację konta — np. usunąć konwersje, zmienić model atrybucji lub wyeksportować dane. Były pracownicy, agencje które zakończyły współpracę, konta testowe — wszystkie powinny być usunięte. To podstawowa higiena bezpieczeństwa danych.

**Jak sprawdzić:** GA4 → Admin → Zarządzanie dostępem do konta. Sprawdź każdego użytkownika: czy jest aktywny, czy poziom uprawnień jest adekwatny.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.25–3.26 Historia zmian i Kosz
**Priorytet:** Niski

Historia zmian pozwala zobaczyć kto i kiedy zmieniał konfigurację konta — przydatna przy diagnostyce problemów ("kiedy zaczęły się tracić dane?"). Kosz może zawierać usunięte zasoby wymagające przywrócenia.

| # | Punkt | Status | Komentarz |
|---|-------|--------|-----------|
| 3.25 | Historia zmian konta | | |
| 3.26 | Kosz GA4 | | |

---

## 3D — Ustawienia Usługi

| # | Punkt | Priorytet | Opis | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|------|---------------|--------|-----------|
| 3.27 | Ustawienia usługi, domeny, języka | Niski | Nazwa usługi, URL, strefa czasowa i język powinny być poprawnie ustawione. Błędna strefa czasowa = błędne dane godzinowe. | GA4 → Admin → Ustawienia usługi | | |
| 3.28 | Waluta | Średni | Krytyczne dla e-commerce: błędna waluta oznacza błędne raportowanie przychodów. Np. PLN zamiast EUR może zmylić raporty. | GA4 → Admin → Ustawienia usługi → Waluta | | |
| 3.29 | Historia zmian usługi | Średni | Pozwala wykryć nieautoryzowane zmiany w ustawieniach usługi. | GA4 → Admin → Historia zmian usługi | | |

---

## 3E — Zbieranie i modyfikowanie danych

### 3.30 Google Signals
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Google Signals to funkcja, która łączy dane o użytkownikach korzystających z wielu urządzeń — pod warunkiem że są zalogowani do konta Google. Dzięki temu zamiast widzieć jedną osobę jako trzech różnych użytkowników (laptop w pracy, telefon w domu, tablet), GA4 rozpoznaje ją jako jedną osobę. Dla właściciela sklepu oznacza to dokładniejsze dane o zasięgu kampanii i ścieżkach zakupowych. Google Signals jest też wymagany do pełnego działania raportów demograficznych i zainteresowań.

**Jak sprawdzić:** GA4 → Admin → Zbieranie i modyfikowanie danych → Google Signals → Status: Aktywne.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.31 User-ID
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
User-ID to unikalny identyfikator przypisany do zalogowanego użytkownika przez system (np. numer klienta z bazy danych). Przekazując User-ID do GA4 możemy śledzić ścieżkę zakupową użytkownika ponad granicami urządzeń, sesji i cookies. Bez User-ID, jeśli ktoś odwiedza stronę z laptopa, potem z telefonu, a zakupu dokonuje na tablecie — GA4 widzi trzy różne "osoby". Z User-ID to zawsze ten sam klient. Kluczowe dla e-commerce z rejestracją.

**Jak sprawdzić:** GA4 → Admin → Zbieranie danych → User-ID. Sprawdź czy funkcja jest włączona i czy dane faktycznie napływają (GA4 → Raporty → Tożsamość → User-ID Coverage).

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.32–3.35 Pozostałe ustawienia zbierania danych

| # | Punkt | Priorytet | Opis | Status | Komentarz |
|---|-------|-----------|------|--------|-----------|
| 3.32 | Szczegółowe dane o lokalizacji i urządzeniu | Średni | Umożliwia raportowanie szczegółów: miasto, model urządzenia, system operacyjny. Przydatne dla targetowania i UX. | | |
| 3.33 | Import danych | Średni | Sprawdź czy są aktywne importy (koszty kampanii, dane CRM). Nieaktualizowane importy = błędne dane. | | |
| 3.34 | Przechowywanie danych — 14 miesięcy | Niski | Domyślnie GA4 przechowuje dane szczegółowe przez 2 miesiące. Zmiana na 14 miesięcy zachowuje historię do analiz long-term. Kluczowe ustawienie często pominięte. | | |
| 3.35 | Resetowanie danych | Średni | Umożliwia użytkownikom żądanie usunięcia danych — wymóg RODO. | | |

---

### 3.36 Filtrowanie ruchu wewnętrznego i deweloperskiego
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Pracownicy firmy, deweloperzy testujący stronę, agencja obsługująca konto — wszyscy generują ruch, który nie pochodzi od prawdziwych klientów. Jeśli tego ruchu nie wykluczymy, zawyżamy metryki zaangażowania, zaniżamy współczynnik konwersji (bo deweloperzy rzadko kupują) i zaburzamy dane demograficzne. Filtr ruchu wewnętrznego w GA4 działa na podstawie adresów IP lub parametru `traffic_type=internal` ustawionego przez GTM.

**Jak sprawdzić:** GA4 → Admin → Filtry danych. Szukaj filtru "Ruch wewnętrzny" ze statusem Aktywny. Sprawdź czy lista IP jest aktualna.

**Czerwona flaga:** Brak jakiegokolwiek filtra ruchu = dane zawierają ruch pracowników i deweloperów.

| Status | Komentarz |
|--------|-----------|
| | |

---

## 3F — Strumienie danych

### 3.37–3.39 Strumienie Web, iOS, Android
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Strumień danych to połączenie między konkretną platformą (strona www, aplikacja iOS, aplikacja Android) a usługą GA4. Jeden GA4 property może zbierać dane z wielu platform w jednym miejscu. Sprawdzamy czy strumień jest aktywny i zbiera dane — GA4 pokazuje ostrzeżenie jeśli dane nie napływały przez 48h.

**Jak sprawdzić:** GA4 → Admin → Strumienie danych → dla każdego strumienia sprawdź status "Dane napływające w ciągu ostatnich 48h".

| # | Strumień | Priorytet | Status | Komentarz |
|---|----------|-----------|--------|-----------|
| 3.37 | Web | Wysoki | | |
| 3.38 | iOS (jeśli dotyczy) | Wysoki | | |
| 3.39 | Android (jeśli dotyczy) | Wysoki | | |

---

### 3.40–3.46 Konfiguracja strumienia Web — szczegóły

| # | Punkt | Priorytet | Opis / Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------------|--------|-----------|
| 3.40 | URL strumienia | Niski | URL strumienia musi być zgodny z domeną. Niezgodność = dane z błędnej domeny. | | |
| 3.41 | Ustawienia zgody strumienia | Wysoki | GA4 → Strumień → Ustawienia zgody. Brak konfiguracji = brak modelowania danych. | | |
| 3.42 | Parametr wyszukiwarki | Niski | Jeśli strona ma wewnętrzną wyszukiwarkę, parametr URL (np. `q`, `s`, `search`) musi być zdefiniowany aby GA4 zbierał zdarzenia wyszukiwania. | | |
| 3.43 | Tajny klucz API / Measurement Protocol | Średni | Klucz API umożliwia wysyłanie danych do GA4 z backendu serwera (np. potwierdzenie płatności z serwera). Wymagany dla zaawansowanych implementacji. | | |
| 3.44 | Implementacja przez GTM | Wysoki | Sprawdź czy Measurement ID w strumieniu zgadza się z ID w tagu GTM. | | |
| 3.45 | Cross-domain tracking | Wysoki | Jeśli sklep i płatności są na różnych domenach — musi być skonfigurowany cross-domain. Brak = każde przejście na bramkę płatności tworzy nową sesję z `direct` jako źródłem. Zaburza całą atrybucję. | | |
| 3.46 | Pomiar zaawansowany | Średni | Automatyczny pomiar: scroll, kliknięcia wychodzące, wideo YouTube, pobrane pliki. Warto włączyć — zero kodu dodatkowego. | | |

---

## 3G — Zarządzanie strumieniem (Ustawienia tagowania)

### 3.47–3.57 Szczegóły konfiguracji strumienia

**Czym jest sekcja i dlaczego sprawdzamy:**
W ustawieniach strumienia GA4 kryje się wiele konfiguracji, które mają ogromny wpływ na jakość danych — od wykluczeń domen, przez czas trwania sesji, po blokowanie botów CMP. Wiele z nich jest ustawionych przez wdrożeniowców przy starcie i nigdy nie weryfikowanych — stąd często zawierają błędy lub braki.

| # | Punkt | Priorytet | Opis / Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------------|--------|-----------|
| 3.47 | Brak powiadomień w zarządzaniu tagami | Wysoki | GA4 → Strumień → Zarządzaj tagiem Google. Sprawdź czy są ostrzeżenia. | | |
| 3.48 | Konfiguracja domen (cross-domain) | Wysoki | GA4 → Strumień → Konfigurowanie domen. Lista powinna zawierać wszystkie własne domeny (sklep, blog, checkout). | | |
| 3.49 | Ignorowanie zduplikowanych konfiguracji | Wysoki | Zapobiega podwójnemu liczeniu page_view gdy GA4 jest wdrożone zarówno przez GTM jak i hardcoded. GA4 → Strumień → Zarządzaj tagiem Google → Zduplikowane tagi → Ignoruj. | | |
| 3.50 | Ruch wewnętrzny — traffic_type | Niski | GA4 → Strumień → Definiowanie ruchu wewnętrznego. Parametr `traffic_type=internal` powinien być ustawiony dla IP biura/deweloperów. | | |
| 3.51 | Lista niechcianych witryn odsyłających | Niski | Baza "referral exclusion" — domeny które nie powinny być traktowane jako zewnętrzne źródło ruchu. | | |
| 3.52 | Wykluczono bramki pocztowe | Średni | Polskie serwisy pocztowe (wp.pl, onet.pl, o2.pl, interia.pl) w emailach klientów mogą generować ruch referral. Muszą być wykluczone. | | |
| 3.53 | Wykluczono bramki płatności | Wysoki | **Krytyczne dla e-commerce.** Operatorzy płatności (PayU, Przelewy24, PayPal, BLIK, banki) muszą być na liście wykluczeń. Bez tego: użytkownik kupuje → przechodzi na płatność → wraca → GA4 rejestruje nową sesję z bramką jako źródłem. Atrybucja jest zepsuta. | | |
| 3.54 | Wykluczono boty CMP (Cookiebot itp.) | Wysoki | Roboty CMP (np. Cookiebot scanner) regularnie skanują stronę i generują fałszywy ruch. Muszą być wykluczone z GA4. | | |
| 3.55 | Czas trwania sesji | Średni | Standardowo 30 minut. Dla e-commerce rekomendowane jest wydłużenie do 5 godzin — użytkownicy często wychodzą na chwilę i wracają, co bez wydłużenia tworzy nowe sesje. GA4 → Strumień → Czas trwania sesji. | | |
| 3.56 | Czas zaangażowania | Niski | Standardowe 10 sekund. Użytkownicy którzy spędzają mniej niż 10 sekund są klasyfikowani jako "niezaangażowani". | | |
| 3.57 | Zastąp ustawienia plików cookies | Niski | Opcja wydłużenia czasu życia cookies GA4 do max 25 miesięcy (standardowo 2 lata). Przydatne dla długich cykli zakupowych. | | |

---

## 3H — Wyświetlanie danych

### 3.58 Zdarzenia jako konwersje
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
W GA4 zdarzenia które mają znaczenie biznesowe powinny być oznaczone jako "konwersje" (poprzednio zwane "kluczowymi zdarzeniami"). Dla e-commerce to minimum: `purchase`. Ale warto też oznaczać: `add_to_cart`, `begin_checkout`, `generate_lead` (jeśli dotyczy), `sign_up`. Oznaczenie zdarzenia jako konwersja powoduje że pojawia się w raportach konwersji, może być importowane do Google Ads i optymalizowane w kampaniach. Brak oznaczenia = dane są, ale nie są "widoczne" dla systemu reklamowego.

**Jak sprawdzić:** GA4 → Admin → Konwersje. Sprawdź listę i czy wszystkie biznesowo ważne zdarzenia są oznaczone. Weryfikuj też w kontekście modelu biznesowego klienta.

| Status | Komentarz |
|--------|-----------|
| | |

---

### 3.59–3.67 Definicje, odbiorcy, atrybucja

| # | Punkt | Priorytet | Opis / Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------------|--------|-----------|
| 3.59 | Odbiorcy | Niski | Min. 1 grupa odbiorców — podstawa remarketingu. | | |
| 3.60 | Porównania | Niski | Min. 1 porównanie — szybka filtracja w raportach. | | |
| 3.61 | Segmenty | Niski | Min. 1 segment w eksploracji. | | |
| 3.62 | Definicje niestandardowe | Niski | Custom dimensions/metrics — potrzebne do raportowania własnych parametrów. | | |
| 3.63 | Własna grupa kanałów | Średni | Domyślne grupowanie kanałów GA4 często nie odpowiada strukturze kampanii klienta. Własna grupa pozwala na precyzyjną atrybucję. GA4 → Admin → Grupy kanałów. | | |
| 3.64 | Model atrybucji — Data-Driven | Średni | Model oparty na danych (Data-Driven Attribution) jest rekomendowany przez Google i daje najdokładniejszy obraz skuteczności kanałów. Wymaga min. 400 konwersji/30 dni. GA4 → Admin → Ustawienia atrybucji. | | |
| 3.65 | Zasięg atrybucji — płatne i bezpłatne | Średni | Ustawienie "Płatne i bezpłatne kanały" uwzględnia w atrybucji zarówno kampanie płatne jak i SEO/social. | | |
| 3.66 | Ważność kluczowego zdarzenia — 30 dni | Średni | Okno konwersji 30 dni oznacza, że zakup dokonany do 30 dni po kliknięciu jest przypisywany do tej kampanii. Standardowo rekomendowane. | | |
| 3.67 | Tożsamość raportowania — Mieszana | Niski | Tryb "Mieszany" łączy dane z User-ID, Google Signals i identyfikatorów urządzeń — najdokładniejszy dostępny model. GA4 → Admin → Tożsamość raportowania. | | |

---

## 3I — Połączenie usług

**Czym jest i dlaczego sprawdzamy:**
GA4 może być zintegrowane z wieloma usługami Google i zewnętrznymi. Integracje obligatoryjne (Google Ads, BigQuery, Search Console) są kluczowe dla kompletnej analityki i reklamy. Integracje opcjonalne zależą od tego czego używa klient.

| # | Integracja | Obligatoryjna? | Jak sprawdzić | Status | Komentarz |
|---|-----------|---------------|---------------|--------|-----------|
| 3.68 | Google Ads | TAK | GA4 → Admin → Połączone usługi → Google Ads. Status: Połączono | | |
| 3.69 | Reklamy spersonalizowane | TAK | GA4 → Połączone usługi → Google Ads → "Włącz reklamy spersonalizowane" | | |
| 3.70 | BigQuery | TAK | GA4 → Admin → Połączone usługi → BigQuery. Sprawdź projekt GCP i dataset | | |
| 3.71 | Search Console | TAK | GA4 → Admin → Połączone usługi → Search Console | | |
| 3.72 | AdSense | Opcjonalna | Jeśli klient monetyzuje treści przez AdSense | | |
| 3.73 | Ad Manager | Opcjonalna | Jeśli klient używa DFP/GAM | | |
| 3.74 | Display & Video 360 | Opcjonalna | Jeśli klient używa DV360 | | |
| 3.75 | Search Ads 360 | Opcjonalna | Jeśli klient używa SA360 | | |

---

## 3J — Raporty i alerty

### 3.76–3.80 Custom Insights i alerty

**Czym jest i dlaczego sprawdzamy:**
GA4 oferuje system automatycznych alertów i raportów o trendach (Insights). Alerty niestandardowe pozwalają ustawić powiadomienia np. "gdy ruch spadnie o 20% w stosunku do poprzedniego tygodnia, wyślij email". Dla właściciela e-commerce to system wczesnego ostrzegania — problemy z GA4 lub strony są wykrywane natychmiast, nie tydzień później.

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 3.76 | Custom Insights | Wysoki | GA4 → Strona główna → sekcja Insights → Zarządzaj insightami | | |
| 3.77 | Alerty o anomaliach | Wysoki | GA4 → Insights → Alerty niestandardowe. Szukaj alertów dla: sessions, transactions, revenue | | |
| 3.78 | Powiadomienia email o anomaliach | Wysoki | Dla każdego alertu → konfiguracja → powiadomienie email. Brak email = alert jest ale nikt go nie widzi | | |
| 3.79 | Własne eksploracje | Średni | GA4 → Eksploracje → min. 1 własna eksploracja | | |
| 3.80 | Własne raporty | Średni | GA4 → Raporty → Biblioteka → Własne raporty | | |

---

# SEKCJA 3K — BigQuery Export Audit

> **Warunek wejścia:** GA4 połączone z BigQuery (weryfikacja w punkcie 3.70). Jeśli eksport nieaktywny — pomiń tę sekcję i oznacz jako ➖ Nie dotyczy.
>
> **Cel:** Weryfikacja kompletności i jakości surowych danych GA4 w BigQuery — fundamentu wszystkich raportów, modeli atrybucji i analiz produktowych. Błędy na tym poziomie propagują się do wszystkich dashboardów i decyzji biznesowych opartych na danych.
>
> **Narzędzie:** Połączenie z BigQuery przez `mcp__Google_Cloud_BigQuery__authenticate` lub Python `google-cloud-bigquery`. Wszystkie zapytania wykonuj z `WHERE _TABLE_SUFFIX BETWEEN ...` (zawsze filtruj po dacie — oszczędność kosztów BQ).

---

## 3K.1 — Health check eksportu (świeżość danych)
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
GA4 eksportuje dane do BigQuery codziennie (batch) i opcjonalnie w trybie streaming (intraday). Jeśli eksport zawiedzie przez noc — tabele za ostatni dzień nie istnieją, a wszystkie raporty i pipeline mają lukę w danych. Sprawdzamy czy tabela za wczoraj istnieje, jaki jest zakres dat historycznych i czy eksport streaming działa.

```sql
-- Zakres dat i liczba tabel
SELECT
  MIN(_TABLE_SUFFIX) AS first_date,
  MAX(_TABLE_SUFFIX) AS last_date,
  COUNT(*) AS table_count,
  DATE_DIFF(CURRENT_DATE(), PARSE_DATE('%Y%m%d', MAX(_TABLE_SUFFIX)), DAY) AS days_lag
FROM `{project}.{dataset}.INFORMATION_SCHEMA.TABLES`
WHERE table_name LIKE 'events_2%';

-- Czy jest streaming (intraday)?
SELECT COUNT(*) AS intraday_tables
FROM `{project}.{dataset}.INFORMATION_SCHEMA.TABLES`
WHERE table_name LIKE 'events_intraday_%';
```

**Kryteria oceny:**
- `days_lag = 0` lub `1` → ✅ dane aktualne (GA4 może mieć do 24h opóźnienia)
- `days_lag = 2–3` → ⚠️ sprawdź ustawienia eksportu
- `days_lag > 3` → ❌ eksport prawdopodobnie zepsuty
- Brak `events_intraday_*` → ⚠️ brak streamingu (dane tylko dziennie)

| Status | days_lag | Komentarz |
|--------|----------|-----------|
| | | |

---

## 3K.2 — Wolumen zdarzeń (trend i anomalie)
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Drastyczny spadek liczby zdarzeń w dniu może oznaczać: awarię tagu GTM, problem z Consent Mode (zgody zaczęły być odrzucane), zmianę w kodzie strony, lub błąd w eksporcie. Porównujemy wolumen ostatnich 30 dni z mediany i szukamy outlierów (> 2σ odchylenia).

```sql
SELECT
  event_date,
  COUNT(*) AS total_events,
  COUNTIF(event_name = 'page_view') AS page_views,
  COUNTIF(event_name = 'purchase') AS purchases,
  COUNTIF(event_name = 'session_start') AS sessions
FROM `{project}.{dataset}.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 35 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
GROUP BY event_date
ORDER BY event_date DESC;
```

**Szukaj:** Dni z `page_views` o > 30% niższym niż mediana 30d → anomalia. Dni z `purchases = 0` przy normalnym ruchu → krytyczny błąd.

| Status | Anomalie | Komentarz |
|--------|----------|-----------|
| | | |

---

## 3K.3 — Schemat i kompletność pól
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Schemat GA4 w BigQuery zawiera zagnieżdżone pola (RECORD/REPEATED). Weryfikujemy czy kluczowe pola są obecne i wypełnione — bez nich pipeline danych i raporty będą miały luki. Szczególnie ważne: `items[]`, `ecommerce.*`, `collected_traffic_source`, `session_traffic_source_last_click`.

```sql
-- Sprawdź dostępne kolumny najwyższego poziomu
SELECT column_name, data_type, is_nullable
FROM `{project}.{dataset}.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name LIKE 'events_2%'
  AND table_name = (
    SELECT MAX(table_name) FROM `{project}.{dataset}.INFORMATION_SCHEMA.TABLES`
    WHERE table_name LIKE 'events_2%'
  )
ORDER BY ordinal_position;

-- Sprawdź wypełnienie kluczowych pól (na ostatnim dniu)
SELECT
  COUNTIF(user_pseudo_id IS NULL) AS null_user_id,
  COUNTIF(event_name IS NULL) AS null_event_name,
  COUNTIF(ecommerce.transaction_id IS NULL AND event_name = 'purchase') AS purchase_no_txn,
  COUNTIF(collected_traffic_source.manual_source IS NULL) AS null_collected_source,
  COUNTIF(session_traffic_source_last_click IS NULL) AS null_lastclick,
  COUNTIF(user_id IS NULL) AS null_user_id_crm,
  COUNT(*) AS total_events
FROM `{project}.{dataset}.events_*`
WHERE _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY));
```

**Kluczowe pola do weryfikacji:**

| Pole | Czy obecne | % wypełnienia | Ocena |
|------|-----------|---------------|-------|
| `user_pseudo_id` | | | |
| `user_id` (CRM) | | | |
| `ecommerce.transaction_id` (przy purchase) | | | |
| `ecommerce.purchase_revenue` | | | |
| `items[]` (przy purchase) | | | |
| `collected_traffic_source.manual_source` | | | |
| `session_traffic_source_last_click` | | | |
| `traffic_source.source` (first touch) | | | |

---

## 3K.4 — Jakość danych e-commerce: items[]
**Priorytet:** Wysoki *(e-commerce only)*

**Czym jest i dlaczego sprawdzamy:**
Tablica `items[]` to serce danych produktowych w GA4. Każdy produkt w zakupie musi być opisany jako osobny obiekt z polami `item_id`, `item_name`, `price`, `quantity`. Błędy w `items[]` powodują że raporty produktowe są puste, BCG Matrix jest niemożliwa do zbudowania, a analiza portfela produktowego — bezużyteczna. Najczęstsze problemy: `item_id = (not set)`, `price = 0`, `quantity = NULL`, brak pola `item_category`.

```sql
SELECT
  -- Kompletność klucza produktu
  COUNTIF(i.item_id IS NULL OR i.item_id = '(not set)') AS null_item_id,
  COUNTIF(i.item_name IS NULL OR i.item_name = '(not set)') AS null_item_name,
  COUNTIF(i.price IS NULL OR i.price = 0) AS zero_price,
  COUNTIF(i.quantity IS NULL OR i.quantity = 0) AS zero_quantity,
  COUNTIF(i.item_category IS NULL OR i.item_category = '(not set)') AS null_category,
  COUNTIF(i.item_brand IS NULL OR i.item_brand = '(not set)') AS null_brand,
  -- Wartości
  ROUND(AVG(i.price), 2) AS avg_item_price,
  MAX(i.price) AS max_price,
  COUNT(*) AS total_items_rows,
  COUNT(DISTINCT i.item_id) AS unique_products
FROM `{project}.{dataset}.events_*`,
  UNNEST(items) AS i
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  AND event_name IN ('purchase', 'add_to_cart', 'view_item', 'begin_checkout');

-- Najpopularniejsze item_id — czy wyglądają poprawnie?
SELECT
  i.item_id,
  i.item_name,
  i.item_brand,
  i.item_category,
  COUNT(*) AS appearances,
  ROUND(AVG(i.price), 2) AS avg_price
FROM `{project}.{dataset}.events_*`,
  UNNEST(items) AS i
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  AND event_name = 'purchase'
  AND i.item_id IS NOT NULL AND i.item_id != '(not set)'
GROUP BY i.item_id, i.item_name, i.item_brand, i.item_category
ORDER BY appearances DESC
LIMIT 20;
```

| Pole items[] | % null/(not set) | Benchmark | Ocena |
|-------------|-----------------|-----------|-------|
| item_id | | < 2% | |
| item_name | | < 2% | |
| price | | 0% | |
| quantity | | 0% | |
| item_category | | < 15% | |
| item_brand | | < 20% | |

---

## 3K.5 — Duplikaty transakcji
**Priorytet:** Wysoki *(e-commerce only)*

**Czym jest i dlaczego sprawdzamy:**
Zduplikowane `transaction_id` w GA4 to jeden z najpoważniejszych błędów — podwójnie liczone transakcje zawyżają przychód, co prowadzi do błędnych decyzji budżetowych i fałszywego ROAS. Przyczyny: tag purchase wywołuje się dwa razy (np. z GTM i hardcoded), użytkownik odświeża stronę potwierdzenia, błąd w DataLayer (push purchase przy każdym page_view na stronie thankyou).

```sql
-- Duplikaty transaction_id w tym samym dniu
WITH purchases AS (
  SELECT
    event_date,
    ecommerce.transaction_id AS transaction_id,
    COUNT(*) AS event_count,
    SUM(ecommerce.purchase_revenue) AS total_revenue,
    COUNTIF(ecommerce.purchase_revenue > 0) AS events_with_revenue
  FROM `{project}.{dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN
    FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    AND event_name = 'purchase'
    AND ecommerce.transaction_id IS NOT NULL
  GROUP BY event_date, transaction_id
)
SELECT
  COUNT(*) AS total_transactions,
  COUNTIF(event_count > 1) AS duplicate_transactions,
  ROUND(COUNTIF(event_count > 1) / COUNT(*) * 100, 2) AS duplicate_pct,
  SUM(CASE WHEN event_count > 1 THEN total_revenue - (total_revenue / event_count) ELSE 0 END)
    AS estimated_inflated_revenue
FROM purchases;

-- Przykłady duplikatów
SELECT
  event_date,
  transaction_id,
  event_count,
  total_revenue,
  ROUND(total_revenue / event_count, 2) AS actual_order_value
FROM (
  SELECT
    event_date,
    ecommerce.transaction_id AS transaction_id,
    COUNT(*) AS event_count,
    SUM(ecommerce.purchase_revenue) AS total_revenue
  FROM `{project}.{dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN
    FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    AND event_name = 'purchase'
  GROUP BY event_date, transaction_id
)
WHERE event_count > 1
ORDER BY event_count DESC
LIMIT 10;
```

| Metryka | Wynik | Ocena |
|---------|-------|-------|
| Łączna liczba purchase events (30d) | | |
| Zduplikowane transaction_id | | |
| % duplikatów | | < 1% ✅ / 1–5% ⚠️ / >5% ❌ |
| Szacowany zawyżony przychód | | |

---

## 3K.6 — Jakość źródeł ruchu w BQ
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
GA4 przechowuje dane o źródle ruchu na czterech poziomach (user first touch, event params, collected_traffic_source, session_traffic_source_last_click). Weryfikujemy kompletność każdego poziomu, poziom `(not set)` oraz poprawność hierarchii COALESCE stosowanej w pipeline. Wynik tej sekcji bezpośrednio wpływa na wiarygodność modeli atrybucji.

```sql
SELECT
  -- Hierarchia source (od najbardziej do najmniej wiarygodnego)
  COUNTIF(collected_traffic_source.manual_source IS NOT NULL) AS has_collected_source,
  COUNTIF(session_traffic_source_last_click.manual_campaign.source IS NOT NULL) AS has_lastclick_source,
  COUNTIF(
    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'source') IS NOT NULL
  ) AS has_event_param_source,
  COUNTIF(traffic_source.source IS NOT NULL) AS has_first_touch_source,
  -- (not set) na poziomie sesji
  COUNTIF(
    COALESCE(
      collected_traffic_source.manual_source,
      session_traffic_source_last_click.manual_campaign.source,
      (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'source'),
      traffic_source.source
    ) IS NULL
  ) AS sessions_without_source,
  COUNT(*) AS total_session_starts
FROM `{project}.{dataset}.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  AND event_name = 'session_start';

-- Rozkład source/medium z hierarchią COALESCE (ostatnie 30d)
SELECT
  COALESCE(
    collected_traffic_source.manual_source,
    session_traffic_source_last_click.manual_campaign.source,
    traffic_source.source,
    '(direct)'
  ) AS source,
  COALESCE(
    collected_traffic_source.manual_medium,
    session_traffic_source_last_click.manual_campaign.medium,
    traffic_source.medium,
    '(none)'
  ) AS medium,
  COUNT(*) AS sessions
FROM `{project}.{dataset}.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  AND event_name = 'session_start'
GROUP BY source, medium
ORDER BY sessions DESC
LIMIT 30;
```

| Metryka | Wynik | Ocena |
|---------|-------|-------|
| % sesji z collected_traffic_source | | > 70% ✅ |
| % sesji z lastclick source | | |
| % sesji bez żadnego source (not set) | | < 5% ✅ |
| Dominacja direct/none | | < 30% ✅ |

---

## 3K.7 — User-ID pokrycie
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
User-ID (`user_id`) to identyfikator CRM przekazywany przez stronę dla zalogowanych użytkowników. Im wyższy odsetek sesji/eventów z User-ID — tym lepsze dane o cross-device, tym lepsza jakość modeli atrybucji. Niski odsetek przy sklepie z obowiązkową rejestracją = błąd wdrożenia.

```sql
SELECT
  COUNT(DISTINCT user_pseudo_id) AS total_users,
  COUNT(DISTINCT CASE WHEN user_id IS NOT NULL THEN user_pseudo_id END) AS users_with_crm_id,
  ROUND(
    COUNT(DISTINCT CASE WHEN user_id IS NOT NULL THEN user_pseudo_id END)
    / COUNT(DISTINCT user_pseudo_id) * 100, 2
  ) AS user_id_coverage_pct,
  -- Pokrycie wśród kupujących
  COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_pseudo_id END) AS buyers,
  COUNT(DISTINCT CASE WHEN event_name = 'purchase' AND user_id IS NOT NULL THEN user_pseudo_id END) AS buyers_with_id
FROM `{project}.{dataset}.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY));
```

| Metryka | Wynik | Ocena |
|---------|-------|-------|
| % użytkowników z User-ID | | > 20% dla sklepu z rejestracją ✅ |
| % kupujących z User-ID | | > 60% ✅ |

---

## 3K.8 — Spójność GA4 BQ vs GA4 UI
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Dane w BigQuery i w interfejsie GA4 powinny być spójne — ale mogą się różnić ze względu na: próbkowanie w UI, opóźnienie eksportu, różne definicje sesji, zagregowane dane o nowych użytkownikach. Delta > 5% w transakcjach lub przychodzie wskazuje na problem. To weryfikacja "sanity check" całego systemu.

```sql
-- Przychód i transakcje per tydzień z BQ
SELECT
  DATE_TRUNC(PARSE_DATE('%Y%m%d', _TABLE_SUFFIX), WEEK) AS week,
  COUNTIF(event_name = 'purchase') AS purchase_events,
  COUNT(DISTINCT ecommerce.transaction_id) AS unique_transactions,
  ROUND(SUM(ecommerce.purchase_revenue), 2) AS total_revenue,
  ROUND(AVG(ecommerce.purchase_revenue), 2) AS avg_order_value
FROM `{project}.{dataset}.events_*`
WHERE _TABLE_SUFFIX BETWEEN
  FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 60 DAY))
  AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  AND event_name = 'purchase'
  AND ecommerce.transaction_id IS NOT NULL
GROUP BY week
ORDER BY week DESC;
```

Porównaj wyniki z GA4 UI → Monetyzacja → Przegląd (ten sam zakres dat).

| Metryka (30d) | BQ | GA4 UI | Delta % | Ocena |
|--------------|-----|--------|---------|-------|
| Sesje | | | | |
| Transakcje | | | | < 5% ✅ |
| Przychód | | | | < 5% ✅ |
| AOV | | | | |

---

## 3K.9 — Zaawansowane: analiza ścieżek i retencji
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
BigQuery umożliwia analizy niemożliwe w interfejsie GA4: sekwencje zdarzeń per sesja, analiza retencji kohortowej, czas od pierwszej wizyty do zakupu, liczba sesji przed konwersją. Te dane są fundamentem rekomendacji UX i strategii marketingowych.

```sql
-- Liczba sesji przed pierwszym zakupem per użytkownik
WITH user_sessions AS (
  SELECT
    user_pseudo_id,
    CONCAT(user_pseudo_id, '-',
      (SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id')
    ) AS session_id,
    MIN(TIMESTAMP_MICROS(event_timestamp)) AS session_start,
    MIN(CASE WHEN event_name = 'purchase'
      THEN TIMESTAMP_MICROS(event_timestamp) END) AS first_purchase_ts
  FROM `{project}.{dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN
    FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  GROUP BY user_pseudo_id, session_id
),
first_purchase AS (
  SELECT user_pseudo_id, MIN(first_purchase_ts) AS first_purchase_ts
  FROM user_sessions WHERE first_purchase_ts IS NOT NULL
  GROUP BY user_pseudo_id
)
SELECT
  sessions_before_purchase,
  COUNT(*) AS user_count,
  ROUND(COUNT(*) / SUM(COUNT(*)) OVER() * 100, 1) AS pct
FROM (
  SELECT
    fp.user_pseudo_id,
    COUNT(DISTINCT us.session_id) AS sessions_before_purchase
  FROM first_purchase fp
  JOIN user_sessions us
    ON fp.user_pseudo_id = us.user_pseudo_id
    AND us.session_start <= fp.first_purchase_ts
  GROUP BY fp.user_pseudo_id
)
GROUP BY sessions_before_purchase
ORDER BY sessions_before_purchase;

-- Czas od pierwszej wizyty do zakupu (dni)
WITH first_visit AS (
  SELECT
    user_pseudo_id,
    MIN(DATE(TIMESTAMP_MICROS(event_timestamp), 'Europe/Warsaw')) AS first_visit_date
  FROM `{project}.{dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN
    FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
  GROUP BY user_pseudo_id
),
first_purchase AS (
  SELECT
    user_pseudo_id,
    MIN(DATE(TIMESTAMP_MICROS(event_timestamp), 'Europe/Warsaw')) AS purchase_date
  FROM `{project}.{dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN
    FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    AND event_name = 'purchase'
  GROUP BY user_pseudo_id
)
SELECT
  days_to_purchase,
  COUNT(*) AS users,
  ROUND(COUNT(*) / SUM(COUNT(*)) OVER() * 100, 1) AS pct_users
FROM (
  SELECT
    fp.user_pseudo_id,
    DATE_DIFF(fp.purchase_date, fv.first_visit_date, DAY) AS days_to_purchase
  FROM first_purchase fp
  JOIN first_visit fv USING(user_pseudo_id)
)
WHERE days_to_purchase >= 0
GROUP BY days_to_purchase
ORDER BY days_to_purchase
LIMIT 30;
```

| Obserwacja | Wynik | Interpretacja |
|-----------|-------|---------------|
| Mediana sesji przed zakupem | | |
| % kupujących w 1 sesji (impulse) | | |
| % kupujących po > 7 dniach | | |
| Mediana dni od wizyty do zakupu | | |

---

## 3K.10 — Ocena i punktacja BigQuery
**Priorytet:** —

| Punkt | Opis | Wynik | Max |
|-------|------|-------|-----|
| 3K.1 | Eksport aktywny i aktualny (lag ≤ 1 dzień) | | 3 |
| 3K.2 | Brak anomalii wolumenu (> 30% drop) | | 2 |
| 3K.3 | Kluczowe pola wypełnione (user_id, transaction_id, items) | | 3 |
| 3K.4 | items[] jakość: item_id < 2% null, price > 0 | | 3 |
| 3K.5 | Duplikaty transakcji < 1% | | 3 |
| 3K.6 | % (not set) source < 5% | | 2 |
| 3K.7 | User-ID coverage > 20% | | 2 |
| 3K.8 | Delta BQ vs GA4 UI < 5% | | 2 |

**Łącznie sekcja 3K:** ___/20

---

# SEKCJA 4 — Data Quality (Jakość Danych)

> Cel: Ocena wiarygodności danych w GA4. To najważniejsza sekcja z perspektywy analitycznej — bez dobrych danych żadna decyzja biznesowa oparta na GA4 nie ma wartości.

**Interpretacja wyników tej sekcji:**

| Wynik | Interpretacja | Działanie |
|-------|---------------|-----------|
| < 70% | Danym nie można ufać | Przed jakąkolwiek analizą konieczna jest naprawa jakości danych |
| 70–80% | Dane średniej jakości | Analiza możliwa z zastrzeżeniami — zaznacz ograniczenia w raporcie |
| > 80% | Wynik dobry | Można prowadzić analizy marketingowe i biznesowe |

---

## 4A — Wstępny przegląd ruchu

### 4.1–4.2 Udział "(not set)" w sesjach i użytkownikach
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
"(not set)" w GA4 oznacza brak informacji — GA4 nie wie skąd pochodzi wizyta. Naturalny poziom to < 5%. Wyższy udział wskazuje na problemy: brak UTM na kampaniach, błędna konfiguracja cross-domain (własna domena pojawia się jako referral), problemy z Consent Mode, lub błędy w implementacji tagów. Wysoki "(not set)" bezpośrednio uniemożliwia ocenę skuteczności kanałów marketingowych.

**Jak sprawdzić:** GA4 → Raporty → Pozyskiwanie ruchu → sprawdź udział sesji z source/medium = "(not set)". Powtórz dla Pozyskiwanie użytkowników.

| # | Punkt | Status | % (not set) | Komentarz |
|---|-------|--------|-------------|-----------|
| 4.1 | Sesje — udział (not set) | | | |
| 4.2 | Pierwsze źródło użytkownika — (not set) | | | |

---

### 4.3–4.6 Przegląd jakości ruchu

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 4.3 | Pierwsze źródło użytkownika wygląda naturalnie | Wysoki | Rozkład kanałów powinien odpowiadać oczekiwanemu mix mediów. Dominacja direct > 40% = podejrzane. | | |
| 4.4 | Pozostały ruch wygląda naturalnie | Wysoki | Sprawdź czy nie ma dziwnych nazw (google vs Google, cpc vs paid). Duplikaty nazw = problem z UTM. | | |
| 4.5 | Brak własnych domen w referral | Średni | Jeśli `twojadomena.pl` pojawia się jako referral = brak cross-domain tracking | | |
| 4.6 | Wszystkie źródła ruchu wyglądają naturalnie | Wysoki | Nagłe skoki z nowych źródeł = potencjalny spam lub błąd | | |
| 4.7 | Brak ruchu spamowego | Średni | Eksploracja: source/medium + bounce > 90% + czas sesji < 5s | | |
| 4.8 | Bramki płatności nie w referral | Wysoki | Jeśli payu.pl, przelewy24.pl itp. są w źródłach = brak wykluczenia bramek | | |
| 4.9 | Bramki pocztowe nie w referral | Wysoki | Jeśli wp.pl, gmail.com itp. są w źródłach = brak UTM na emailach | | |
| 4.10 | Facebook — ujednolicone dane | Średni | Sprawdź czy nie ma: facebook / fb / Facebook / Facebook.com jako oddzielnych źródeł | | |
| 4.11 | Ruch międzynarodowy | Średni | Rozkład geograficzny powinien odpowiadać rynkowi docelowym firmy | | |

---

## 4B — Jakość strony

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 4.12 | Strony docelowe | Średni | GA4 → Raporty → Strony docelowe. Brak (not set), brak podejrzanych URL, strony mają sens biznesowy. | | |
| 4.13 | Czas trwania sesji | Średni | GA4 → Engagement. E-commerce: realistyczny czas 2–5 min. < 30s = problem z tagiem lub boty. | | |
| 4.14 | Współczynnik zaangażowania | Średni | E-commerce: 40–70%. Poniżej 30% = problem z implementacją lub wysoki ruch spamowy. | | |
| 4.15 | Conversion Rate | Średni | E-commerce: branżowo 1–4%. Wartości > 20% lub < 0.1% są podejrzane. | | |
| 4.16 | Strona odsyłająca | Średni | Raporty → Pozyskiwanie → filtruj referral. Sprawdź czy nie ma podejrzanych domen. | | |
| 4.17 | Błędy JS | Wysoki | GA4 → Zdarzenia → szukaj `javascript_error` lub `exception`. Błędy JS mogą blokować tagi. | | |

---

## 4C — Szczegółowa analiza (not set) dla wymiarów

**Czym jest i dlaczego sprawdzamy:**
"(not set)" może pojawiać się w różnych wymiarach GA4. Jego analiza pozwala zlokalizować konkretny problem. Na przykład: (not set) w nazwie produktu = błąd w DataLayer (brak `item_name`). (not set) w transakcjach = atrybucja sprzedaży jest niemożliwa.

| # | Wymiar | Priorytet | Akceptowalny poziom | Status | % (not set) | Komentarz |
|---|--------|-----------|---------------------|--------|-------------|-----------|
| 4.18 | source/medium — (not set) | Wysoki | < 5% | | | |
| 4.19 | source/medium — direct/none | Wysoki | < 30% (branżowo) | | | |
| 4.20 | Trend (not set) w czasie | Wysoki | Brak nagłego wzrostu | | | |
| 4.21 | Trend direct w czasie | Wysoki | Stabilny | | | |
| 4.22 | Suma not set + direct | Wysoki | < 35% | | | |
| 4.23 | Landing page (not set) | Wysoki | < 5% | | | |
| 4.24 | Ścieżka strony (not set) | Wysoki | Brak wzorca | | | |
| 4.25 | Pierwszy użytkownik (not set) | Wysoki | < 5% | | | |
| 4.26 | Transakcje — (not set) | Wysoki | < 5% — krytyczne | | | |
| 4.27 | Tytuł strony | Średni | < 10% | | | |
| 4.28 | Kraj | Średni | Brak | | | |
| 4.29 | Kategoria urządzeń | Średni | Brak | | | |
| 4.30 | Przeglądarka | Średni | Brak | | | |
| 4.31 | Nazwa produktu | Średni | < 5% — brak nazwy = błąd w DataLayer | | | |
| 4.32 | Kategoria produktu | Średni | < 10% | | | |
| 4.33 | Marka produktu | Średni | < 10% | | | |

---

## 4D — Weryfikacja transakcji

**Czym jest i dlaczego sprawdzamy:**
Transakcje to najważniejsze zdarzenia w e-commerce. Błędna atrybucja transakcji (zbyt dużo direct, za dużo not set) oznacza, że nie wiemy które kampanie generują sprzedaż. To bezpośrednio uniemożliwia optymalizację budżetu reklamowego. Sprawdzamy nie tylko atrybucję, ale też duplikaty, kompletność parametrów i spójność danych e-commerce.

### 4D-A — Atrybucja transakcji

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 4.34 | Transakcje — udział (not set) | Wysoki | Eksploracja: source/medium × purchase. Udział (not set) w zakupach < 5%. | | |
| 4.35 | Transakcje — udział direct/none | Wysoki | Jw. Duży udział direct w transakcjach przy małym w sesjach = problem z atrybucją. | | |
| 4.36 | Łączny udział not set + direct w transakcjach | Wysoki | < 35% | | |
| 4.37 | Trend transakcji w czasie | Wysoki | GA4 → Monetyzacja → wykres. Anomalie nieuzasadnione kampaniami = potencjalny błąd. | | |

---

### 4D-B — Duplikaty transakcji (zdarzenia purchase)
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Zduplikowane `transaction_id` to cichy błąd — GA4 i Google Ads liczą tę samą transakcję wielokrotnie, zawyżając przychód i ROAS. Często niewidoczne w standardowych raportach GA4, ale wykrywalne przez eksploracje. Przyczyny: tag purchase wyzwala się przy każdym page_view strony thankyou, brak deduplication w GTM, zdarzenie wyzwalane przy odświeżeniu strony.

**Jak sprawdzić w GA4:**
1. Eksploracje → Eksploracja niestandardowa
2. Wymiary: `Transaction ID`, `Session default channel group`, `Date`
3. Metryki: `Transactions`, `Purchase revenue`
4. Filtr: szukaj tych samych wartości `Transaction ID` — jeśli ten sam ID pojawia się w wielu wierszach → duplikat
5. Alternatywa: GA4 → Monetyzacja → Zakupy e-commerce → filtruj po ID produktu, sprawdź czy te same transakcje nie są sumowane wielokrotnie

**Czerwone flagi:**
- Ten sam `transaction_id` z wieloma zdarzeniami w tej samej sesji lub dniu
- Nagłe skoki `Transactions` bez wzrostu `Sessions`
- AOV (przychód / transakcje) drastycznie niższy niż w systemie zamówień → zawyżona liczba transakcji

| Status | Duplikaty (estymacja %) | Komentarz |
|--------|------------------------|-----------|
| | | |

---

### 4D-C — Parametry zdarzenia purchase
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Zdarzenie `purchase` musi zawierać kompletny zestaw parametrów — bez nich raporty e-commerce są niekompletne lub błędne. Weryfikujemy wszystkie wymagane i rekomendowane parametry wg dokumentacji Google.

**Jak sprawdzić:** GA4 → DebugView po testowym zakupie LUB GA4 → Zdarzenia → kliknij `purchase` → sprawdź parametry.

**Wymagane parametry `purchase` wg Google:**

| Parametr | Typ | Wymagany? | Status | Wartość przykładowa |
|---------|-----|-----------|--------|---------------------|
| `transaction_id` | string | ✅ TAK | | `"T_12345"` |
| `value` | number | ✅ TAK | | `299.99` |
| `currency` | string | ✅ TAK — kod ISO 4217 | | `"PLN"` |
| `tax` | number | rekomendowany | | `56.09` |
| `shipping` | number | rekomendowany | | `9.99` |
| `coupon` | string | opcjonalny | | `"SUMMER20"` |
| `items` | array | ✅ TAK | | `[{...}]` |

**Typowe błędy:**
- `transaction_id` = `"undefined"` lub `""` lub `null` → krytyczny błąd
- `value` = `0` lub brak → przychód = 0 w GA4 i Google Ads
- `currency` puste → GA4 nie raportuje wartości konwersji do Ads
- `items` = `[]` (pusta tablica) → brak danych produktowych, BCG niemożliwa

| Status | Brakujące/błędne parametry | Komentarz |
|--------|--------------------------|-----------|
| | | |

---

### 4D-D — Parametry produktów w items[] przy purchase
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Każdy produkt w tablicy `items[]` powinien mieć kompletne dane. Bez `item_id` niemożliwa jest analiza produktowa, BCG Matrix i optymalizacja kampanii Shopping/PMax. Bez `price` raporty przychodowe są błędne.

**Jak sprawdzić:** GA4 → DebugView → zdarzenie purchase → rozwiń `items` → sprawdź każdy obiekt. Lub: GA4 → Monetyzacja → Zakupy produktów → sprawdź czy produkty mają nazwy i ID.

**Parametry items[] — kompletna weryfikacja (standard Google):**

| Parametr | Wymagany? | Akceptowalny % null | Status | Komentarz |
|---------|-----------|---------------------|--------|-----------|
| `item_id` | ✅ TAK | < 1% | | Klucz do analizy produktów i mapowania z Merchant Center |
| `item_name` | ✅ TAK | < 1% | | Czytelna nazwa produktu |
| `price` | ✅ TAK | 0% | | Cena jednostkowa (number, nie string) |
| `quantity` | ✅ TAK | 0% | | Ilość (brak = GA4 przyjmuje 1) |
| `discount` | rekomendowany | < 50% | | Kwota rabatu na sztukę |
| `item_brand` | rekomendowany | < 20% | | Marka produktu |
| `item_category` | rekomendowany | < 15% | | Kategoria L1 |
| `item_category2` | opcjonalny | — | | Kategoria L2 |
| `item_category3` | opcjonalny | — | | Kategoria L3 |
| `item_category4` | opcjonalny | — | | Kategoria L4 |
| `item_category5` | opcjonalny | — | | Kategoria L5 |
| `item_variant` | opcjonalny | — | | Wariant (kolor, rozmiar) |
| `item_list_name` | opcjonalny | — | | Skąd pochodzi produkt (lista/kategoria) |
| `item_list_id` | opcjonalny | — | | ID listy |
| `affiliation` | opcjonalny | — | | Sklep/magazyn/marka sklepu |
| `coupon` | opcjonalny | — | | Kupon per produkt |
| `index` | opcjonalny | — | | Pozycja na liście |
| `location_id` | opcjonalny | — | | ID lokalizacji (sklep stacjonarny) |

**Czerwone flagi:**
- `price` jako string zamiast number → błąd konwersji, dane są ignorowane
- `item_id` = `"undefined"`, `null` lub `""` → cały pipeline produktowy bezużyteczny
- Brak `quantity` → GA4 zakłada quantity=1, zaburza metryki ilościowe
- `item_name` = `"(not set)"` → raporty produktowe bez nazw

| Status | Problematyczne pola | Komentarz |
|--------|---------------------|-----------|
| | | |

---

## 4E — Weryfikacja zdarzeń e-commerce

### 4.38 Kompletność i poprawność zdarzeń e-commerce
**Priorytet:** Wysoki *(e-commerce only)*

**Czym jest i dlaczego sprawdzamy:**
Google definiuje standardowe zdarzenia e-commerce GA4 z wymaganymi parametrami na poziomie zdarzenia i produktu (`items[]`). Porównujemy wdrożone zdarzenia z pełną specyfikacją Google (developers.google.com/analytics/devguides/collection/ga4/ecommerce). Każde brakujące zdarzenie = ślepa plamka. Każde zdarzenie bez wymaganych parametrów = niepełne dane.

**Jak sprawdzić:** GA4 → Raporty → Zdarzenia → lista. Porównaj z tabelą poniżej. Weryfikuj parametry przez DebugView.

---

#### Pełna lista zdarzeń e-commerce GA4 — porównanie z wdrożeniem

**Ścieżka główna (funnel zakupowy):**

| Zdarzenie | Kiedy wywoływać | Param. zdarzenia (wymagane) | Param. zdarzenia (rekomend.) | items[] | Status | Komentarz |
|-----------|-----------------|----------------------------|------------------------------|---------|--------|-----------|
| `view_item_list` | Wyświetlenie listy produktów (kategoria, wyniki wyszukiwania) | — | `item_list_id`, `item_list_name` | ✅ Wymagane | | |
| `select_item` | Kliknięcie produktu na liście | — | `item_list_id`, `item_list_name` | ✅ Wymagane | | |
| `view_item` | Wyświetlenie strony produktu (PDP) | `currency`, `value` | — | ✅ Wymagane | | |
| `add_to_cart` | Dodanie do koszyka | `currency`, `value` | — | ✅ Wymagane | | |
| `remove_from_cart` | Usunięcie z koszyka | `currency`, `value` | — | ✅ Wymagane | | |
| `view_cart` | Wyświetlenie koszyka | `currency`, `value` | — | ✅ Wymagane (wszystkie produkty w koszyku) | | |
| `begin_checkout` | Przejście do kasy | `currency`, `value` | `coupon` | ✅ Wymagane | | |
| `add_shipping_info` | Wybór metody dostawy | `currency`, `value` | `coupon`, `shipping_tier` | ✅ Wymagane | | |
| `add_payment_info` | Wybór metody płatności | `currency`, `value` | `coupon`, `payment_type` | ✅ Wymagane | | |
| `purchase` | Potwierdzenie zamówienia | `transaction_id`, `value`, `currency` | `tax`, `shipping`, `coupon` | ✅ Wymagane | | |
| `refund` | Zwrot zamówienia | `transaction_id`, `currency` | `value`, `tax`, `shipping`, `coupon` | Opcjonalne (min. `item_id` + `quantity`) | | |

**Promocje:**

| Zdarzenie | Kiedy wywoływać | Param. zdarzenia | items[] | Status | Komentarz |
|-----------|-----------------|------------------|---------|--------|-----------|
| `view_promotion` | Wyświetlenie bannera/promocji | `creative_name`, `creative_slot`, `promotion_id`, `promotion_name` | ✅ Wymagane | | |
| `select_promotion` | Kliknięcie bannera/promocji | `creative_name`, `creative_slot`, `promotion_id`, `promotion_name` | ✅ Wymagane | | |

**Dodatkowe (opcjonalne ale wartościowe):**

| Zdarzenie | Kiedy wywoływać | Status | Komentarz |
|-----------|-----------------|--------|-----------|
| `add_to_wishlist` | Dodanie do listy życzeń | | |
| `search` | Wewnętrzne wyszukiwanie | | |
| `share` | Udostępnienie produktu | | |
| `login` | Logowanie użytkownika | | |
| `sign_up` | Rejestracja | | |

---

**Dla lead gen — sprawdź te zdarzenia:**

| Zdarzenie | Kiedy wywoływać | Status | Komentarz |
|-----------|-----------------|--------|-----------|
| `generate_lead` | Wypełnienie formularza leadowego | | |
| `form_submit` | Każde wysłanie formularza | | |
| `contact` | Kontakt (tel, email kliknięcie) | | |
| `schedule` | Rezerwacja terminu/spotkania | | |
| `newsletter_signup` | Zapis do newslettera | | |

---

**Weryfikacja parametrów zdarzeń przez DebugView — checklisty:**

| Zdarzenie | Czy wywołuje się? | currency OK? | value > 0? | items[] niepuste? | item_id != null? | Komentarz |
|-----------|------------------|-------------|------------|-------------------|------------------|-----------|
| `view_item` | | | | | | |
| `add_to_cart` | | | | | | |
| `view_cart` | | | | | | |
| `begin_checkout` | | | | | | |
| `add_shipping_info` | | | | | | |
| `add_payment_info` | | | | | | |
| `purchase` | | | | | | |

| Status ogólny | Brakujące zdarzenia | Zdarzenia z błędami parametrów |
|---------------|---------------------|-------------------------------|
| | | |

---

### 4.39–4.40 Jakość danych e-commerce

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 4.39 | Lejek e-commerce wygląda naturalnie | Wysoki | GA4 → Eksploracje → Lejek: view_item_list > view_item > add_to_cart > begin_checkout > purchase. Każdy krok mniejszy od poprzedniego. | | |
| 4.40 | AOV spójne dla różnych źródeł | Wysoki | Eksploracja: source/medium × transactions × revenue. Oblicz AOV = revenue/transactions. Jedno źródło z 10x wyższym AOV = anomalia. | | |

---

## 4F — Eksploracja jakości

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 4.41 | Użytkownicy nie zaczynają sesji od view_cart/checkout | Wysoki | Eksploracja → Lejek: pierwsze zdarzenie w sesji to session_start lub page_view. Brak użytkowników zaczynających od view_cart. | | |
| 4.42 | Google/cpc nie ma campaign=organic | Wysoki | Eksploracja: filtruj source=google, medium=cpc → sprawdź wartości `campaign`. Nie powinno być "(not set)" lub "organic". | | |

---

# SEKCJA 5 — UTM

> Cel: Weryfikacja standaryzacji i kompletności tagowania UTM. UTM to "metka" przyklejona do każdego linku marketingowego, informująca GA4 skąd pochodzi użytkownik. Bez UTM lub ze złymi UTM — dane atrybucji są bezużyteczne.

**Czym jest UTM i dlaczego to ważne:**
UTM (Urchin Tracking Module) to zestaw parametrów dodawanych do URL-i w kampaniach marketingowych: `utm_source` (skąd), `utm_medium` (przez co), `utm_campaign` (jaka kampania), `utm_content` (jaka kreacja), `utm_term` (jakie słowo kluczowe). Na przykład: `?utm_source=google&utm_medium=cpc&utm_campaign=black_friday`. Dzięki UTM GA4 wie że użytkownik przyszedł z kampanii Google Ads Black Friday — bez UTM ten sam użytkownik może pojawić się jako "direct" lub "not set", co uniemożliwia ocenę efektywności kampanii.

| # | Punkt | Priorytet | Jak sprawdzić | Status | Komentarz |
|---|-------|-----------|---------------|--------|-----------|
| 5.1 | Standaryzacja UTM | Niski | GA4 → Pozyskiwanie → lista unikalnych wartości source. Szukaj wariantów: meta / fb / Facebook / Facebook.com — każdy to oddzielne "źródło" w GA4. | | |
| 5.2 | Google Ads — UTM source/medium | Wysoki | GA4 → Pozyskiwanie → sprawdź czy jest ruch z `google/cpc`. Brak = kampanie Google Ads nie są tagowane. | | |
| 5.3 | Google Ads — UTM kampanii i niżej | Wysoki | Eksploracja → filtruj google/cpc → sprawdź wymiar "Kampania". Brak wartości lub "(not set)" = brak ValueTrack parameters. | | |
| 5.4 | Facebook Ads — UTM | Wysoki | GA4 → Pozyskiwanie → ruch z facebook/cpc lub facebook/paid. Sprawdź spójność wartości. | | |
| 5.5 | Facebook Ads — ID kampanii | Średni | Custom dimension lub parametr UTM zawierający `{{campaign.id}}` dla zaawansowanych analiz i atrybucji post-iOS14. | | |
| 5.6 | Organiczne social media — UTM | Średni | Sprawdź czy ruch z social z medium=organic_social lub social istnieje. Brak = posty organiczne wpadają w direct. | | |
| 5.7 | Email marketing — UTM | Średni | Sprawdź czy jest ruch z medium=email. Sprawdź czy nie ma referral z wp.pl, gmail.com (= brak UTM na emailach). | | |
| 5.8 | Wizytówka Google — UTM | Średni | Sprawdź ruch z gmb lub google_business. Wizytówka bez UTM = wchodzi jako direct lub google/organic. | | |
| 5.9 | Linki SEO — UTM | Średni | Linki sponsorowane bez UTM wpadają jako referral z domeny linkującej lub direct. | | |
| 5.10 | Pozostałe kanały — UTM | Średni | Przejrzyj z klientem listę aktywnych kanałów i zweryfikuj czy każdy ma UTM. | | |

---

# SEKCJA 6 — Rekomendacje

> Ta sekcja zawiera standardowe rekomendacje do uwzględnienia gdy dany element nie jest wdrożony. Agent wypełnia je na podstawie wyników audytu.

| Rekomendacja | Priorytet | Opis |
|-------------|-----------|------|
| Wydłużenie czasu trwania sesji do 5h | Wysoki | Standardowe 30 minut powoduje że użytkownicy robiący przerwę w zakupach "wracają" jako nowa sesja z direct. Wydłużenie do 5h zachowuje ciągłość sesji i poprawia atrybucję. |
| Ręczne zdarzenia zamiast automatycznych | Średni | Automatyczne zdarzenia GA4 (np. wyszukiwanie) są mniej precyzyjne. Wdrożenie ręcznego `search` w DataLayer daje pełną kontrolę nad jakością i parametrami zdarzenia. |
| Wykluczenie bramek płatności i pocztowych | Wysoki | Obowiązkowe dla e-commerce. Bez wykluczeń atrybucja transakcji jest zepsuta. |
| Brama tagów (CloudFlare Workers/Fastly) | Wysoki | Proxy dla requestów analitycznych przez własną domenę. Zapobiega blokowaniu przez ad-blockery i wydłuża życie cookies (Apple ITP). |
| Wdrożenie User-ID | Wysoki | Identyfikacja zalogowanych użytkowników ponad granicami urządzeń i sesji. Kluczowe dla e-commerce z kontem klienta. |
| Analiza i wykluczenie botów | Średni | Identyfikacja i wykluczenie znanych botów (Cookiebot, SemRush, Ahrefs) zawyżających ruch. |
| Wykluczenie ruchu wewnętrznego i deweloperskiego | Średni | Filtry IP dla pracowników i deweloperów. |
| Fingerprint dla client_id | Wysoki | Dodanie fingerprintu urządzenia do client_id poprawia identyfikację użytkowników w środowiskach bez cookies (Safari, Firefox). |
| Fingerprint dla session_id | Wysoki | Jw. dla identyfikacji sesji. |

---

# SEKCJA 8 — Spójność GA4 ↔ Google Ads

> **Warunek wejścia:** Aktywne połączenie GA4↔Google Ads (weryfikacja automatyczna przez API w KROK 2.5 — sprawdź czy wymiar `sessionGoogleAdsAdGroupName` jest dostępny). Jeśli brak połączenia → zaznacz 3.68 jako ❌ i pomiń tę sekcję.
>
> **Cel:** Weryfikacja czy dane między GA4 a Google Ads są spójne, czy konwersje są poprawnie importowane, czy smart bidding korzysta z właściwych danych. Rozbieżności w tej sekcji bezpośrednio przekładają się na błędną optymalizację kampanii i zawyżone/zaniżone ROAS.

---

## 8.1 — Status połączenia GA4 ↔ Google Ads
**Priorytet:** Wysoki

**Jak sprawdzić (automatycznie przez API):**
- Sprawdź dostępność wymiaru `sessionGoogleAdsAdGroupName` przez `get_property_schema` lub `get_ga4_data`
- Jeśli dostępny → połączenie aktywne
- Jeśli niedostępny → brak połączenia, błąd 3.68

**Jak sprawdzić (ręcznie):**
- GA4 → Admin → Połączone usługi → Google Ads → Status "Połączono"
- Google Ads → Narzędzia → Połączone konta → Google Analytics 4

| # | Punkt | Status | Komentarz |
|---|-------|--------|-----------|
| 8.1 | Połączenie GA4↔Ads aktywne | | |
| 8.2 | Reklamy spersonalizowane włączone | | |
| 8.3 | Konwersje GA4 widoczne w Google Ads | | |

---

## 8.2 — Delta przychodów: GA4 vs Google Ads
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Przychód raportowany przez Google Ads i przychód raportowany przez GA4 (filtr: kanał CPC) powinny być podobne. Duża delta (>30%) wskazuje na: różne okna atrybucji, brak `currency` w zdarzeniu purchase, rozbieżności w modelowaniu konwersji, błędnie skonfigurowane konwersje w Ads.

**Jak sprawdzić:**

```
# Przez mcp__ga4-analytics:
get_ga4_data(
  dimensions=["sessionDefaultChannelGroup"],
  metrics=["sessions", "ecommercePurchases", "purchaseRevenue"],
  date_from="30daysAgo",
  filters={"sessionDefaultChannelGroup": ["Paid Search", "Paid Shopping", "Cross-network"]}
)
→ Porównaj purchaseRevenue z kosztem i przychodem w Google Ads (BDOS lub Google Ads UI)
```

| Metryka (30d) | GA4 (CPC/Cross-network) | Google Ads | Delta % | Ocena |
|--------------|------------------------|------------|---------|-------|
| Transakcje | | | | < 20% ✅ |
| Przychód | | | | < 20% ✅ |
| ROAS (GA4) vs ROAS (Ads) | | | | |

**Typowe przyczyny dużej delty:**
- GA4 używa atrybucji Data-Driven (many channels), Ads Last-Click → różne wyniki
- Brak `currency` w purchase → GA4 nie raportuje wartości
- Cross-network (PMax) nie jest w filtrze CPC → GA4 niedoszacowuje
- Okno konwersji Ads (30d klik) vs GA4 (7d domyślnie)

| Status | Delta % | Główna przyczyna | Komentarz |
|--------|---------|-----------------|-----------|
| | | | |

---

## 8.3 — Konwersje importowane z GA4 do Google Ads
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Google Ads może używać konwersji z dwóch źródeł: własnych tagów Google Ads lub importowanych z GA4. Korzystanie z konwersji GA4 jest rekomendowane — są dokładniejsze (Consent Mode, modelowanie). Sprawdzamy czy import jest aktywny, czy konwersje mają poprawną kategorię i wartość.

**Jak sprawdzić:** Google Ads → Cele → Konwersje → sprawdź źródło konwersji.

| Konwersja | Źródło (GA4 / Ads tag / import) | Kategoria | Wartość | Główna? | Status |
|-----------|--------------------------------|-----------|---------|---------|--------|
| | | | | | |
| | | | | | |

**Czerwone flagi:**
- Konwersja `purchase` z wartością = 1 zł (błąd domyślnej wartości zamiast AOV)
- Konwersja z kategorią "Inne" zamiast "Zakup"
- Brak konwersji z wartością przy kampaniach bidujących na ROAS (Target ROAS bez wartości = błąd)
- Duplikaty konwersji (ta sama akcja liczona z Ads taga I z GA4)

| Status | Błędy | Komentarz |
|--------|-------|-----------|
| | | |

---

## 8.4 — Smart bidding i jakość sygnałów
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Smart bidding (Target ROAS, Target CPA, Maximize Conversion Value) korzysta z sygnałów konwersji aby optymalizować stawki. Jeśli konwersje mają błędne wartości (1 zł zamiast AOV), brak historii lub są zduplikowane — algorytm biduje na podstawie złych danych, co przekłada się bezpośrednio na zły ROAS.

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Kampanie z Target ROAS mają konwersje wartościowe (nie 1 zł)? | | |
| Konwersja `purchase` jako "Primary" (nie Secondary)? | | |
| Historia konwersji ≥ 30 (dla prawidłowego działania smart biddingu)? | | |
| Brak duplikatów konwersji (tag Ads + import GA4 tej samej akcji)? | | |
| Enhanced Conversions włączone dla konwersji zakupu? | | |

---

## 8.5 — Enhanced Conversions — jakość matchingu w GA4
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Enhanced Conversions (EC) poprawiają dokładność pomiaru konwersji poprzez hashowanie danych pierwszej strony (email, telefon, imię) i wysyłanie ich do Google w momencie konwersji. Dzięki EC Google może przypisać konwersję do użytkownika nawet jeśli cookie zostało usunięte lub zablokowane. Jest to kluczowe w dobie iOS 14+, ITP (Safari) i blokowania cookies przez Firefox. Bez EC tracisz 15–30% danych konwersyjnych — algorytm smart bidding "widzi" mniej konwersji i biduje zachowawczo.

**Jak sprawdzić:**
- Google Ads → Cele → Konwersje → kliknij konwersję zakupu → sekcja "Enhanced Conversions" → sprawdź status
- GA4 → Admin → Połączone usługi → Google Ads → Enhanced Conversions
- GTM: sprawdź czy tag "Google Ads Conversion Tracking" ma skonfigurowane pola: `email`, `phone_number`, `first_name`, `last_name`

**Weryfikacja jakości matchingu:**
- Google Ads → Cele → Diagnostyka konwersji → kolumna "Enhanced conversions match rate"
- Benchmark: match rate > 40% = dobra implementacja; < 20% = problem z danymi lub wdrożeniem

**Czerwone flagi:**
- Enhanced Conversions włączone ale match rate < 10% → dane są hashowane z błędem (email nie w formacie przed hashowaniem, brak normalizacji)
- Tag EC skonfigurowany ale dane nie napływają → tag nie wyzwala się na stronie potwierdzenia
- Dane osobowe w czytelnej formie zamiast zahashowane → błąd RODO

| # | Punkt | Status | Wynik | Komentarz |
|---|-------|--------|-------|-----------|
| 8.5.1 | Enhanced Conversions włączone w Google Ads | | | |
| 8.5.2 | EC skonfigurowane w GTM (pola: email, phone) | | | |
| 8.5.3 | Match rate > 40% | | | |
| 8.5.4 | Dane są hashowane (SHA-256) przed wysłaniem | | | |
| 8.5.5 | EC obejmuje konwersję purchase (primary) | | | |

---

## 8.6 — Audience Lists — eksport do Google Ads i jakość
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
GA4 może budować grupy odbiorców (audiences) na podstawie zachowania użytkowników i eksportować je do Google Ads. To fundament remarketingu i Customer Match. Bez poprawnie skonfigurowanych list odbiorców kampanie Google Ads nie mają dostępu do najcenniejszych segmentów: porzucających koszyk, oglądających konkretne produkty, klientów z ostatnich 30 dni. Sprawdzamy czy listy są zbudowane, aktualizowane i czy rozmiar jest wystarczający do działania remarketingu (min. 1000 użytkowników dla Display, 1000 dla Search RLSA).

**Jak sprawdzić:**
- GA4 → Admin → Odbiorcy → lista grup + rozmiary
- Google Ads → Narzędzia → Menadżer odbiorców → Twoje segmenty danych → sprawdź czy listy GA4 są zsynchronizowane i mają status "Gotowe"
- Sprawdź czy audience listy są używane w kampaniach (w ustawieniach grup reklam lub PMax Audience Signals)

**Kluczowe listy do weryfikacji:**

| Lista odbiorców | Okno | Min. rozmiar | Status GA4 | Rozmiar | Używana w Ads? |
|-----------------|------|-------------|------------|---------|---------------|
| Wszyscy użytkownicy (All Users) | 30d | 1000+ | | | |
| Porzucający koszyk (add_to_cart bez purchase) | 30d | 500+ | | | |
| Oglądający produkt (view_item) bez zakupu | 14d | 500+ | | | |
| Kupujący — powracający (purchase w 180d) | 180d | 200+ | | | |
| Odwiedzający stronę bez zaangażowania | 7d | 1000+ | | | |
| Niestandardowe segmenty (np. kategoria X) | — | — | | | |

**Czerwone flagi:**
- Brak eksportu GA4 → Ads (listy nie widoczne w Ads)
- Listy z rozmiarem "< 1000" → za małe do działania RLSA/Display
- Listy nieużywane w żadnej kampanii → marnujemy dane GA4
- Brak listy "Porzucający koszyk" → najtańszy i najskuteczniejszy remarketing pominięty

**Łącznie sekcja 8:** ___/12

---

## 8.7 — Conversion Value Rules
**Priorytet:** Niski

**Czym jest i dlaczego sprawdzamy:**
Conversion Value Rules to zaawansowana funkcja Google Ads pozwalająca modyfikować raportowaną wartość konwersji w zależności od segmentu użytkownika. Na przykład: zakup od nowego klienta wart jest 2x więcej niż od powracającego (bo generuje nową relację), zakup z Warszawy wart więcej niż z mniejszego miasta. Reguły pozwalają Smart Biddingowi bidować agresywniej na bardziej wartościowych użytkowników.

**Jak sprawdzić:** Google Ads → Cele → Reguły wartości konwersji.

| Pytanie | Wynik |
|---------|-------|
| Czy są skonfigurowane reguły wartości konwersji? | |
| Czy nowi klienci (new customer) mają wyższy mnożnik? | |
| Czy reguła geograficzna jest skonfigurowana (jeśli dotyczy)? | |
| Czy reguła "urządzenie" jest skonfigurowana? | |

---

## 8.8 — Audience Audit: pełna weryfikacja list odbiorców
**Priorytet:** Wysoki

> Rozszerzona weryfikacja list remarketingowych — sprawdź nie tylko istnienie ale JAKOŚĆ i UŻYCIE każdej listy.

### 8.8.1 — Kompletność zestawu list w GA4

**Standard kompletny (e-commerce):**

| Lista | Definicja | Okno | Minimum | Status | Rozmiar | W kampaniach? |
|-------|-----------|------|---------|--------|---------|---------------|
| All visitors — 30d | Wszystkie sesje | 30d | 1000+ | | | |
| All visitors — 90d | Wszystkie sesje | 90d | 5000+ | | | |
| Purchasers — 180d | purchase event | 180d | 200+ | | | |
| Cart abandoners | add_to_cart bez purchase, 14d | 14d | 500+ | | | |
| Product viewers | view_item bez purchase, 14d | 14d | 500+ | | | |
| Checkout starters | begin_checkout bez purchase, 7d | 7d | 200+ | | | |
| High-value customers | purchase × revenue > AOV × 1.5 | 180d | 100+ | | | |
| Category viewers (konkretna kategoria) | view_item + item_category = X | 30d | 200+ | | | |
| Engaged visitors | engagementTime > 120s | 30d | 1000+ | | | |
| New users without purchase | session_start, brak purchase | 30d | 1000+ | | | |

### 8.8.2 — Customer Match

**Czym jest:** Customer Match pozwala przesłać listę klientów (emaile, telefony) do Google Ads i targetować ich bezpośrednio w kampaniach Search, Shopping i YouTube. Najlepszy ROAS ze wszystkich form remarketingu bo targetujesz prawdziwych klientów z historią zakupów.

**Weryfikacja:**

| Punkt | Status | Komentarz |
|-------|--------|-----------|
| Konto Google Ads spełnia wymagania Customer Match (min. wydatki, historia) | | Sprawdź: Ads → Menadżer odbiorców → Customer Match |
| Listy Customer Match przesłane i aktywne | | |
| Match rate > 30% (< 30% = zła jakość danych emaili) | | |
| Listy Customer Match używane jako "Audience Signal" w PMax | | |
| Listy Customer Match używane w RLSA (Search) | | |
| Listy Customer Match w wykluczeniach (np. obecni klienci wykluczeni z akwizycji) | | |

### 8.8.3 — RLSA (Remarketing Lists for Search Ads)

**Czym jest:** RLSA to użycie list remarketingowych do modyfikowania stawek w kampaniach Search. Np. biduj 30% wyżej gdy użytkownik szuka hasła brandowego i był wcześniej na stronie produktu. To zwiększa CR kampanii Search bez podnoszenia kosztu dla zimnego ruchu.

| Punkt | Status | Komentarz |
|-------|--------|-----------|
| Kampanie Search mają przypisane listy RLSA | | Ads → kampania → Odbiorcy |
| Stosowane bid adjustments per lista (np. cart abandoners: +50%) | | |
| Tryb "Observation" (zalecany) lub "Targeting" (węższy zasięg) | | |
| Osobna kampania brand dla RLSA (wyższe stawki dla remarketingu brand) | | |

### 8.8.4 — Szacunek wpływu braku remarketingu

Jeśli brak list lub są puste:

```
Szacowany koszt braku remarketingu:
- Cart abandoners (4% CR vs 0.8% CR cold traffic):
  sesje_cart_abandoners × (0.04 - 0.008) × AOV = utracony przychód/msc
- Powracający klienci (ROAS 8x vs ROAS 3x cold):
  wydatki_remarketing × (8-3) = nadmiarowy przychód możliwy do osiągnięcia
```

| Segment | Sesje/msc | CVR cold | CVR remarketing | Utracony przychód PLN |
|---------|-----------|---------|-----------------|----------------------|
| Cart abandoners | | 0.8% | 4% | |
| Viewers bez zakupu | | 0.3% | 1.5% | |
| Powracający klienci | | — | — | potencjalny ROAS x2 |
| **ŁĄCZNIE szacunkowo** | | | | PLN/msc |

---

## 8.9 — Attribution Model: porównanie modeli atrybucji
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Model atrybucji decyduje jak Google Ads i GA4 "przypisują" zasługę za konwersję do poszczególnych touchpointów w ścieżce zakupowej. Domyślny Data-Driven Attribution (DDA) Google Ads vs Last Click vs First Click może dawać bardzo różne wyniki — szczególnie dla kampanii Upper Funnel (Display, Video, DemGen). Błędny model może powodować niedoinwestowanie kampanii świadomościowych (bo "nie konwertują" wg Last Click) lub ich nadmierną wycenę.

**Jak sprawdzić:**
- Google Ads → Raporty → Modele atrybucji (Attribution) → porównaj Last Click vs Data-Driven
- GA4 → Admin → Atrybucja → Model raportowania

| Model | Zastosowanie | Transakcje (30d) | Przychód | ROAS | Delta vs Last Click |
|-------|-------------|-----------------|---------|------|---------------------|
| Last Click | Bazowy (referencja) | | PLN | x | 0% |
| Data-Driven (DDA) | Rekomendowany | | PLN | x | % |
| Linear | Cross-check | | PLN | x | % |
| Time Decay | Cross-check | | PLN | x | % |
| First Click | Świadomość | | PLN | x | % |

**Interpretacja delty DDA vs Last Click:**
- Delta > 20% dla Display/Video → kampanie świadomościowe mają realny wpływ, niedoceniany przez Last Click
- Delta < 5% → ścieżki zakupowe są krótkie (1-2 touchpointy), model nie ma dużego znaczenia
- Delta negatywna dla Search Brand → marka jest "zbieraczem" konwersji, Search brandowy może być przeinwestowany

**Rekomendacja modelu dla konta:**

| Typ konta | Rekomendowany model | Uzasadnienie |
|-----------|--------------------|--------------| 
| E-commerce — prosty (1 wizyta → zakup) | Last Click | Krótka ścieżka, DDA bez przewagi |
| E-commerce — złożony (wiele touchpointów) | Data-Driven | DDA odzwierciedla prawdziwy mix |
| Lead gen (długi cykl sprzedaży) | Data-Driven lub 60-90d time decay | Uwzględnia górę lejka |
| Brand + Performance mix | Data-Driven | Rozdziela rolę Brand vs Non-brand |

---

# Pytania briefingowe po audycie

Po zakończeniu weryfikacji technicznej zadaj użytkownikowi następujące pytania w celu uzupełnienia raportu:

1. Jakie są główne cele biznesowe klienta w kontekście analityki? (np. optymalizacja ROAS, redukcja porzuceń koszyka, wzrost udziału mobile)
2. Czy są znane problemy techniczne lub zmiany wdrożeniowe w ostatnich 3 miesiącach?
3. Które kanały marketingowe są priorytetowe dla klienta? (określa co jest krytyczne vs. opcjonalne)
4. Czy klient prowadzi sprzedaż na innych platformach niż strona? (marketplace, aplikacja)
5. Czy były reklamacje dotyczące jakości danych analitycznych? (np. rozbieżności z systemem zamówień)
6. Jaki jest poziom zaawansowania technicznego osoby która będzie wdrażać rekomendacje?

---

# SEKCJA 9 — Analiza danych

> Cel: Ocena biznesowo-marketingowa wyników mierzonych przez GA4. Uzupełnienie audytu technicznego (sekcje 1–8) o perspektywę efektywności kanałów, zachowań użytkowników i potencjału wzrostu. Wypełniaj wyłącznie w oparciu o dane z GA4 API.

---

## KROK: Dane do pobrania automatycznie (GA4 API)

Przed wypełnieniem sekcji uruchom następujące zapytania:

```
# 1. Efektywność kanałów — 90 dni
get_ga4_data(
  dimensions=["sessionDefaultChannelGroup"],
  metrics=["sessions", "totalUsers", "engagementRate", "ecommercePurchases",
           "totalRevenue", "addToCarts", "checkouts"],
  date_from="90daysAgo"
)

# 2. Analiza urządzeń — 90 dni
get_ga4_data(
  dimensions=["deviceCategory"],
  metrics=["sessions", "totalUsers", "engagementRate",
           "ecommercePurchases", "totalRevenue"],
  date_from="90daysAgo"
)

# 3. Trend dzienny — 90 dni (do wykrycia anomalii i trendów)
get_ga4_data(
  dimensions=["date"],
  metrics=["sessions", "totalUsers", "engagementRate",
           "averageSessionDuration", "ecommercePurchases", "totalRevenue"],
  date_from="90daysAgo",
  enable_aggregation=False
)

# 4. Source/medium top 25 — 30 dni
get_ga4_data(
  dimensions=["sessionSourceMedium"],
  metrics=["sessions", "ecommercePurchases", "totalRevenue", "engagementRate"],
  date_from="30daysAgo",
  limit=25
)

# 5. Kraje — 90 dni
get_ga4_data(
  dimensions=["country"],
  metrics=["sessions", "totalUsers", "ecommercePurchases", "totalRevenue"],
  date_from="90daysAgo",
  limit=15
)

# 6. Zdarzenia — 90 dni (sygnały omnichannel, lojalność, UX)
get_ga4_data(
  dimensions=["eventName"],
  metrics=["eventCount", "keyEvents"],
  date_from="90daysAgo"
)
```

---

## Jak liczyć i interpretować

### 9.1 — Efektywność kanałów

**CVR per kanał** = ecommercePurchases / sessions × 100%
**Rev/sesja** = totalRevenue / sessions
**Stosunek paid/organic CVR** = CVR_paid_search / CVR_organic_search × 100%
- Benchmark: ≥ 50% oznacza sensowną jakość ruchu płatnego względem organicznego
- < 30% = sygnał alarmu — ruch płatny jest słabej jakości lub LP niedopasowany

**Punktacja (max 4 pkt):**
- Najlepszy kanał płatny ≥ 70% CVR organic: 2 pkt
- Żaden kanał płatny < 0,2% CVR przy wydatkach: 2 pkt

**Czerwone flagi:**
- Paid Social CVR < 0,3% — typowy sygnał zbyt szerokiego targetowania
- Display CVR < 0,1% — możliwy ruch bot/viewability problem
- PMax CVR < 0,4% — PMax kanibalizuje ruch organiczny bez zwrotu

---

### 9.2 — Analiza urządzeń

**Mobile/Desktop CVR ratio** = CVR_mobile / CVR_desktop × 100%
- Benchmark: ≥ 60% = ok; 40–60% = do poprawy; < 40% = krytyczny mobile gap
- Typowe przyczyny: wolne ładowanie, trudny checkout, brak BLIK/Google Pay

**Szacunek potencjału:**
- Dodatkowe transakcje = sesje_mobile × (CVR_docelowy - CVR_obecny)
- CVR docelowy = 70% CVR desktop (realny target przy UX mobile fix)

**Punktacja (max 2 pkt):**
- Mobile CVR ≥ 60% desktop: 2 pkt
- Mobile CVR 40–59% desktop: 1 pkt
- Mobile CVR < 40% desktop: 0 pkt

---

### 9.3 — Trend ruchu i zaangażowania

Pogrupuj dane dzienne na okresy (np. miesiące lub co 30 dni). Oblicz:
- Średnie sesje/dzień per okres
- Średni engagement rate per okres
- Średni averageSessionDuration per okres

**Sygnały alarmowe:**
- Engagement rate spada o > 5 p.p. między okresami → pogorszenie jakości ruchu (możliwa zmiana mix kanałów)
- Avg session duration spada o > 20% → użytkownicy nie angażują się (UX, content, mobile)
- Nagły wzrost sesji bez wzrostu transakcji → bot/spamowy ruch lub zdarzenie bez intencji zakupowej

**Punktacja (max 2 pkt):**
- Engagement rate stabilny lub rosnący: 2 pkt
- Spadek o 5–10 p.p.: 1 pkt
- Spadek > 10 p.p.: 0 pkt

---

### 9.4 — Wartość zamówienia i struktura sprzedaży

**AOV** = totalRevenue / ecommercePurchases
Porównaj AOV per kanał — rozbieżności > 50% między kanałami mogą wskazywać na:
- Różne produkty kupowane z różnych kanałów (email → droższe, social → tańsze)
- Problem z duplikatami transakcji (revenue=0 w duplikatach zaniża/zawyża)

**Punktacja (max 2 pkt):**
- AOV spójne ± 30% między głównymi kanałami: 2 pkt
- Duże rozbieżności: 0 pkt + komentarz

---

### 9.5 — Lejek porzuceń (behawioralny)

Oblicz na podstawie danych eventów:
- **view→cart rate** = add_to_cart / view_item × 100% (benchmark: 5–20%)
- **cart→checkout rate** = begin_checkout / add_to_cart × 100% (benchmark: 30–60%)
- **checkout→purchase rate** = purchase / begin_checkout × 100% (benchmark: 50–80%)

Jeśli checkout→purchase > 100% → begin_checkout nie działa poprawnie (błąd implementacji — raportuj w Sekcji 4).

**Wskaźnik porzucenia koszyka** = 1 - (purchase / add_to_cart)
- Benchmark: 70–80% porzuceń
- > 90% = alarm — sprawdź UX koszyka, checkout, metody płatności

**Punktacja (max 2 pkt):**
- cart→checkout ≥ 20%: 2 pkt
- cart→checkout 10–19%: 1 pkt
- cart→checkout < 10% lub begin_checkout wadliwy: 0 pkt

---

### 9.6 — Sygnały omnichannel i lojalność

Przejrzyj zdarzenia niestandardowe. Szukaj:

| Typ sygnału | Przykładowe event names | Co oznacza |
|-------------|------------------------|------------|
| Offline interest | "znajdź w salonie", "mapa", "oddziały", "store_locator" | Klient chce zobaczyć produkt offline — ROAS online niedoszacowany |
| Lojalność | "dołącz do PL", "join_loyalty", "zapisz się do klubu" | Program lojalnościowy aktywny — warto mierzyć LTV |
| Alerty | "mailalert", "price_alert", "notify_me" | Klient odłożył zakup — potencjał sekwencji email/SMS |
| Login | "login" | Duży udział zalogowanych → możliwy User-ID → lepszy cross-device |
| Wishlist | "add_to_wishlist" | Lista życzeń aktywna → remarketing materialny |

Jeśli event "offline interest" > 5% sesji → zarekomenduj offline conversion import do Google Ads.
Jeśli login > 50% sesji → zarekomenduj aktywację User-ID w GA4.

**Punktacja (max 2 pkt):**
- Wykryto sygnały omnichannel i raportują się poprawnie: 1 pkt
- Wykryto program lojalnościowy z mierzalnymi zdarzeniami: 1 pkt

---

### 9.7 — Analiza geograficzna

Sprawdź top 10 krajów. Oceń:
- **Ruch bez konwersji** (duży wolumen sesji, CVR ≈ 0%) → możliwy bot/scraper → zablokować w GA4 lub Google Ads audience exclusions
- **Kraje z CVR wyższym niż główny rynek** → potencjał ekspansji
- **Kraje EU z ruchem > 500 sesji/90d** → sprawdzić czy strona ma lokalizację (język, waluta, dostawa)

**Punktacja (max 2 pkt):**
- Brak podejrzanego ruchu (kraj 0 CVR, > 500 sesji): 1 pkt
- Główny rynek > 90% przychodu (zdrowa koncentracja): 1 pkt

---

### 9.8 — Ukryte możliwości i quick wins

Przeanalizuj source/medium top 25. Szukaj:

| Sygnał | Jak identyfikować | Rekomendacja |
|--------|------------------|--------------|
| Organic Bing z CVR > organic Google | CVR = purchases/sessions > google/organic CVR | Uruchomić Microsoft Ads |
| Referral z CVR > 2% | np. poczta.wp.pl, webmaile | UTM na emaile transakcyjne lub wyklucz z referral |
| google/maps z CVR > 1% | 526+ sesji, CVR > 1% | Aktywuj Google Business Posts |
| Bramki płatności w referral | klarna, paypal, przelewy24 | Wyklucz z referral w GA4 |
| Social referral (l.instagram.com) z CVR < 0,5% | | Dodaj UTM do linków w bio/stories |

**Punktacja (max 2 pkt):**
- Zidentyfikowano ≥ 2 quick wins z danymi: 1 pkt
- Bramki płatności nie pojawiają się w referral: 1 pkt

---

---

### 9.9 — Retencja i wartość klienta w czasie (LTV per kanał)

**Czym jest i dlaczego sprawdzamy:**
Analiza LTV (Customer Lifetime Value) per kanał to jedna z najważniejszych analiz, której nie robi 90% audytów. Kanał może mieć gorszy ROAS w pierwszej transakcji, ale pozyskiwać klientów którzy kupują częściej i dłużej — co czyni go najlepszym kanałem pod względem faktycznej rentowności. Bez tej analizy budżet reklamowy jest alokowany na podstawie niepełnych danych. Sprawdzamy powracających kupujących, częstotliwość zakupów i udział transakcji od powracających klientów.

**Dane do pobrania:**
```
# Nowi vs powracający per kanał (90d)
get_ga4_data(
  dimensions=["sessionDefaultChannelGroup", "newVsReturning"],
  metrics=["sessions", "ecommercePurchases", "purchaseRevenue"],
  date_from="90daysAgo"
)

# Częstotliwość zakupów per kanał (jeśli User-ID aktywne)
get_ga4_data(
  dimensions=["sessionDefaultChannelGroup"],
  metrics=["totalUsers", "ecommercePurchases", "purchaseRevenue"],
  date_from="90daysAgo"
)
→ Oblicz: zakupy/użytkownik = częstotliwość. Wyżej = lojalniejszy kanał.
```

**Jak interpretować:**
- **Zakupy/użytkownik** = ecommercePurchases / totalUsers per kanał
  - > 1.5 = kanał z dużym powrotem (email, direct, SEO brandowe)
  - < 1.1 = jednorazowi klienci (display, demand gen, nowe kampanie)
- **Revenue/użytkownik** = najlepsza miara wartości kanału długoterminowo
- **% transakcji od powracających** per kanał — email i direct mają zwykle > 40%

**Punktacja (max 2 pkt):**
- Zidentyfikowano top kanał LTV vs top kanał jednorazowy (z danymi): 1 pkt
- Kanał z najwyższym LTV ma alokację budżetu adekwatną do wartości: 1 pkt

**Czerwone flagi:**
- Email marketing z revenue/użytkownik 3x wyższy niż paid — a brak inwestycji w email → missed opportunity
- Direct z 50%+ transakcji od powracających → klienci kupują ponownie bez reklamy (brand jest silny, oszczędność na remarketingu)
- Paid social z zakupy/użytkownik < 1.05 → jednorazowi, nierentowni klienci

---

### 9.10 — Analiza wyszukiwań wewnętrznych
**Priorytet:** Średni *(tylko jeśli strona ma wyszukiwarkę i event `search` jest wdrożony)*

**Czym jest i dlaczego sprawdzamy:**
Wewnętrzna wyszukiwarka to kopalnia informacji o intencji zakupowej — klienci mówią wprost czego szukają. Frazy wyszukiwane przez użytkowników to gotowy materiał na: nowe kategorie produktów, brakujące asortymentowe, tematy SEO i copywriting reklam Google Ads. Fraza wyszukana i niezakupiona = produkt, który strona powinna mieć lub lepiej prezentować.

**Jak sprawdzić:**
```
# Wyszukiwania wewnętrzne — frazy i co po nich następuje
get_ga4_data(
  dimensions=["searchTerm", "sessionDefaultChannelGroup"],
  metrics=["eventCount", "ecommercePurchases", "totalRevenue"],
  date_from="90daysAgo",
  filters={"eventName": "search"}
)
→ Frazy z wysoką liczbą wyszukiwań i CVR = 0% → produkt niedostępny lub źle wyświetlany
→ Frazy z CVR > 2% → najsilniejsze intencje zakupowe → materiał na słowa kluczowe Search
```

**Analiza wyników:**

| Kategoria frazy | Co oznacza | Rekomendacja |
|-----------------|------------|--------------|
| Wysoka częstotliwość + CVR < 0.5% | Produkt brakuje lub jest ukryty | Dodaj do asortymentu lub popraw widoczność |
| Wysoka częstotliwość + CVR > 2% | Silna intencja, dobra oferta | Użyj jako słowa kluczowe w kampanii Search |
| Branded search (własna marka) | Klienci szukają konkretnego produktu | Sprawdź czy kampania brandowa jest aktywna |
| Typo / błędy ortograficzne | Problem z UX wyszukiwarki | Wdrożenie fuzzy search lub aliasów |

**Punktacja (max 2 pkt):**
- Zdarzenie `search` wdrożone i raportuje frazy: 1 pkt
- Zidentyfikowano ≥ 3 frazy z insight (brakujący produkt lub materiał do Ads): 1 pkt

---

### 9.11 — Analiza kohortowa: powracający kupujący
**Priorytet:** Średni *(wymaga User-ID lub BigQuery)*

**Czym jest i dlaczego sprawdzamy:**
Analiza kohortowa pokazuje co dzieje się z klientami po pierwszym zakupie — ilu wraca i kiedy. Jeśli 90% klientów kupuje tylko raz i nigdy nie wraca — strategia retencyjna (email marketing, programy lojalnościowe) nie działa lub nie istnieje. Dla e-commerce z wysokimi kosztami pozyskania (CAC), retencja nawet 1 dodatkowego zakupu na klienta podwaja LTV.

**Jak sprawdzić (GA4 Eksploracje):**
- GA4 → Eksploracje → Analiza kohort
- Kohortuj po: data pierwszej sesji (tygodniowo) — metryka: ecommercePurchases lub purchaseRevenue
- Obserwuj: jakie % kohorty wraca w tygodniu 1, 2, 4, 8 po pierwszym zakupie

**Sygnały:**
- Retencja tygień 4 > 15% → silny produkt + marketing retencyjny działa
- Retencja tydzień 4 < 5% → jednorazowi klienci → konieczna strategia CRM/email
- Kohorty z emaila mają 2x wyższą retencję niż kohorty z paid → email jest priorytetem

**Alternatywa przez GA4 API:**
```
# Nowi vs powracający kupujący (30d)
get_ga4_data(
  dimensions=["newVsReturning"],
  metrics=["totalUsers", "ecommercePurchases", "purchaseRevenue"],
  date_from="90daysAgo"
)
→ % transakcji od powracających vs nowych
→ Revenue od powracających / Revenue łącznie
```

**Punktacja (max 2 pkt):**
- Udział transakcji od powracających > 20% (zdrowy mix): 1 pkt
- Zidentyfikowano kanał z najwyższą retencją (baseline dla strategii CRM): 1 pkt

---

### 9.12 — Ścieżki konwersji wielodotykowe
**Priorytet:** Średni *(wymaga GA4 Eksploracje lub BigQuery)*

**Czym jest i dlaczego sprawdzamy:**
Większość zakupów e-commerce poprzedza wiele wizyt z różnych kanałów. Jeśli widzimy tylko last-click — nie widzimy pełnej roli każdego kanału. Typowy przykład: klient znajdzie produkt przez PMax → odejdzie → wróci 3 dni później przez email → kupi. Last-click przypisze 100% wartości do emaila, ignorując PMax. Analiza ścieżek ujawnia realne znaczenie każdego kanału w procesie decyzyjnym.

**Jak sprawdzić:**
- GA4 → Reklamowanie → Ścieżki konwersji (wymaga połączenia z Ads lub bezpośrednio)
- GA4 → Eksploracje → Eksploracja lejka (wielosesyjna)
- Alternatywnie przez BigQuery: analiza sekwencji sesji per user_pseudo_id (patrz sekcja 3K.9)

**Co mierzyć:**
```
# Ścieżki konwersji — kanały (przez GA4 API jeśli dostępne)
get_ga4_data(
  dimensions=["defaultChannelGroup"],
  metrics=["conversions", "purchaseRevenue"],
  date_from="30daysAgo"
)
→ Porównaj z Last-Click vs Data-Driven Attribution w GA4 Admin
→ Duże różnice = kanały wspomagające (assisted) vs domykające (last-click)
```

**Kluczowe wzorce:**
| Wzorzec | Interpretacja | Rekomendacja |
|---------|---------------|--------------|
| SEO → Direct → zakup | SEO inicjuje, brand domyka | Inwestuj w SEO jako kanał inicjujący |
| Paid Social → Email → zakup | Social buduje świadomość, email domyka | Nie oceniaj social po ROAS last-click |
| PMax → Organic → zakup | PMax "kradnie" organic credit | Sprawdź kannibalizację PMax vs organic |
| Direct dominuje | Za dużo direct = problem z atrybucją | Sprawdź missing UTM i cross-domain |

**Punktacja (max 2 pkt):**
- Analiza ścieżek wykonana (GA4 Eksploracje lub BQ): 1 pkt
- Zidentyfikowano ≥ 1 kanał "wspomagający" niedoceniany w last-click: 1 pkt

---

---

### 9.13 — ROAS per kategoria produktów (GA4 + Merchant Center)
**Priorytet:** Wysoki *(tylko e-commerce z feedem)*

**Czym jest i dlaczego sprawdzamy:**
Średni ROAS konta maskuje ogromne różnice między kategoriami produktów. Konto może mieć ROAS 6x dzięki jednej kategorii (np. meble premium), podczas gdy pozostałe 70% asortymentu generuje ROAS 1.5x. Bez tej analizy budżet jest alokowany proporcjonalnie do historycznych wydatków zamiast do rentowności.

**Dane do pobrania:**
```
# ROAS per kategoria (GA4 — wszystkie kanały)
get_ga4_data(
  dimensions=["itemCategory", "sessionDefaultChannelGroup"],
  metrics=["itemRevenue", "itemsPurchased", "addToCarts"],
  date_from="30daysAgo",
  filters={"sessionDefaultChannelGroup": ["Paid Search", "Paid Shopping", "Cross-network"]}
)

# Porównaj z danymi z Merchant Center / Google Ads
# shopping_performance per item_category2 / item_category3 (przez BDOS lub Ads UI)
```

**Tabela ROAS per kategoria:**

| Kategoria | Wydatki Ads | Przychód | ROAS | % budżetu | % przychodu | Quadrant BCG | Działanie |
|-----------|------------|---------|------|-----------|-------------|--------------|-----------|
| | PLN | PLN | x | % | % | | |
| | PLN | PLN | x | % | % | | |

**Interpretacja:**
- Kategoria z ROAS > 8x i < 10% budżetu → niedoinwestowana (przesuń budżet)
- Kategoria z ROAS < 2x i > 25% budżetu → nadmiernie finansowana (ogranicz lub zoptymalizuj feed)
- Kategoria sezonowa (ROAS wysoki 3 msc, niski 9 msc) → zdefiniuj sezonowe budżety

---

### 9.14 — Analiza reklam displayowych i video (Upper Funnel)
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Kampanie Display, Demand Gen i YouTube pełnią rolę świadomościową (Upper Funnel) — nie domykają konwersji last-click ale budują popyt, który domykają inne kanały. Błędem jest ocenianie ich przez ROAS last-click. Poprawna ocena = wpływ na Search volume i assisted conversions.

**Dane i metodologia:**
```
# Sprawdź udział Brand w Google Search po uruchomieniu kampanii Display/YT
get_ga4_data(
  dimensions=["sessionCampaignName", "sessionMedium"],
  metrics=["sessions", "ecommercePurchases", "purchaseRevenue"],
  date_from="60daysAgo",
  filters={"sessionMedium": "cpc"}
)
→ Porównaj sesje branded search przed i po uruchomieniu kampanii Upper Funnel
```

**Metryki oceny Upper Funnel:**

| Kampania | Typ | Wydatki | VCR / CTR | Assisted conv. | Brand search lift | Ocena |
|----------|-----|---------|-----------|---------------|-------------------|-------|
| | Display | PLN | % | | % | |
| | DemGen | PLN | % | | % | |
| | YouTube | PLN | % | | % | |

**Progi:**
- VCR (View-through Rate) YouTube > 25% = dobra kreacja
- Brand Search Lift > 10% w 30d po uruchomieniu = kampania Upper Funnel działa
- CTR Display > 0.1% = akceptowalny dla branży
- Kampania YT z 0 assisted conversions i < 0.2% CTR → kandydat do wstrzymania

---

## Łączna punktacja sekcji 9

| Podsekcja | Max pkt |
|-----------|---------|
| 9.1 Efektywność kanałów | 4 |
| 9.2 Urządzenia | 2 |
| 9.3 Trend | 2 |
| 9.4 AOV | 2 |
| 9.5 Lejek behawioralny | 2 |
| 9.6 Omnichannel | 2 |
| 9.7 Geografia | 2 |
| 9.8 Quick wins | 2 |
| 9.9 Retencja / LTV per kanał | 2 |
| 9.10 Wyszukiwania wewnętrzne | 2 |
| 9.11 Analiza kohortowa | 2 |
| 9.12 Ścieżki wielodotykowe | 2 |
| 9.13 ROAS per kategoria | 3 |
| 9.14 Upper Funnel (Display/Video) | 2 |
| **ŁĄCZNIE** | **31** |

---

# SEKCJA 10 — Audyt Google Ads

> **Cel:** Weryfikacja poprawności konfiguracji i efektywności kampanii Google Ads powiązanych z audytowaną stroną. Sekcja ta wypełnia lukę między danymi GA4 a faktycznym stanem konta reklamowego — GA4 mówi nam co dzieje się na stronie, Google Ads mówi nam za ile i z jakiej jakości ruchu. Razem dają pełny obraz.
>
> **Warunek wejścia:** Dostęp do konta Google Ads (przez BDOS API lub ręcznie w interfejsie). Jeśli brak dostępu → zaznacz jako 🔒 Brak dostępu i pomiń.
>
> **Dane wejściowe:** Jeśli używasz BDOS — uruchom `bdos report --account {account_id}` lub użyj danych z raportu MCC. Jeśli ręcznie — korzystaj z Google Ads UI, zakres dat: ostatnie 30 dni + poprzednie 30 dni (porównanie trendu).
>
> **Zasada BDOS w tej sekcji:** Każde konto, kampania lub błąd musi być opisany z konkretnymi liczbami. "Niski ROAS" bez wartości to nie jest audyt.

---

## KROK: Dane do pobrania przed audytem Ads

Przed wypełnieniem sekcji pobierz następujące dane:

```
# Przez BDOS API lub ręcznie z Google Ads UI (zakres: ostatnie 30 dni):

1. Metryki konta zbiorcze:
   Wydatki | Kliknięcia | Wyświetlenia | CTR | Avg CPC | Konwersje
   Wartość konwersji | ROAS | CPA | Avg QS | Kampanii aktywnych

2. Podział na typy kampanii:
   Performance Max | Search | Shopping | Display | Demand Gen | Video | Smart
   → Per typ: wydatki, konwersje, ROAS, liczba kampanii aktywnych

3. Per kampania (wszystkie aktywne):
   Nazwa | Typ | Wydatki | Kliknięcia | Konwersje | Wartość konwersji
   ROAS% | Budżet/dzień | Strategia biddingowa | Avg QS

4. Quality Score (Search):
   Rozkład QS 1–10 | Kampanie z avg QS < 5
   Przyczyny: Expected CTR / Ad Relevance / Landing Page Experience

5. Kampanie bez konwersji:
   Kampanie z wydatkami > 300 PLN/msc i 0 konwersji
   → Szacowany miesięczny koszt drenażu

6. Impression Share:
   IS total | IS utracony (budżet) | IS utracony (ranking) per kampania

7. Feed / Merchant Center (e-commerce):
   Łączna liczba produktów | Zatwierdzone | Odrzucone | Błędy | % z GTIN
```

---

## 10A — Przegląd konta: metryki zbiorcze (30 dni)

### 10.1 — Podstawowe KPI konta
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Przegląd zbiorczy to "temperatura" konta reklamowego. ROAS (Return on Ad Spend) to najważniejszy wskaźnik efektywności — pokazuje ile złotych wraca z każdej wydanej złotówki. ROAS < 100% oznacza stratę na każdej transakcji. CPA (Cost per Acquisition) mówi ile kosztuje pozyskanie jednej konwersji. Quality Score (QS) mierzy jakość reklam — niski QS = droższe kliknięcia, gorsze pozycje, wyższy CPA.

**Benchmarki e-commerce PL:**
- ROAS > 300% = dobry wynik (na każdą złotówkę wracają 3 zł)
- ROAS 150–300% = do optymalizacji
- ROAS < 150% = konto generuje straty przy typowej marży e-commerce
- CPA nie powinien przekraczać 30% AOV
- Avg QS > 7 = dobra relevance; QS 4–6 = do poprawy; QS < 4 = krytyczne

| Metryka | Wartość (30d) | Poprzednie 30d | Trend | Ocena |
|---------|---------------|----------------|-------|-------|
| Wydatki łączne (PLN) | | | ↑/→/↓ | |
| Kliknięcia | | | | |
| Wyświetlenia | | | | |
| CTR (%) | | | | |
| Avg CPC (PLN) | | | | |
| Konwersje łączne | | | | |
| Wartość konwersji (PLN) | | | | |
| ROAS (%) | | | | < 150% ❌ / 150–300% ⚠️ / > 300% ✅ |
| CPA (PLN) | | | | |
| Avg Quality Score | | | | < 5 ❌ / 5–7 ⚠️ / > 7 ✅ |
| Kampanie aktywne | | | | |
| Kampanie bez konwersji | | | | |

**Ocena ogólna konta:** ✅ Dobry / ⚠️ Do optymalizacji / ❌ Krytyczny

---

### 10.2 — Udział w wyświetleniach (Impression Share)
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Impression Share (IS) to procent wyświetleń które kampania faktycznie otrzymała vs wszystkie dostępne wyświetlenia na rynku. IS = 60% oznacza, że 40% potencjalnego ruchu trafia do konkurencji. Niski IS może wynikać z ograniczonego budżetu (IS lost to budget) lub niskiego rankingu (IS lost to rank — zbyt niska stawka lub QS). Przy dobrej rentowności konta i niskim IS — budżet jest ogranicznikiem wzrostu, a zwiększenie go bezpośrednio przekłada się na więcej transakcji.

**Jak sprawdzić:** Google Ads → Kampanie → Kolumny → dodaj: "Udział w wyświetleniach", "IS utracony (budżet)", "IS utracony (ranking)".

| Kampania / Typ | IS (%) | IS utracony budżet (%) | IS utracony ranking (%) | Interpretacja |
|----------------|--------|----------------------|------------------------|---------------|
| | | | | |
| | | | | |
| **Łącznie konto** | | | | |

**Czerwona flaga:** IS utracony (budżet) > 30% przy ROAS > 300% → konto ograniczone budżetem. Potencjał wzrostu istnieje — wymaga zwiększenia finansowania.

---

## 10B — Analiza struktury kampanii

### 10.3 — Mapa kampanii: typy i podział budżetu
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Struktura kampanii powinna odzwierciedlać strategię marketingową. Typowy błąd: wszystkie środki w jednej kampanii PMax "ALL" bez segmentacji — Google decyduje gdzie je wydać i często wybiera najłatwiejszy ruch (branded, remarketing) zamiast nowych klientów (prospecting). Sprawdzamy czy typy kampanii są dobrane do celów i czy budżety są alokowane zgodnie z performance.

**Rozkład typów kampanii:**

| Typ kampanii | Kampanii aktywnych | Wydatki (PLN) | % budżetu | Konwersje | ROAS% | Ocena |
|-------------|-------------------|---------------|-----------|-----------|-------|-------|
| Performance Max | | | | | | |
| Search | | | | | | |
| Shopping (Standard) | | | | | | |
| Display | | | | | | |
| Demand Gen | | | | | | |
| Video | | | | | | |
| Smart (legacy) | | | | | | |

**Sygnały alarmu:**
- > 80% budżetu w jednej kampanii PMax "ALL" bez segmentacji → brak kontroli nad alokacją → podziel na minimum "nowi" i "powracający"
- Brak kampanii brandowej (Search na własną markę) → własny brand sprzedawany konkurencji za ich stawkę
- Kampanie Video/Display > 15% budżetu bez mierzalnego ROAS → świadomościowe bez kontrtroli efektywności

---

### 10.4 — Kampanie Performance Max — głęboka analiza
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Performance Max (PMax) łączy wszystkie sieci Google (Search, Shopping, Display, YouTube, Gmail, Maps) w jednej strukturze. Jest potężny, ale bez odpowiedniej konfiguracji "kanibalizuje" inne kampanie i wydaje budżet na tani ruch branded lub remarketingowy zamiast nowych klientów. Kluczowe: segmentacja na Grupy Zasobów, Audience Signals, kontrola Final URL expansion i separacja feed-only vs zasoby.

**Per kampania PMax:**

| Kampania PMax | Wydatki | ROAS% | Gr. zasobów | Audience Signals | Feed-only? | URL expansion | Ocena |
|---------------|---------|-------|-------------|-----------------|------------|--------------|-------|
| | | | | tak/nie | tak/nie | wł/wył | |
| | | | | | | | |

**Kluczowe pytania dla wszystkich kampanii PMax:**

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Ile grup zasobów na kampanię? (min. 2, optymalnie 3+ per segment) | | |
| Audience Signals ustawione (remarketing + Customer Match + custom intent)? | | |
| Final URL expansion — czy wyłączone dla kontroli LP? | | |
| Wykluczenia brand w PMax (własna marka nie kanibalizuje branded Search)? | | |
| Oddzielna kampania PMax feed-only vs z zasobami kreatywnymi? | | |
| Segmentacja BCG: Gwiazdy w osobnej kampanii/grupie zasobów? | | |
| Weryfikacja kanibalizacji: PMax vs organic w Search Terms? | | |

**Grupy zasobów — kompletność zasobów kreatywnych:**

| Zasób | Wymagane | Optymalnie | Status | Uwagi |
|-------|----------|------------|--------|-------|
| Nagłówki (Headlines) | 3 | 5 | | |
| Długie nagłówki | 1 | 5 | | |
| Opisy | 2 | 5 | | |
| Obrazy poziome (1.91:1) | 1 | 5 | | |
| Obrazy kwadratowe (1:1) | 1 | 5 | | |
| Logo | 1 | — | | |
| Video YouTube | opcjonalne | 1 | | |
| Końcowy URL | 1 | — | | |
| Sygnał odbiorców (Audience Signals) | opcjonalne | ✅ TAK | | |

---

### 10.5 — Kampanie Search — jakość i struktura
**Priorytet:** Wysoki *(sprawdzaj tylko jeśli kampanie Search aktywne)*

**Czym jest i dlaczego sprawdzamy:**
Kampanie Search są fundamentem dla fraz brandowych i produktów o wysokiej intencji zakupowej. Ich jakość mierzy się przez Quality Score (1–10) — im wyższy, tym niższy CPC i lepsze pozycje. Kluczowa jest tight thematic grouping: każda grupa reklam powinna zawierać słowa kluczowe na jeden temat, a reklama powinna bezpośrednio odwoływać się do tych słów. Sprawdzamy strukturę kont, typy dopasowania, Ad Strength i extensions.

**Struktura kampanii Search:**

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Reklamy RSA (Responsive Search Ads) — każda aktywna grupa ma RSA? | | |
| Ad Strength kampanii > "Dobra" (Good/Excellent) | | |
| Typy dopasowania — czy jest Exact match i Phrase (nie tylko Broad)? | | |
| Grupy reklam mają ≤ 20 słów kluczowych (tight ad groups)? | | |
| Assets/Extensions: sitelinks (min. 4), callouts (min. 4), structured snippets | | |
| Asset: Image extensions (obrazy) | | |
| Asset: Promotion extension (jeśli promocja) | | |
| Kampania brandowa istnieje i oddzielna od generycznych? | | |
| Negatywna lista słów kluczowych aktywna? | | |

---

### 10.6 — Kampanie Shopping Standard
**Priorytet:** Wysoki *(e-commerce z feedem, jeśli Shopping aktywne)*

**Czym jest i dlaczego sprawdzamy:**
Standard Shopping daje pełną kontrolę nad strukturą produktową — można dokładnie licytować per kategoria, marka lub produkt. Często lepiej sprawdza się dla stabilnych bestsellerów (Dojne Krowy BCG) gdzie nie potrzebujemy eksperymentowania PMax. Bez precyzyjnych podziałów Google sam decyduje co pokazywać i często wybiera produkty z najwyższą ceną niezależnie od marżowości.

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Podział produktów w grupach (nie tylko "Wszystkie produkty") | | |
| Custom Labels — używane (BCG segment, marża, bestseller)? | | |
| Priorytet kampanii ustawiony (gdy obok PMax Shopping — Shopping powinien mieć Niski) | | |
| Negatywy brandowe jeśli PMax i Shopping działają równolegle | | |
| ROAS Target ustawiony (nie Maximize Clicks dla konta z historią) | | |

---

## 10C — Bidding i budżety

### 10.7 — Strategie biddingowe — poprawność i adekwatność
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Strategia biddingowa to instrukcja dla algorytmu Google jak licytować. Zła strategia = przepalony budżet lub zbyt ostrożne biddowanie. Kluczowe błędy:
- `Maximize Clicks` w kampanii e-commerce → Google kupuje najtańsze kliknięcia, niekoniecznie od osób które kupią
- `Maximize Conversions` bez Target CPA dla dojrzałego konta → Google może przebidować i podwoić CPA
- `Target Impression Share` dla kampanii produktowej → priorytet widoczności zamiast konwersji
- `Target ROAS` przy < 30 konwersji/30d → algorytm działa na ślepo bez danych do uczenia

**Weryfikacja per kampania:**

| Kampania | Typ | Aktualna strategia | Właściwa? | Konwersje/30d | Uwagi |
|----------|-----|-------------------|-----------|---------------|-------|
| | | | tak/nie | | |
| | | | | | |

**Matryca: Strategia vs Faza konta:**

| Faza kampanii | Rekomendowana strategia | Dlaczego |
|--------------|------------------------|----------|
| Nowa kampania (< 30 konwersji/30d) | Maximize Conversions (bez target) | Zbiera dane do algorytmu |
| Dojrzała kampania e-commerce (> 50 konw./30d) | Maximize Conv. Value / Target ROAS | Optymalizacja wartości |
| Kampania brandowa | Maximize Conv. Value lub Target Impression Share | Broń własnej marki |
| Kampania zasięgowa (Display, DG) | Maximize Conversions lub CPM | Cel: zasięg, nie konwersje |
| Lead gen (formularze) | Target CPA | Optymalizacja kosztu leada |

**Czerwone flagi:**
- `Maximize Clicks` w kampanii e-commerce z historią → zmień na `Maximize Conv. Value`
- `Target ROAS` przy < 30 konwersji/30d → ogranicz target lub zmień na `Max Conv. Value`
- `Target Impression Share` w kampaniach nie-brandowych → ≠ strategia konwersyjna
- Wszystkie kampanie na `Maximize Conversions` bez targetów → brak "sufitu" kosztowego

---

### 10.8 — Kampanie bez konwersji — identyfikacja i koszt drenażu
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Kampanie aktywne z wydatkami ale zerowymi konwersjami to "drenaż budżetu" — pieniądze wydane bez mierzalnego efektu. Mogą oznaczać: błąd w śledzeniu konwersji, złe targetowanie, odrzucone reklamy, zbyt restrykcyjne ustawienia odbiorców lub kampanię która po prostu nie działa dla tego rynku. Standard BDOS: każda kampania z > 300 PLN/msc i 0 konwersji wymaga działania w ciągu 7 dni.

**Jak zidentyfikować:** Google Ads → Kampanie → Kolumny → dodaj "Konwersje" → sortuj rosnąco.

| Kampania | Typ | Wydatki (30d) | Kliknięcia | Konwersje | Szacowany koszt drenażu/msc | Diagnoza |
|----------|-----|---------------|-----------|-----------|---------------------------|---------|
| | | PLN | | 0 | | |
| | | | | 0 | | |
| **ŁĄCZNIE drenażu** | | **PLN** | | | | |

**Diagnoza dla każdej kampanii bez konwersji — checklist:**

| Pytanie diagnostyczne | Wynik |
|----------------------|-------|
| Śledzenie konwersji działa na tej stronie? (DebugView GA4) | |
| Reklamy są zatwierdzone i wyświetlają się (status: Eligible)? | |
| Landing page jest relevantny do słów/audience? | |
| Targetowanie nie jest zbyt wąskie (< 1000 osób na liście)? | |
| Kampania ma wystarczający budżet dzienny (≥ 3× docelowy CPA)? | |

---

### 10.9 — Ograniczenia budżetowe i alokacja
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Kampania "ograniczona budżetem" to kampania, która by wydała więcej gdyby miała środki — i wg Google przyniosłaby więcej konwersji. Priorytetem jest: zwiększenie budżetu kampaniom z dobrym ROAS, zmniejszenie lub wstrzymanie kampaniom z ROAS poniżej progu opłacalności. Sprawdzamy czy alokacja jest zgodna z performance.

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Kampanie z IS utracony (budżet) > 30% i ROAS > 300% → niedofinansowane rentowne kampanie? | | |
| Kampanie z IS utracony (budżet) > 30% i ROAS < 150% → nadmiernie finansowane nierentowne? | | |
| Wspólne budżety (shared budgets) — poprawnie skonfigurowane? | | |
| Sezonowe dostosowania budżetu (seasonality adjustments) używane? | | |
| Portfolio bid strategies dla grup kampanii z podobnymi celami? | | |

---

## 10D — Quality Score i relevance

### 10.10 — Analiza Quality Score — szczegółowa
**Priorytet:** Wysoki *(tylko kampanie Search)*

**Czym jest i dlaczego sprawdzamy:**
Quality Score (1–10) to ocena Google jakości i relevance reklam. Ma bezpośredni wpływ na koszt kliknięcia — QS 10 może być nawet 50% tańsze vs QS 5 dla tej samej pozycji. QS składa się z trzech komponentów: Expected CTR (jak często klikają taką reklamę), Ad Relevance (jak reklama pasuje do słowa kluczowego), Landing Page Experience (jak dobra i relevantna jest strona docelowa).

**Rozkład QS konta:**

| Zakres QS | Liczba słów kluczowych | % całości | Szacowany nadkoszt vs QS 8 |
|-----------|----------------------|-----------|---------------------------|
| QS 9–10 | | | oszczędność ~20% |
| QS 7–8 | | | bazowy |
| QS 5–6 | | | +20–40% CPC |
| QS 3–4 | | | +50–80% CPC |
| QS 1–2 | | | +100–200% CPC |

**Analiza komponentów:**

| Komponent | Status konta | Najczęstsza przyczyna | Akcja naprawcza |
|-----------|-------------|----------------------|-----------------|
| Expected CTR — poniżej przeciętnej | | | |
| Ad Relevance — poniżej przeciętnej | | | |
| Landing Page Exp. — poniżej przeciętnej | | | |

**Kampanie z Avg QS < 5 — szczegóły:**

| Kampania | Avg QS | Najsłabszy komponent | Szacowany CPC naddatek/msc | Propozycja naprawy |
|----------|--------|---------------------|--------------------------|-------------------|
| | | | PLN | |

---

### 10.11 — Search Terms Report — analiza zapytań
**Priorytet:** Wysoki *(Search i PMax z zasobami tekstowymi)*

**Czym jest i dlaczego sprawdzamy:**
Search Terms Report pokazuje realne zapytania użytkowników które wyzwoliły reklamy. Bez regularnej analizy każda kampania Broad Match wydaje pieniądze na ruch o zerowej intencji zakupowej. Ujawnia też: słowa przynoszące konwersje (do dodania jako Exact match), frazy niekomercyjne (do negatywów) i kanibalizację PMax/Search.

**Jak sprawdzić:** Google Ads → Słowa kluczowe → Wyszukiwane hasła (last 30d).

| Kategoria zapytań | Liczba unikalnych | % wydatków | Konwersje | Rekomendacja |
|------------------|------------------|-----------|-----------|--------------|
| Branded (własna marka) | | | | Wyodrębnij do kampanii brandowej |
| Competitor (marka konkurencji) | | | | Decyzja: atakować czy wykluczyć |
| Informacyjne (jak, co to, poradnik) | | | | Wyklucz (brak intencji zakupowej) |
| Produktowe (konkretny SKU/model) | | | | Dodaj jako Exact match |
| Kategoriowe (np. "buty sportowe") | | | | Utrzymaj, monitoruj CVR |
| Bez sensu / spam | | | | Wyklucz natychmiast |

**Top 10 fraz do dodania jako negatywy:**
1. ___
2. ___
3. ___

---

## 10E — Feed produktowy i Merchant Center

### 10.12 — Health check feedu produktowego
**Priorytet:** Wysoki *(e-commerce z Shopping / PMax z feedem)*

**Czym jest i dlaczego sprawdzamy:**
Feed produktowy to rdzeń kampanii Shopping i Performance Max. Produkt z odrzuconym feedem = 0 wyświetleń = 0 sprzedaży. Jakość feedu (tytuły, opisy, zdjęcia, atrybuty takie jak GTIN) bezpośrednio wpływa na CTR kampanii Shopping i na to czy Google potrafi dopasować produkt do zapytań użytkowników. Tytuł produktu to odpowiednik słowa kluczowego w kampanii Search — musi zawierać słowa kluczowe klienta.

**Jak sprawdzić:** Google Merchant Center → Produkty → Diagnostyka.

| Metryka | Wartość | Benchmark | Ocena |
|---------|---------|-----------|-------|
| Łączna liczba produktów w feedzie | | | |
| Produkty zatwierdzone (active) | | > 95% ✅ | |
| Produkty odrzucone (disapproved) | | < 2% ✅ | |
| Produkty oczekujące / pending | | | |
| Produkty z GTIN/EAN wypełnionym | | > 80% ✅ | |
| Produkty z polem `brand` | | > 90% ✅ | |
| Produkty z `condition` (new/used/refurbished) | | 100% ✅ | |
| Średnia długość tytułu (znaki) | | 70–150 znaków ✅ | |
| Obrazy: min 800×800px, bez watermarków | | 100% ✅ | |

**Najczęstsze błędy feedu:**

| Błąd | Liczba produktów | Wpływ | Priorytet |
|------|-----------------|-------|-----------|
| Brakujący GTIN (EAN/UPC) | | Brak dopasowania do branded searches | Wysoki |
| Cena niezgodna ze stroną (price mismatch) | | Odrzucenie przez GMC | Krytyczny |
| Brakujące lub niezgodne zdjęcie | | Odrzucenie | Krytyczny |
| Zbyt krótkie tytuły (< 40 znaków) | | Niski CTR, słabe dopasowanie | Średni |
| Brak `google_product_category` | | Gorsze dopasowanie do zapytań | Średni |
| Brakujący atrybut `brand` | | Gorsze QS | Wysoki |

---

### 10.13 — Custom Labels i segmentacja BCG w feedzie
**Priorytet:** Średni *(e-commerce z feedem produktowym)*

**Czym jest i dlaczego sprawdzamy:**
Custom Labels (pola 0–4 w feedzie) to pola własne do segmentacji produktów w kampaniach Shopping/PMax. Umożliwiają stworzenie osobnych kampanii lub grup zasobów dla: bestsellerów, produktów z wysoką marżą, gwiazd BCG, nowych produktów, produktów sezonowych. Bez Custom Labels wszystkie produkty trafiają do jednego "wiadra" — Google sam decyduje na co wydaje budżet. Efekt: budżet idzie na produkty z najwyższą ceną, nie na najmarżowsze.

| Custom Label | Co powinno zawierać | Status | Przykładowe wartości w feedzie |
|-------------|---------------------|--------|-------------------------------|
| custom_label_0 | Segment BCG (star/cash_cow/question/dog/inactive) | | |
| custom_label_1 | Marżowość (high/medium/low) | | |
| custom_label_2 | Bestseller (yes/no) | | |
| custom_label_3 | Sezonowość (summer/winter/year_round) | | |
| custom_label_4 | Nowość (new_30d/new_90d/established) | | |

---

## 10F — Konwersje Google Ads

### 10.14 — Konfiguracja konwersji — kompletna weryfikacja
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Konwersje to "cel" dla algorytmu Google Ads. Błędna konfiguracja = algorytm optymalizuje pod złe zdarzenia lub złe wartości, wydając pieniądze na coraz gorszy ruch. Najczęstsze błędy w klientach BDOS: konwersja purchase z wartością 1 PLN (domyślna), duplikat konwersji (tag Ads + import GA4 liczą to samo dwa razy), mikrokonwersja (scroll) jako Primary zamiast zakup.

**Weryfikacja każdej konwersji:**

| Konwersja | Źródło | Typ zdarzenia | Wartość | Primary? | Okno klik. | Okno wyśw. | Błędy | Ocena |
|-----------|--------|--------------|---------|---------|-----------|-----------|-------|-------|
| | Ads tag / GA4 import | Zakup / Lead / Inna | Dynamiczna / Stała / 0 PLN | Tak/Nie | | | | |
| | | | | | | | | |

**Matryca błędów konwersji:**

| Błąd | Konsekwencja | Priorytet |
|------|-------------|-----------|
| Konwersja `purchase` z wartością = 1 PLN (stała domyślna) | ROAS fałszywy — zawsze 0.0x | 🔴 Krytyczny |
| Duplikat: Ads tag + GA4 import tej samej akcji | Konwersje liczone 2x → ROAS zawyżony o 100% | 🔴 Krytyczny |
| Mikrokonwersja (scroll, klik w tel.) jako Primary | Algorytm optymalizuje pod microeventy, nie zakupy | 🔴 Krytyczny |
| Brak konwersji z wartością przy kampanii Target ROAS | Target ROAS nie może działać bez wartości | 🟡 Wysoki |
| Wartość konwersji = 0 PLN (lead gen bez wartości leada) | Algorytm nie może wyceniać leadów | 🟡 Wysoki |
| Okno konwersji < 7 dni przy długim cyklu zakupowym | Konwersje "znikają" — algorytm niedouczony | 🟡 Wysoki |
| Konwersja z kategorią "Inna" zamiast "Zakup" | Smart bidding gorzej interpretuje sygnały | 🟢 Niski |

---

### 10.15 — Enhanced Conversions — wdrożenie i jakość matchingu
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Enhanced Conversions poprawiają dokładność pomiaru poprzez hashowanie danych pierwszej strony (email, telefon) i porównywanie z kontami Google użytkowników. Bez EC w erze iOS 14+ i ITP tracisz 15–30% danych konwersyjnych — algorytm smart bidding "widzi" mniej konwersji i biduje zachowawczo, co pogarsza ROAS.

**Jak sprawdzić:**
- Google Ads → Cele → Konwersje → kliknij konwersję → zakładka "Enhanced Conversions"
- Google Ads → Cele → Diagnostyka konwersji → kolumna "Enhanced conversions match rate"

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Enhanced Conversions włączone dla konwersji purchase | | |
| EC skonfigurowane w GTM (pola: email, phone_number) | | |
| EC match rate > 40% | | < 20% ❌ / 20–40% ⚠️ / > 40% ✅ |
| Dane hashowane SHA-256 (nie czytelny tekst) | | |
| EC działa na stronie potwierdzenia zamówienia | | |

---

## 10G — Audience i sygnały

### 10.16 — Customer Match — konfiguracja i jakość
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Customer Match pozwala targetować reklamy do własnej bazy klientów (emaile, telefony) i jest najcenniejszym Audience Signal dla PMax — Google używa listy aby znaleźć podobnych (lookalike). Wymaga: > 1000 dopasowanych emaili (minimum dla działania), regularnej aktualizacji i zgodności z RODO (klienci musieli wyrazić zgodę na remarketing).

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Lista Customer Match załadowana w Google Ads? | | |
| Rozmiar listy > 1000 dopasowanych użytkowników? | | |
| Lista aktualizowana w ciągu ostatnich 90 dni? | | |
| Lista używana jako Audience Signal w kampaniach PMax? | | |
| Lista używana w RLSA dla kampanii Search? | | |
| Klienci wyrazili zgodę RODO na remarketing marketingowy? | | |
| Match rate > 20% (dopasowani / przesłanych rekordów)? | | |

---

### 10.17 — Remarketing i RLSA — listy i użycie
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
RLSA (Remarketing Lists for Search Ads) pozwala modyfikować stawki w kampaniach Search dla użytkowników z określoną historią — np. podwój stawkę dla osób które porzuciły koszyk (najwyższa intencja powrotu). Display remarketing dociera do użytkownika banerem podczas przeglądania innych stron. Obydwa wymagają list z GA4 lub Google Ads pixel i minimalnych rozmiarów list (1000 dla Search, 100 dla Display).

| Lista | Rozmiar (Ads) | Używana w Search (RLSA) | Używana w Display | Modyfikator stawki | Ocena |
|-------|--------------|------------------------|------------------|-------------------|-------|
| Wszyscy odwiedzający (30d) | | | | | |
| Porzucający koszyk (add_to_cart bez purchase) | | | | | |
| Oglądający produkt bez zakupu | | | | | |
| Kupujący (30d) — up/cross sell | | | | | |
| Kupujący (180d) — retention | | | | | |

---

## 10H — Ocena zbiorcza konta

### 10.18 — Tabela ocen per typ kampanii
**Priorytet:** —

| Typ kampanii | ROAS% | Trend | Struktura /5 | QS /5 | Błędy kryt. | Ocena |
|-------------|-------|-------|-------------|-------|-------------|-------|
| Performance Max | | ↑/→/↓ | | — | | |
| Search | | | | | | |
| Shopping | | | | — | | |
| Display | | | — | — | | |
| Demand Gen | | | — | — | | |
| Video | | | — | — | | |

---

### 10.19 — Ocena specjalisty prowadzącego konto
**Priorytet:** —

**Czym jest i dlaczego sprawdzamy:**
Ocena holistyczna pracy specjalisty SEM — nie konta, ale człowieka który je prowadzi. Bierze pod uwagę: trend ROAS (rośnie czy spada), porządek w strukturze (nazewnictwo, segmentacja), aktywność optymalizacyjna (czy są regularne zmiany, testy A/B, aktualizacje feedu), jakość wykluczeń i użycie zaawansowanych funkcji. Standard BDOS: każde konto z ROAS < 150% i brakiem działań w ciągu 30 dni = krytyczna ocena specjalisty.

| Obszar | Ocena /5 | Komentarz |
|--------|---------|-----------|
| Trend ROAS (ostatnie 3 miesiące) | | ↑ rośnie / → stabilny / ↓ spada |
| Struktura kampanii (nazewnictwo, segmentacja) | | |
| Aktywność optymalizacyjna (ostatnie 30 dni) | | |
| Jakość wykluczeń i negatywów | | |
| Użycie zaawansowanych funkcji (EC, CM, CL, IS) | | |
| Reakcja na kampanie bez konwersji | | |

**Łączna ocena specjalisty:** ⭐⭐⭐⭐⭐ (___/5)

**Narracja:** _______________

---

### 10.20 — Łączna punktacja sekcji 10

| Podsekcja | Max pkt |
|-----------|---------|
| 10.1 KPI konta | 3 |
| 10.2 Impression Share | 2 |
| 10.3 Mapa kampanii | 2 |
| 10.4 Performance Max | 5 |
| 10.5 Search | 5 |
| 10.6 Shopping | 3 |
| 10.7 Bidding strategies | 4 |
| 10.8 Kampanie bez konwersji | 3 |
| 10.9 Budżety | 2 |
| 10.10 Quality Score | 3 |
| 10.11 Search Terms | 3 |
| 10.12 Feed / Merchant Center | 4 |
| 10.13 Custom Labels | 2 |
| 10.14 Konwersje Ads | 5 |
| 10.15 Enhanced Conversions | 3 |
| 10.16 Customer Match | 3 |
| 10.17 RLSA / Remarketing | 2 |
| **ŁĄCZNIE** | **54** |
| *10.21–10.28 PMax Zaawansowany (opcja)* | *+19* |

**Wynik sekcji 10:** ___/54 (+ ___/19 PMax Zaawansowany) = ___/73 (___%)

---

## 10I — Performance Max — Zaawansowany audyt

> Wypełniaj tylko gdy konto ma aktywne kampanie PMax. PMax to "czarna skrzynka" — wymaga osobnej, głębokiej diagnostyki, której nie obejmuje standardowe 10.4.

---

### 10.21 — Asset Groups — jakość i pokrycie kreacji
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Asset Group to jednostka kreatywna w PMax. Każda Asset Group powinna być tematycznie spójna (np. jedna kategoria produktów lub jeden segment odbiorców). Google ocenia każde zasoby (teksty, obrazy, wideo) i wyświetla "Ad Strength" od Słabej do Doskonałej. Asset Groups z oceną "Słaba" lub "Dobra" marnują budżet bo Google nie ma z czego budować reklam.

**Jak sprawdzić:** Google Ads → kampania PMax → Asset Groups → kolumny: Ad Strength, Wyświetlenia, Konwersje, Koszt

| Asset Group | Ad Strength | Teksty (nagłówki/opisy) | Obrazy (krajobraz/kwadrat/logo) | Wideo | Konwersje | Koszt | Działanie |
|-------------|------------|------------------------|--------------------------------|-------|-----------|-------|-----------|
| AG 1 — nazwa | Doskonała/Dobra/Słaba | 15/4 | 4/3/1 | tak/nie | | | |
| AG 2 — nazwa | | / | // | | | | |

**Reguły oceny:**
- Ad Strength "Słaba" lub brak wideo → ❌ (Google nie może w pełni optymalizować)
- < 5 nagłówków lub < 2 opisy → ⚠️ uzupełnij do maksimum (15 nagłówków, 4 opisy)
- Brak obrazów krajobrazowych (1.91:1) → ⚠️
- Brak wideo → Google generuje automatyczne (niskiej jakości) → ❌ dodaj własne

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Każda Asset Group ma Ad Strength ≥ "Dobra" | | ✅/⚠️/❌ |
| Każda AG ma ≥ 10 nagłówków (max 15) | | |
| Każda AG ma ≥ 3 opisy (max 4) | | |
| Obrazy: min. 3 krajobrazowe + 3 kwadratowe + 1 logo | | |
| Wideo: własne (nie auto-generowane przez Google) | | |
| Asset Groups tematycznie spójne (nie "wszystko w jednej") | | |

---

### 10.22 — Listing Groups / Product Groups
**Priorytet:** Wysoki (tylko konta e-commerce z feedem)

**Czym jest i dlaczego sprawdzamy:**
Listing Groups w PMax określają które produkty z feedu może wyświetlać dana Asset Group. Domyślnie PMax wyświetla WSZYSTKIE produkty — bez segmentacji oznacza to, że budżet trafia do produktów o najwyższym ROAS i "Psy" BCG konkurują z "Gwiazdami" bez żadnej kontroli. Właściwa segmentacja Listing Groups to fundamentalna różnica między wydatnym PMax a efektywnym PMax.

**Jak sprawdzić:** Google Ads → kampania PMax → Asset Group → Listing Groups

| Asset Group | Segmentacja Listing Groups | Liczba grup | Wykluczone produkty | Ocena |
|-------------|--------------------------|-------------|---------------------|-------|
| AG 1 | Brak / Kategoria / Marka / Custom Label | | | |
| AG 2 | | | | |

**Reguły oceny:**
- "Wszystkie produkty" bez segmentacji → ❌ fundamentalny błąd
- Brak wykluczenia produktów z ROAS < 0.5x → ⚠️
- Brak Custom Label BCG jako Listing Group filter → ⚠️

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Listing Groups podzielone (nie "All products" w jednej AG) | | |
| Custom Labels BCG użyte jako filtry Listing Groups | | |
| Produkty "Psy" wykluczone lub w osobnej AG z niskim budżetem | | |
| Produkty out-of-stock wykluczone z feedu / Listing Groups | | |

---

### 10.23 — Audience Signals — konfiguracja i jakość
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
Audience Signals to "wskazówki" dla algorytmu PMax — nie targetowanie, ale sugestia kto prawdopodobnie kupi. Im lepsze sygnały, tym szybciej PMax uczy się i tym lepszy ROAS w pierwszych tygodniach kampanii. Najcenniejszy sygnał: Customer Match (własna baza klientów). Drugi: Custom Segments (słowa kluczowe które wyszukują kupujący).

**Jak sprawdzić:** Google Ads → kampania PMax → Asset Group → Audience signals

| Typ sygnału | Skonfigurowany | Szczegóły | Ocena |
|-------------|---------------|-----------|-------|
| Customer Match (własna baza emaili) | tak/nie | rozmiar: ___ | |
| Niestandardowe segmenty (słowa kluczowe intencji zakupowej) | tak/nie | liczba segmentów: ___ | |
| Remarketing GA4 (odwiedzający, porzucający koszyk) | tak/nie | listy: ___ | |
| Zainteresowania / In-market audiences | tak/nie | kategorie: ___ | |
| Podobni odbiorcy (Similar Audiences) | tak/nie | | |

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Customer Match załadowany i aktualny (< 90 dni) | | |
| Niestandardowe segmenty z intencją zakupową (nie ogólne) | | |
| Remarketing GA4 podłączony jako sygnał | | |
| Każda Asset Group ma własne, tematyczne sygnały | | |

---

### 10.24 — Kanibalizacja PMax vs Search/Shopping
**Priorytet:** Wysoki

**Czym jest i dlaczego sprawdzamy:**
PMax ma najwyższy priorytet w aukcji Google Ads — wygrywa z kampaniami Search i Shopping gdy targetuje te same zapytania. W praktyce PMax często "kradnie" konwersje marki (branded queries) i kliki z dobrze zoptymalizowanych kampanii Search, zawyżając ROAS PMax kosztem innych kampanii. To najczęstszy ukryty problem w kontach z mieszanymi typami kampanii.

**Jak sprawdzić:** Google Ads → Sekcja Search Terms → porównaj PMax vs Search; Auction Insights; Campaign-level segment "Conversion source"

| Sprawdzenie | Wynik | Ocena |
|-------------|-------|-------|
| PMax przechwytuje branded queries (nazwa marki/domeny)? | tak/nie | |
| Kampania brandowa Search ma niższy Impression Share YoY? | tak/nie | |
| Search Terms PMax zawiera ogólne/drogie frazy bez konwersji? | tak/nie | |
| Auction Insights: nakładanie się PMax z własnymi kampaniami? | tak/nie | |

**Rozwiązanie kanibalizacji branded:**
- Dodaj brand terms jako Brand Exclusions w PMax (Google Ads → PMax → Ustawienia → Wykluczenia marki)
- Stwórz oddzielną kampanię Search Exact Match na brand terms
- Monitoruj IS kampanii brandowej po wdrożeniu

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Brand exclusions skonfigurowane w PMax | | |
| Oddzielna kampania Search dla brand terms | | |
| Negatywne słowa kluczowe na poziomie MCC (jeśli dotyczy) | | |

---

### 10.25 — Search Themes (nowa funkcja PMax)
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
Search Themes to sugestie fraz kluczowych dla PMax wprowadzone w 2024 — pozwalają "podpowiedzieć" algorytmowi jakich zapytań szukać, bez klasycznych słów kluczowych. Maks. 25 Search Themes per Asset Group. Szczególnie ważne gdy PMax nie ma wystarczających danych historycznych (nowe kampanie) lub gdy chcemy kierować na niszowe frazy.

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| Search Themes skonfigurowane (min. 5 per AG) | | |
| Search Themes pokrywają główne intencje zakupowe | | |
| Search Themes nie pokrywają się z branded queries (→ kanibalizacja) | | |
| Search Themes aktualizowane w ciągu ostatnich 60 dni | | |

---

### 10.26 — URL Expansion i Final URL
**Priorytet:** Średni

**Czym jest i dlaczego sprawdzamy:**
URL Expansion pozwala Google kierować użytkowników na różne podstrony, nie tylko Final URL z Asset Group. Domyślnie włączone — Google "decyduje" gdzie wysłać użytkownika. Problem: Google może kierować na strony z błędami, nieistniejące podstrony lub strony o niskiej konwersji. Wyłączenie URL Expansion daje kontrolę ale ogranicza zasięg.

| Pytanie | Wynik | Ocena |
|---------|-------|-------|
| URL Expansion: włączone / wyłączone / z wykluczeniami URL | | |
| Sprawdzono które URL Google najczęściej wybiera | | |
| Wykluczone: strony błędów, strony logowania, polityki prywatności | | |
| Final URL każdej AG prowadzi do tematycznie spójnej podstrony | | |

---

### 10.27 — Performance Insights per Asset Group
**Priorytet:** Średni

**Jak sprawdzić:** Google Ads → PMax → Asset Groups → "View Asset Details"

| Asset Group | Wydatki | Konwersje | Wartość | ROAS | Gest. budżetem | Status | Działanie |
|-------------|---------|-----------|---------|------|----------------|--------|-----------|
| AG 1 | | | | | | Learning/Active | |
| AG 2 | | | | | | | |

**Flagi diagnostyczne:**
- Kampania PMax w statusie "Learning" > 6 tygodni → ⚠️ problem z sygnałami lub konwersjami
- ROAS < target ROAS o > 30% → sprawdź Asset Strength i Listing Groups
- Jeden Asset Group generuje > 80% wydatków → ⚠️ brak segmentacji

---

### 10.28 — Łączna punktacja PMax Zaawansowany

| Podsekcja | Max pkt |
|-----------|---------|
| 10.21 Asset Groups jakość | 4 |
| 10.22 Listing Groups segmentacja | 4 |
| 10.23 Audience Signals | 4 |
| 10.24 Kanibalizacja PMax | 3 |
| 10.25 Search Themes | 2 |
| 10.26 URL Expansion | 2 |
| **ŁĄCZNIE** | **19** |

**Wynik PMax Zaawansowany:** ___/19 (___%)

> Jeśli konto nie ma kampanii PMax — wpisz "N/D" i pomiń sekcję.

---

## 10 MULTI — Tryb wielu kont: per-konto sekcje _(tylko gdy N > 1 kont)_

> Gdy audytujesz więcej niż jedno konto Google Ads, KAŻDE konto otrzymuje własny blok poniżej.
> Blok kopiuj tyle razy ile kont. Numeruj: KONTO 1, KONTO 2, itd.
> Skróconą wersję (tylko tabele) → Plik 1 (Podsumowanie). Pełny blok → Plik 2 (Szczegółowy).

---

### KONTO [N] — [Nazwa konta]

> Wzorzec z audytów Invette (BDOS). Wypełnij każde pole automatycznie z API.

**ID konta:** ___ | **MCC:** ___ | **GA4 Property:** ___ | **Typ:** e-commerce / lead gen
**Alias BDOS / ID audytu:** ___

#### Wyniki kampanii Google Ads (ostatnie 30 dni)

| Metryka | Wartość |
|---------|--------|
| Wydatki łączne | PLN |
| Kliknięcia | |
| Wyświetlenia | |
| CTR | % |
| Avg. CPC | PLN |
| Konwersje | |
| Wartość konwersji | PLN |
| ROAS | % (Xx) |
| CPA | PLN |
| Kampanii łącznie | (aktywne: N) |
| Słów kluczowych | |
| Avg. Quality Score | /10 |

**Typy kampanii:** PMax: N, Search: N, Shopping: N, Display: N, DemGen: N, Video: N
**Strategie bidowania:** ___

#### Kampanie (ostatnie 30 dni)

| Kampania | Typ | Wydatki | Konw. | ROAS% | Budżet/d | Strategia | Ocena |
|----------|-----|---------|-------|-------|---------|-----------|-------|
| | PMax | PLN | | % | PLN | | ✅/⚠️/🔴 |
| | Search | PLN | | % | PLN | | |
| **ŁĄCZNIE** | | PLN | | % | | | |

**Kampanie bez konwersji (drenaż budżetu):**

| Kampania | Typ | Wydatki 30d | Diagnoza |
|----------|-----|-------------|---------|
| | | PLN | |
| **Łącznie drenażu** | | PLN | |

#### Analiza danych GA4

> Uzupełnij po autoryzacji GA4 API lub oznacz jako brak dostępu:
> `⚠️ Brak dostępu do GA4 — wymaga autoryzacji.`
>
> Do weryfikacji gdy dostęp aktywny:
> - Czy GA4 property jest połączone z tym kontem Google Ads?
> - Czy kluczowe eventy są oznaczone jako konwersje?
> - Czy dane GA4 są zgodne z danymi Google Ads? (delta < 15% akceptowalna)
> - Bounce rate i czas sesji z kampanii płatnych vs organic?
> - Udział (not set) w source/medium?

#### Błędy w konfiguracji

```
Lista wykrytych błędów. Format:
- [KRYTYCZNY] Opis błędu — wpływ biznesowy
- [UWAGA] Opis — co sprawdzić
- Nie wykryto błędów krytycznych
```

Typowe błędy do sprawdzenia:
- Niski Quality Score (< 5.0) — sprawdź relevance słów kluczowych / LP
- Kampanie z wydatkami ale bez konwersji: [lista nazw]
- Strategia Maximize Clicks na koncie e-commerce — powinna być Maximize Conv. Value
- Brak rozszerzeń reklam (sitelinks, callouts, structured snippets)
- Auto-apply recommendations włączone — ryzyko nieautoryzowanych zmian

#### Analiza trackingu

```
- ✅/❌ Konwersje śledzone (N konwersji w 30 dniach)
- ✅/❌ Wartości konwersji aktywne: PLN
- ✅/❌ Enhanced Conversions skonfigurowane
- ✅/❌ GA4 połączone z kontem Ads
- ✅/❌ Brak duplikacji konwersji
- ℹ️ Uwagi: ___
```

#### Sugestie i rekomendacje

1. ___
2. ___
3. ___

#### Ogólna ocena konta

**Format flag-ów (w jednej linii, rozdzielone |):**

```
⚠️ niski ROAS | 📉 niski QS | ❌ brak konwersji | ⚠️ wysoki CPA
```

Dostępne flagi:
- `✅ Brak krytycznych problemów` — ROAS > 3x, QS > 7, konwersje śledzone
- `⚠️ niski ROAS` — ROAS < 3x dla e-commerce (< 2x = krytyczny, ❌)
- `📉 niski QS` — Avg. Quality Score < 5.0
- `❌ brak konwersji` — 0 konwersji na całym koncie przy aktywnych wydatkach
- `⚠️ wysoki CPA` — CPA przekracza estymowany próg rentowności klienta
- `⚠️ mikrokonwersje` — konwersje mają wartość < 5 PLN lub > 1000/msc przy ROAS < 1x (podejrzenie błędnej konfiguracji)
- `ℹ️ lead gen` — brak wartości konwersji, konto lead gen (ocena ROAS niemożliwa)

**Rozwinięcie diagnostyczne:**
- ❌ / ✅ ROAS: __x (próg: 3x dla e-commerce; wzorzec: conv_value / cost)
- ❌ / ✅ Quality Score: __ / 10 (próg: min. 7.0; < 5.0 = konieczna interwencja)
- ❌ / ✅ Kampanie bez konwersji: N kampanii, szacowany drenaż PLN/msc
- ❌ / ✅ Tracking: wartości konwersji aktywne / brak / mikrokonwersje anomalii

#### Ocena specjalisty prowadzącego konto

⭐⭐ (2/5) — [komentarz jedno zdanie]

**Skala oceny specjalisty:**
| Ocena | Opis |
|-------|------|
| ⭐ (1/5) | Konto w katastrofalnym stanie — straty, brak konwersji, błędy strukturalne |
| ⭐⭐ (2/5) | Kampanie generują straty lub marnują budżet — wymagana pilna optymalizacja |
| ⭐⭐⭐ (3/5) | Konto działa ale jest dużo do poprawy — wyniki poniżej potencjału |
| ⭐⭐⭐⭐ (4/5) | Konto w dobrej kondycji — drobne optymalizacje |
| ⭐⭐⭐⭐⭐ (5/5) | Konto w doskonałej kondycji — benchmark dla innych |

---

### KONTO [N+1] — [Nazwa konta]

_[kopiuj blok powyżej]_

---

## 10 CROSS — BCG cross-account _(tryb multi-konto, tylko e-commerce z feedem)_

> Gdy masz dane produktowe z Google Ads shopping_performance dla >1 konta, dodaj analizę BCG cross-account.
> Wzorzec: GAdsBDOS_BCG.md z audytów Invette.

### Łączna baza produktowa

| Metryka | Wartość |
|---------|---------|
| Kont z danymi produktowymi | |
| Wszystkich produktów (unikalne item_id) | |
| Produktów aktywnych (min. 10 kliknięć) | |
| Łączna wartość konwersji (30d) | PLN |
| Łączne wydatki (30d) | PLN |
| ROAS portfela | x |

### Rozkład BCG — wszystkie konta

| Kwadrant | Produkty | % aktywnych | Wydatki | Przychód | ROAS | Śr. CTR | Śr. Conv Rate |
|----------|----------|-------------|---------|----------|------|---------|---------------|
| ⭐ Gwiazdy | | | PLN | PLN | x | % | % |
| 🐄 Dojne Krowy | | | PLN | PLN | x | % | % |
| ❓ Znaki Zapytania | | | PLN | PLN | x | % | % |
| 🐕 Psy | | | PLN | PLN | x | % | % |

**Kluczowe insighty BCG:**
- Gwiazdy (___% produktów) generują ___% całkowitego przychodu przy ___% wydatków → priorytet skalowania
- Znaki Zapytania mają ROAS ___x ale pochłaniają tylko ___% budżetu → niedoinwestowane
- Psy (___% produktów) pochłaniają ___% wydatków przy ROAS ___x → drenaż wymagający decyzji: feed audit lub wykluczenie
- Rekomendacja realokacji: ___% z Psów → Znaki Zapytania = szacowany wpływ ___PLN przychodów/msc

### Konta z dominacją Psów (>70% produktów w Dog)

| Konto | % Psów | Wydatki | ROAS konta | Działanie |
|-------|--------|---------|-----------|-----------|
| | % | PLN | x | Feed audit / MC health check |

### Konta z największym potencjałem Znaków Zapytania

| Konto | ZQ z wzrostem >20% | Wydatki | Akcja |
|-------|-------------------|---------|-------|
| | | PLN | Wydziel do osobnych kampanii |

---

# Format raportu DOCX

Poniżej szablon struktury dokumentu do wygenerowania:

```
RAPORT AUDYTU GA4
Klient: {nazwa_klienta}
Data: {data}
Audytor: Adrian Andrzejczyk
Property ID: {ID}
Typ biznesu: {e-commerce / lead gen / SaaS}

════════════════════════════════════
CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE
(max 2 strony A4)
════════════════════════════════════

1. WYNIKI SEKCJI
[Tabela: Sekcja | Wynik % | Ocena]

2. JAKOŚĆ DANYCH
[Odpowiedź na pytanie: Czy danym można ufać?
W jakim zakresie? Co jest wiarygodne, co nie?]

3. KONFIGURACJA GA4
[Czy GA4 jest dobrze skonfigurowane?
Czy wykorzystujemy pełny potencjał narzędzia?]

4. INFRASTRUKTURA (GTM / sGTM)
[Czy infrastruktura jest nowoczesna i odporna?]

5. KLUCZOWE WNIOSKI
[3–5 najważniejszych obserwacji]

════════════════════════════════════
CZĘŚĆ II — OMÓWIENIE SZCZEGÓŁOWE
════════════════════════════════════

[Dla każdego punktu audytu:]

## {Numer}. {Nazwa punktu}

{Opis — min. ¼ strony A4: czym jest zagadnienie,
dlaczego je sprawdzamy, napisane językiem zrozumiałym
dla dyrektora/właściciela firmy}

Wynik: ✅ OK / ❌ Błąd / ⚠️ Do weryfikacji / ➖ Nie dotyczy

{Komentarz jeśli nie OK}

{Rekomendacja jeśli nie OK}

════════════════════════════════════
CZĘŚĆ III — REKOMENDACJE
════════════════════════════════════

🔴 PILNE (wdrożenie ASAP):
1. ...
2. ...

🟡 DO ZAPLANOWANIA:
1. ...

🟢 USPRAWNIENIA:
1. ...
```

---

# SEKCJA F — METODOLOGIA KWANTYFIKACJI FINANSOWEJ

> **Zasada:** Każdy problem audytowy musi być przeliczony na PLN. Wyniki bez wartości pieniężnej są ignorowane przez właścicieli firm i dyrektorów marketingu. Każda rekomendacja = konkretna liczba: koszt niedziałania LUB oszczędność/przychód z wdrożenia.

---

## F1 — Formuły bazowe

### F1.1 — Koszt zduplikowanych transakcji (GA4)

```
Zduplikowane transakcje = purchase_count - unique_transaction_id_count
Przychód zawyżony = zduplikowane_tx × średnia_wartość_zamówienia (AOV)
AOV = total_revenue / unique_transactions
Korekta ROAS = true_revenue / ad_spend
```

**Przykład:** 150 transakcji, 40 duplikatów, AOV = 280 PLN → zawyżony przychód = 40 × 280 = **11 200 PLN/msc**. ROAS raportowany: 8.4x → prawdziwy ROAS: 7.1x.

---

### F1.2 — Koszt niskiego Quality Score

```
Szacunkowe CPC penalty per punkt QS:
QS 1–3: płacisz ~400% normy
QS 4–5: płacisz ~150% normy
QS 6–7: płacisz ~100% normy (baseline)
QS 8–10: płacisz ~80–90% normy (premium)

Oszczędność z poprawy QS = ad_spend × (1 - QS_factor_po / QS_factor_przed)
```

**Tabela przelicznikowa:**

| QS przed | QS po | Mnożnik kosztu (przed) | Mnożnik (po) | Oszczędność CPC |
|----------|-------|------------------------|--------------|-----------------|
| 3 | 6 | ~4.0x | ~1.0x | ~75% |
| 4 | 7 | ~1.5x | ~0.9x | ~40% |
| 5 | 8 | ~1.2x | ~0.85x | ~29% |
| 6 | 9 | ~1.0x | ~0.8x | ~20% |

**Przykład (TABLE4U, QS 3.3, 66 998 PLN/msc):**
Poprawa QS 3→6 = oszczędność ~50% CPC = **~33 500 PLN/msc** przy tym samym budżecie lub +100% klików.

---

### F1.3 — Koszt braku konwersji (kampanie z wydatkami, 0 konwersji)

```
Zmarnowany budżet = ad_spend_bez_konwersji (100% straty)
Potencjalny przychód = ad_spend × benchmark_ROAS_branży
Szacunkowa marża stracona = ad_spend × marża_klienta%
```

**Przykład:** Kampania 5 000 PLN/msc, 0 konwersji, benchmark ROAS branży = 4x → strata szacunkowego przychodu = **20 000 PLN/msc**. Marża 30% → stracona marża = **1 500 PLN/msc**.

---

### F1.4 — Koszt niedoinwestowania liderów (wysokie ROAS, niski budżet)

```
Potencjalny przychód dodatkowy = budżet_dodatkowy × aktualny_ROAS
Warunek: konto/kampania w fazie skalowania (nie saturacja rynku)
Sygnał saturacji: Impression Share > 80% → ograniczone pole do skalowania
```

**Przykład (IN-SKYCAMP, ROAS 101.7x, budżet 6 521 PLN/msc):**
Zwiększenie budżetu 3x → +13 042 PLN wydatków → potencjalnie +**1 327 000 PLN** dodatkowych przychodów (przy zachowaniu ROAS — w praktyce zakładaj 40–60% regresji ROAS przy skalowaniu).
Realistycznie przy ROAS 50x: +13 042 PLN × 50 = +**652 100 PLN/msc**.

---

### F1.5 — Koszt błędnej atrybucji (Last Click vs DDA)

```
Różnica przychodu raportowanego = |LCA_revenue - DDA_revenue|
Różnica ROAS = LCA_ROAS - DDA_ROAS
Budżet źle alokowany = ad_spend × |delta_ROAS%| / 100
```

**Przykład:** Last Click ROAS = 5.2x, DDA ROAS = 7.8x dla Display. Różnica 50% → Display niedofinansowane. Przy budżecie Display 20 000 PLN → niedoalokacja **10 000 PLN/msc** (relatywnie vs. potencjał kanału).

---

### F1.6 — Koszt braku Customer Match (e-commerce)

```
Benchmark: remarketing CVR = 3–5% vs cold traffic CVR = 0.5–1.5%
Customer Match boost: +20–40% CVR vs zwykły remarketing
Potencjalny przychód z CM = lista_emaili × match_rate × CVR_boost × AOV × zakładana_aktywność%
```

**Uproszczony kalkulator:**
```
Lista: 10 000 emaili
Match rate: 40% → 4 000 dopasowanych
Aktywność (zakup w 90 dni): 5% → 200 transakcji
AOV: 350 PLN
Potencjalny przychód z remarketing CM: 200 × 350 = 70 000 PLN
Przy braku CM: tracisz precyzję targetowania, płacisz za zimny traffic
```

---

### F1.7 — Koszt złej segmentacji BCG (Psy vs Gwiazdy)

```
Strata z Psów = wydatki_Psy × (1 - ROAS_Psy/ROAS_min_akceptowalny)
Zysk z realokacji na Znaki Zapytania = realokowany_budżet × ROAS_ZQ
Delta przychodu = zysk_ZQ - strata_Psy (po odliczeniu Psów)
```

**Przykład (Invette portfel):**
```
Psy: 137 195 PLN wydatków, ROAS 0.8x → przychód 109 756 PLN (strata 27 439 PLN netto)
Realokacja 10% (13 700 PLN) na ZQ przy ROAS 21.3x → przychód 291 810 PLN
Delta: +291 810 - 10 960 (utracony przychód Psów) = +280 850 PLN/msc
```

---

### F1.8 — Koszt błędnego śledzenia GA4 (brak/zduplikowane eventy)

```
Wpływ na decyzje = % decyzji budżetowych opartych na błędnych danych × budżet
Korekta ROAS przy brakujących konwersjach:
  true_ROAS = reported_ROAS × (1 + brakujace_konwersje% / 100)
Korekta ROAS przy duplikatach:
  true_ROAS = reported_ROAS × (1 - duplikaty% / 100)
```

**Przykład:** GA4 raportuje 200 zakupów/msc, po korekcie duplikatów = 140 prawdziwych. ROAS raportowany 6.5x → prawdziwy ROAS = 6.5 × (140/200) = **4.55x**. Przy 100 000 PLN budżetu reklamowego: decyzja o skalowaniu oparta na fałszywym ROAS może wygenerować **stratę** zamiast zysku.

---

## F2 — Tabela Impact Summary (do każdego raportu)

> Każdy audyt kończy się tą tabelą. Wypełnij WSZYSTKIE wykryte problemy z wartością PLN.

| # | Problem | Koszt miesięczny (PLN) | Koszt roczny (PLN) | Priorytet | Status wdrożenia |
|---|---------|----------------------|-------------------|-----------|-----------------|
| 1 | Zduplikowane transakcje GA4 (zawyżony ROAS) | | | 🔴 Pilny | ☐ |
| 2 | Kampanie bez konwersji (zmarnowany budżet) | | | 🔴 Pilny | ☐ |
| 3 | Niski QS (przepłacony CPC) | | | 🟡 Ważny | ☐ |
| 4 | Psy BCG (nieefektywny budżet feedu) | | | 🟡 Ważny | ☐ |
| 5 | Niedoinwestowani liderzy (utracony przychód) | | | 🟡 Ważny | ☐ |
| 6 | Brak Customer Match (niższe CVR) | | | 🟢 Zalecane | ☐ |
| 7 | Błędna atrybucja (źle alokowany budżet) | | | 🟢 Zalecane | ☐ |
| 8 | Brak Enhanced Conversions (mniejsza dokładność) | | | 🟢 Zalecane | ☐ |
| **ŁĄCZNIE** | | | | | |

**Potencjał wzrostu przychodów:** ___% przy tym samym budżecie, przez realokację i naprawę problemów.

---

## F3 — Język narracji finansowej

> Używaj tych zwrotów w raporcie — właściciel/dyrektor musi poczuć koszt zaniechania:

**Zamiast:** "Quality Score jest niski"
**Napisz:** "Niski QS 3.3 na koncie TABLE4U oznacza przepłacanie za kliknięcia o szacowane 40–75%. Przy budżecie 66 998 PLN/msc to **26 800–50 000 PLN miesięcznie** wydanych więcej niż potrzeba. W skali roku: **321 000–600 000 PLN nadpłaty**."

**Zamiast:** "Kampanie bez konwersji wymagają optymalizacji"
**Napisz:** "10 kampanii pochłania 12 700 PLN/msc nie generując ani jednej transakcji. To **152 400 PLN rocznie** bez żadnego zwrotu — środki które można natychmiast przesunąć na kampanie z udowodnionym ROAS."

**Zamiast:** "Należy skalować konto IN-SKYCAMP"
**Napisz:** "IN-SKYCAMP osiąga ROAS 101.7x przy budżecie 6 521 PLN. Każda złotówka zainwestowana zwraca ponad 100 PLN. Brak decyzji o skalowaniu to **koszt utraconych przychodów szacowany na 300 000–650 000 PLN miesięcznie** przy 3–5x budżetu."

---

## KROK KOŃCOWY — Zapis plików po zakończeniu audytu (OBOWIĄZKOWE)

Po ukończeniu audytu **zawsze** zapisujesz 4 wersje pliku dla każdego klienta:

### Wymagane pliki wyjściowe

| Plik | Opis | Jak wygenerować |
|------|------|-----------------|
| `{DATA}_{klient}_audyt.md` | **Wersja long** — pełny audyt ze wszystkimi danymi, tabelami, metodologią | Piszesz bezpośrednio (Write tool) |
| `{DATA}_{klient}_podsumowanie.md` | **Wersja short** — skrócone executive summary (max 2–3 strony A4): KPI, TOP 3 problemy, TOP 3 rekomendacje, priorytety | Piszesz osobno na podstawie wersji long |
| `{DATA}_{klient}_audyt.docx` | **Word (long)** — wygenerowany z `_audyt.md` | `"C:/Program Files/Python310/python.exe" generate_docx.py {DATA}_{klient}_audyt.md` |
| `{DATA}_{klient}_podsumowanie.docx` | **Word (short)** — wygenerowany z `_podsumowanie.md` | `"C:/Program Files/Python310/python.exe" generate_docx.py {DATA}_{klient}_podsumowanie.md` |

> **PDF** — generujesz w Word ręcznie: Plik → Eksportuj → Utwórz PDF/XPS → zapisz obok pliku .docx jako `{DATA}_{klient}_audyt.pdf` i `{DATA}_{klient}_podsumowanie.pdf`

### Kolejność zapisu

1. Napisz `_audyt.md` (wersja long — pełny raport)
2. Napisz `_podsumowanie.md` (wersja short — executive summary)
3. Wygeneruj `_audyt.docx` przez `generate_docx.py`
4. Wygeneruj `_podsumowanie.docx` przez `generate_docx.py`
5. Poinformuj użytkownika: **"Wygeneruj PDF ręcznie w Word: Plik → Eksportuj → PDF"**

### Co zawiera wersja SHORT (_podsumowanie.md)

Struktura executive summary:
```
# Audyt MarTech — {Klient} | {Data}

## Wynik ogólny
[Jedna tabela: 5–7 KPI z oceną ✅/⚠️/❌]

## TOP 3 Problemy krytyczne
[Max 3 punkty z opisem wpływu finansowego]

## TOP 3 Rekomendacje
[Max 3 punkty z konkretnym działaniem i priorytetem]

## Priorytety wdrożenia
[Tabela: Działanie | Pilność | Szacowany wpływ]
```

### Informacja dla użytkownika po zakończeniu

Po zapisaniu wszystkich plików zawsze napisz:
```
Zapisano:
✅ {DATA}_{klient}_audyt.md (wersja long)
✅ {DATA}_{klient}_podsumowanie.md (wersja short)
✅ {DATA}_{klient}_audyt.docx
✅ {DATA}_{klient}_podsumowanie.docx
⏳ PDF — wygeneruj ręcznie w Word: Plik → Eksportuj → Utwórz PDF/XPS
```
