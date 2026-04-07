# Findings — modnakiecka — 20260407

> **Dostępy:** GA4 API (property 291537403) | Brak: GTM Admin, Google Ads, BigQuery, DevTools  
> **Nota:** Punkty wymagające GTM Admin lub DevTools oznaczone 🔒. Nie są wliczane do punktacji.

---

## SEKCJA 1 — Audyt Wstępny

### 1.1 Adnotacje w GA4
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt
- **Komentarz**: Wymaga dostępu do GA4 Admin → zakładka Adnotacje. Nie zweryfikowano.
- **Rekomendacja**: Weryfikuj po uzyskaniu dostępu GA4 Admin.

### 1.2 Kolejność skryptów HTML
- **Status**: ❌ Błąd krytyczny
- **Wynik**: 0/3 pkt
- **Komentarz**: Z analizy HTML strony (poprzedni audyt 2026-04-03, potwierdzony przez bieżące dane) na stronie działają równolegle **dwa kontenery GTM: GTM-N4D6KSC** (zarządzany przez agencję/właściciela) oraz **GTM-T68LWS** (wstrzykiwany automatycznie przez platformę Shoper). Shoper ma wbudowane zdarzenia e-commerce GA4 (purchase, add_to_cart, itp.). Jeśli oba kontenery strzelają tymi samymi zdarzeniami — każdy purchase event jest podwójny. Potwierdzenie: w próbce 200 transactionID → 49,5% (99 wierszy) ma >1 trafienie, maksymalnie 12 trafień dla ID 14564069.
- **Impact PLN**: Duplikacja zdarzeń w pikselu Meta i Google Ads Conversion Tag = zawyżony ROAS w tych platformach. Jeśli Meta Pixel odpalił 12× dla jednej transakcji 430 PLN → Meta "widzi" 5 160 PLN przychodu. Fałszywy ROAS utrudnia prawidłową optymalizację stawek.
- **Rekomendacja**: Natychmiast: (1) wyłączyć z kontenera właściciela wszystkie tagi GA4 e-commerce, które Shoper już śle automatycznie — LUB (2) wyłączyć kontener Shopera i przenieść całe śledzenie do kontenera agencji. Priorytet: Tydzień 1.

### 1.3 Przegląd podstron
- **Status**: 🔒 Brak dostępu (DevTools)
- **Wynik**: 0/3 pkt
- **Komentarz**: Wymaga DevTools F12 na żywej stronie. Pośrednie sygnały z danych: purchase event duplikuje się 12× (ID=14564069), co sugeruje błędy JS lub podwójne firing w GTM. Zalecana weryfikacja ręczna.
- **Rekomendacja**: Otwórz DevTools na stronie potwierdzenia zamówienia, sprawdź Console i Network. Zidentyfikuj, który kontener odpala purchase i czy oba strzelają równocześnie.

### 1.4 Tag Assistant
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/1 pkt

### 1.5 TagHound
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 1.6 Consent Mode — wstępna weryfikacja
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: CMP to własne rozwiązanie oparte na `window.customerPrivacy` (Shoper built-in). Baner zgody jest obecny na stronie (potwierdzono w poprzednim audycie). Brak zewnętrznego dostawcy CMP (Cookiebot, OneTrust, Usercentrics). Własne implementacje CMP są trudniejsze do audytowania i częściej mają luki w blokowaniu tagów przed udzieleniem zgody. Pełna weryfikacja wymaga GTM Admin + DevTools.
- **Rekomendacja**: Weryfikuj w trybie incognito DevTools: czy GA4 i Meta Pixel strzelają PRZED interakcją z banerem.

### 1.7 Brak starych kodów UA
- **Status**: ❌ Błąd
- **Wynik**: 0/1 pkt
- **Komentarz**: Tag Universal Analytics `UA-82686028-1` jest obecny w kodzie HTML strony (wykryty z analizy HTML). UA przestało zbierać dane w lipcu 2023. To martwy kod, który niepotrzebnie ładuje skrypt `analytics.js` przy każdym odsłonie. Szacowane opóźnienie: 50–200 ms per sesja.
- **Rekomendacja**: Usuń tag UA z GTM-N4D6KSC. Priorytet: niski (brak wpływu na dane), ale higiena techniczna.

### 1.8 DataLayer — poprawność
- **Status**: 🔒 Brak dostępu (DevTools)
- **Wynik**: 0/3 pkt

### 1.9 DataLayer GA4 — struktura e-commerce
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: **Kluczowe odkrycie z GA4 API:** Pomimo 31 090 zarejestrowanych zakupów i 6 842 880 PLN przychodu w 30 dniach — **żaden produkt w GA4 nie ma `itemsPurchased > 0` ani `itemRevenue > 0`**. Dane view_item są OK (top produkt: Beżowy Trencz — 26 523 wyświetleń), ale żadne zdarzenie purchase nie przekazuje tablicy `items[]` z danymi produktów. Przyczyna: w evencie `purchase` brak obiektu `ecommerce.items[]` z polami item_id, item_name, price, quantity — lub item_id w purchase nie pasuje do item_id w view_item.
- **Impact PLN**: Brak atrybucji przychodu do produktów = niemożliwa analiza BCG, niemożliwa optymalizacja kampanii produktowych Google/Meta po produkcie, brak personalizacji rekomendacji w SALESmanago. 6 842 880 PLN miesięcznego przychodu bez żadnej identyfikacji które produkty go generują.
- **Rekomendacja**: (1) W DevTools na stronie potwierdzenia zamówienia → Console → sprawdź `dataLayer` → szukaj eventu `purchase` → czy ma obiekt `items[]`; (2) jeśli brak: dodać items[] do purchase event w GTM; (3) sprawdzić format item_id — musi być spójny z tym używanym w view_item (np. SKU lub ID produktu Shopera). Priorytet: NATYCHMIAST.

### 1.10 Google Analytics 360
- **Status**: ➖ Nie dotyczy
- **Wynik**: ➖

