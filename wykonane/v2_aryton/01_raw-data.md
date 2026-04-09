# Dane surowe v2: patrizia.aryton.pl — 2026-04-09

**GA4 Property:** G-93NK3C48R3 (ID: 326801658) | **Platforma:** PrestaShop | **CMP:** Cookiebot
**Okres bieżący:** 9 marca – 8 kwietnia 2026 (30 dni)
**Okres YoY:** 10 marca – 9 kwietnia 2025 (30 dni)

---

## GA4 — Totale ogólne (bieżące vs YoY)

| Metryka | 2026 (30d) | 2025 (YoY) | Delta YoY |
|---------|-----------|-----------|-----------|
| Sesje | 330 296 | 438 646 | **-24.7%** |
| Użytkownicy | 180 654 | — | — |
| Nowi użytkownicy | 126 174 | — | — |
| **Transakcje** | **427** | **1 495** | **-71.4%** |
| ecommercePurchases (raw) | 1 610 | 1 515 | +6.3% |
| **Przychód (PLN)** | **529 914** | **1 856 701** | **-71.5%** |
| **AOV** | **1 241 PLN** | **1 242 PLN** | ≈0% |
| **CR (trans/sesje)** | **0.129%** | **0.341%** | **-62%** |
| Avg session duration | 899s (15min) | — | — |
| Engagement rate | 47.8% | — | — |

**⚠️ KRYTYCZNE:** W 2025 roku ratio `ecommercePurchases:transactions` = 1515/1495 = **1.013** (tracking normalny). W 2026 = 1610/427 = **3.77** (tracking uszkodzony). Szczegóły poniżej.

---

## GA4 — Analiza ecommercePurchases vs Transactions (duplikaty)

**Wynik:** Brak zduplikowanych transaction_id w sensie klasycznym. Problem ma INNĄ NATURĘ.

| Kategoria | Liczba ID | ecommercePurchases | Transactions | Przychód |
|-----------|-----------|-------------------|--------------|---------|
| Prawidłowe (numeryczne ID) | 427 | 427 | 427 | 529 914 PLN |
| Malformed (`ID&key=...`) | 1 105 | 1 105 | 0 | 0 PLN |
| `(not set)` | 1 | 89 | 0 | 0 PLN |
| Pusty string `""` | 1 | 2 | 0 | 0 PLN |
| **ŁĄCZNIE** | **1 534** | **1 623** | **427** | **529 914 PLN** |

**Przykłady malformed transaction_id (konkretne ID z GA4):**
```
210032&key=1abe2783234b4109f15a80bdd3246c14
210033&key=1abe2783234b4109f15a80bdd3246c14
210034&key=1abe2783234b4109f15a80bdd3246c14
210035&key=1abe2783234b4109f15a80bdd3246c14
```

**Prawidłowe transakcje (próbka):**
```
ID=210034   trans=1  ePurch=1  rev=2 069.00 PLN
ID=221110   trans=1  ePurch=1  rev=3 799.00 PLN
ID=222970   trans=1  ePurch=1  rev=  881.00 PLN
ID=224562   trans=1  ePurch=1  rev=5 047.00 PLN
ID=224679   trans=1  ePurch=1  rev=  599.00 PLN
```

**Przyczyna problemu:**
PrestaShop URL potwierdzenia zamówienia: `/order-confirmation?id=210034&key=1abe2783234b4109f15a80bdd3246c14`
- GTM DataLayer push: poprawnie przekazuje `transaction_id = "210034"` → 427 prawdziwych transakcji ✅
- Drugie źródło (tag lub hardcoded gtag): odczytuje transaction_id z URL parametru `?id=...` bez obcinania `&key=...` → 1105 malformed IDs ❌
- Trzeci problem: hardcoded gtag fires 89 razy BEZ DataLayer (transaction_id = `not set`, revenue = 0) ❌

**W 2025 brak malformed IDs** → tracking był poprawny (ratio 1.01). Problem pojawił się w 2026 — prawdopodobnie po aktualizacji strony lub zmianie konfiguracji GTM.

---

## GA4 — Zdarzenia (30d) — TOP 30

| Zdarzenie | Liczba | Liczba/użytkownik |
|-----------|--------|-------------------|
| page_view | ~1.38M | 8.26 |
| view_item_list | ~842k | 11.56 |
| user_engagement | ~854k | 7.23 |
| session_start | ~675k | 4.03 |
| first_visit | ~614k | 3.04 |
| view_item | ~590k | 5.99 |
| login | ~459k | 4.28 ⚠️ |
| scroll | ~238k | 3.82 |
| add_to_cart | 32 653 | 5.55 |
| begin_checkout | ~1 296 | 2.00 |
| add_shipping_info | ~2 132 | 3.76 ⚠️ > begin_checkout |
| purchase | 1 610 (raw) | — |
| add_payment_info | ~806 | 1.71 |
| begin_checkout | 1 296 | 2.00 |
| sign_up | 24 | 1.00 |

