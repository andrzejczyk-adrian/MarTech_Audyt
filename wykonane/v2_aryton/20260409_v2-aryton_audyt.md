# Raport Audytu MarTech v2 — Patrizia by Aryton

**Data:** 2026-04-09
**Audytor:** Adrian Andrzejczyk
**GA4 Property:** patrizia.aryton.pl — G-93NK3C48R3 (ID: 326801658)
**GTM Container:** GTM-MDGSP8
**Google Ads:** 196-867-6668
**BigQuery:** dane-z-ga4-aryton-pl
**URL:** https://patrizia.aryton.pl/
**Platforma:** PrestaShop (potwierdzone z URL wzorców i struktury serwera)
**Typ biznesu:** E-commerce (odzież i akcesoria premium)
**CMP:** Cookiebot
**Okres bieżący:** 9 marca – 8 kwietnia 2026
**Okres porównawczy (YoY):** 10 marca – 9 kwietnia 2025

> **Uwaga v2:** Niniejszy raport jest korektą audytu z 2026-04-07 (v1), który zawierał błędne konkluzje:
> - v1 błędnie podał platformę jako "Shoper" → faktycznie PrestaShop
> - v1 błędnie stwierdził "duplikaty transaction_id" → faktycznie malformed IDs (inna natura)
> - v1 błędnie stwierdził "itemRevenue = 0 dla wszystkich produktów" → faktycznie 100 produktów ma dane

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE

### Wyniki sekcji

| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | 10 | 36 | 28% | ❌ Krytyczny |
| 2. ePrivacy / Consent Mode | 1 | 45 | 2% | ❌ Krytyczny |
| 3. Konfiguracja GA4/GTM | 15 | 93 | 16% | ❌ Krytyczny |
| 4. Data Quality | 30 | 75 | 40% | ❌ Krytyczny |
| 5. UTM | 9 | 18 | 50% | ⚠️ Wymaga poprawy |
| 6. BCG | 0 | 12 | 0% | 🔒 Brak dostępu Ads |
| 7. Lejki zakupowe | 2 | 8 | 25% | ❌ Krytyczny |
| 8. GA4 ↔ Google Ads | 3 | 27 | 11% | 🔒 Brak dostępu Ads |
| 9. Analiza danych | 4 | 24 | 17% | ❌ Krytyczny |
| 10. Google Ads | 0 | 81 | 0% | 🔒 Brak dostępu |
| **ŁĄCZNIE (bez sek. 10)** | **74** | **338** | **22%** | **❌ Krytyczny** |

---

### Wyniki rok do roku — ALARMUJĄCE

| Metryka | Kwi 2026 | Kwi 2025 | Zmiana |
|---------|---------|---------|-------|
| Sesje | 330 296 | 438 646 | -24.7% |
| **Transakcje** | **427** | **1 495** | **-71.4%** |
| **Przychód** | **529 914 PLN** | **1 856 701 PLN** | **-71.5%** |
| AOV (wartość zamówienia) | 1 241 PLN | 1 242 PLN | ≈0% |
| CR (konwersja) | 0.129% | 0.341% | -62% |

**Kluczowe spostrzeżenie:** Wartość średniego zamówienia (AOV) jest niemal identyczna rok do roku — to oznacza, że problem NIE LEŻY w cenach, kolekcji ani wartości produktu. Problem jest w liczbie kupujących, a dokładniej: w liczbie użytkowników, którzy docierają do sklepu i w tym, jak skutecznie strona i reklamy ich konwertują.

---

### Jakość danych — CZY DANYM MOŻNA UFAĆ?

**Tak — dane o transakcjach i przychodzie są wiarygodne, ale dane o liczbie "eventów zakupu" są zaburzone.**

GA4 posiada mechanizm deduplicacji — każde zamówienie ze swoim unikalnym numerem jest liczone dokładnie raz w metryce `transactions`. Ta liczba (427 w bieżącym miesiącu) jest prawdziwa.

Jednak istnieje równoległy problem techniczny: system śledzi też 1 105 "fałszywych" eventów zakupu z błędnymi numerami zamówień oraz 89 eventów bez żadnego numeru. Łącznie daje to 1 610 eventów zamiast 427 — ratio 3.77×. To nie są duplikaty (każdy numer jest inny), ale błędne zdarzenia bez rzeczywistych zakupów. Ich wpływ na licznik prawdziwych transakcji = zero. Ale mają destrukcyjny wpływ na kampanie Google Ads.