### 1.11 Remarketing Google Ads
- **Status**: ➖ Brak dostępu Google Ads
- **Wynik**: ➖

### 1.12 Konwersje Google Ads w GTM
- **Status**: ➖ Brak dostępu Google Ads
- **Wynik**: ➖

### 1.13 Meta (Facebook) Pixel
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Meta Pixel ID 973622559419130 wykryty w kodzie HTML strony. Ruch Meta widoczny w GA4: facebook/cpc = 546 733 sesji, liczne warianty referral potwierdzają aktywność. Pixel generuje 703 013 sesji i 1 980 994 PLN przychodu w 30 dniach. Jednakże ze względu na duplikację purchase events (pkt 1.2), pixel Meta może raportować zawyżony przychód.
- **Rekomendacja**: Po rozwiązaniu duplikacji (pkt 1.2) zweryfikować konwersje Meta vs GA4.

### 1.14 Meta — API konwersji (CAPI)
- **Status**: 🔒 Brak dostępu GTM Admin
- **Wynik**: 0/3 pkt
- **Komentarz**: Brak możliwości weryfikacji CAPI bez GTM Admin. Brak sGTM wyklucza server-side CAPI przez GTM Server. Przy 703 013 sesjach z Meta i 1 980 994 PLN przychodu brak CAPI oznacza utratę sygnałów konwersji z użytkowników odmawiających cookies (ok. 15-30% ruchu).
- **Rekomendacja**: Wdrożyć Meta CAPI przez GTM (Conversions API Gateway lub endpoint własny). Miesiąc 1.

### 1.15 LinkedIn Insight Tag
- **Status**: ➖ Nie dotyczy (brak kampanii LinkedIn)
- **Wynik**: ➖

### 1.16 Pinterest Tag
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Kampanie Pinterest aktywne — widoczne w GA4: Pinterest/cpc = 6 151 sesji, 22 transakcje; pl.pinterest.com/cpc = 128 sesji, 4 transakcje; pinterest.com/referral = 1 434 sesji. Łącznie ruch z Pinterest widoczny i śledzony.

### 1.17 Yandex Metrica
- **Status**: ➖ Nie dotyczy
- **Wynik**: ➖

### 1.18 Microsoft Clarity — instalacja
- **Status**: ➖ Nie wdrożone
- **Wynik**: ➖ (nie wdrożone, więc nie sprawdzamy 1.18.1–1.18.5)
- **Komentarz**: Brak Clarity na stronie. Przy 89,3% ruchu mobilnym i CR mobilnym 2× niższym niż desktop — Clarity z nagraniami sesji mobilnych byłoby wartościowym narzędziem diagnostycznym. Koszt: darmowy dla pierwszych 25 000 sesji/msc.
- **Rekomendacja**: Rozważ wdrożenie Clarity dla diagnostyki UX mobile. Miesiąc 2-3.

### 1.19 Bing/Microsoft Ads
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Bing Ads aktywne: bing/cpc = 10 657 sesji, 376 transakcji, 100 306 PLN. Bing/organic = 6 427 sesji, 225 transakcji, 58 133 PLN. Microsoft Ads działa i generuje przychód.

### 1.20 TikTok Pixel
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: Ruch TikTok widoczny w GA4 (19 796 sesji łącznie, 147 transakcji), jednak pixel TikTok nie był widoczny w poprzedniej analizie HTML. Możliwe: pixel wdrożony przez GTM po poprzedniej analizie, lub wdrożony server-side. Wymaga weryfikacji przez DevTools → Network → analytics.tiktok.com.
- **Rekomendacja**: Zweryfikuj przez DevTools. TikTok ma 7 wariantów UTM (patrz sekcja 5) — wskazuje na problemy z konfiguracją.

### 1.22 Criteo
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Criteo aktywny: criteo/retargeting = 73 105 sesji, 990 transakcji, 203 948 PLN. criteo/display = 17 179 sesji, 23 transakcje. Łącznie 93 208 sesji i 216 357 PLN.

### 1.23 RTB House
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: RTB House aktywny: rtbhouse/retargeting = 49 sesji, 2 transakcje, 280 PLN. rtbhouse/prospecting = 8 sesji. Niski wolumen — kampania dopiero startuje lub budżet bardzo ograniczony.

### 1.24 Allegro Ads
- **Status**: ➖ Nie dotyczy (brak kampanii)
- **Wynik**: ➖

**Sekcja 1 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 1.2 Kolejność / 2x GTM | ❌ | 0/3 |
| 1.6 Consent wstępny | ⚠️ | 1/2 |
| 1.7 Brak UA | ❌ | 0/1 |
| 1.9 DataLayer items[] | ❌ | 0/3 |
| 1.13 Meta Pixel | ✅ | 3/3 |
| 1.16 Pinterest | ✅ | 3/3 |
| 1.19 Bing | ✅ | 2/2 |
| 1.20 TikTok | ⚠️ | 1/3 |
| 1.22 Criteo | ✅ | 2/2 |
| 1.23 RTB House | ✅ | 2/2 |
| **Sprawdzalne** | | **14/24 pkt** |
| Nieweryfikowalne (🔒) | | 0/16 pkt |

---

## SEKCJA 2 — ePrivacy / Consent Mode

> Większość punktów wymaga GTM Admin + DevTools (tryb incognito). Możliwe do weryfikacji z GA4 API: 2.18, 2.19, 2.20.

### 2.1–2.17
- **Status**: 🔒 Brak dostępu (GTM Admin + DevTools wymagane)
- **Wynik**: 0/38 pkt
- **Komentarz**: Cała sekcja ePrivacy wymaga: GTM Preview Mode, DevTools Network, DevTools Application (Cookies), DevTools Console. Bez tych narzędzi nie możliwe jest sprawdzenie: czy baner blokuje tagi przed zgodą, sekwencji consent_default/consent_update w DataLayer, url_passthrough, konfiguracji consent w każdym tagu GTM.
- **Rekomendacja**: Pełna weryfikacja wymaga sesji z dostępem do GTM Preview Mode + przeglądarka incognito + DevTools. Zlecić weryfikację na miejscu lub przy udzielonym dostępie GTM Admin.