---

## GA4 — Kanały domyślne (bieżące vs YoY)

| Kanał | Sesje 26 | Trans 26 | CR 26 | Rev 26 | Sesje 25 | Trans 25 | CR 25 | Delta trans |
|-------|---------|---------|------|-------|---------|---------|------|------------|
| Cross-network (PMax) | 137 557 | 70 | **0.051%** | 74 896 | 84 140 | 186 | **0.221%** | -62% |
| Organic Search | 80 770 | 206 | **0.255%** | 281 223 | 141 985 | 538 | **0.379%** | -62% |
| Paid Social (Meta) | 58 776 | 31 | **0.053%** | 64 782 | 51 659 | 82 | **0.159%** | -62% |
| Email (edrone) | 17 721 | 37 | **0.209%** | 45 826 | 30 609 | 159 | **0.519%** | -77% |
| Direct | 17 459 | 19 | **0.109%** | 21 197 | 32 297 | 212 | **0.656%** | -91% |
| Unassigned | 10 547 | 30 | **0.284%** | 13 675 | 20 635 | 66 | **0.320%** | -55% |
| Paid Search | 4 600 | 14 | **0.304%** | 11 114 | 58 884 | 171 | **0.290%** | -92% |
| Display | 4 675 | 8 | **0.171%** | 8 623 | 8 811 | 16 | **0.182%** | -50% |
| Organic Social | 4 926 | 8 | **0.162%** | 6 756 | 14 989 | 37 | **0.247%** | -78% |
| SMS | 1 710 | 0 | **0.000%** | 0 | 2 428 | 8 | **0.330%** | -100% |
| Referral | 1 094 | 4 | **0.366%** | 1 822 | 3 393 | 19 | **0.560%** | -79% |

**Kluczowe obserwacje:**
- **Paid Search (-92% sesji):** Z 58,884 do 4,600 sesji — kampanie Search prawdopodobnie wyłączone lub budżet drastycznie obcięty
- **CR PMax: 0.05% (vs 0.22% w 2025)** — PMax generuje więcej ruchu ale 4× mniej efektywny niż rok temu
- **Email CR: 0.21% (vs 0.52% w 2025)** — efektywność emaili spadła 2.5×
- **Direct CR: 0.11% (vs 0.66% w 2025)** — ruch bezpośredni stracił 6× na CR
- **SMS: 0 transakcji** (vs 8 w 2025) — coś się zepsuło w SMS trackingu

---

## GA4 — Źródła ruchu (source/medium) — TOP 15

| source | medium | Sesje | Trans | Przychód (PLN) |
|--------|--------|-------|-------|----------------|
| google | cpc | 142 854 | 90 | 92 185 |
| google | organic | 75 838 | 173 | 241 879 |
| facebook | cpc | 58 776 | 31 | 64 782 |
| edrone | email | 17 711 | 37 | 45 826 |
| (direct) | (none) | 17 459 | 19 | 21 197 |
| **(not set)** | **(not set)** | **10 502** | **30** | **13 675** |
| (data not available) | (data not available) | 3 548 | 2 | 2 448 |
| bing | organic | 2 859 | 26 | 30 063 |
| m.facebook.com | referral | 1 736 | 4 | 3 821 |
| sms | smsapi | 1 708 | 0 | 0 |
| l.instagram.com | referral | 1 703 | 1 | 1 198 |
| l.facebook.com | referral | 706 | 0 | 0 |
| pl.search.yahoo.com | referral | 626 | 2 | 2 633 |
| google | maps | 558 | 2 | 3 527 |
| facebook | referral | 366 | 3 | 1 737 |

**(not set)/(not set): 10 502 sesji = 3.18% całości**

**Fragmentacja Meta:** facebook/cpc (58 776) + m.facebook.com (1 736) + l.instagram.com (1 703) + l.facebook.com (706) + lm.facebook.com (365) + facebook/referral (366) + facebook.com/referral (~86) = **~63 738 sesji w 7 silosach**

---

## GA4 — Urządzenia (bieżące vs YoY)

| Urządzenie | Sesje 26 | Trans 26 | CR 26 | AOV 26 | Sesje 25 | Trans 25 | CR 25 | Delta CR |
|-----------|---------|---------|------|--------|---------|---------|------|---------|
| **mobile** | **259 439** | **246** | **0.095%** | 1 302 PLN | **318 860** | **919** | **0.288%** | **-67%** |
| **desktop** | **65 243** | **180** | **0.276%** | 1 162 PLN | **120 419** | **561** | **0.466%** | **-41%** |
| tablet | 4 784 | 1 | 0.021% | 499 PLN | 8 090 | 15 | 0.185% | -89% |

