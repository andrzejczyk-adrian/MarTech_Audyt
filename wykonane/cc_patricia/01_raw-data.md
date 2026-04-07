# Dane surowe: patrizia.aryton.pl — 20260407

> **Źródło:** GA4 Data API (property 326801658 / stream G-93NK3C48R3) | Okres: 30d (08.03.2026 – 07.04.2026)
> **Brak dostępu:** GTM Admin, Google Ads Customer ID, BDOS

---

## GA4 — KPI ogólne (30d)

| Wskaźnik | Wartość | Uwaga |
|---|---|---|
| Sesje łącznie | **320 607** | suma kanałów |
| ecommercePurchases (raw event) | **1 582** | BEZ deduplikacji |
| transactions (unique transactionId) | **413** | z deduplikacją GA4 |
| purchaseRevenue | **515 556 PLN** | |
| addToCarts | **32 652** | |
| begin_checkout | **1 296** | |
| purchase events / transactions | **3,83x** | ⚠️ KRYTYCZNE |
| CR (transactions / sesje) | **0,13%** | |
| AOV | **1 249 PLN** | 515 556 / 413 |

---

## GA4 — Zdarzenia (30d) — TOP 33

| Zdarzenie | Liczba | Liczba/użytkownik |
|-----------|--------|-------------------|
| page_view | 1 382 942 | 8,26 |
| user_engagement | 853 900 | 7,23 |
| view_item_list | 842 079 | 11,56 |
| session_start | 675 482 | 4,03 |
| first_visit | 614 091 | 3,04 |
| view_item | 590 146 | 5,99 |
| login | 459 013 | 4,28 |
| scroll | 238 284 | 3,82 |
| menu_click | 152 640 | 6,02 |
| form_start | 54 682 | 4,64 |
| Click - Znajdz w salonie | 34 868 | 4,84 |
| add_to_cart | 32 652 | 5,55 |
| view_search_results | 12 030 | 3,98 |
| form_submit | 11 361 | 3,15 |
| slider_klik | 9 688 | 1,82 |
| add_to_wishlist | 8 261 | 5,13 |
| view_cart | 5 281 | 3,60 |
| search | 2 470 | 3,09 |
| add_shipping_info | **2 131** | 3,76 ⚠️ |
| mailalert_button_click | 1 865 | 2,00 |
| **purchase** | **1 582** | 1,73 |
| click | 1 538 | 1,87 |
| product-desc | 1 408 | 1,82 |
| **begin_checkout** | **1 296** | 2,00 ⚠️ |
| dołącz do PL | 1 043 | 6,56 |
| add_payment_info | 806 | 1,71 |
| slider_klik_kropki | 698 | 3,79 |
| snippet_text | 592 | 1,20 |
| file_download | 560 | 1,45 |
| remove_from_cart | 383 | 2,34 |
| Blog | 76 | 3,80 |
| sign_up | 24 | 1,00 |
| refund | 13 | — |

### ⚠️ Anomalie lejka zakupowego

| Etap | Liczba | Kolejny / poprzedni | Status |
|------|--------|---------------------|--------|
| add_to_cart | 32 652 | — | OK |
| view_cart | 5 281 | 16,2% ATC → view_cart | OK |
| **add_shipping_info** | **2 131** | — | ❌ > begin_checkout |
| **begin_checkout** | **1 296** | — | ❌ < add_shipping_info |
| add_payment_info | 806 | 62,2% checkout → payment | ⚠️ |
| **purchase** | **1 582** | **122,1% begin_checkout** | ❌ NIEMOŻLIWE |
| transactions | 413 | 26,1% checkout | ⚠️ |

**purchase (1 582) > begin_checkout (1 296) → fizycznie niemożliwe. Potwierdza duplikację purchase events.**
**add_shipping_info (2 131) > begin_checkout (1 296) → implementacja odwrócona lub firing rule błędna.**

---

## GA4 — Transakcje (weryfikacja duplikatów)

| Metryka | Wartość |
|---|---|
| Łączne wiersze (unique transactionId) | 1 503 |
| ecommercePurchases (suma) | 1 582 |
| transactions (suma) | 413 |
| Ratio ecommercePurchases:transactions | **3,83x** |
| (not set) transactionId | **1 wiersz → 92 purchase events, 0 transactions** |
| Malformed IDs (`&key=…`) | **1 088 / 1 503 (72,4%)** |
| Revenue (suma) | 515 556 PLN |

### Przykłady malformed transaction ID:
```
210032&key=1abe2783234b4109f15a80bdd3246c14
210033&key=1abe2783234b4109f15a80bdd3246c14
210034&key=1abe2783234b4109f15a80bdd3246c14
210035&key=1abe2783234b4109f15a80bdd3246c14
```
**72,4% transakcji ma ID z parametrem URL `&key=…` — błąd w DataLayer na stronie potwierdzenia zamówienia. PrestaShop zwraca URL z query string zamiast czystego ID zamówienia.**