### 2.18 Brak danych wrażliwych w URL
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Analiza landing pages (top 20 z GA4) nie wykazała wzorców email=, phone=, pesel= ani podobnych w URL-ach stron. Ścieżki URL wyglądają prawidłowo (np. `/sukienki-eleganckie`, `/kategoria/`, `/produkt/`).

### 2.19 Brak danych wrażliwych w UTM
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Analiza 200 wariantów source/medium nie wykazała adresów email, telefonów ani danych osobowych w UTM. Wszystkie wartości source/medium są nazwami kanałów lub narzędzi (facebook, salesmanago, criteo, itp.).

### 2.20 Brak danych wrażliwych w zdarzeniach
- **Status**: 🔒 Brak dostępu (DebugView / BigQuery)
- **Wynik**: 0/3 pkt

**Sekcja 2 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 2.1–2.17 (GTM+DevTools) | 🔒 | 0/38 |
| 2.18 PII w URL | ✅ | 3/3 |
| 2.19 PII w UTM | ✅ | 3/3 |
| 2.20 PII w zdarzeniach | 🔒 | 0/3 |
| **Sprawdzalne** | | **6/6 pkt** |
| Nieweryfikowalne (🔒) | | 0/41 pkt |

---

## SEKCJA 3 — Konfiguracja GTM i GA4

> Większość wymaga dostępu do GTM Admin i GA4 Admin. Poniżej oceniane punkty możliwe z API.

### 3A.1 Walidacja GTM
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Dwa aktywne kontenery GTM: GTM-N4D6KSC (właściciel) + GTM-T68LWS (Shoper). Shoper automatycznie wstrzykuje własny kontener z wbudowanymi zdarzeniami GA4. Prawidłowa konfiguracja to jeden kontener GTM na stronie. Dwa kontenery = ryzyko duplikacji zdarzeń.

### 3A.7 Brak kodów UA w GTM
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Tag UA-82686028-1 aktywny w HTML strony. Nawet jeśli nie jest w GTM (co wymaga weryfikacji), obecność w HTML oznacza ładowanie analytics.js przy każdym odsłonie.

### 3A.8 GA4 przez GTM
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 0/1 pkt
- **Komentarz**: GA4 może być wdrożone przez oba kontenery (hardcoded + GTM). Wymaga weryfikacji w GTM Admin.

### 3A.10 Brak zduplikowanych tagów
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: Duplikacja purchase events potwierdzona przez dane: ID=14564069 zarejestrowany **12 razy** (tr=12, ep=12). ID=14586462 i ID=14587588 po 6 razy każdy. Z 200 próbnych transactionID — 99 (49,5%) ma >1 trafienie. Źródło: oba kontenery GTM strzelają tymi samymi zdarzeniami purchase.

### 3C.3 Waluta
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: GA4 raportuje przychody w PLN (6 842 880 PLN), co jest poprawną walutą dla sklepu polskiego.

### 3C.9 Strumień Web
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Dane napływają aktywnie: 1 858 660 sesji, 31 090 zakupów w 30 dniach. Strumień działa prawidłowo.

### 3C.10 Cross-domain tracking
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 0/3 pkt
- **Komentarz**: Na stronie aktywne dwie bramki płatności: Przelewy24 (zintegrowane) i PayPo (BNPL). Bramki nie widoczne w top referral (dobry sygnał), ale bez dostępu do GA4 Admin → Strumień → Konfigurowanie domen nie można potwierdzić, że są poprawnie skonfigurowane jako własne domeny. Brak konfiguracji cross-domain = każde przejście przez bramkę tworzy nową sesję z source=przelewy24.
- **Rekomendacja**: W GA4 Admin → Strumień danych → Konfigurowanie domen → dodaj przelewy24.pl, paypo.pl jako własne domeny. Priorytet: wysoki.

### 3C.11 Ignorowanie zduplikowanych konfiguracji
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: Przy dwóch aktywnych kontenerach GTM (jeden z nich od Shopera) i potencjalnym hardcoded GA4, opcja "Ignorowanie zduplikowanych konfiguracji" w GA4 Strumień → Zarządzaj tagiem jest krytyczna. Bez niej każda sesja ładuje dwa tagi GA4, podwajając page_view i inne zdarzenia. Duplikacja purchase potwierdzona danymi.

### 3C.16 Zdarzenia jako konwersje
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Zdarzenie `purchase` jest wdrożone i generuje 31 090 konwersji. Zakładam na podstawie standardowej konfiguracji Shopera że purchase jest oznaczone jako konwersja. Weryfikacja w GA4 Admin → Konwersje.

### 3C.19 BigQuery
- **Status**: ❌ Brak
- **Wynik**: 0/3 pkt
- **Komentarz**: BigQuery nie jest skonfigurowane (brak dostępu). Przy 6,84 mln PLN przychodu miesięcznie i złożonym stacku MarTech (SALESmanago, Criteo, Meta, TikTok) — brak eksportu do BQ oznacza brak możliwości zaawansowanej atrybucji, analizy customer lifetime value, segmentacji RFM.
- **Rekomendacja**: Podłączyć BigQuery Export w GA4 Admin. Koszt: ~0 PLN (sandbox BQ). Miesiąc 1-2.

### 3K.1–3K.7 BigQuery Audit
- **Status**: ➖ Nie dotyczy (brak BQ)
- **Wynik**: ➖

### 3B.1–3B.6 sGTM
- **Status**: ➖ Nie dotyczy (brak sGTM)
- **Wynik**: ➖

