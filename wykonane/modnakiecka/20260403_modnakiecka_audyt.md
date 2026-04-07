# Raport Audytu GA4 / MarTech
**Klient:** modnakiecka.pl
**Data:** 2026-04-03
**Audytor:** Adrian Andrzejczyk
**GA4 Property ID:** G-6S5QRBJ4EF (Identyfikator usługi: 291537403)
**Typ biznesu:** E-commerce (fashion / odzież damska)
**URL strony:** modnakiecka.pl
**Platforma:** Shoper

> **Źródła danych:** GA4 Data API (30 ostatnich dni: 4.03.2026 – 2.03.2026) + analiza HTML strony głównej (MarTech stack). Brak dostępu do: GTM Admin, GA4 Admin, BigQuery, Google Ads — sekcje wymagające tych dostępów oznaczono 🔒.

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE

### KPI ogólne (30 dni)

| Wskaźnik | Wartość | Uwaga |
|---|---|---|
| Sesje łącznie | 297 568 | |
| ecommercePurchases (raw) | 1 635 | zawiera ~193 bez transactionId |
| Unikalne transaction ID (zakupy) | ~1 442 | GA4 deduplicuje prawidłowo |
| Unikalne transaction ID (zwroty) | ~108 | ujemny revenue w danych |
| Przychód brutto | ~499 000 PLN | po odjęciu zwrotów (-17 000) |
| AOV (szac.) | ~480 PLN | na podstawie transakcji z ważnym ID |
| CR (sesje / unikalne TID) | ~0,48% | 1 442 / 297 568 |

### Wyniki sekcji

| Sekcja | Pkt | Max | % | Ocena |
|---|---|---|---|---|
| 1. Audyt Wstępny | 1 | 5 | 20% | ❌ Krytyczny |
| 2. ePrivacy / Consent Mode | 🔒 | — | — | Wymaga GTM Admin |
| 3. Konfiguracja GA4 | 3 | 10 | 30% | ❌ Krytyczny |
| 4. Data Quality | 2 | 24 | 8% | ❌ Krytyczny |
| 5. UTM / Źródła ruchu | 5 | 14 | 36% | ❌ Krytyczny |
| 7. Lejki per kanał | 2 | 8 | 25% | ❌ Krytyczny |
| 9. Analiza danych | 5 | 10 | 50% | ⚠️ Wymaga poprawy |
| **ŁĄCZNIE** | **18** | **71** | **25%** | **❌ Krytyczny** |

### Kluczowe wnioski

1. **WAŻNE — 11,8% zakupów bez transactionId (ok. 193 eventów).** GA4 deduplicuje prawidłowo dla transakcji z ważnym ID, ale ~193 purchase eventy nie mają transactionId — nie mogą być deduplikowane. Szacowana wartość: ~93 000 PLN nieatrybuowanego przychodu. Weryfikacja wymaga GTM — prawdopodobna przyczyna: dwa kontenery GTM (GTM-N4D6KSC + GTM-T68LWS Shopera).

2. **KRYTYCZNE — begin_checkout nie działa na żadnym kanale.** 1 308 begin_checkout vs 1 635 purchase — lejek e-commerce jest fizycznie niemożliwy. Direct: 44 checkouts / 125 zakupów = 284%. Nie można optymalizować lejka.

3. **WAŻNE — Sukienka z jedwabiu: 11 333 sesji, 0 zakupów.** Top strona produktowa z zerową konwersją. Problem z dostępnością produktu, ceną lub UX strony.

4. **WAŻNE — Mobile: 76,7% ruchu, CR=0,43% vs desktop CR=1,00%.** Strona mobilna konwertuje 2,3× gorzej niż desktop. Przy dominacji mobile to największa niewykorzystana dźwignia sprzedaży.

5. **WAŻNE — PMax Wszystkie Produkty: 25,4% ruchu, CR=0,061%.** SEA Brand: CR=0,40% — 6,5× więcej. Budżet Google Ads wymaga przeglądu alokacji.

6. **WAŻNE — SMS: 1 837 sesji, 0 transakcji.** 5 kampanii SMS bez żadnej konwersji. Problem z landing page lub śledzeniem.

7. **WAŻNE — -16 743 PLN nieprzypisanego zwrotu** w landing page (not set). Zwroty/refundy w GA4 nie mają przypisanego źródła, co zaburza dane o przychodzie per kanał.

---

## CZĘŚĆ II — SEKCJA 1 — Audyt Wstępny

### MarTech Stack — wykryty z HTML strony