| Obszar | Wiarygodność | Uzasadnienie |
|--------|------------|-------------|
| Liczba zamówień (`transactions`) | ✅ Wiarygodna | GA4 deduplicuje po transaction_id; 427 to prawdziwa liczba |
| Przychód (`purchaseRevenue`) | ✅ Wiarygodna | 529 914 PLN pochodzi wyłącznie z 427 prawdziwych zamówień |
| Dane produktowe (`itemRevenue`) | ✅ Dostępne | 100 produktów z danymi przychodowymi |
| `ecommercePurchases` raw | ❌ Zaburzone | 1 610 eventów (3.77×) — obejmuje 1 183 błędne zdarzenia |
| CR lejka (checkout→purchase) | ⚠️ Niedokładny | begin_checkout (~1 296) wymaga weryfikacji DevTools |
| Kampanie w Google Ads | ❌ Błędnie zoptymalizowane | Smart Bidding "widzi" 3.77× za dużo konwersji |

---

### Kluczowe wnioski — Top 5 problemów

**1. 🔴 Sprzedaż spadła o 71% rok do roku — utrata ~1.33M PLN/miesiąc**
W marcu-kwietniu 2025 sklep generował 1 495 zamówień miesięcznie za 1 856 701 PLN. W marcu-kwietniu 2026 — 427 zamówień za 529 914 PLN. Utracono 1 068 transakcji i 1 326 787 PLN przychodu miesięcznie. Przyczyny są wielorakie i zidentyfikowane.

**2. 🔴 Malformed transaction IDs — 1 105 konkretnych błędnych ID**
System tworzy podwójne zdarzenia zakupu: jedno z prawidłowym numerem zamówienia (np. `210034`) i drugie z błędnym (`210034&key=1abe2783234b4109f15a80bdd3246c14`). Drugie zdarzenie nie jest prawdziwym zakupem — nie ma revenue, nie jest liczone jako transakcja przez GA4. Jednak zasila metrykę `ecommercePurchases`, którą Google Ads używa do optymalizacji. Algorytm PMax "myśli", że kampanie są 3.77× bardziej skuteczne niż są, i na tej podstawie podejmuje błędne decyzje.

**3. 🔴 Kampanie Google Search praktycznie nieaktywne (-92% sesji)**
Rok temu kampanie Search przynosiły 58 884 sesji miesięcznie. Dziś — 4 600. CR pozostał identyczny (0.29–0.30%), co oznacza że jakość tych kampanii była dobra. Brak sesji = brak budżetu lub wyłączone kampanie. Szacowana strata: ~190 000–215 000 PLN przychodów miesięcznie.

**4. 🔴 Konwersja na telefonach spadła o 67% rok do roku**
Mobile stanowi 78% ruchu (260 tys. sesji/msc). W 2025 CR mobile wynosił 0.288% — dziś 0.095%. Każda sesja mobilna jest teraz 3× mniej opłacalna niż rok temu. Desktop też spadł (-41%), ale znacznie mniej. Wskazuje to na pogorszenie doświadczenia na telefonach — prawdopodobnie po aktualizacji szablonu lub PrestaShop.

**5. 🟡 PMax generuje więcej ruchu ale 4× mniej efektywny**
Kampanie PMax (Cross-network) przynoszą 63% więcej sesji (+53 417 sesji/msc) ale 62% mniej transakcji (-116 trans/msc). CR z 0.221% (2025) spadł do 0.051% (2026). Kampanie "rosną" ale nie konwertują — algorytm optymalizuje na błędne sygnały konwersji.

---

## CZĘŚĆ II — OMÓWIENIE SZCZEGÓŁOWE

---

## SEKCJA 1 — Audyt wstępny infrastruktury

*Audyt wstępny sprawdza czy "maszyna" śledzenia działa poprawnie. Szczególnie ważne jest to, żeby kod śledzący uruchamiał się dokładnie raz, we właściwej kolejności, na właściwych stronach. Każde odstępstwo powoduje błędne dane, na których biznes podejmuje błędne decyzje.*

**Wynik: 10/36 pkt (28%) — ❌**

---

### Hardcoded snippet GA4 w PrestaShop

