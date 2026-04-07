# Dane surowe: modnakiecka — 20260407

> **Źródło:** GA4 Data API (property 291537403) | Okres: 30 ostatnich dni (8.03.2026 – 7.04.2026)
> **Brak dostępu:** GTM Admin, Google Ads, BigQuery

---

## GA4 — KPI ogólne (30d)

| Wskaźnik | Wartość |
|---|---|
| Sesje łącznie | 1 858 660 |
| ecommercePurchases (purchase event) | 31 090 |
| purchaseRevenue | **6 842 880 PLN** |
| addToCarts | 249 979 |
| checkouts (begin_checkout) | 81 640 |
| CR (ecommercePurchases / sesje) | **1,673%** |
| AOV | **220,10 PLN** |

---

## GA4 — Zdarzenia (30d) — TOP 20

| Zdarzenie | Liczba | Liczba/użytkownik |
|-----------|--------|-------------------|
| page_view | 17 750 478 | 19,73 |
| user_engagement | 7 518 413 | 10,08 |
| view_item_list | 5 040 000 | 7,86 |
| view_item | 4 629 750 | 6,65 |
| session_start | 2 187 099 | 2,46 |
| select_item | 1 457 814 | 5,29 |
| first_visit | 1 141 367 | 1,60 |
| view_search_results | 304 506 | 2,11 |
| add_to_cart | 249 979 | 3,13 |
| view_cart | 165 875 | 3,76 |
| begin_checkout | 81 640 | 2,29 |
| add_payment_info | 81 130 | 2,28 |
| add_shipping_info | 80 967 | 2,27 |
| **złożenie_zamówienia** ⚠️ | **76 136** | 2,66 |
| purchase | 31 090 | 1,12 |
| remove_from_cart | 22 343 | 2,08 |
| video_progress | 2 809 | 9,49 |
| click | 2 171 | 1,24 |
| file_download | 1 535 | 1,23 |
| video_start | 779 | 2,62 |

**⚠️ KRYTYCZNA ANOMALIA:** `złożenie_zamówienia` = 76 136 vs `purchase` = 31 090. Różnica 2,45×. Custom event Shopera odpala 2,45× częściej niż GA4 purchase event. Prawdopodobna duplikacja custom eventu LUB zaniżanie purchase.

**⚠️ ANOMALIA LEJKA:** begin_checkout = 81 640, ale purchase = 31 090 → tylko 38,1% checkout kończy się purchase. Przy prawidłowym wdrożeniu GA4 purchase powinien odzwierciedlać faktyczne zamówienia złożone.

---

## GA4 — Źródła ruchu (30d)

| Source | Medium | Sessions | Transactions | Revenue PLN |
|--------|--------|----------|--------------|-------------|
| google | cpc | 623 547 | 12 129 | 2 796 793 |
| facebook | cpc | 546 733 | 7 999 | 1 554 203 |
| google | organic | 136 835 | 1 595 | 361 049 |
| criteo | retargeting | 73 105 | 990 | 203 948 |
| (direct) | (none) | 64 812 | 1 267 | 281 116 |
| wpads | display | 54 741 | 743 | 158 390 |
| **m.facebook.com** | **referral** | **51 530** | 993 | 200 792 |
| **fb** | **paid** | **48 461** | 485 | 88 834 |
| **(not set)** | **(not set)** | 34 214 | 386 | 91 486 |
| **lm.facebook.com** | **referral** | **28 769** | 436 | 82 553 |
| pwa | (not set) | 23 019 | 731 | 171 877 |
| salesmanago.pl | referral | 20 410 | 924 | 283 728 |
| criteo | display | 17 179 | 23 | 4 345 |
| **facebook** | **traffic** | **16 365** | 20 | 4 430 |
| lamoda | cpc | 14 725 | 198 | 37 441 |
| bing | cpc | 10 657 | 376 | 100 306 |
| tiktok | paid | 10 112 | 90 | 20 202 |
| salesmanago | sms | 9 672 | 82 | 18 001 |
| (data not available) | (data not available) | 8 195 | 153 | 31 299 |
| l.facebook.com | referral | 8 171 | 159 | 39 374 |

### Agregacje kluczowych problemów UTM

**Facebook — fragmentacja na 14 wariantów:**
| Wariant | Sessions |
|---------|----------|
| facebook/cpc | 546 733 |
| m.facebook.com/referral | 51 530 |
| fb/paid | 48 461 |
| lm.facebook.com/referral | 28 769 |
| facebook/traffic | 16 365 |
| l.facebook.com/referral | 8 171 |
| facebook.com/referral | 1 442 |
| fb/traffic | 1 438 |
| pozostałe (6 wariantów) | 104 |
| **ŁĄCZNIE (Facebook)** | **703 013 sesji** |