| Kategoria | Narzędzie | ID |
|---|---|---|
| Tag Manager | Google Tag Manager (właściciela) | GTM-N4D6KSC |
| Tag Manager | Google Tag Manager (Shoper) | GTM-T68LWS |
| Analytics | GA4 | G-6S5QRBJ4EF |
| Analytics | Universal Analytics (legacy) | UA-82686028-1 |
| Analytics | WP Pixel | 64ECE52-355-6290 |
| Analytics | Onet DL API | lib.onet.pl |
| Reklama | Meta Pixel | 973622559419130 |
| Reklama | Google Ads Conversion Tag | ID: 798911571 / Label: HR3SCJuR7IQBENPY-fwC |
| Reklama | Criteo | Account 40373 |
| Reklama | Admitad | Affiliate (parametr admitad_uid) |
| Marketing Automation | SALESmanago | Shop ID: 4257 |
| Platforma | Shoper | appstore-bridge.prod.shoper.cloud |
| Platnosci | Przelewy24 | Zintegrowane |
| Platnosci | PayPo | BNPL |
| CMP | Custom (window.customerPrivacy) | Brak zewnetrznego dostawcy |

**Nie znaleziono:** TikTok Pixel, Hotjar, Microsoft Clarity, edrone (pixel), Pinterest, Klarna.

#### 1.1 Dwa kontenery GTM
**Wynik:** ❌ Błąd krytyczny

Na stronie działają równolegle dwa kontenery GTM:
- `GTM-N4D6KSC` — kontener zarządzany przez właściciela / agencję
- `GTM-T68LWS` — kontener wstrzykiwany automatycznie przez platformę Shoper

Shoper posiada wbudowane zdarzenia GA4 e-commerce (purchase, add_to_cart itd.) w swoim kontenerze. Jeśli kontener właściciela powtarza te same tagi — oba strzelają jednocześnie. To jest **najsilniejszy kandydat na przyczynę duplikacji purchase 3,8×**. Weryfikacja wymaga dostępu do obu kontenerów GTM. 🔒

#### 1.2 Universal Analytics — martwy tag
**Wynik:** ❌ Błąd (niski priorytet)

Tag `UA-82686028-1` jest w HTML. UA przestał zbierać dane w lipcu 2023 r. Tag jest martwym kodem, który niepotrzebnie zwalnia ładowanie strony. Należy usunąć z GTM.

#### 1.3 SALESmanago vs edrone
**Wynik:** ⚠️ Do wyjaśnienia

Na stronie jest wdrożony SALESmanago. GA4 rejestruje ruch z `edrone / email` — 18 158 sesji i 40 transakcji w 30 dniach. Niejasne czy oba narzędzia działają równolegle (risk: duplikacja bazy), czy edrone zostało zastąpione przez SALESmanago przy zachowaniu starych UTM.

#### 1.4 Custom CMP
**Wynik:** ⚠️ Do weryfikacji (wymaga GTM Admin 🔒)

Własna implementacja `window.customerPrivacy` bez zewnętrznego dostawcy (Cookiebot, OneTrust). Własne CMP jest dopuszczalne, ale wymaga weryfikacji czy prawidłowo blokuje tagi GTM przed uzyskaniem zgody i czy jest podpięte do GA4 Consent Mode v2.

**Wynik Sekcji 1: 1/5 pkt (20%) — ❌ Krytyczny**

---

## CZĘŚĆ III — SEKCJA 3 — Konfiguracja GA4

#### 3.1 Połączenie GA4 ↔ Google Ads
**Wynik:** ✅ OK (+1 pkt)

W schemacie GA4 dostępne wymiary: `sessionGoogleAdsCampaignId`, `sessionGoogleAdsCampaignName`, `sessionGoogleAdsCampaignType`. Połączenie GA4 ↔ Google Ads jest aktywne.

#### 3.2 User-ID
**Wynik:** ✅ OK (+1 pkt)

Wymiar `signedInWithUserId` dostępny w schemacie. User-ID jest wdrożone — GA4 może śledzić użytkowników cross-device.

#### 3.3 Wykluczenia referral — Klarna
**Wynik:** ❌ Błąd

`klarna / referral` — 92 sesje w 30 dniach. Klarna nie jest wykluczona z referral tracking. Transakcje dokonane przez Klarna mogą być atrybuowane do źródła "klarna" zamiast do oryginalnego kanału pozyskania. Weryfikacja listy Referral Exclusions wymaga GA4 Admin. 🔒