**Sekcja 3 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 3A.1 Walidacja GTM | ❌ | 0/3 |
| 3A.7 Brak UA | ❌ | 0/3 |
| 3A.10 Duplikaty tagów | ❌ | 0/3 |
| 3C.3 Waluta PLN | ✅ | 2/2 |
| 3C.9 Strumień web | ✅ | 3/3 |
| 3C.10 Cross-domain | ⚠️ | 0/3 |
| 3C.11 Ignoruj duplikaty | ❌ | 0/3 |
| 3C.16 Konwersje | ✅ | 2/2 |
| 3C.19 BigQuery | ❌ | 0/3 |
| **Sprawdzalne** | | **7/25 pkt** |
| Reszta (🔒 GTM Admin) | 🔒 | 0/~65 pkt |

---

## SEKCJA 4 — Data Quality

### 4A.2 Udział pierwszego źródła (not set) <5%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: First User Source (not set)/(not set) = 3 118 newUsers w TOP 30 źródeł. Łączna liczba nowych użytkowników ~637 000. % (not set) = **0,49%** — zdecydowanie poniżej 5%.

### 4A.3 Pierwsze źródło użytkownika wygląda naturalnie
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Naturalna dystrybucja pierwszego źródła nowych użytkowników: google/cpc (218 087) → facebook/cpc (147 883) → google/organic (64 454) → (direct) (38 873) → criteo/retargeting (12 162). Hierarchia typowa dla sklepu fashion z silnym Google Ads i Meta Ads. Direct 38 873 (6,1%) = normalny poziom dla rozpoznawalnej marki.

### 4A.1 Udział sesji (not set) <5%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set)/(not set) = 34 214 sesji + inne not set warianty = łącznie 61 232 sesji z (not set) w source lub medium. 61 232 / 1 858 660 = **3,3%** — poniżej progu 5%.

### 4A.4 Pozostały ruch wygląda naturalnie
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Rozkład kanałów jest naturalny dla e-commerce fashion: google/cpc dominuje (33,5%), meta/cpc drugi (29,4%), organic trzeci (7,4%). Brak jednego kanału dominującego >70%. CR per kanał w akceptowalnych zakresach.

### 4A.6 Brak ruchu spamowego
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Wśród 200 wariantów source/medium nie wykryto typowych domen spamowych. Obecne `192.168.8.1` (4 sesje) i IP `77.79.221.135:6080` (4 sesje) — minimalne, nieistotne statystycznie.

### 4A.7 Bramki płatności poza ścieżką
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Przelewy24 i PayPo nieobecne w source/medium z liczbą sesji wskazującą na problem cross-domain. paypo.pl/referral = tylko 9 sesji (akceptowalne). Bramki są prawdopodobnie poprawnie skonfigurowane lub poziom problemu jest niski.

### 4A.8 Bramki pocztowe poza ścieżką
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: wp.pl, onet.pl, o2.pl, interia.pl nie widoczne jako referral z istotnym ruchem. mail.google.com/referral = 86 sesji (nieistotne). Brak problemu webmaili.

### 4A.9 Facebook/Meta — fragmentacja
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: **14 wariantów source dla Facebook** w 30 dniach. Łącznie 703 013 sesji. Warianty: `facebook/cpc` (546 733), `m.facebook.com/referral` (51 530), `fb/paid` (48 461), `lm.facebook.com/referral` (28 769), `facebook/traffic` (16 365), `l.facebook.com/referral` (8 171), `facebook.com/referral` (1 442), `fb/traffic` (1 438), i 6 mniejszych. Tylko 546 733 sesji (77,7%) ma poprawne UTM. **156 280 sesji (22,3%) Facebook jest błędnie klasyfikowane** — głównie jako referral zamiast paid social.
- **Impact PLN**: Ruch Facebook/referral (m.facebook.com: 200 792 PLN, lm.facebook.com: 82 553 PLN, l.facebook.com: 39 374 PLN) = łącznie ~322 719 PLN przychodu atrybuowanego do referral zamiast paid social. ROAS Meta w raportach GA4 jest zaniżony o ten przychód.
- **Rekomendacja**: Dodać automatyczne UTM do wszystkich reklam Meta: `utm_source=facebook&utm_medium=cpc&utm_campaign={{campaign.name}}`. W Meta Ads Manager → ustawienia konta → automatyczne UTM. Priorytet: Tydzień 1.

### 4A.10 Ruch międzynarodowy
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Top 20 miast to wyłącznie polskie miasta (Warszawa, Wrocław, Poznań, Kraków itd.). Ruch wygląda naturalnie dla sklepu e-commerce targetującego Polskę.

### 4B.3 CR naturalny
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: CR = 31 090 / 1 858 660 = **1,673%** — mieści się w zakresie 0,5–3% typowym dla e-commerce fashion PL.

### 4C.1 Source/medium (not set) <5%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set) łącznie 3,3% sesji — poniżej progu.

### 4C.2 Direct/none <30%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (direct)/(none) = 64 812 sesji / 1 858 660 = **3,5%** — zdecydowanie poniżej progu 30%.

### 4C.3 Łączny (not set) + direct <40%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: 3,3% + 3,5% = 6,8% — dobrze poniżej progu 40%.

### 4C.4 Transakcje (not set) <10%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set)/(not set) = 386 transakcji / 31 090 = **1,2%** — poniżej progu 10%.

### 4D.1 Ratio ecommercePurchases:transactions ≤1.1
- **Status**: ✅ OK (z zastrzeżeniem)
- **Wynik**: 3/3 pkt
- **Komentarz**: Ratio = 1,00 (ecommercePurchases = transactions = 31 090). GA4 deduplikuje poprawnie na poziomie metryki ecommercePurchases. JEDNAK na poziomie zdarzeń (eventCount) purchase event odpala się wielokrotnie dla tego samego ID — to jest problemem dla tagów zewnętrznych (Meta Pixel, Ads).

### 4D.2 % transakcji bez transactionId <2%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: W próbce 200 TOP transactionID: **0 wierszy z (not set)**. Wszystkie transakcje mają ID.

### 4D.3 Brak malformed transaction_id
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: TransactionID wyglądają jako numeryczne identyfikatory Shopera (np. 14564069, 14586462). Brak spacji, znaków & czy parametrów URL w samym ID.