Platforma PrestaShop oferuje własny moduł Google Analytics, który wstrzykuje kod śledzący bezpośrednio do szablonu HTML — niezależnie od GTM. Gdy jednocześnie aktywny jest GTM z tagiem GA4, każde zdarzenie na stronie wysyłane jest DWUKROTNIE.

Dane GA4 potwierdzają ten problem w 2026:

| Kategoria | Eventy | Trans | Revenue |
|-----------|--------|-------|---------|
| Prawidłowe (GTM DataLayer) | 427 | 427 | 529 914 PLN |
| Malformed (PrestaShop/URL) | 1 105 | 0 | 0 PLN |
| Bez ID (hardcoded gtag) | 89 | 0 | 0 PLN |

W 2025 ten problem NIE ISTNIAŁ — ratio ePurchases:transactions = 1.013 (prawie 1:1). Pojawił się w 2026, co wskazuje na zmianę konfiguracji strony lub aktualizację PrestaShop.

**Rekomendacja:** W panelu PrestaShop → Ustawienia → Integracje → Google Analytics → wyłączyć wbudowaną integrację. Śledzenie GA4 powinno działać WYŁĄCZNIE przez GTM.

---

### DataLayer — poprawność

DataLayer dla 427 prawidłowych transakcji działa poprawnie. Produkty mają dane:
- TOP bestseller: "Camelowy płaszcz teddy bear z wełną" (ID: 26271) — 8 zakupów, 27 992 PLN
- "Brązowa kurtka ze skóry zamszowej" (ID: 26420) — 6 zakupów, 23 994 PLN
- "Czarna kurtka bomberka z jedwabiem" (ID: 26325) — 9 zakupów, 20 691 PLN

Dane produktowe są dostępne i poprawne dla 100 produktów.

---

### Malformed transaction_id — mechanizm błędu

PrestaShop strona potwierdzenia zamówienia ma URL:
```
/order-confirmation?id=210034&key=1abe2783234b4109f15a80bdd3246c14
```

- **GTM DataLayer** odczytuje poprawnie: transaction_id = `210034` ✅
- **Drugi tag/snippet** (prawdopodobnie w GTM lub hardcoded) odczytuje ze zmiennej URL: transaction_id = `210034&key=1abe2783234b4109f15a80bdd3246c14` ❌

Konkretne przykłady z GA4 (30d):
```
210032&key=1abe2783234b4109f15a80bdd3246c14  → ePurch=1, trans=0, rev=0
210033&key=1abe2783234b4109f15a80bdd3246c14  → ePurch=1, trans=0, rev=0
210034&key=1abe2783234b4109f15a80bdd3246c14  → ePurch=1, trans=0, rev=0
210035&key=1abe2783234b4109f15a80bdd3246c14  → ePurch=1, trans=0, rev=0
(... 1101 kolejnych malformed IDs ...)
```

Jednocześnie prawidłowe zdarzenie:
```
210034  → ePurch=1, trans=1, rev=2069.00 PLN ✅
```

**Rekomendacja:** W GTM → zidentyfikować zmienną, która odczytuje transaction_id z URL → zmienić na `Page URL Query Parameter` z parametrem `id` BEZ capture group (lub z regex `^([^&]+)` żeby obciąć wszystko po `&`). Alternatywnie — upewnić się, że transaction_id pochodzi WYŁĄCZNIE z DataLayer.

---

## SEKCJA 2 — ePrivacy / Consent Mode

*Consent Mode to mechanizm Google, który pozwala na częściowe śledzenie nawet gdy użytkownik odmówił cookies — przez anonimowe pingi. Bez prawidłowej implementacji traci się zarówno dane jak i możliwość optymalizacji kampanii Smart Bidding.*

**Wynik: ~1/45 pkt (2%) — ❌ (wymaga weryfikacji DevTools)**

Cookiebot jest wdrożony. Jednak (not set)/(not set) = 10 502 sesji (3.18%) i 30 transakcji (7.0% = ~13 675 PLN) bez atrybuacji wskazują na niekompletną implementację. Pełna weryfikacja wymaga testu w incognito z DevTools.

**url_passthrough** — prawdopodobnie nieskonfigurowane (30 trans/msc bez atrybuacji = ~13 675 PLN tracone co miesiąc).

---

## SEKCJA 3 — Konfiguracja GTM i GA4

**Wynik: 15/93 pkt (16%) — ❌**