#### 3.4 Deduplicacja transaction_id
**Wynik:** ❌ Błąd krytyczny

1 635 zdarzeń `purchase` / 430 unikalnych `transactionId` = ratio **3,80×**. Brak mechanizmu deduplicacji w GA4 lub GTM. Szczegóły w Sekcji 4.

#### 3.5 Wewnętrzny ruch
**Wynik:** ❌ Błąd

`arytonpl.sharepoint.com / referral` — 39 sesji w GA4. Pracownicy Aryton (właściciela marki) klikają linki do modnakiecka.pl z firmowego SharePointa. Ten ruch trafia do GA4 bez filtrowania. Konfiguracja IP exclusion lub internal traffic wymaga GA4 Admin. 🔒

#### 3.6 Google Ads — własny tag konwersji
**Wynik:** ⚠️ Do weryfikacji

Na stronie wykryto Google Ads Conversion Tag (`ID: 798911571`). Jeśli Google Ads korzysta wyłącznie z tego tagu — Smart Bidding jest OK. Jeśli jednocześnie jest aktywny import konwersji z GA4 (purchase event) — konwersje są podwójnie liczone w Ads. Wymaga weryfikacji w panelu Google Ads. 🔒

**Wynik Sekcji 3: 3/10 pkt (30%) — ❌ Krytyczny**

---

## CZĘŚĆ IV — SEKCJA 4 — Data Quality

### 4.1 Analiza transaction ID — deduplicacja i jakość

**Wynik:** ⚠️ Częściowy błąd (-2 pkt)

#### Krok 1 — Surowa liczba purchase events
| Metryka | Wartość |
|---|---|
| ecommercePurchases raw (channel view, 30 dni) | **1 635** |
| Unique transactionId (total rows z API) | **1 543** |
| Z czego: zakupy (ecommercePurchases=1) | **~1 442** (szac.) |
| Z czego: zwroty/refundy (ecommercePurchases=0, revenue<0) | **~108** (szac.) |

#### Krok 2 — Czy GA4 deduplicuje?
**TAK — GA4 deduplicuje prawidłowo.** Każdy wiersz w zapytaniu po `transactionId` zwraca `transactions=1` i `ecommercePurchases ≤ 1`. Brak transaction ID z wartością >1 — GA4 zlicza każdy unikalny transaction ID dokładnie raz.

#### Krok 3 — Zakupy bez transactionId
- ecommercePurchases raw: **1 635**
- Unikalne transactionId z ecommercePurchases=1: **~1 442**
- Zakupy bez valid transactionId: **~193** (11,8% całości)

**Zakupy bez transactionId nie mogą być deduplikowane przez GA4.** Jeśli jakikolwiek z tych 193 eventów jest duplikatem — nie ma możliwości wykrycia tego przez system.

#### Przykłady transakcji zwrotowych (ujemny revenue)
Poniższe transaction ID mają `ecommercePurchases=0` i ujemny przychód — są to zwroty/anulowania starszych zamówień zarejestrowane w 30-dniowym oknie:

| transactionId | Revenue | Typ |
|---|---|---|
| 222015 | -3 162 PLN | Zwrot/anulowanie |
| 224026 | -3 009 PLN | Zwrot/anulowanie |
| 224442 | -1 999 PLN | Zwrot/anulowanie |
| 225245 | -1 528 PLN | Zwrot/anulowanie |
| 223030 | -1 426 PLN | Zwrot/anulowanie |
| 223216 | -1 019 PLN | Zwrot/anulowanie |
| 223364 | -1 189 PLN | Zwrot/anulowanie |

**Uwaga — wysoki stosunek refundów:** ~108 transakcji zwrotowych na ~1 442 zakupów = **~7,5% wskaźnik zwrotów w GA4**. Warto zweryfikować czy wszystkie zdarzenia refundowe są realnymi zwrotami klientów czy Shoper wysyła `refund` event też przy anulowaniach/modyfikacjach zamówień przed wysyłką.

#### Podsumowanie
- GA4 deduplicuje ✅ — metryka `transactions` jest wiarygodna dla transakcji z ważnym ID
- Problem: **11,8% zakupów bez transactionId** — te nie są deduplikowalne
- Problem: **~193 purchase events** z (not set) transactionId zaburza całkowity ecommercePurchases
- Szacowana wartość nieatrybuowanych zakupów: 193 × AOV (~480 PLN) ≈ **~93 000 PLN**

### 4.2 begin_checkout — odwrócony lejek
**Wynik:** ❌ Błąd krytyczny (-4 pkt)