Z 703 013 sesji Facebook tylko ~546 733 (77,7%) ma poprawne UTM `facebook/cpc`. Pozostałe 156 280 sesji (22,3%) jest przypisane jako referral lub ma błędne medium.

**SALESmanago — 9 różnych mediums:**
| Medium | Sessions | Transactions | Revenue PLN |
|--------|----------|--------------|-------------|
| referral | 20 410 | 924 | 283 728 |
| sms | 9 672 | 82 | 18 001 |
| newsletter | 7 040 | 91 | 21 317 |
| email_confirmation | 3 406 | 240 | 52 564 |
| email | 3 376 | 34 | 7 012 |
| workflow | 1 837 | 124 | 28 680 |
| salesmanago.com/referral | 228 | 4 | 2 097 |
| RFM 1WEB / test | 12 | 0 | 0 |
| **ŁĄCZNIE** | **45 981** | **1 499** | **413 399 PLN** |

⚠️ `salesmanago.pl/referral` (20 410 sesji) — web push lub linki SALESmanago bez UTM klasyfikowane jako referral zamiast email/push.

**TikTok — 7 wariantów (brak spójności UTM):**
- tiktok/paid: 10 112 ses, tiktok/cpc: 5 317, tiktok/traffic: 3 784, tiktok/(not set): 311, tiktok.com/referral: 184, tiktok/referral: 76, tiktok?utm_id/paid: 12
- **ŁĄCZNIE: 19 796 sesji, 147 transakcji** — 4 różne medium dla TikToka

**(not set) — łącznie:**
- Wiersze z (not set) w source lub medium: **61 232 sesji, 1 136 transakcji**
- % sesji: 61 232 / 1 858 660 = **3,3%**

---

## GA4 — Transakcje (weryfikacja duplikatów)

| Wskaźnik | Wartość |
|---|---|
| Próba: transaction rows (TOP 200 po transactionId) | 200 |
| Sum transactions w próbie | 320 |
| Sum ecommercePurchases w próbie | 320 |
| Wiersze z duplicatami (>1 transakcja na ID) | **99 / 200 = 49,5%** |
| Ratio ecommercePurchases:transactions | 1,00 (GA4 deduplicuje prawidłowo) |
| Wiersze bez transactionId (not set) | **0** (w TOP 200) |

**Przykłady zduplikowanych transactionId:**

| transactionId | transactions | ecommercePurchases | Revenue PLN |
|---|---|---|---|
| 14564069 | **12** | 12 | 5 159,52 |
| 14586462 | **6** | 6 | 839,94 |
| 14587588 | **6** | 6 | 1 169,88 |
| 14572136 | 3 | 3 | 239,97 |
| 14578366 | 3 | 3 | 389,94 |
| 14586458 | 3 | 3 | 419,97 |
| (10 kolejnych) | 2 | 2 | ... |

**⚠️ KRYTYCZNE:** 49,5% transactionId w TOP 200 ma więcej niż 1 trafienie. Transakcja ID=14564069 zarejestrowana **12 razy**. GA4 deduplicuje na poziomie `ecommercePurchases` (transactions = ecommercePurchases), ale sugeruje to duplikację na poziomie firing purchase eventu (np. dwa kontenery GTM strzelają osobno).

---

## GA4 — Lejek zakupowy (30d)

| Kanał | Sessions | addToCarts | Checkouts | Purchases | CR |
|-------|----------|------------|-----------|-----------|-----|
| Paid Social | 620 375 | 75 792 | 27 487 | 8 667 | **1,40%** |
| Cross-network | 442 595 | 44 129 | 12 561 | 5 776 | 1,31% |
| **Paid Search** | **168 729** | **47 900** | **14 826** | **6 262** | **3,71%** |
| Organic Search | 143 668 | 14 926 | 4 094 | 1 857 | 1,29% |
| Organic Social | 128 817 | 14 371 | 4 987 | 1 785 | 1,39% |
| Paid Other | 93 961 | 10 917 | 3 460 | 1 359 | 1,45% |
| **Unassigned** | **82 600** | **14 682** | **4 613** | **1 601** | **1,94%** |
| Display | 73 711 | 6 801 | 2 064 | 775 | 1,05% |
| Direct | 64 812 | 6 770 | 2 729 | 1 267 | 1,95% |
| **Paid Shopping** | **25 149** | **5 066** | **1 370** | **611** | **2,43%** |
| Referral | 24 198 | 7 206 | 2 954 | 1 005 | **4,15%** |
| SMS | 9 839 | 925 | 372 | 85 | 0,86% |
| Email | 3 376 | 458 | 113 | 34 | 1,01% |
| Mobile Push | 696 | 30 | 3 | 1 | 0,14% |
| Affiliates | 13 | 6 | 7 | 5 | 38,5%* |
| Paid Video | 3 | 0 | 0 | 0 | - |