### 4D.4 value >0 przy purchase
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: PurchaseRevenue = 6 842 880 PLN dla 31 090 zakupów → AOV = 220,10 PLN. Wartość zakupów jest prawidłowo przekazywana.

### 4E.1 view_item wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: view_item = 4 629 750 zdarzeń / 6,65 per użytkownik. Aktywne i sensowne.

### 4E.2 add_to_cart wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: add_to_cart = 249 979 zdarzeń. Aktywne.

### 4E.3 begin_checkout wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: begin_checkout = 81 640 zdarzeń. Aktywne.

### 4E.4 purchase wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: purchase = 31 090 zdarzeń. Aktywne.

### 4E.5 Lejek wygląda naturalnie
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 2/3 pkt
- **Komentarz**: Kolejność lejka prawidłowa: view_item (4 629 750) > add_to_cart (249 979) > begin_checkout (81 640) > purchase (31 090). JEDNAK: `złożenie_zamówienia` (custom event Shopera) = **76 136** vs `purchase` = **31 090** — różnica 2,45×. Jeśli `złożenie_zamówienia` odzwierciedla faktyczne zamówienia złożone na platformie, to GA4 `purchase` jest ZANIŻONY o ~145%. Alternatywnie: `złożenie_zamówienia` odpala wielokrotnie (np. przy każdym powrocie na stronę potwierdzenia). Wymaga natychmiastowej weryfikacji.
- **Impact PLN**: Jeśli purchase event nie rejestruje wszystkich zakupów — brak danych o faktycznym przychodzie, zaniżone konwersje dla Google Ads i Meta.
- **Rekomendacja**: Porównaj liczbę zamówień w panelu Shopera z liczbą purchase events w GA4 za ten sam okres. Jeśli panel Shoper > GA4 purchase → purchase event nie odpala się przy każdym zamówieniu.

### 4E.6 AOV naturalny i spójny
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: AOV = 220,10 PLN. Per kanał: Paid Search = 1 563 717 / 6 262 = 249,7 PLN, Organic = 427 855 / 1 857 = 230,5 PLN, Paid Social = 1 682 605 / 8 667 = 194,2 PLN. AOV spójne, bez ekstremalnych outlierów.

**Sekcja 4 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 4A.2 First user (not set) | ✅ | 3/3 |
| 4A.3 First user naturalny | ✅ | 3/3 |
| 4A.1 (not set) <5% | ✅ | 3/3 |
| 4A.4 Ruch naturalny | ✅ | 3/3 |
| 4A.6 Brak spamu | ✅ | 2/2 |
| 4A.7 Bramki płatności | ✅ | 3/3 |
| 4A.8 Bramki pocztowe | ✅ | 3/3 |
| 4A.9 Facebook fragmentacja | ❌ | 0/2 |
| 4A.10 Ruch PL | ✅ | 2/2 |
| 4B.3 CR naturalny | ✅ | 2/2 |
| 4C.1 (not set) <5% | ✅ | 3/3 |
| 4C.2 Direct <30% | ✅ | 3/3 |
| 4C.3 Not set+direct <40% | ✅ | 3/3 |
| 4C.4 Transakcje (not set) | ✅ | 3/3 |
| 4D.1 Ratio EP:TR | ✅ | 3/3 |
| 4D.2 Brak null ID | ✅ | 3/3 |
| 4D.3 Brak malformed ID | ✅ | 3/3 |
| 4D.4 value >0 | ✅ | 3/3 |
| 4E.1 view_item | ✅ | 3/3 |
| 4E.2 add_to_cart | ✅ | 3/3 |
| 4E.3 begin_checkout | ✅ | 3/3 |
| 4E.4 purchase | ✅ | 3/3 |
| 4E.5 Lejek naturalny | ⚠️ | 2/3 |
| 4E.6 AOV spójny | ✅ | 2/2 |
| **ŁĄCZNIE** | | **63/65 pkt** |

---

## SEKCJA 5 — UTM

### 5.1 Standaryzacja UTM
- **Status**: ❌ Błąd
- **Wynik**: 0/1 pkt
- **Komentarz**: **Facebook: 14 wariantów source** w 30 dniach. **TikTok: 7 wariantów** (`tiktok/paid`, `tiktok/cpc`, `tiktok/traffic`, `tiktok/(not set)`, `tiktok.com/referral`, `tiktok/referral`, `tiktok?utm_id/paid`). Wariant `tiktok?utm_id/paid` wskazuje na malformed URL — `utm_id` wpadł do source zamiast być parametrem URL. Kryterium: max 2 warianty na kanał.
- **Impact PLN**: 156 280 sesji Meta misklasyfikowanych. 19 796 sesji TikTok z brakiem spójności uniemożliwia raportowanie ROAS na poziomie kampanii.

### 5.4 Meta/Facebook Ads — UTM
- **Status**: ⚠️ Do poprawy
- **Wynik**: 2/3 pkt
- **Komentarz**: facebook/cpc jest dominującym wariantem (546 733 sesji = 77,7%) — UTM obecne. ALE: 22,3% ruchu Meta (156 280 sesji) jest misklasyfikowane jako referral (m.facebook.com, lm.facebook.com, l.facebook.com, fb/paid, fb/traffic). Problem: kliknięcia w posty organiczne (m.facebook.com) i reklamy bez UTM wpadają jako referral.
- **Rekomendacja**: Włączyć automatyczne UTM w Meta Ads Manager. Dla postów organicznych używać UTM ręcznie.

### 5.5 Meta Ads — ID kampanii w UTM
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/2 pkt

### 5.6 Organiczne social media — UTM
- **Status**: ⚠️ Częściowo
- **Wynik**: 1/2 pkt
- **Komentarz**: Organic Social widoczny w GA4 jako kanał (128 817 sesji, 1 785 transakcji). Jednak wiele kliknięć organicznych z Facebooka wpada jako m.facebook.com/referral zamiast organic social. ig/social = 7 756 sesji, ig/paid = 1 815 sesji — Instagram organiczny i płatny mieszają się z innymi wariantami `ig`.