### (not set) transactionId:
- 92 purchase events bez żadnego transaction ID → 0 zliczonych transactions
- Prawdopodobnie hardcoded `gtag('event', 'purchase')` bez danych e-commerce

---

## GA4 — Źródła ruchu (30d) — TOP 50 wierszy (109 łącznie)

| Source | Medium | Sessions | Purchases | Revenue PLN |
|--------|--------|----------|-----------|-------------|
| google | cpc | 132 384 | 320 | 95 560 |
| google | organic | 74 329 | 608 | 234 013 |
| facebook | cpc | 57 699 | 186 | 34 433 |
| edrone | email | 17 457 | 178 | 51 771 |
| (direct) | (none) | 16 366 | 122 | 20 139 |
| **(not set)** | **(not set)** | **8 053** | 45 | 34 954 |
| bing | organic | 2 801 | 46 | 26 428 |
| (data not available) | (data not available) | 2 302 | 3 | 0 |
| sms | smsapi | 1 735 | 5 | **0** |
| m.facebook.com | referral | 1 722 | 10 | 4 220 |
| l.instagram.com | referral | 1 645 | 5 | 1 198 |
| l.facebook.com | referral | 690 | 1 | 0 |
| pl.search.yahoo.com | referral | 615 | 13 | 2 633 |
| google | maps | 540 | 8 | 3 527 |
| lm.facebook.com | referral | 381 | 0 | 0 |
| facebook | referral | 363 | 6 | 1 737 |
| poczta.onet.pl | referral | 198 | 3 | 0 |
| ig | social | 112 | 2 | 0 |
| ntp.msn.com | referral | 88 | 6 | 3 121 |
| facebook.com | referral | 86 | 0 | 0 |
| poczta.interia.pl | referral | 80 | 2 | 0 |
| klarna | referral | 71 | 1 | **0** |
| zasobygwp.pl | referral | 78 | 2 | 305 |
| statics.teams.cdn.office.net | referral | 72 | 0 | 0 |
| instagram | referral | 54 | 0 | 0 |
| **arytonpl.sharepoint.com** | referral | 28 | 0 | 0 |
| **dev18.arytondev.local** | referral | 10 | 0 | 0 |

**% (not set): 8 053 / 320 607 = 2,5%** — akceptowalny poziom, ale (data not available) = 2 302 sesji to dodatkowa wpadka Consent Mode.

### Problemy UTM / Source:
- **Meta fragmentacja**: `facebook/cpc` (57 699) + `m.facebook.com/referral` (1 722) + `lm.facebook.com/referral` (381) + `facebook/referral` (363) + `facebook.com/referral` (86) = co najmniej **5 wariantów**
- **sms/smsapi: revenue = 0 PLN** przy 5 purchases — tracking nie przesyła revenue
- **Klarna referral** — nie wykluczony z referral exclusions → sesje po Klarna są przypisywane do referral zamiast do oryginalnego źródła
- **arytonpl.sharepoint.com** — ruch wewnętrzny (SharePoint Aryton), nie filtrowany
- **dev18.arytondev.local** — środowisko developerskie, nie filtrowane jako internal traffic

---

## GA4 — Lejek zakupowy per kanał (30d)

| Kanał | Sessions | Add to Cart | Checkout | Purchases | CR Purch |
|-------|----------|-------------|----------|-----------|----------|
| **Cross-network** | 125 584 | 5 356 | 247 | 255 | **0,20%** |
| Organic Search | 79 134 | 13 693 | 570 | 683 | **0,86%** |
| Paid Social | 57 699 | 4 207 | 136 | 186 | **0,32%** |
| Email | 17 470 | 3 302 | 142 | 178 | **1,02%** |
| Direct | 16 366 | 2 290 | 45 | 122 | **0,75%** |
| Unassigned | 8 079 | 1 374 | 47 | 45 | 0,56% |
| Organic Social | 4 879 | 508 | 19 | 24 | 0,49% |
| **Paid Search** | **4 457** | 900 | 47 | 46 | **1,03%** |
| Display | 3 996 | 498 | 25 | 22 | 0,55% |
| SMS | 1 737 | 332 | 3 | 5 | 0,29% |
| Referral | 1 072 | 191 | 15 | 15 | 1,40% |
| Organic Shopping | 89 | 1 | 0 | 1 | 1,12% |
| Organic Video | 45 | 0 | 0 | 0 | — |

**⚠️ ANOMALIA Cross-network:** 125 584 sesji (39% całego ruchu) — prawdopodobnie PMax / kampanie Performance Max przypisywane do Cross-network zamiast do Paid Search / Shopping. Przy CR 0,20% i 255 purchase eventach — bardzo niska efektywność.