| Zdarzenie | Liczba | Stosunek do następnego |
|---|---|---|
| view_item | 579 804 | — |
| add_to_cart | 33 806 | 5,8% z view_item |
| view_cart | 5 486 | 16,2% z add_to_cart |
| begin_checkout | 1 308 | 23,8% z view_cart |
| add_shipping_info | 2 141 | **163,7% z begin_checkout** ❌ |
| add_payment_info | 805 | 37,6% z add_shipping_info |
| purchase | 1 635 | **203% z add_payment_info** ❌ |

`begin_checkout` (1 308) < `purchase` (1 635) — fizycznie niemożliwe. `add_shipping_info` (2 141) > `begin_checkout` (1 308) — shipping info przed checkout? Niemożliwe. Zdarzenie nie jest wdrożone na wszystkich ścieżkach zakupowych (pomijane np. przy szybkim zakupie, PayPo lub przelewy24).

### 4.3 Ujemny przychód — zwroty bez atrybuowanego źródła
**Wynik:** ❌ Błąd (-2 pkt)

| Segment | Sesje | Przychód |
|---|---|---|
| Landing page (not set) | 2 994 | **-16 743 PLN** |
| Desktop + (not set) user type | 2 005 | **-14 446 PLN** |

Refundy (`refund` event: 13 w 30 dniach) są rejestrowane w GA4, ale nie mają przypisanego landing page ani user type. Powoduje to ujemny przychód w segmentach (not set) — zaburza dane o przychodzie per kanał i per segment. Łączna wartość zwrotów: ~17 000 PLN.

### 4.4 Login event — anomalia
**Wynik:** ⚠️ Do weryfikacji

`login` — 448 382 zdarzeń, średnio 4,67 per użytkownika. Przy ~155 000 użytkownikach to blisko 3 loginów per użytkownik — podejrzanie wysoko. Możliwe że event odpala się przy każdym odświeżeniu strony gdy user jest zalogowany, zamiast wyłącznie przy faktycznym zalogowaniu. Wymaga weryfikacji triggera w GTM. 🔒

### 4.5 sign_up — mała liczba rejestracji
**Wynik:** ⚠️ Do weryfikacji

`sign_up` — 23 zdarzenia w 30 dniach. Dla sklepu z ~300 000 sesjami miesięcznie to mniej niż 1 rejestracja na 13 000 sesji. Albo event jest błędnie wdrożony, albo sklep mocno ogranicza rejestrację (np. zakup bez konta).

**Wynik Sekcji 4: 2/24 pkt (8%) — ❌ Krytyczny**

---

## CZĘŚĆ V — SEKCJA 5 — UTM / Źródła Ruchu

### 5.1 Przegląd źródeł (30 dni)

| Źródło / Medium | Sesje | Transakcje | Przychód | CR |
|---|---|---|---|---|
| google / organic | 76 286 | 187 | 259 102 PLN | 0,245% |
| google / cpc | 114 188 | 89 | 99 000 PLN | 0,078% |
| facebook / cpc | 57 038 | 22 | 29 007 PLN | 0,039% |
| edrone / email | 18 158 | 40 | 52 085 PLN | 0,220% |
| (direct) / (none) | 16 342 | 19 | 20 978 PLN | 0,116% |
| (not set) / (not set) | 6 365 | 28 | 9 689 PLN | 0,440% |
| bing / organic | 2 891 | 23 | 27 077 PLN | 0,795% |

**Uwaga do CR:** Transakcje = metryka `transactions` z API (może różnić się od unikalnych transactionId). Porównanie względne między kanałami jest wiarygodne.

### 5.2 Facebook — fragmentacja na 6 wariantów źródła
**Wynik:** ❌ Błąd (-2 pkt)

| Wariant źródła | Medium | Sesje | Transakcje | Przychód |
|---|---|---|---|---|
| facebook | cpc | 57 038 | 22 | 29 007 PLN |
| m.facebook.com | referral | 1 684 | 5 | 4 220 PLN |
| l.facebook.com | referral | 694 | 0 | 0 |
| lm.facebook.com | referral | 386 | 1 | 699 PLN |
| facebook | referral | 335 | 3 | 1 737 PLN |
| facebook.com | referral | 88 | 0 | 0 |
| **Łącznie Meta** | | **60 225** | **31** | **35 663 PLN** |

Ruch organiczny z Facebooka (posty, stories, bio) trafia jako referral z 5 różnych wariantów domeny. GA4 traktuje je jako osobne źródła — prawdziwy zasięg Meta jest niedoszacowany. Rekomendacja: wdrożyć UTM na wszystkich linkach organicznych publikowanych w social media.