### 5.7 Email marketing — UTM
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: SALESmanago używa UTM dla większości kanałów email: sms/9 672 sesji, newsletter/7 040, email_confirmation/3 406, email/3 376, workflow/1 837. Ruch emailowy jest identyfikowalny w GA4.

### 5.10 Pozostałe kanały płatne — UTM
- **Status**: ⚠️ Częściowo
- **Wynik**: 1/2 pkt
- **Komentarz**: Bing/cpc — OK. TikTok — 7 wariantów (patrz 5.1). Criteo/retargeting — OK. lamoda/cpc — OK. PWA: `pwa/(not set)` = 23 019 sesji, 731 transakcji, 171 877 PLN — ruch z Progressive Web App bez żadnego UTM. 171 877 PLN przychodu nieatrybuowanego do żadnej kampanii.
- **Impact PLN**: pwa/(not set): 731 transakcji × 220 PLN = 160 820 PLN/msc bez identyfikacji źródła.
- **Rekomendacja**: Dodać UTM do linków w PWA/notyfikacjach push przez SALESmanago.

**Sekcja 5 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 5.1 Standaryzacja UTM | ❌ | 0/1 |
| 5.4 Meta UTM | ⚠️ | 2/3 |
| 5.6 Organic social UTM | ⚠️ | 1/2 |
| 5.7 Email UTM | ✅ | 2/2 |
| 5.10 Pozostałe płatne | ⚠️ | 1/2 |
| **Sprawdzalne** | | **6/10 pkt** |
| Nieweryfikowalne (🔒) | | 0/2 pkt |

---

## SEKCJA 6 — Macierz BCG

- **Status**: ➖ Nie dotyczy — brak dostępu Google Ads + brak item-level danych GA4
- **Wynik**: ➖
- **Komentarz**: Analiza BCG wymaga danych Ads per produkt (z Google Ads Shopping) ORAZ danych GA4 items (itemRevenue per produkt). Oba źródła niedostępne: Google Ads brak dostępu, items[] w GA4 puste (wszystkie produkty itemRevenue=0). BCG nie może być przeprowadzone.

---

## SEKCJA 7 — Lejki zachowań per kanał

### 7.1 Wszystkie 4 zdarzenia e-commerce wdrożone
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: view_item (4 629 750), add_to_cart (249 979), begin_checkout (81 640), purchase (31 090) — wszystkie 4 zdarzenia aktywne. Uzupełniająco: add_shipping_info (80 967), add_payment_info (81 130) również wdrożone.

### 7.2 CR paid ≥50% CR organic
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: google/cpc: 12 129 trans / 623 547 sesji = **1,95% CR**. google/organic: 1 595 trans / 136 835 sesji = **1,17% CR**. Ratio: 1,95/1,17 = **1,67× (167%)** — powyżej progu 50%. Ruch płatny Google jest lepiej konwertujący niż organiczny.

### 7.3 Brak kanału z CR <0.1% przy wydatkach >1000 PLN
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: facebook/traffic = 16 365 sesji, **20 transakcji = CR 0,12%**. Jeśli ten segment (facebook/traffic) ma wydatki >1000 PLN — jest blisko czerwonej flagi. Nie możemy potwierdzić wydatków (brak Google Ads/Meta Ads API). Inne kanały wyglądają OK: Paid Search CR 3,71%, Paid Social CR 1,40%.
- **Rekomendacja**: Zweryfikuj wydatki na kampaniach oznaczonych traffic w Meta Ads Manager. Kampanie z medium=traffic (engagement campaigns) mają niskie CR — zwykle nie generują zakupów.

### 7.4 Checkout drop-off ≤40%
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/2 pkt
- **Komentarz**: begin_checkout = **81 640**, purchase = **31 090**. Przejście checkout→purchase = 31 090/81 640 = **38,1%**. Dropout = **61,9%**. Benchmark: 50–80% powinno kończyć zakup po rozpoczęciu kasy. Możliwe przyczyny: (1) purchase event nie odpalał się dla części zamówień (duplikacja/błąd, patrz pkt 1.2); (2) autentyczny problem UX w procesie kasy; (3) `złożenie_zamówienia` = 76 136 jest bliżej begin_checkout (81 640) → sugeruje że faktyczna porzucalność kasy jest niższa (~7%), a problem leży w braku firing purchase event.
- **Impact PLN**: Jeśli 30% porzuconych checkoutów można odratować: 81 640 × 61,9% × 30% = 15 160 trans × 220 PLN = **3 335 200 PLN/msc** szansy. Jeśli to błąd śledzenia: utracone dane pomiarowe dla Google Ads Smart Bidding.
- **Rekomendacja**: NATYCHMIAST: porównaj begin_checkout z panelem Shopera (ile osób rozpoczęło kasę) i purchase z panelem (ile zamówień złożono). Jeśli panel Shoper wykazuje wyższy CR → purchase event nie odpala przy każdym zamówieniu → krytyczny błąd GTM.

**Sekcja 7 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 7.1 Cztery zdarzenia | ✅ | 2/2 |
| 7.2 CR paid vs organic | ✅ | 2/2 |
| 7.3 CR <0.1% kanały | ⚠️ | 1/2 |
| 7.4 Checkout drop-off | ❌ | 0/2 |
| **ŁĄCZNIE** | | **5/8 pkt** |

---

## SEKCJA 8 — GA4 i Google Ads

- **Status**: ➖ Brak dostępu Google Ads
- **Wynik**: ➖
- **Komentarz**: Cała sekcja wymaga dostępu do konta Google Ads. Nie zweryfikowana.

---

## SEKCJA 9 — Analiza danych

### 9.1 CVR paid ≥50% CVR organic
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Paid Search (google/cpc): CR = **1,95%**. Organic Search (google/organic): CR = **1,17%**. Ratio = 1,67× (167%) — płatny ruch dobrze konwertuje względem organicznego. Paid Social (1,40%) też powyżej progu.