### Ruch deweloperski w produkcyjnym GA4

Serwery deweloperskie Aryton rejestrują sesje w produkcyjnym GA4:

| Hostname | Sesje | Transakcje |
|----------|-------|------------|
| dev18.arytondev.pl | 26 | 1 (!) |
| dev18.arytondev.local | 14 | 0 |
| aryton81.local | 7 | 0 |

1 transakcja testowa z serwera deweloperskiego trafiła do danych produkcyjnych — zaburza dane o przychodzie.

**Rekomendacja:** GA4 → Admin → Filtry danych → dodać filtr wykluczający hostname zawierający `arytondev` i `aryton81`.

### Referral exclusion — braki

Niezwykluczone z referral:
- `klarna` (55 sesji) — bramka płatności BNPL
- `poczta.onet.pl` (191 sesji), `poczta.interia.pl` (88), `poczta.o2.pl` (83) — webmaile

Użytkownicy wracający z Klarna po autoryzacji płatności są traktowani jako nowa sesja z referral=klarna zamiast kontynuować sesję oryginalną.

**Rekomendacja:** GA4 → Strumień → Referral exclusion → dodać: `klarna.com`, `wp.pl`, `onet.pl`, `o2.pl`, `interia.pl`.

### Połączenia — poprawne

- ✅ Google Ads połączone z GA4
- ✅ BigQuery eksport aktywny (`dane-z-ga4-aryton-pl`)
- ✅ Model atrybucji Data-Driven

---

## SEKCJA 4 — Jakość danych

**Wynik: 30/75 pkt (40%) — ❌**

### Ratio ecommercePurchases:transactions = 3.77×

**KOREKTA v1**: Problem NIE jest spowodowany zduplikowanymi transaction_id. Każde ID jest unikalne. Prawdziwa przyczyna:

1. **1 105 malformed IDs** (np. `210034&key=1abe2783...`) — tag odczytuje URL zamiast DataLayer
2. **89 eventów z (not set)** — hardcoded gtag bez DataLayer
3. **2 eventy z pustym ID** — błąd konfiguracji

Łącznie 1 196 błędnych eventów purchase influje `ecommercePurchases` do 1 610, podczas gdy prawdziwych transakcji jest 427.

**Kluczowa różnica YoY:** W 2025 ratio = 1.013 (normalne). Problem pojawił się w 2026. Oznacza to, że Google Ads Smart Bidding przez ostatnie miesiące "uczył się" na fałszywych sygnałach.

### Anomalia lejka

```
view_item:          ~590 000
add_to_cart:          32 653
begin_checkout:        ~1 296
add_shipping_info:     ~2 132  ← ANOMALIA (> begin_checkout — niemożliwe)
add_payment_info:        ~806
purchase (raw):         1 610
purchase (real):          427
```

`add_shipping_info` > `begin_checkout` wskazuje na błąd w kolejności triggerów — prawdopodobnie event `add_shipping_info` odpala się na wcześniejszym etapie checkout w PrestaShop niż `begin_checkout`. Wymaga przeglądu konfiguracji GTM.

### Produkty — dane dostępne ✅

TOP 10 produktów wg przychodu (30d):

| Produkt | Zakupów | Przychód |
|---------|---------|---------|
| Camelowy płaszcz teddy bear z wełną (26271) | 8 | 27 992 PLN |
| Brązowa kurtka ze skóry zamszowej (26420) | 6 | 23 994 PLN |
| Czarna kurtka bomberka z jedwabiem (26325) | 9 | 20 691 PLN |
| Długi bawełniany trencz beżowy (22390) | 11 | 18 469 PLN |
| Beżowa dwurzędowa kurtka z wełny (26204) | 14 | 17 486 PLN |

---

## SEKCJA 5 — UTM

**Wynik: 9/18 pkt (50%) — ⚠️**

Google Ads (google/cpc) i Email (edrone/email) prawidłowo oznaczone. Problemy:
- Meta fragmentation: 7 wariantów (~63 738 sesji) — zaniża mierzony ROAS Meta
- SMS: 0 transakcji z 1 708 sesji (vs 8 transakcji w 2025)

---

## SEKCJA 7 — Lejki zakupowe

**Wynik: 2/8 pkt (25%) — ❌**

### CR google/cpc vs google/organic (YoY)