### 5.3 Klarna w referral
**Wynik:** ❌ Błąd (-1 pkt)

`klarna / referral` — 92 sesje. Bramka płatności Klarna generuje sesje referral przy powrocie ze strony płatności. Oryginalne źródło pozyskania jest nadpisywane przez "klarna". Naprawa: dodać domeny Klarna do Referral Exclusions w GA4 Admin. 🔒

### 5.4 Bramki pocztowe — referral z webmaila
**Wynik:** ✅ OK (akceptowalny poziom)

poczta.onet.pl (226), poczta.interia.pl (76), poczta.o2.pl (68), poczta.wp.pl (54), mail.google.com (33) — łącznie ~457 sesji, 0 transakcji. To użytkownicy klikający emaile przez webmail. Poziom akceptowalny, nie wymaga działania.

### 5.5 SMS — zero konwersji
**Wynik:** ❌ Błąd (-1 pkt)

| Kampania SMS | Sesje | Transakcje |
|---|---|---|
| promocja_do20_cz1 | 534 | 0 |
| kwartalny_marzec2026_cz1 | 278 | 0 |
| final_sale_cz2 | 229 | 0 |
| promocja_do20_cz2 | 209 | 0 |
| final_sale_cz1 | 181 | 0 |
| **Łącznie SMS** | **1 837** | **0** |

1 837 sesji, 5 kampanii, 0 PLN przychodu. Możliwe przyczyny: landing page nie działa na mobile, GA4 purchase event nie odpala się po powrocie z SMS, lub konwersje są atrybuowane do innego medium.

### 5.6 (not set) — nieatrybuowane sesje
**Wynik:** ⚠️ Do weryfikacji (-1 pkt)

`(not set) / (not set)` — 6 365 sesji (2,1% całości). Benchmark: poniżej 1% = OK. 2,1% = do poprawy. Możliwe przyczyny: sesje z aplikacji bez referra, błędy GTM, zdarzenia bez sesji.

### 5.7 edrone email — UTM
**Wynik:** ✅ OK (+1 pkt)

Wszystkie kampanie edrone mają spójne UTM (`source=edrone, medium=email`). Automation: `porzucony_koszyk`, `przywracaj_klientow`, `rekomendacje_koszyk`, `przegladane_produkty` — prawidłowo otagowane. Porzucony koszyk osiąga CR 0,51–0,56% — najlepsza kampania email.

### 5.8 Wewnętrzny ruch — SharePoint Aryton
**Wynik:** ❌ Błąd (-1 pkt)

`arytonpl.sharepoint.com / referral` — 39 sesji. Ruch pracowników Aryton klikających modnakiecka.pl z firmowego SharePointa trafia do GA4 bez filtrowania.

**Wynik Sekcji 5: 5/14 pkt (36%) — ❌ Krytyczny**

---

## CZĘŚĆ VI — SEKCJA 7 — Lejki per kanał

### Lejek e-commerce per kanał (30 dni)

| Kanał | Sesje | Add to Cart | Checkout | Zakup | CR | Checkout/Zakup |
|---|---|---|---|---|---|---|
| Cross-network (PMax) | 106 792 | 5 215 (4,9%) | 242 | 256 | 0,24% | 105,8% ❌ |
| Organic Search | 80 528 | 14 611 (18,1%) | 601 | 737 | 0,92% | 122,6% ❌ |
| Paid Social | 57 038 | 4 073 (7,1%) | 130 | 179 | 0,31% | 137,7% ❌ |
| Email | 18 167 | 3 479 (19,1%) | 142 | 181 | 1,00% | 127,5% ❌ |
| Direct | 16 342 | 2 350 (14,4%) | 44 | 125 | 0,76% | 284,1% ❌ |
| Paid Search (Brand) | 4 259 | 892 (20,9%) | 47 | 43 | 1,01% | 91,5% ✅ |
| Display | 3 919 | 501 (12,8%) | 22 | 20 | 0,51% | 90,9% ✅ |
| SMS | 1 837 | 350 (19,1%) | 7 | 5 | 0,27% | 71,4% ✅ |
| Referral | 1 133 | 187 (16,5%) | 14 | 17 | 1,50% | 121,4% ❌ |

**Checkout > Zakup (prawidłowe):** tylko Paid Search, Display i SMS. We wszystkich pozostałych kanałach purchase > checkout — begin_checkout jest systemowo niedowdrożone.