*Affiliates: 13 sesji = dane statystycznie nieistotne

**Obserwacje:**
- Paid Search: CR = 3,71% → najlepszy płatny kanał, 2,8× lepszy niż Paid Social
- Unassigned: 82 600 sesji, CR=1,94% → serio niezaklasyfikowany ruch (UTM problem)
- SMS: tylko 85 zakupów z 9 839 sesji → CR=0,86%, najgorszy kanał poza Mobile Push
- Referral CR=4,15% (1 005 zakupów) → wysoka jakość ruchu z partnerów
- Paid Shopping oddzielony od Cross-network → 611 zakupów, CR=2,43%

---

## GA4 — Urządzenia (30d)

| Urządzenie | Sessions | ecommercePurchases | Revenue PLN | CR | AOV PLN |
|---|---|---|---|---|---|
| Mobile | 1 658 971 (89,3%) | 24 900 (80,1%) | 5 252 254 | **1,50%** | 210,9 |
| Desktop | 188 525 (10,1%) | 6 013 (19,3%) | 1 552 462 | **3,19%** | 258,2 |
| Tablet | 21 481 (1,2%) | 177 (0,6%) | 38 164 | 0,82% | 215,6 |
| Smart TV | 15 (<0,1%) | 0 | 0 | — | — |

**Mobile gap: Desktop CR (3,19%) jest 2,13× wyższy niż Mobile CR (1,50%).** Przy 89,3% ruchu mobilnego to największa dźwignia wzrostu sprzedaży.
**AOV gap: Desktop AOV 258 PLN vs Mobile AOV 211 PLN — różnica 47 PLN/zamówienie (+22,3%).**

---

## GA4 — Top 20 miast

| Miasto | Sessions | ecommercePurchases | Revenue PLN | CR |
|--------|----------|---------------------|-------------|-----|
| Warsaw | 318 811 | 5 336 | 1 204 280 | 1,67% |
| (not set) | 198 855 | 2 234 | 486 195 | 1,12% |
| Wroclaw | 114 327 | 2 019 | 449 904 | 1,77% |
| Poznan | 95 639 | 1 579 | 331 205 | 1,65% |
| Krakow | 94 652 | 1 618 | 354 244 | 1,71% |
| Lodz | 70 044 | 1 204 | 261 802 | 1,72% |
| Gdansk | 64 369 | 1 121 | 235 213 | 1,74% |
| Katowice | 63 512 | 952 | 192 646 | 1,50% |
| Bydgoszcz | 41 458 | 719 | 154 067 | 1,73% |
| Lublin | 37 001 | 723 | 157 797 | 1,95% |
| Rzeszow | 30 115 | 528 | 111 281 | 1,75% |
| Szczecin | 24 669 | 458 | 103 472 | 1,86% |
| Bialystok | 21 568 | 397 | 90 197 | 1,84% |
| Czestochowa | 18 536 | 308 | 61 763 | 1,66% |
| Kielce | 17 971 | 314 | 65 431 | 1,75% |
| Radom | 17 133 | 331 | 77 880 | 1,93% |
| Torun | 11 468 | 201 | 44 407 | 1,75% |
| Plock | 11 050 | 189 | 37 032 | 1,71% |
| Olsztyn | 10 417 | 174 | 39 168 | 1,67% |
| Sosnowiec | 10 382 | 163 | 33 361 | 1,62% |

**Uwaga:** 198 855 sesji (10,7%) ma city = (not set) — geolokalizacja nie jest wykrywana dla tej grupy ruchu.

---

## GA4 — Produkty (TOP 20 według wyświetleń)