| Metryka | google/cpc | google/organic | Ratio |
|---------|-----------|---------------|-------|
| Sesje | 142 854 | 75 838 | — |
| Trans | 90 | 173 | — |
| CR | 0.063% | 0.228% | **27.6%** |

Kampanie CPC mają CR 4× niższy niż organic. Przy prawidłowym CR (50% organic = 0.114%) z 142 854 sesji byłoby ~163 transakcji zamiast 90 = **+73 transakcje/msc × 1 241 PLN = ~91 000 PLN/msc**.

### Checkout drop-off: 67.1%

Ze ~1 296 checkout beginners tylko 427 finalizuje zakup. Drop-off: 67.1%.

Rev/sesja per kanał:

| Kanał | Rev/sesja | Komentarz |
|-------|-----------|---------|
| **Bing organic** | **10.51 PLN** | 2 859 sesji — bardzo niedoinwestowany! |
| Organic Search | 3.48 PLN | — |
| Email (edrone) | 2.59 PLN | — |
| Paid Search | 2.42 PLN | — |
| Direct | 1.21 PLN | — |
| Paid Social (Meta) | 1.10 PLN | — |
| Cross-network (PMax) | 0.54 PLN | Najgorszy Rev/sesja |

**Bing organic**: 26 transakcji, 30 063 PLN z zaledwie 2 859 sesji = najwyższy Rev/sesja na koncie (10.51 PLN). Przy 10× wolumenie = ~300 000 PLN/msc z kampanii Microsoft Ads.

---

## SEKCJA 9 — Analiza danych

**Wynik: 4/24 pkt (17%) — ❌**

### Mobile vs Desktop (YoY)

| | Mobile 2026 | Mobile 2025 | Desktop 2026 | Desktop 2025 |
|---|------------|------------|-------------|-------------|
| Sesje | 259 439 | 318 860 | 65 243 | 120 419 |
| Trans | 246 | 919 | 180 | 561 |
| CR | **0.095%** | **0.288%** | **0.276%** | **0.466%** |
| CR delta | **-67%** | — | **-41%** | — |

Mobile stracił znacznie więcej CR niż desktop (-67% vs -41%). Oznacza to problem specyficzny dla mobile — zmiana szablonu, wolniejsze ładowanie na 4G, lub problemy z procesem checkout na małym ekranie.

**Potencjał mobile** (gdyby CR mobile = 50% desktop = 0.138%):
```
Dodatkowe transakcje = (0.138% - 0.095%) × 259 439 = +112 trans/msc
Dodatkowy przychód = 112 × 1 241 PLN = ~139 000 PLN/msc
```

### Anomalia 2026-04-04

Data | Sesje | Transakcje
2026-04-04 | 9 564 | **0** ← AWARIA

9 564 użytkowników odwiedziło sklep bez ŻADNEJ transakcji. To niemal 3× normalny wolumen dzienny. Możliwa awaria bramki płatności lub systemu checkout.

---

## SEKCJA 11 — ANALIZA SPADKU SPRZEDAŻY YoY

*Sekcja stworzona na życzenie — głęboka analiza przyczyn spadku transakcji o 71.4% rok do roku.*

### Skala problemu

```
Kwiecień 2025: 1 495 transakcji → 1 856 701 PLN
Kwiecień 2026:   427 transakcji →   529 914 PLN
               ————————————————————————————
Delta:         -1 068 transakcji → -1 326 787 PLN/msc
```

**Sprzedaż spadła o 71.4% przy AOV niemal identycznym (1 241 vs 1 242 PLN)** — problem nie jest w produktach, cenie ani wartości zamówień.

### Analiza kanałów (YoY) — co się zmieniło

**Paid Search: -92% wolumenu, CR NIEZMIENIONY**

| | 2026 | 2025 | Delta |
|---|------|------|-------|
| Sesje | 4 600 | 58 884 | **-92%** |
| Transakcje | 14 | 171 | -92% |
| CR | 0.304% | 0.290% | +5% |

CR Paid Search jest TAKI SAM (0.30%). Oznacza to że kampanie Search DZIAŁAŁY dobrze — problem jest wyłącznie w skali (budżet/liczba kampanii). Przy CR 0.30% i 58 884 sesjach (jak w 2025) byłoby ~176 transakcji/msc zamiast 14. Strata = 162 trans × 1 241 PLN = **~201 000 PLN/msc**.