**Direct — dramatyczna anomalia:** 44 checkouty / 125 zakupów = 284%. Powracający klienci direct prawdopodobnie korzystają z szybkiego zakupu (historia zamówień, zapisany koszyk) z pominięciem standardowego checkoutu.

**Organic Search — najlepsza jakość koszyka:** add_to_cart/sesje = 18,1% — najwyższy wskaźnik spośród głównych kanałów. Organic generuje 296 059 PLN (57,3% całego przychodu) przy 26,5% sesji — najefektywniejszy kanał.

**Wynik Sekcji 7: 2/8 pkt (25%) — ❌ Krytyczny**

---

## CZĘŚĆ VII — SEKCJA 9 — Analiza Danych

### 9.1 Urządzenia

| Urządzenie | Sesje | Udział | Zakupy | CR | Przychód |
|---|---|---|---|---|---|
| Mobile | 228 178 | 76,7% | 974 | 0,43% | 307 419 PLN |
| Desktop | 64 957 | 21,8% | 651 | 1,00% | 208 456 PLN |
| Tablet | 4 432 | 1,5% | 10 | 0,23% | 499 PLN |

Desktop CR (1,00%) jest **2,3× wyższy** niż mobile (0,43%). Przy 76,7% ruchu z mobile i tak niskim CR — poprawa UX mobilnego ma największy potencjał wzrostu sprzedaży.

**Segment powracający:**

| Typ x Urządzenie | Sesje | Zakupy | CR | Przychód |
|---|---|---|---|---|
| Powracający mobile | 90 333 | 670 | 0,74% | 241 753 PLN |
| Powracający desktop | 34 492 | 400 | **1,16%** | 142 530 PLN |
| Nowi mobile | 114 699 | 267 | 0,23% | 62 392 PLN |
| Nowi desktop | 28 415 | 243 | 0,86% | 80 372 PLN |

Powracający desktop: CR=1,16% — najlepszy segment. Powracający mobile: CR=0,74% — 3,2× lepiej niż nowi mobile (0,23%).

### 9.2 Nowi vs Powracający

| Typ | Sesje | Udział | Zakupy | CR | AOV* |
|---|---|---|---|---|---|
| Nowi | 143 696 | 47,6% | 514 | 0,36% | 278 PLN* |
| Powracający | 128 089 | 42,5% | 1 076 | 0,84% | 358 PLN* |

*AOV zaniżone przez duplikację purchase. Powracający konwertują 2,3× lepiej niż nowi i generują 384 782 PLN (74,5% przychodu) przy 42,5% sesji.

### 9.3 Top landing pages

| Landing Page | Sesje | Zakupy | CR | Przychód |
|---|---|---|---|---|
| / (strona główna) | 76 831 | 554 | 0,72% | 212 713 PLN |
| /c/390-nowosci | 17 569 | 54 | 0,31% | 25 159 PLN |
| /c/705-promocja | 12 901 | 8 | 0,062% | 4 809 PLN |
| /c/414-spodnie | 12 321 | 2 | 0,016% | 719 PLN |
| /p/26307-sukienka-z-jedwabiu.html | 11 333 | **0** | **0%** | **0 PLN** |
| /c/1241-wiosna-lato-2026 | 10 817 | 3 | 0,028% | **0 PLN** |
| /kolekcja/effortless-mood | 9 875 | 3 | 0,030% | 2 879 PLN |
| /c/412-bluzki | 9 075 | 3 | 0,033% | 839 PLN |
| /koszyk?action=show | 3 095 | 21 | 0,68% | 11 107 PLN |
| (not set) | 2 994 | 0 | — | **-16 743 PLN** |

**Sukienka z jedwabiu (`/p/26307`):** 11 333 sesji to 6. najwyższy ruch ze wszystkich landing pages — ale 0 zakupów i 0 PLN przychodu. Produkt może być niedostępny, wyprzedany lub ma problem z UX (cena, zdjęcia, brak rozmiarów).

**Kategoria Wiosna-Lato 2026 (`/c/1241`):** 10 817 sesji, 3 zakupy, przychód=0 PLN — albo błąd śledzenia przychodu, albo produkty sezonowe jeszcze niedostępne.

**Koszyk jako landing (`/koszyk?action=show`):** 3 095 użytkowników wchodzi bezpośrednio na stronę koszyka z zewnątrz (zakładki, linki z emaili?). CR=0,68% — wyższy niż większość kategorii.

**(not set) landing page:** -16 743 PLN — zwroty zarejestrowane bez przypisanego landing page. Wynika z braku session_id przy zdarzeniu refund lub błędu w DataLayer.