| itemId | itemName | Kategoria | Wyświetlenia | Zakupy | Revenue PLN |
|--------|----------|-----------|--------------|--------|-------------|
| 23061976 | Beżowy Trencz12112-205-A | Okrycia Wierzchnie | 26 523 | **0** | **0** |
| 23067535 | Błękitny Komplet Marynarka+Spodnie | Komplety | 20 796 | **0** | **0** |
| 23068322 | Beżowy Komplet Marynarka+Spodnie | Komplety | 19 883 | **0** | **0** |
| 23071316 | Brązowa Plisowana Sukienka | Sukienki Eleganckie | 19 348 | **0** | **0** |
| 23071507 | Beżowa Elegancka Sukienka z Marszczeniem | Sukienki Eleganckie | 19 302 | **0** | **0** |
| 23071275 | Beżowa Przejściowa Kurtka z Kapturem | Okrycia Wierzchnie | 17 851 | **0** | **0** |
| 23071733 | Beżowa Plisowana Sukienka w Grochy | Sukienki na co Dzień | 17 763 | **0** | **0** |
| 23071297 | Beżowa Satynowa Sukienka Midi | Sukienki Eleganckie | 17 145 | **0** | **0** |
| 23068172 | Beżowa Sukienka w Kwiaty z Paskiem | Sukienki Eleganckie | 16 504 | **0** | **0** |
| 23071826 | Kremowy Elegancki Komplet | Komplety | 15 251 | **0** | **0** |
| 23071293 | Beżowy Krótki Płaszcz Teddy | Okrycia Wierzchnie | 15 199 | **0** | **0** |
| 23054688 | Beżowy Komplet Marynarka+Spodnie 9613 | Komplety | 14 838 | **0** | **0** |
| 23054689 | Kremowy Komplet Marynarka+Spodnie 9613 | Komplety | 14 817 | **0** | **0** |
| 23067528 | Beżowa Przejściowa Kurtka z Kieszeniami | Okrycia Wierzchnie | 14 412 | **0** | **0** |
| 23068327 | Różowy Komplet Marynarka+Spodnie | Komplety | 13 683 | **0** | **0** |
| 23067812 | Beżowa Sukienka z Bufiastymi Rękawami | Sukienki Eleganckie | 13 422 | **0** | **0** |
| 23071158 | Pudrowa Sukienka z Motywem Roślinnym | Sukienki na co Dzień | 13 081 | **0** | **0** |
| 23061519 | Beżowa Sukienka 11932 | Sukienki Eleganckie | 12 923 | **0** | **0** |
| 23071037 | Beżowa Klasyczna Sukienka z Kieszeniami | Sukienki na co Dzień | 12 782 | **0** | **0** |
| 23071734 | Błękitna Plisowana Sukienka w Grochy | Sukienki na co Dzień | 12 639 | **0** | **0** |

**🚨 KRYTYCZNE:** Wszystkie top 20 produktów według wyświetleń mają `itemsPurchased = 0` i `itemRevenue = 0 PLN`. Pomimo 31 090 zakupów i 6,84 mln PLN przychodu — **ani jeden produkt nie ma przypisanego przychodu na poziomie item**. Oznacza to, że w evencie `purchase` nie są przesyłane dane o zakupionych produktach (brak tablicy `items[]`), lub itemId w purchase event nie pasuje do itemId w view_item event.

---

## Google Ads — 🔒 Brak dostępu

Sekcja pominięta — brak dostępu do Google Ads API / BDOS.

---

## Notatki — pierwsze obserwacje (bez interpretacji)

1. **Duplikacja `purchase` event:** 49,5% transactionId w próbie ma >1 trafienie (max 12×). Jeden ID pojawia się 12 razy. Ratio ecommercePurchases:transactions = 1:1 (GA4 deduplicuje), ale to wskazuje na problem na poziomie tagów.

2. **`złożenie_zamówienia` vs `purchase`:** 76 136 vs 31 090 — różnica 2,45×. Custom event Shopera i GA4 purchase event są niespójne.

3. **Brak danych product-level w purchase:** Wszystkie produkty mają itemRevenue=0 mimo 6,84 mln PLN przychodu. Items nie są przekazywane w purchase event lub itemId nie jest spójny.

4. **Facebook UTM fragmentation:** 703 013 sesji na 14 wariantach. Tylko 77,7% ma poprawne utm_source=facebook&utm_medium=cpc.

5. **Unassigned 82 600 sesji z CR=1,94%:** Wyższe CR niż Cross-network (1,31%). Wartościowy ruch bez identyfikacji kanału.

6. **PWA bez UTM:** `pwa/(not set)`: 23 019 sesji, 731 transakcji, 172 000 PLN — ruch z Progressive Web App nieoznaczony UTM.

7. **Mobile gap:** Desktop CR 3,19% vs Mobile CR 1,50% — 2,13× różnica przy 89,3% udziale mobile.

8. **Produkty:** TOP 20 wg wyświetleń to Okrycia Wierzchnie, Komplety, Sukienki Eleganckie — sezonowość wiosna 2026.

9. **SALESmanago/referral 20 410 sesji:** Błędna klasyfikacja — web push/linki SALESmanago bez UTM wpadają jako referral.

10. **TikTok 7 wariantów:** Brak spójnego UTM. `tiktok?utm_id/paid` — malformed URL z utm_id w source zamiast parametrze.