**Rev/sesja 2026:** mobile = 1.23 PLN, desktop = 3.21 PLN
**Rev/sesja 2025:** mobile ≈ 3.57 PLN (919×1242/318860), desktop ≈ 5.79 PLN

**Mobile potencjał (gdyby CR mobile = 50% desktop):**
- Cel CR mobile: 0.138% (50% × 0.276%)
- Dodatkowe trans: (0.138% - 0.095%) × 259,439 = +111 trans/msc
- Dodatkowy przychód: 111 × 1,241 PLN = **~138 000 PLN/msc**

---

## GA4 — Platforma — Hostnames

| Hostname | Sesje | Trans | Komentarz |
|----------|-------|-------|-----------|
| patrizia.aryton.pl | 330 296 | 413 | Główna domena produkcyjna |
| dev18.arytondev.pl | 26 | 1 | Serwer deweloperski Aryton |
| dev18.arytondev.local | 14 | 0 | Lokalny serwer deweloperski |
| aryton81.local | 7 | 0 | Lokalny serwer deweloperski |
| aryton.b-cdn.net | 2 | 0 | CDN Bunny |
| (not set) | 0 | 13 | 13 transakcji bez hostname ⚠️ |

**Potwierdzenie PrestaShop** (URL wzorce z danych):
- Produkty: `/p/26307-sukienka-z-jedwabiu.html` = PrestaShop format `ID-slug.html`
- Kategorie: `/c/390-nowosci`, `/c/414-spodnie`, `/c/705-promocja` = PrestaShop format `ID-slug`
- Potwierdzenie zamówienia: `?id=210034&key=1abe2783...` = PrestaShop order confirmation URL
- Dev serwer: `aryton81.local` = typowa PrestaShop instalacja lokalna

---

## GA4 — Produkty e-commerce (30d) — TOP 10 po przychodzie

| itemId | Nazwa produktu | Kategoria | Zakupów | Przychód (PLN) |
|--------|----------------|-----------|---------|----------------|
| 26271 | Camelowy płaszcz teddy bear z wełną | Płaszcze | 8 | 27 992 |
| 26420 | Brązowa kurtka ze skóry zamszowej | Płaszcze | 6 | 23 994 |
| 26325 | Czarna kurtka bomberka z jedwabiem | Płaszcze | 9 | 20 691 |
| 22390 | Długi bawełniany trencz beżowy | Płaszcze | 11 | 18 469 |
| 26204 | Beżowa dwurzędowa kurtka z wełny | Płaszcze | 14 | 17 486 |
| 26427 | Niebieskie zwężane jeansy | Odzież | 18 | 14 382 |
| 23206 | Camelowy bawełniany płaszcz z paskami | Płaszcze | 11 | 14 289 |
| 26020 | Płaszcz camel z wełny wielbłądziej | Płaszcze | 2 | 13 998 |
| 26526 | Czekoladowa skórzana torebka | Akcesoria | 6 | 13 794 |
| 26271 | Camelowy płaszcz teddy bear z wełną | Płaszcze | 7 | 24 493 |

**Produkty z przychodem > 0: 100 z 100** (w przeciwieństwie do błędnej konkluzji v1, dane produktowe SĄ dostępne)

**Produkty YoY (2025, TOP 5):**
| itemId | Nazwa | Zakupów | Przychód |
|--------|-------|---------|---------|
| 09009-32 | Beżowy płaszcz trencz z paskiem | 11 | 26 389 PLN |
| 08847-19 | Czarny bawełniany trencz z paskiem | 9 | 23 391 PLN |
| 10322-11 | Białe buty sportowe | 23 | 20 677 PLN |
| 10048-12 | Szara kurtka z jedwabiem doubleface | 7 | 20 293 PLN |
| 08844-97 | Jeansy z szeroką nogawką | 22 | 19 778 PLN |

**Uwaga:** Różne formaty ID produktów: 2025 = format `NNNNN-NN` (np. `09009-32`), 2026 = numeryczny (np. `26271`). Sugeruje migrację katalogu produktów lub zmianę atrybutów PrestaShop.

---

## GA4 — Dzienny trend (kluczowe dni)

### 2026 — Top dni sprzedaży
| Data | Sesje | Trans | Przychód |
|------|-------|-------|---------|
| 2026-03-31 | 11 425 | 29 | 44 627 PLN |
| 2026-04-01 | 10 956 | 22 | 37 239 PLN |
| 2026-04-07 | 12 663 | 16 | 37 895 PLN |
| 2026-03-22 | 13 817 | 23 | 30 598 PLN |
| 2026-03-11 | 8 063 | 25 | 35 822 PLN |
| **2026-04-04** | **9 564** | **0** | **0 PLN** ⚠️ |