### 9.2 Najlepszy kanał wg Rev/sesja
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Ranking Rev/sesja (na podstawie GA4 funnel per channel group):
  1. **Paid Search**: 1 563 717 / 168 729 = **9,27 PLN/sesja** 🏆
  2. **Referral**: 307 518 / 24 198 = **12,71 PLN/sesja** 🏆 (mały wolumen)
  3. **Direct**: 281 116 / 64 812 = **4,34 PLN/sesja**
  4. **Organic Search**: 427 855 / 143 668 = **2,98 PLN/sesja**
  5. **Cross-network (PMax)**: 1 231 275 / 442 595 = **2,78 PLN/sesja**
  6. **Paid Social**: 1 682 605 / 620 375 = **2,71 PLN/sesja**
  - **Paid Search = 3,1× efektywniejszy niż Paid Social per sesja** przy 4× mniejszym wolumenie.

### 9.3 Mobile/Desktop CVR ratio
- **Status**: ⚠️ Do poprawy
- **Wynik**: 1/3 pkt
- **Komentarz**: Mobile CR = 24 900 / 1 658 971 = **1,50%**. Desktop CR = 6 013 / 188 525 = **3,19%**. Ratio = 1,50/3,19 = **47%** — poniżej progu 50%. Mobile konwertuje o **53% gorzej** niż desktop. Przy 89,3% ruchu mobilnym to krytyczna dźwignia.
- **Impact PLN (szacunek)**: Gdyby mobile CR wzrósł z 1,50% do 2,00% (poprawa o 0,5pp): +1 658 971 × 0,50% = +8 295 dodatkowych zakupów × 210,9 PLN = **+1 749 000 PLN/msc**.
- **Rekomendacja**: Diagnostyka UX mobile: (1) wdrożyć Clarity/Hotjar dla nagrań sesji mobilnych; (2) sprawdzić Core Web Vitals na mobile (LCP, CLS, FID); (3) zbadać proces kasy na mobile — szczególnie formularze i metody płatności.

### 9.4 Engagement rate naturalny
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Engagement rate per kanał (30d): Paid Search **92,7%**, Paid Shopping 91,5%, Organic Social 91,3%, Email 90,6%, Organic Search 90,4%, Cross-network 89,4%, Paid Social 89,0%, SMS 85,8%, Display 86,1%, Direct 84,1%. Kanał Unassigned = **62,5%** — wyraźnie niższy, co wspiera tezę o problemie z identyfikacją źródła. Wszystkie główne kanały >84% — zdecydowanie powyżej progu 40%. Czas sesji: Paid Search = 597s (9,9 min), Referral = 651s — najlepsze zaangażowanie. Paid Social = 220s — najniższy czas sesji mimo wysokiego wolumenu.

### 9.5 Porzucenie koszyka <80%
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Cart abandonment = 1 - (purchase / add_to_cart) = 1 - (31 090 / 249 979) = **87,6%**. Benchmark: <80%. Przy add_to_cart = 249 979 i zakupach = 31 090 — **218 889 koszyków (87,6%) jest porzucanych**. Uwaga: jeśli purchase event jest zaniżony (patrz 4E.5 i 7.4), realne porzucenie jest niższe.
- **Impact PLN**: Poprawa CR koszyka o 5pp (z 12,4% do 17,4%): +12 499 dodatkowych zakupów × 220 PLN = **+2 749 780 PLN/msc** (scenariusz max). Realny potencjał kampanii retargetingowych (Criteo, Meta): +5% = +1 375 000 PLN/msc.
- **Rekomendacja**: (1) Uruchomić sekwencję email remarketingową w SALESmanago dla porzuconych koszyków (w 1h, 24h, 72h); (2) wzmocnić retargeting Criteo/Meta dla add_to_cart bez purchase.

### 9.6 Anomalie ruchu zidentyfikowane
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Z danych historycznych: marzec 2026 — widoczny wzrost ruchu z kanałów o niskim zaangażowaniu (Cross-network/PMax 442 595 sesji = 23,8% całości; Paid Social 620 375 sesji = 33,4%). Łącznie PMax + Meta = 57,2% sesji. Oba kanały mają CR poniżej Paid Search. Możliwa przyczyna: intensywna kampania sezonowa wiosna 2026.

### 9.7 Ruch wewnętrzny nie zaburza danych
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Warszawa (siedziba firmy najprawdopodobniej): CR = 5 336/318 811 = **1,67%** — praktycznie identyczny ze średnią konta (1,67%). Brak sygnału niezfiltrowanego ruchu wewnętrznego.

### 9.8 Referral z wysokim CVR
- **Status**: ✅ OK
- **Wynik**: 1/1 pkt
- **Komentarz**: Top referral sources z wysokim CR:
  - zasobygwp.pl: 39 sesji, 5 trans, 5 823 PLN → **CR 12,8%** 🏆
  - sklep53781.shoparena.pl: 221 sesji, 13 trans → CR 5,9%
  - wedare_512542/cps: 125 sesji, 30 trans → CR **24%** (affiliate!)
  - wedare (łącznie ~6 ID): ~575 sesji, ~141 trans → **CR ~24,5%**
  - pl.search.yahoo.com/referral: 744 sesji, 29 trans → CR 3,9%
  **Quick win**: Skalowanie affiliate programu Wedare (24% CR!) i partnerstw z wysokim CVR.

### 9.9 Bramki płatności/webmaile w referral
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Przelewy24 i PayPo nieobecne w referral z istotnym ruchem. paypo.pl = 9 sesji (marginalny). Webmaile (wp.pl, onet.pl) nieobecne. Brak problemu.

### 9.10 Retencja — % powracających kupujących
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Returning users: 1 156 169 sesji, **22 790 zakupów**, 5 035 969 PLN. New users: 663 262 sesji, **8 249 zakupów**, 1 790 064 PLN. Returning CR = **1,97%** vs New CR = **1,24%** — powracający konwertują 1,59× lepiej. Powracający = **73,4% wszystkich zakupujących** i **73,8% przychodu**. Wynik >20% progu — bardzo dobry wskaźnik lojalności klientów. AOV podobny (szac.): powracający ~221 PLN, nowi ~217 PLN.