**Cross-network (PMax): +63% sesji, CR -77%**

| | 2026 | 2025 | Delta |
|---|------|------|-------|
| Sesje | 137 557 | 84 140 | +63% |
| Transakcje | 70 | 186 | -62% |
| CR | 0.051% | 0.221% | **-77%** |

PMax dostał więcej budżetu (sesje +63%) ale konwertuje 4× gorzej. Hipoteza: w 2026 PMax optymalizuje na sygnał `ecommercePurchases` = 1 610 (zaburzone), podczas gdy w 2025 sygnał był `ecommercePurchases` = 1 515 ≈ `transactions` = 1 495 (normalne). Fałszywe sygnały sprawiają, że PMax "myśli" że konwertuje dobrze i kupuje tani, niekonwertujący ruch.

**Direct: -46% sesji, CR -83%**

| | 2026 | 2025 | Delta |
|---|------|------|-------|
| Sesje | 17 459 | 32 297 | -46% |
| Transakcje | 19 | 212 | **-91%** |
| CR | 0.109% | 0.656% | **-83%** |

Dramatyczny spadek CR ruchu bezpośredniego (-83%) sugeruje, że stali klienci (lojalni, znający markę) kupują rzadziej. Może wskazywać na:
- Pogorszenie oferty/dostępności produktów
- Problemy z kontem klienta (logowanie, historia zamówień)
- Zmieniona ścieżka checkout zniechęcająca do powrotu

**Organic Search: -43% sesji, CR -33%**

Dwoisty problem: mniej ruchu organicznego I niższy CR z tego ruchu. Sugeruje zmiany w algorytmie Google (mniej widoczności na frazy non-brand) ORAZ degradację landing pages.

**Email (edrone): -42% sesji, CR -60%**

Znaczny spadek efektywności email marketingu. Możliwe: zmniejszona aktywność wysyłek lub gorsza segmentacja.

### Główne hipotezy wyjaśniające -71.4%

**H1 — Wyłączenie kampanii Google Search (UDOWODNIONE)**
- Sesje Paid Search: -92%
- CR Paid Search: +5% (stabilne)
- Wniosek: budżet Search drastycznie obcięty lub kampanie wyłączone
- Szacunkowa strata: ~162 trans/msc × 1 241 PLN = **~201 000 PLN/msc**

**H2 — PMax zoptymalizowany na fałszywe dane (UDOWODNIONE)**
- Malformed transaction IDs powodują że PMax "widzi" 3.77× więcej konwersji niż faktycznie jest
- PMax zwiększa zasięg ale na jakościowo słabym ruchu
- CR PMax: -77% YoY przy +63% sesji
- Szacunkowa strata: ~116 trans/msc × 1 241 PLN = **~144 000 PLN/msc**

**H3 — Degradacja mobile (UDOWODNIONE)**
- Mobile CR: -67% YoY (0.288% → 0.095%)
- Desktop CR: -41% YoY (0.466% → 0.276%)
- Mobile stracił 3× więcej niż desktop → problem specyficzny dla mobile
- Szacunkowa strata: ~280 trans/msc × 1 241 PLN = **~347 000 PLN/msc**

**H4 — Brak promocji porównywalnych do 2025 (PRAWDOPODOBNE)**
- W 2025 były skoki: 125 trans/dzień (14.03), 113 (26.03), 110 (31.03)
- W 2026 max = 29 trans/dzień
- Jeśli 2025 zawierał wielką wyprzedaż której w 2026 nie było, część różnicy YoY = czynnik sezonowy
- Nie da się precyzyjnie oddzielić od innych przyczyn

**H5 — Problemy techniczne podczas migracji/aktualizacji (CZĘŚCIOWO POTWIERDZONE)**
- Malformed IDs pojawiły się w 2026 (brak w 2025) → zmiana w kodzie strony
- Zmiana formatu item_id: 2025 = `09009-32` (stary format), 2026 = `26271` (numeryczny) → migracja katalogu
- Anomalia 04.04: 9 564 sesji, 0 transakcji → incydent techniczny
- Lejek rozbity (add_shipping_info > begin_checkout)

### Priorytetyzacja działań