**Anomalia: 2026-04-04 = 0 transakcji przy 9 564 sesjach** — możliwa awaria strony, bramki płatności lub problemy techniczne.

### 2025 — Top dni sprzedaży (dla porównania)
| Data | Sesje | Trans | Przychód |
|------|-------|-------|---------|
| 2025-03-14 | 16 064 | **125** | 187 793 PLN |
| 2025-03-26 | 19 026 | **113** | 145 822 PLN |
| 2025-03-31 | 13 116 | **110** | 138 935 PLN |
| 2025-04-09 | 15 961 | 82 | 99 924 PLN |

**Średnia dzienna 2025:** 48 transakcji/dzień vs **2026: 14 transakcji/dzień**

---

## GA4 — Landing Pages TOP 10 (z CR)

| Strona | Sesje | Trans | CR |
|--------|-------|-------|----|
| / (strona główna) | 86 825 | 161 | 0.19% |
| /kolekcja/effortless-mood | 19 660 | 4 | 0.02% |
| /c/390-nowosci | 19 195 | 13 | 0.07% |
| /c/414-spodnie | 17 799 | 2 | 0.01% |
| /c/705-promocja | 16 305 | 5 | 0.03% |
| /c/412-bluzki | 15 163 | 0 | 0.00% |
| /p/26307-sukienka-z-jedwabiu.html | 13 252 | 0 | 0.00% ⚠️ |
| /c/1241-wiosna-lato-2026 | 12 379 | 0 | 0.00% |
| /c/434-outlet | 7 069 | 8 | 0.11% |

**⚠️ Top strona produktowa (13 252 sesji) z CR = 0.00%** — brak konwersji z najpopularniejszego produktu.

---

## GA4 — Referrals (szczegółowe)

| Source | Sesje | Trans | Przychód |
|--------|-------|-------|---------|
| m.facebook.com | 1 736 | 4 | 3 821 PLN |
| l.instagram.com | 1 703 | 1 | 1 198 PLN |
| l.facebook.com | 706 | 0 | 0 |
| pl.search.yahoo.com | 626 | 2 | 2 633 PLN |
| facebook | 366 | 3 | 1 737 PLN |
| lm.facebook.com | 365 | 0 | 0 |
| poczta.onet.pl | 191 | 0 | 0 |
| ntp.msn.com | 103 | 3 | 3 121 PLN |
| poczta.interia.pl | 88 | 0 | 0 |
| facebook.com | 86 | 0 | 0 |
| poczta.o2.pl | 83 | 0 | 0 |
| zasobygwp.pl | 75 | 1 | 305 PLN |
| statics.teams.cdn.office.net | 72 | 0 | 0 |
| klarna | 55 | 0 | 0 |

---

## Notatki — pierwsze obserwacje (tylko fakty, bez interpretacji)

### ❌ Potwierdzone problemy (z konkretnymi danymi):

1. **1105 malformed transaction_id** — konkretne przykłady: `210032&key=1abe2783234b4109f15a80bdd3246c14`, `210033&key=...` — każdy generuje 1 `ecommercePurchase` z revenue=0 i transactions=0. Łącznie 1105 takich zdarzeń influje `ecommercePurchases`.

2. **89 eventów purchase z (not set) transaction_id** — generują 89 `ecommercePurchases` ale 0 transactions i 0 revenue. Źródło: hardcoded gtag BEZ DataLayer.

3. **Transakcje YoY -71.4%** — 427 w 2026 vs 1495 w 2025. AOV identyczny (1241 vs 1242 PLN) → problem NIE jest cenowy.

4. **Paid Search sesje -92%** — 4600 vs 58884 YoY. CR Paid Search unchanged (0.30% vs 0.29%) → problem = dramatyczny spadek wolumenu, nie jakości.

5. **CR mobile: 0.095% vs 0.288% YoY** = -67%. CR desktop: 0.276% vs 0.466% = -41%.

6. **PMax CR: 0.051% vs 0.221% YoY** — MORE sesji (137k vs 84k) ale LESS transakcji (70 vs 186). PMax przynosi niekonwertujący ruch.

7. **Anomalia 2026-04-04** — 9564 sesji, 0 transakcji. Potencjalna awaria techniczna.

8. **Serwery deweloperskie widoczne w GA4** — dev18.arytondev.pl (26 sesji), dev18.arytondev.local (14), aryton81.local (7). Brak filtrowania ruchu deweloperskiego.

9. **Klarna w referral** — 55 sesji bez transakcji (bramka płatności nie wykluczana z referral).

10. **Webmaile jako referral** — poczta.onet.pl (191 sesji), poczta.interia.pl (88), poczta.o2.pl (83).