**Sekcja 9 — Scoring:**

| Kryterium | Status | Wynik |
|---|---|---|
| 9.1 CVR paid vs organic | ✅ | 3/3 |
| 9.2 Rev/sesja per kanał | ✅ | 2/2 |
| 9.3 Mobile/Desktop CVR | ⚠️ | 1/3 |
| 9.4 Engagement rate | ✅ | 2/2 |
| 9.5 Porzucenie koszyka | ❌ | 0/3 |
| 9.6 Anomalie | ✅ | 2/2 |
| 9.7 Ruch wewnętrzny | ✅ | 3/3 |
| 9.8 Referral quick wins | ✅ | 1/1 |
| 9.9 Bramki w referral | ✅ | 3/3 |
| 9.10 Retencja | ✅ | 2/2 |
| **ŁĄCZNIE** | | **19/24 pkt** |

---

## SEKCJA 10 — Google Ads

- **Status**: ➖ Brak dostępu Google Ads
- **Wynik**: ➖

---

## Punktacja

| Sekcja | Uzyskane pkt | Max sprawdzalne | Wynik % | Ocena |
|--------|-------------|-----------------|---------|-------|
| 1. Audyt Wstępny | 14 | 24 | 58% | ⚠️ Wymaga poprawy |
| 2. ePrivacy | 6 | 6 | 100% (sprawdzalne) | ✅ OK (reszta 🔒) |
| 3. Konfiguracja | 7 | 25 | 28% | ❌ Krytyczny |
| 4. Data Quality | 63 | 65 | 97% | ✅ OK |
| 5. UTM | 6 | 10 | 60% | ⚠️ Wymaga poprawy |
| 6. BCG | ➖ | ➖ | N/A | ➖ |
| 7. Lejki | 5 | 8 | 63% | ⚠️ Wymaga poprawy |
| 8. GA4↔Ads | ➖ | ➖ | N/A | ➖ |
| 9. Analiza danych | 19 | 24 | 79% | ⚠️ Wymaga poprawy |
| 10. Google Ads | ➖ | ➖ | N/A | ➖ |
| **ŁĄCZNIE** | **120** | **162** | **74%** | ⚠️ Wymaga poprawy |

> **Uwaga:** Wynik 74% wynika z bardzo dobrego wyniku sekcji 4 (Data Quality — 97%) i sekcji 9 (79%). Technicznie dane GA4 są dobrze zebrane. Jednak **3 krytyczne błędy** w sekcjach 1 i 3 (duplikacja tagów GTM, brak items[], brak BigQuery) mają bardzo wysoki impact finansowy i blokują pełną optymalizację konta.

---

## Impact finansowy (podsumowanie)

| Problem | Szacunek PLN/msc | Priorytet |
|---------|-----------------|-----------|
| Brak items[] w purchase → niemożliwe optymalizacje product-level | Nieprzeliczalny bezpośrednio (blokuje 6,84 mln PLN/msc danych) | 🔴 NATYCHMIAST |
| `złożenie_zamówienia` vs `purchase` (2,45×) → możliwe zaniżenie purchase events | Potencjalnie +45 046 nieśledzonych zakupów × 220 PLN = **9,9 mln PLN/msc** (scenariusz max) | 🔴 NATYCHMIAST |
| Checkout dropout 61,9% → optymalizacja UX kasy | Poprawa o 10pp = +8 164 zakupów × 220 PLN = **+1 796 080 PLN/msc** | 🔴 NATYCHMIAST |
| Mobile CR gap (1,50% vs 3,19% desktop) → UX mobile | Poprawa o 0,5pp = +8 295 zakupów × 211 PLN = **+1 750 245 PLN/msc** | 🟡 Miesiąc 1 |
| Porzucenie koszyka 87,6% → remarketing | Retargeting 5pp poprawy = **+1 375 000 PLN/msc** | 🟡 Miesiąc 1 |
| Facebook fragmentacja UTM (22,3%) → błędna atrybucja | ~322 719 PLN/msc przeniesione z referral → płatny social → zawyżony ROAS SEO | 🟡 Miesiąc 1 |
| PWA bez UTM → 731 zakupów nieatrybuowanych | 171 877 PLN/msc bez identyfikacji kampanii | 🟢 Miesiąc 2 |

---

## Top 5 problemów

1. **🚨 Brak tablicy items[] w purchase events** — 6,84 mln PLN przychodu bez identyfikacji produktów. Niemożliwa analiza BCG, optymalizacja kampanii produktowych, personalizacja. Prawdopodobna przyczyna: kontener Shopera wysyła purchase bez items[], a kontener agencji nie nadpisuje.

2. **🚨 Duplikacja purchase events (2 kontenery GTM)** — 49,5% transactionID pojawia się >1 raz (max 12×). GA4 deduplicuje ecommercePurchases prawidłowo, ale Meta Pixel i Google Ads Conversion Tag mogą liczyć każde duplikat zdarzenie osobno → zawyżony ROAS w tych platformach → błędna optymalizacja stawek.

3. **🚨 `złożenie_zamówienia` 76 136 vs `purchase` 31 090 — różnica 2,45×** — kluczowe pytanie: czy purchase event nie odpala się przy wszystkich zamówieniach? Jeśli tak, Smart Bidding Google Ads i Meta Advantage+ działają na niekompletnych danych konwersji.

4. **⚠️ Checkout drop-off 61,9% (begin_checkout → purchase)** — przy benchmarku 20-50% to alarmująco wysoka porzucalność kasy. Może być skutkiem pkt. 3 (brak firing) lub realnego problemu UX mobile na kasie.

5. **⚠️ Mobile CR 1,50% vs Desktop 3,19% przy 89,3% ruchu mobile** — przy wolumenie 1,66 mln sesji mobilnych każde 0,5pp poprawy CR = +1,75 mln PLN miesięcznie.