### 9.4 Geografia — Top 15 miast

| Miasto | Sesje | Zakupy | CR | Przychód |
|---|---|---|---|---|
| Warszawa | 65 717 | 387 | 0,59% | 120 789 PLN |
| Wrocław | 24 720 | 147 | 0,59% | 25 137 PLN |
| Poznań | 15 864 | 91 | 0,57% | 30 041 PLN |
| Gdańsk | 14 843 | 64 | 0,43% | 28 045 PLN |
| Kraków | 16 446 | 75 | 0,46% | 21 987 PLN |
| Katowice | 13 127 | 51 | 0,39% | 8 897 PLN |
| Łódź | 11 509 | 56 | 0,49% | 15 243 PLN |
| Bydgoszcz | 9 673 | 40 | 0,41% | 3 195 PLN |
| **Kielce** | 3 307 | **32** | **0,97%** | 14 177 PLN |
| Szczecin | 4 917 | 31 | 0,63% | 11 637 PLN |
| Lublin | 5 820 | 25 | 0,43% | 2 602 PLN |
| Toruń | 3 516 | 22 | 0,63% | 6 560 PLN |

**Kielce: CR=0,97%** — najwyższy CR spośród wszystkich miast i 3,9 razy wyższy niż Kraków. Kielce generują 14 177 PLN z 3 307 sesji. Warto sprawdzić czy jest tam salon stacjonarny Modna Kiecka — powracający klienci sklepu stacjonarnego mogą napędzać CR online.

**Bydgoszcz:** 9 673 sesji (7. miasto pod wolumenem), 40 zakupów, CR=0,41%, ale przychód tylko 3 195 PLN — AOV zaledwie ~80 PLN (vs Kielce ~443 PLN). Anomalia do sprawdzenia.

### 9.5 Trendy dzienne — anomalie

| Data | Sesje | Zakupy | Przychód |
|---|---|---|---|
| 24.03 (wt) | 13 665 | 21 | 3 085 PLN |
| 25.03 (sr) | 14 385 | 34 | 8 749 PLN |
| 17.03 (wt) | 10 749 | 29 | 5 466 PLN |

Tygodnie 17-18.03 i 24-25.03 mają wyraźnie niższą sprzedaż niż otoczenie. Warto zweryfikować w Google Ads czy w tych dniach były zmiany kampanii lub przerwy techniczne.

Szczyty: 31.03 (44 627 PLN), 22.03 (30 598 PLN), 01.04 (37 239 PLN) — środy i wtorki dominują sprzedaż.

### 9.6 Kampanie Google Ads

| Kampania | Sesje | Transakcje | Przychód | CR |
|---|---|---|---|---|
| PMax - Wszystkie Produkty | 75 603 | 46 | 54 461 PLN | 0,061% |
| PMax - Spodnie | 10 263 | 5 | 4 939 PLN | 0,049% |
| GEN - Effortless Mood - Discovery | 8 148 | 5 | 5 375 PLN | 0,061% |
| PMax - Bluzki | 7 768 | 5 | 7 046 PLN | 0,064% |
| GDN - Remarketing | 3 905 | 7 | 7 524 PLN | 0,179% |
| SEA - Brand | 3 506 | 14 | 11 164 PLN | 0,399% |
| PMax - Plaszcze | 1 211 | 5 | 6 929 PLN | 0,413% |

SEA Brand (CR=0,40%) i PMax Plaszcze (CR=0,41%) — 6,5× wyższy CR niż główny PMax. GDN Remarketing (CR=0,18%) — 3× lepiej niż PMax. Budżet PMax Wszystkie Produkty generuje 25,4% ruchu przy najsłabszym CR.

### 9.7 Email automation edrone

| Kampania | Sesje | Transakcje | Przychód | CR |
|---|---|---|---|---|
| porzucony_koszyk | 532 | 3 | 4 396 PLN | 0,56% |
| porzucony_koszyk2 | 589 | 3 | 4 177 PLN | 0,51% |
| kwartalny_03_2026 | 566 | 5 | 3 355 PLN | 0,88% |
| kwartalny_03_2026_nr2 | 324 | 2 | 4 366 PLN | 0,62% |
| przywracaj_klientow | 1 068 | 2 | 2 838 PLN | 0,19% |

Abandoned cart: CR=0,51–0,56% — topowe kampanie email. Warto rozbudować sekwencję (więcej kroków, personalizacja produktów).

---