**⚠️ ANOMALIA Direct → checkout:** 16 366 sesji → tylko 45 checkout (0,27% ATC→checkout) vs Email 142/3302 (4,3%) — anomalia wskazuje na problem z atrybucją lub tracking Direct.

---

## GA4 — Zaangażowanie per kanał (30d)

| Kanał | Sessions | Użytkownicy | Nowi | Eng. Sessions | Avg Session Duration |
|-------|----------|-------------|------|---------------|---------------------|
| Cross-network | 125 584 | 92 326 | 60 149 | 54 065 | **5:52** |
| Organic Search | 79 134 | 40 510 | 27 886 | 46 536 | **21:42** ✅ |
| Paid Social | 57 699 | 26 084 | 16 713 | 23 732 | 12:01 |
| Email | 17 470 | 6 270 | 4 114 | 10 104 | **32:23** ✅ |
| Direct | 16 366 | 8 800 | 5 932 | 9 804 | 26:46 |
| Unassigned | 8 079 | 6 297 | 1 724 | 2 720 | 23:03 |
| Organic Social | 4 879 | 3 431 | 1 638 | 2 437 | 12:56 |
| Paid Search | 4 457 | 2 645 | 1 327 | 2 766 | **40:35** ✅✅ |
| Display | 3 996 | 2 191 | 855 | 2 031 | 18:34 |
| SMS | 1 737 | 518 | 422 | 890 | 33:05 |
| Referral | 1 072 | 446 | 290 | 651 | 42:49 |

**Cross-network: 5:52 avg session duration** — najkrótsza z kanałów płatnych. Przy 39% ruchu = podejrzane.

---

## GA4 — Produkty (TOP 20 viewowanych, 30d)

| itemId | Produkt | Kategoria | Viewed | Purchased | Revenue |
|--------|---------|-----------|--------|-----------|---------|
| 26307 | Zielona sukienka midi z jedwabiu | Odzież | 7 052 | **0** | **0** |
| 23308 | Beżowe sneakersy z plecionej skóry | Buty i torby | 1 955 | **0** | **0** |
| 23231 | Śmietankowa dopasowana sukienka midi | Odzież | 1 801 | **0** | **0** |
| 23234 | Czarne buty slingback | Buty i torby | 1 662 | **0** | **0** |
| 26078 | Brązowe buty slingback zamszowe | Buty i torby | 1 655 | **0** | **0** |
| 26351 | Brązowa torebka zamszowa | Buty i torby | 1 376 | **0** | **0** |
| 26347 | Biała luźna sukienka z dzianiny | Odzież | 1 313 | **0** | **0** |
| 26350 | Zielona torebka zamszowa | Buty i torby | 1 309 | **0** | **0** |
| 23427 | Luźna sukienka midi w deseń | Odzież | 1 199 | **0** | **0** |
| 26365 | Beżowe skórzane baleriny | Buty i torby | 1 167 | **0** | **0** |

**❌ KRYTYCZNE: itemsPurchased = 0 i itemRevenue = 0 dla WSZYSTKICH 2 691 produktów.**
Brak items array w purchase event — shopping analytics całkowicie zepsute. Niemożliwa analiza: top produktów, kategorii, marż, feed produktowy.

---

## Notatki — pierwsze obserwacje

1. **Duplikacja purchase 3,83x** — gorsze niż w audycie 03.04 (było 3,53x). Problem nie został naprawiony.
2. **72,4% malformed transactionId** — PrestaShop URL query string (`&key=`) trafia jako transaction ID. Prawdopodobnie pobierany przez JS z `window.location` lub `document.referrer` zamiast z DataLayer.
3. **purchase > begin_checkout** — fizycznie niemożliwe. Potwierdza wielokrotne odpalenie purchase event per sesja.
4. **Items array zepsuty** — 0 purchased dla WSZYSTKICH produktów. Tracking produktów całkowicie niefunkcjonalny.
5. **Consent Mode v2 bez widocznego CMP** — wszystko denied by default, brak bannera w HTML. Użytkownicy nie mogą dać zgody → dane zamodelowane zamiast rzeczywistych.
6. **Cross-network = 125 584 sesji (39% ruchu)** — największy kanał, najniższe zaangażowanie. Prawdopodobnie PMax bez właściwej klasyfikacji.
7. **Internal traffic** — dev18.arytondev.local + arytonpl.sharepoint.com nie filtrowane.
8. **Klarna + poczta.onet.pl + poczta.interia.pl** — bramki nie wykluczone z referral.
9. **SMS channel: revenue = 0 PLN** — 5 zakupów przez SMS ale przychód = 0 → tracking broken.
10. **sign_up = 24 w 30d** — bardzo mało, warto sprawdzić czy rejestracja jest poprawnie śledzona.