```
🔴 Naprawić malformed IDs (GTM) → PMax przestanie optymalizować na fałszywe dane
🔴 Przywrócić kampanie Search → odzysk ~200k PLN/msc
🔴 Audyt UX mobile → odzysk ~100-350k PLN/msc
🟡 Naprawić tracking malformed snippet → czyste dane
🟡 Wdrożyć abandoned cart emails → ~100k PLN/msc
```

---

## CZĘŚĆ II.B — Impact finansowy

| Problem | Szacunek PLN/msc | Źródło danych | Priorytet |
|---------|-----------------|---------------|-----------|
| Paid Search wyłączone (-92% sesji) | ~200 000 strata | Paid Search: 4 600 vs 58 884 sesji YoY | 🔴 |
| Mobile CR -67% YoY | ~100 000–347 000 strata | Mobile CR: 0.095% vs 0.288% YoY | 🔴 |
| PMax na fałszywych danych (-77% CR) | ~100 000–144 000 strata | Cross-network CR: 0.051% vs 0.221% | 🔴 |
| Malformed transaction IDs (1 105) | Niemierzalne przepalanie budżetu | 1 105 konkretnych błędnych IDs | 🔴 |
| Porzucenie koszyka 98.7% | ~100 000 potencjał | 32 653 add_to_cart vs 427 trans | 🟡 |
| Checkout drop-off 67% | ~80 000–120 000 potencjał | begin_checkout vs trans | 🟡 |
| (not set) trans 7% | ~13 675 bez atrybuacji | 30 trans bez źródła | 🟡 |
| Bing organic niedoinwestowany | ~260 000 potencjał | Rev/sess = 10.51 PLN | 🟢 |
| SMS 0 transakcji | ~10 000 potencjał | 1 708 sesji, 0 trans vs 8 w 2025 | 🟢 |

**Łączna skala problemu YoY: -1 326 787 PLN/msc**

---

## CZĘŚĆ III — REKOMENDACJE

### 🔴 Natychmiast (0–7 dni) — Zatamowanie strat

**1. Naprawić malformed transaction_id w GTM** *(2–4h dewelopera GTM)*
- Znaleźć zmienną GA4 odczytującą `transaction_id` z URL parametru
- Zmienić na odczyt z DataLayer LUB użyć regex `^([^&]+)` na parametrze `id`
- Efekt: ratio ePurchases:transactions spada do ~1.0, PMax dostaje prawidłowe sygnały
- Weryfikacja: po wdrożeniu sprawdzić w GA4 DebugView czy malformed IDs zniknęły

**2. Wyłączyć wbudowany moduł Google Analytics w PrestaShop** *(30 min)*
- PrestaShop Admin → Moduły → Google Analytics → wyłączyć lub odinstalować
- Efekt: eliminacja 89 eventów purchase z `(not set)` i ewentualnych innych duplikatów
- UWAGA: upewnić się, że GTM z tagiem GA4 jest aktywny PRZED wyłączeniem modułu

**3. Pilna analiza Google Ads — dlaczego Search wyłączone?** *(1 dzień)*
- Sprawdzić w Google Ads: czy kampanie Search są aktywne, jaki budżet, kiedy ostatnio zmodyfikowane
- Paid Search sesje: 4 600 vs 58 884 rok temu — 92% mniej sesji przy niezmienionej jakości CR
- Szybki odzysk: reaktywacja Search lub zwiększenie budżetu

**4. Skonfigurować Referral exclusion** *(30 min w GA4)*
- GA4 → Strumień → Referral exclusion → dodać: `klarna.com`, `onet.pl`, `wp.pl`, `o2.pl`, `interia.pl`
- Efekt: prawidłowa atrybuacja 362 sesji webmaili + 55 sesji Klarna

---

### 🟡 Miesiąc 1 — Optymalizacja i naprawa

**5. Audyt UX mobile z narzędziem do nagrań** *(2–3 tygodnie)*
- Wdrożyć Microsoft Clarity lub Hotjar na mobile
- Sprawdzić Core Web Vitals na telefonach (PageSpeed Insights → Mobile)
- Zbadać nagrania sesji mobile na stronie checkout
- CR mobile 2026 vs 2025: -67% — coś konkretnego się zmieniło
- Cel: zidentyfikować "punkt bólu" i naprawić w szablonie PrestaShop