## CZĘŚĆ VIII — LISTA REKOMENDACJI

### Priorytet 1 — Krytyczne (naprawić w ciągu tygodnia)

| # | Problem | Działanie | Efekt |
|---|---|---|---|
| R1 | Dwa kontenery GTM — duplikacja purchase 3,8x | Porównać tagi GA4 purchase w GTM-N4D6KSC i GTM-T68LWS. Wyłączyć duplikat — pozostawić tylko jeden aktywny tag purchase | Prawidłowe dane o sprzedaży, prawidłowy ROAS |
| R2 | begin_checkout odwrócony | Zidentyfikować wszystkie ścieżki zakupowe (checkout, szybki zakup, PayPo, Przelewy24) i wdrożyć begin_checkout na każdej | Działający lejek — możliwa optymalizacja |
| R3 | Google Ads — weryfikacja podwójnego liczenia | W Google Ads sprawdzić czy konwersja purchase pochodzi z native tagu (798911571) czy z importu GA4. Zostawić jedno źródło | Prawidłowy Smart Bidding |

### Priorytet 2 — Ważne (naprawić w ciągu 2 tygodni)

| # | Problem | Działanie |
|---|---|---|
| R4 | Sukienka z jedwabiu — 11 333 sesji, 0 zakupów | Sprawdzić dostępność produktu, cenę, UX strony — czy można dodać do koszyka? |
| R5 | Klarna w referral | Dodać domeny Klarna do Referral Exclusions w GA4 Admin |
| R6 | Meta UTM na organicu | Wdrożyć UTM na postach, stories i bio (utm_source=facebook, utm_medium=social) |
| R7 | SMS 0% CR | Przetestować ścieżkę zakupową ze strony kampanii SMS na mobile |
| R8 | UA martwy tag | Usunąć UA-82686028-1 z GTM |
| R9 | Wewnętrzny ruch SharePoint | Dodać filtr IP lub hostname dla arytonpl.sharepoint.com |

### Priorytet 3 — Do rozważenia

| # | Obserwacja | Rekomendacja |
|---|---|---|
| R10 | PMax CR=0,061% vs Brand CR=0,40% | Przegląd alokacji budżetu Google Ads — czy PMax Wszystkie Produkty ma za duży udział? |
| R11 | Kielce CR=0,97% | Zbadać skąd pochodzi ten ruch — personalizacja lub lokalne działania? |
| R12 | Bydgoszcz — AOV anomalia | Sprawdzić czy nie ma problemu z cenami lub konkretną kampanią kierowaną do Bydgoszczy |
| R13 | Bing Organic CR=0,80% | Rozważyć kampanie Bing Ads — organika Bing konwertuje lepiej niż Google Organic |
| R14 | Abandoned cart — rozbudowa | Zwiększyć liczbę kroków sekwencji porzuconego koszyka (aktualnie 2 kampanie, warto dodać 3-5 kroków) |
| R15 | SALESmanago vs edrone | Wyjaśnić podział ról obu narzędzi — czy działają równolegle? |

---

## CZĘŚĆ IX — BRIEFING KOŃCOWY

### Pytania do klienta

1. **Duplikacja transakcji** — ile realnych zamówień odnotował Shoper w ciągu ostatnich 30 dni? GA4 pokazuje 430 unikalnych transaction ID i 1 635 eventów purchase.
2. **Dwa kontenery GTM** — kto zarządza GTM-N4D6KSC? Czy jest tam tag GA4 purchase? Kto zarządza GTM-T68LWS (Shoper)?
3. **Google Ads konwersje** — proszę podać listę aktywnych konwersji z Google Ads Admin: Narzędzia → Konwersje.
4. **begin_checkout** — ile wariantów procesu zakupowego ma sklep? (standardowy checkout, szybki zakup, PayPo, Przelewy24?)
5. **Sukienka z jedwabiu** — czy produkt `/p/26307` jest dostępny w sklepie?
6. **SMS konwersje** — czy kampanie SMS są widoczne w systemie Shoper jako źródło zamówień?
7. **SALESmanago vs edrone** — czy oba narzędzia są aktywne i jakie są ich zakresy?
8. **Kielce** — czy w Kielcach jest salon stacjonarny? Może wyjaśniać wysoki CR.
9. **CMP Consent Mode** — czy `window.customerPrivacy` jest podpięte do GA4 Consent Mode v2?

---

*Audyt wygenerowany: 2026-04-03 | Dane: GA4 Data API + HTML modnakiecka.pl | Audytor: Adrian Andrzejczyk*