**6. Wdrożyć abandoned cart emails w edrone** *(1–2 tygodnie)*
- 32 653 add_to_cart vs 427 zakupów = 98.7% porzuconych koszyków
- edrone posiada moduł Abandoned Cart gotowy do aktywacji
- Sekwencja: 1h (przypomnienie), 24h (+5% rabatu), 72h (ostatnia szansa)
- Cel: odzysk 2–3% koszyków = +650–980 transakcji/rok = +~800 000–1 200 000 PLN/rok

**7. Zbadać i naprawić lejek checkout (drop-off 67%)** *(2–4 tygodnie)*
- Sprawdzić w nagraniach Clarity: gdzie użytkownicy rezygnują
- Prawdopodobne problemy: zbyt wiele kroków, brak Google Pay/Apple Pay, zaskakujące koszty dostawy
- Cel: zmniejszenie drop-off z 67% do 50% = +233 trans/msc × 1 241 PLN = ~289 000 PLN/msc

**8. Naprawić sekwencję eventów lejka (add_shipping_info > begin_checkout)** *(1–2h GTM)*
- Sprawdzić triggery dla `add_shipping_info` i `begin_checkout` w GTM
- Prawdopodobnie `add_shipping_info` triggeruje za wcześnie w procesie PrestaShop
- Efekt: poprawne dane lejka, możliwa analiza per etap

**9. Wdrożyć url_passthrough w GTM** *(15 min)*
- GTM → Tag GA4 Configuration → Pola → dodać `url_passthrough: true`
- Efekt: ~30 trans/msc odzyska atrybuację = ~37 000 PLN/msc widoczne

**10. Filtrowanie ruchu deweloperskiego** *(15 min w GA4)*
- GA4 → Admin → Filtry danych → wykluczyć hostname zawierający `arytondev` i `aryton81`

---

### 🟢 Miesiąc 2–3 — Skalowanie i strategia

**11. Wdrożyć kampanie Microsoft Bing Ads** *(2–3 tygodnie setup)*
- Bing organic: 2 859 sesji, 26 transakcji, 30 063 PLN = Rev/sesja = **10.51 PLN** (najwyższy na koncie!)
- Ten sam feed produktowy co Google Ads
- Przy 10× wolumenie sesji: 26 000 sesji × 26/2859 CR = ~236 trans/msc × 1 241 PLN = **~293 000 PLN/msc**

**12. Analiza BCG po naprawieniu trackingu** *(po 30 dniach czystych danych)*
- Dane produktowe dostępne w GA4 (100 produktów z przychodem)
- Po naprawieniu malformed IDs — PMax dostanie czyste dane
- Przebudować strukturę asset groups per kategoria BCG (Gwiazdy/Psy/Dojne Krowy)

**13. Zbadać przyczyny spadku ruchu Direct (-46%) i Email (-42%)**
- Ruch bezpośredni -46% może wskazywać na mniejszą lojalność klientów
- Email CR -60% → potrzeba resegmentacji bazy lub nowej strategii mailingów
- Zbadać open rates i click rates w edrone

**14. Wdrożyć alerty w GA4** *(30 min)*
- GA4 → Insights → Alerty → dodać dla: transakcje < 5/dzień, przychód < 5 000 PLN/dzień
- Efekt: wcześniejsze wykrycie awarii (jak 04.04 z 0 transakcjami)

---

## Podsumowanie

Patrizia by Aryton to marka premium z realną sprzedażą i wysokim AOV (1 241 PLN). Dane wskazują, że rok temu sklep działał znacznie lepiej — 1 495 zamówień miesięcznie vs 427 teraz, przy identycznym AOV.

Analiza YoY wskazuje na **trzy główne przyczyny** 71% spadku:
1. **Wyłączone kampanie Google Search** — brak budżetu = brak ruchu = brak sprzedaży (~200k PLN/msc strata)
2. **PMax optymalizuje na fałszywe dane** — malformed transaction IDs sprawiają że algorytm kupuje złe kliknięcia
3. **Degradacja CR mobile** — z 0.288% do 0.095% YoY, coś konkretnego zmieniło się w doświadczeniu mobilnym

Naprawienie malformed IDs i reaktywacja Search to działania możliwe w ciągu 1 tygodnia i bezpośrednio adresujące dwie pierwsze przyczyny. Audyt UX mobile i przebudowa strategii kampanii to praca kilkutygodniowa ale z potencjałem odzysku setek tysięcy złotych miesięcznie.
