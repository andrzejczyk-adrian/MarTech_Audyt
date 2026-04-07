# Dane surowe: patrizia-aryton — 2026-04-07

**GA4 Property:** G-93NK3C48R3 (ID: 326801658)
**Okres:** ostatnie 30 dni (8 marca – 7 kwietnia 2026)
**Platforma:** Shoper | CMP: Cookiebot

---

## GA4 — Zdarzenia (30d) — TOP 33

| Zdarzenie | Liczba | Liczba/użytkownik |
|-----------|--------|-------------------|
| page_view | 1 383 032 | 8.26 |
| user_engagement | 853 971 | 7.23 |
| view_item_list | 842 117 | 11.56 |
| session_start | 675 526 | 4.03 |
| first_visit | 614 131 | 3.04 |
| view_item | 590 185 | 5.99 |
| **login** | **459 045** | **4.28** ⚠️ bardzo wysoka liczba |
| scroll | 238 296 | 3.82 |
| menu_click | 152 646 | 6.02 |
| form_start | 54 683 | 4.64 |
| Click - Znajdz w salonie | 34 869 | 4.84 |
| add_to_cart | 32 653 | 5.55 |
| view_search_results | 12 033 | 3.98 |
| form_submit | 11 362 | 3.15 |
| slider_klik | 9 688 | 1.82 |
| add_to_wishlist | 8 262 | 5.13 |
| view_cart | 5 281 | 3.60 |
| search | 2 470 | 3.09 |
| **add_shipping_info** | **2 132** | 3.76 ❌ > begin_checkout |
| mailalert_button_click | 1 865 | 2.00 |
| **purchase** | **1 582** | 1.73 ❌ > add_payment_info |
| click | 1 538 | 1.87 |
| product-desc | 1 408 | 1.82 |
| **begin_checkout** | **1 296** | 2.00 ❌ niższe niż add_shipping_info |
| dołącz do PL | 1 043 | 6.56 |
| **add_payment_info** | **806** | 1.71 ❌ niższe niż begin_checkout |
| slider_klik_kropki | 698 | 3.79 |
| snippet_text | 592 | 1.20 |
| file_download | 560 | 1.45 |
| remove_from_cart | 383 | 2.34 |
| Blog | 76 | 3.80 |
| sign_up | 24 | 1.00 |
| refund | 13 | — |

**⚠️ LEJEK — ANOMALIE KRYTYCZNE:**
- `add_shipping_info` (2 132) > `begin_checkout` (1 296) = **matematycznie niemożliwe**
- `purchase` (1 582) > `add_payment_info` (806) = **niemożliwe bez duplikacji**
- `login` (459 045) na ~316 tys. sesji = podejrzanie wysoka liczba, prawdopodobnie trigger przy każdym załadowaniu strony dla zalogowanych

---

## GA4 — Źródła ruchu (30d) — TOP 15

| source | medium | sessions | transactions | revenue (PLN) | CR |
|--------|--------|----------|--------------|---------------|----|
| google | cpc | 132 384 | 91 | 95 560 | 0.07% |
| google | organic | 74 329 | 168 | 234 013 | 0.23% |
| facebook | cpc | 57 699 | 25 | 34 433 | 0.04% |
| edrone | email | 17 457 | 40 | 51 771 | 0.23% |
| (direct) | (none) | 16 376 | 18 | 20 139 | 0.11% |
| **(not set)** | **(not set)** | **8 057** | 29 | 34 954 | — |
| bing | organic | 2 801 | 22 | 26 428 | 0.79% |
| (data not available) | (data not available) | 2 310 | 0 | 0 | — |
| sms | smsapi | 1 735 | 0 | 0 | 0% ❌ |
| m.facebook.com | referral | 1 722 | 5 | 4 220 | — |
| l.instagram.com | referral | 1 645 | 1 | 1 198 | — |
| l.facebook.com | referral | 690 | 0 | 0 | — |
| pl.search.yahoo.com | referral | 615 | 2 | 2 633 | — |
| google | maps | 540 | 2 | 3 527 | — |
| lm.facebook.com | referral | 381 | 0 | 0 | — |

**% (not set): 2.52%** (8 057 sesji z 319 640 łącznie)

**⚠️ PROBLEMY WYKRYTE W ŹRÓDŁACH:**
- **(not set)/(not set): 8 057 sesji** — Consent Mode niezgodny z konfiguracją Cookiebot
- **Meta fragmentation — co najmniej 7 wariantów:**
  - `facebook/cpc` (57 699), `m.facebook.com/referral` (1 722), `l.instagram.com/referral` (1 645), `l.facebook.com/referral` (690), `lm.facebook.com/referral` (381), `facebook/referral` (363), `facebook.com/referral` (86), `pl-pl.facebook.com/referral` (4)
  - Łącznie: ~62 590 sesji podzielone na 7 wierszy = zaburzone raportowanie
- **sms/smsapi: 1 735 sesji, 0 transakcji** — UTM nie działa lub SMS nie ma linków śledzących
- **Malformed UTM source (cały URL jako source):**
  - `google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|_Aryton&utm_id=19091733253&utm_term=kurtka patrizia aryton...` — 3 sesje
  - `google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|_Aryton&...płaszcze patrizia aryton...` — 2 sesje
  - **To wskazuje na brak proper URL encoding w linkach lub błąd w przekazywaniu UTM**
- **dev18.arytondev.local/referral: 10 sesji** — ruch deweloperski nie jest wykluczony
- **arytonpl.sharepoint.com/referral: 28 sesji** — ruch wewnętrzny firmy
- **klarna/referral: 71 sesji** — bramka płatnicza nie jest wykluczona z referrali
- **Bramki pocztowe jako referral:** poczta.onet.pl (198), poczta.interia.pl (80), poczta.o2.pl (76), poczta.wp.pl (46)
- **newsletter/email: 6 sesji** — zduplikowany kanał email obok edrone/email

---

## GA4 — Transakcje (weryfikacja duplikatów)

| Metryka | Wartość |
|---------|---------|
| Unikalnych transaction ID | 1 503 |
| `transactions` (deduplikowane) | **413** |
| `ecommercePurchases` (raw eventy) | **1 582** |
| **Ratio ecommercePurchases:transactions** | **❌ 3.83x** |
| Transakcje bez ID (`not set`) | 1 |
| ID zduplikowane (transactions > 1) | 0 |
| Łączny przychód | 515 556 PLN |
| **AOV (Average Order Value)** | **1 248 PLN** |

**❌ KRYTYCZNE: ratio 3.83x** — jeden zakup generuje ~3.83 eventy `purchase`. To kontynuacja problemu z poprzedniego audytu (04-03 ratio: 3.53x). Problem **NIE został naprawiony** przez 4 dni od poprzedniego raportu.

**Przyczyna:** Podwójne wdrożenie GA4 — hardcoded `gtag` w HTML ORAZ tag GA4 w GTM. Każda transakcja jest śledzona 2+ razy.

---

## GA4 — Lejek zakupowy per kanał (30d)

| Kanał | sessions | addToCarts | checkouts | purchases | CR (sess→purch) |
|-------|----------|------------|-----------|-----------|-----------------|
| Cross-network | 125 604 | 5 357 | 247 | 255 | 0.20% |
| Organic Search | 79 134 | 13 693 | 570 | 683 | **0.86%** |
| Paid Social | 57 699 | 4 207 | 136 | 186 | 0.32% |
| Email | 17 470 | 3 302 | 142 | 178 | **1.02%** |
| Direct | 16 376 | 2 290 | 45 | 122 | 0.75% |
| Unassigned | 8 081 | 1 374 | 47 | 45 | 0.56% |
| Organic Social | 4 879 | 508 | 19 | 24 | 0.49% |
| Paid Search | 4 458 | 900 | 47 | 46 | 1.03% |
| Display | 3 996 | 498 | 25 | 22 | 0.55% |
| SMS | 1 737 | 332 | 3 | 5 | 0.29% |
| Referral | 1 072 | 191 | 15 | 15 | 1.40% |
| Organic Shopping | 89 | 1 | 0 | 1 | — |
| Organic Video | 45 | 0 | 0 | 0 | — |

**UWAGA:** Wartości `purchases` w tej tabeli to `ecommercePurchases` (raw eventy), nie deduplikowane `transactions`. Rzeczywista liczba zamówień jest ~3.83x niższa.

**Obserwacje:**
- Cross-network (125 604 sesji) = PMax — dominuje ruchem, ale CR zaledwie 0.20%
- Organic Search najsilniejszy kanał jakościowy: 683 zakupów, przychód 269 722 PLN
- Email (edrone): CR 1.02%, przychód 51 771 PLN — dobry kanał retencji
- SMS: 1 737 sesji, 5 zakupów (ecommercePurchases) = anomalia, prawdopodobnie 0 PLN revenue

---

## GA4 — Top 20 miast

| Miasto | sessions | purchases | revenue (PLN) | CR | AOV |
|--------|----------|-----------|---------------|----|-----|
| Warsaw | 69 712 | 381 | 118 823 | 0.55% | 312 PLN |
| Wroclaw | 25 748 | 140 | 22 748 | 0.54% | 162 PLN |
| Krakow | 18 168 | 72 | 21 588 | 0.40% | 300 PLN |
| Poznan | 17 077 | 89 | 31 750 | 0.52% | 357 PLN |
| Gdansk | 15 529 | 57 | 19 421 | 0.37% | 341 PLN |
| (not set) | 15 168 | 80 | 17 123 | — | — |
| Katowice | 13 964 | 45 | 5 110 | 0.32% | 114 PLN |
| Lodz | 12 407 | 56 | 15 243 | 0.45% | 272 PLN |
| Bydgoszcz | 10 226 | 36 | 1 408 | 0.35% | 39 PLN ❌ |
| Lublin | 6 339 | 28 | 2 602 | 0.44% | 93 PLN ❌ |
| Szczecin | 5 306 | 25 | 9 399 | 0.47% | 376 PLN |
| Rzeszow | 5 233 | 15 | 4 412 | 0.29% | 294 PLN |
| Kielce | 3 486 | 28 | 11 599 | 0.80% | 414 PLN |
| Torun | 3 477 | 24 | 6 560 | 0.69% | 273 PLN |

**⚠️ Anomalie:** Bydgoszcz AOV 39 PLN, Lublin AOV 93 PLN — podejrzanie niskie, prawdopodobnie duplikaty lub błędy w danych o przychodzie per transakcję.

---

## GA4 — Produkty (e-commerce) — TOP 20

| itemId | itemName | itemCategory | itemsViewed | itemsPurchased | itemRevenue |
|--------|----------|--------------|-------------|----------------|-------------|
| 26307 | Zielona sukienka midi z jedwabiu | Odzież | 7 052 | **0** | **0 PLN** |
| 23308 | Beżowe sneakersy z plecionej skóry | Buty i torby | 1 956 | **0** | **0 PLN** |
| 23231 | Śmietankowa dopasowana sukienka midi | Odzież | 1 802 | **0** | **0 PLN** |
| 23234 | Czarne buty slingback z plecionej skóry | Buty i torby | 1 662 | **0** | **0 PLN** |
| 26078 | Brązowe buty slingback z zamszowej skóry | Buty i torby | 1 655 | **0** | **0 PLN** |
| 26351 | Brązowa torebka ze skóry zamszowej | Buty i torby | 1 376 | **0** | **0 PLN** |
| 26347 | Biała luźna sukienka z dzianiny | Odzież | 1 313 | **0** | **0 PLN** |
| 26350 | Zielona torebka ze skóry zamszowej | Buty i torby | 1 309 | **0** | **0 PLN** |
| 23427 | Luźna sukienka midi w deseń | Odzież | 1 199 | **0** | **0 PLN** |
| 26365 | Beżowe skórzane baleriny na niskim obcasie | Buty i torby | 1 167 | **0** | **0 PLN** |
| 26427 | Niebieskie zwężane jeansy z wysokim stanem | Odzież | 1 110 | **0** | **0 PLN** |
| 26415 | Czarne dzianinowe spodnie cullote | Odzież | 1 098 | **0** | **0 PLN** |
| 26345 | Białe jeansy barrel z wysokim stanem | Odzież | 1 091 | **0** | **0 PLN** |
| 26392 | Granatowy pudełkowy żakiet w tenis | Odzież | 1 069 | **0** | **0 PLN** |
| 26304 | Zielona kurtka puchowa z kołnierzem | Płaszcze i kurtki | 1 052 | **0** | **0 PLN** |
| 26400 | Koszula w brązowe paski z lnem | Odzież | 977 | **0** | **0 PLN** |
| 26357 | Zielone sneakersy ze skóry zamszowej | Buty i torby | 974 | **0** | **0 PLN** |
| 26444 | Zielone spodnie z lnu i lyocellu | Odzież | 930 | **0** | **0 PLN** |
| 26204 | Beżowa dwurzędowa kurtka z wełny | Płaszcze i kurtki | 900 | **0** | **0 PLN** |
| 23404 | Szara sukienka midi z jedwabiu | Odzież | 898 | **0** | **0 PLN** |

**❌ KRYTYCZNE: 100% produktów ma itemsPurchased = 0 i itemRevenue = 0 PLN**

Całkowity przychód z GA4 to 515 556 PLN (z metryk transakcyjnych), ale w danych product-level NIE MA ŻADNEGO przychodów. Oznacza to że event `purchase` wysyła dane transakcji (transaction_id, revenue) bez wypełnionej tablicy `items[]`. Analiza BCG, produktowa i kategorialna jest całkowicie niemożliwa.

---

## GA4 — Urządzenia (30d)

| Urządzenie | sessions | purchases (raw) | revenue (PLN) | CR | udział revenue |
|-----------|----------|-----------------|---------------|----|----------------|
| mobile | 249 319 | 942 | 314 523 | 0.38% | 61% |
| desktop | 62 954 | 631 | 200 534 | 1.00% | 39% |
| tablet | 4 615 | 9 | 499 | 0.20% | <1% |

CR desktop (1.00%) vs mobile (0.38%) = **2.6x różnica** — wskazuje na problemy UX na mobile lub niekompletne śledzenie mobile.

---

## GA4 — Top 10 Landing Pages

| Landing Page | sessions | purchases (raw) | revenue (PLN) |
|--------------|----------|-----------------|---------------|
| / (strona główna) | 85 033 | 544 | 207 244 |
| /kolekcja/effortless-mood | 19 953 | 8 | 2 696 |
| /c/390-nowosci | 18 636 | 53 | 24 680 |
| /c/414-spodnie | 16 866 | 4 | 719 |
| /c/705-promocja | 16 275 | 22 | 7 000 |
| /c/412-bluzki | 13 909 | — | — |

Strona główna dominuje jako landing page (85 033 sesji, 207 244 PLN) — wysoki ruch bezpośredni i brandowy przez stronę główną.

---

## Notatki — pierwsze obserwacje

### 🔴 KRYTYCZNE (wymagają natychmiastowej naprawy):

1. **Duplikaty purchase event (ratio 3.83x):** Problem istnieje od co najmniej audytu 04-03-2026 i NIE ZOSTAŁ NAPRAWIONY. Każdy zakup generuje ~3.83 eventów purchase. Analityka e-commerce jest fundamentalnie uszkodzona.

2. **itemRevenue = 0 PLN dla WSZYSTKICH produktów (50 z 50 sprawdzonych):** Event purchase nie przekazuje tablicy `items[]` z cenami. Analiza produktowa, BCG, kategorialna — wszystko niemożliwe. Brakuje co najmniej 515 556 PLN przychodów w raportowaniu produktowym.

3. **Anomalia lejka:** add_shipping_info (2 132) > begin_checkout (1 296) — lejek zakupowy jest rozbity. Niemożliwa rzetelna analiza konwersji per etap.

4. **Malformed UTM source:** Cały URL Google Ads jako `sessionSource` (np. `google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|...`) — broken URL encoding w linkach kampanii.

### 🟡 WAŻNE:

5. **(not set) 2.52%:** 8 057 sesji bez atrybukcji — Cookiebot nie przekazuje prawidłowo zgody do GA4 Consent Mode v2.

6. **Meta fragmentation:** 7 wariantów źródeł Facebook (~62 590 sesji łącznie) — zaburzone raportowanie efektywności kampanii Meta.

7. **Ruch deweloperski:** dev18.arytondev.local w referral — 10 sesji; arytonpl.sharepoint.com — 28 sesji.

8. **Bramki płatnicze w referral:** klarna (71 sesji), poczta.onet.pl (198 sesji) — transakcje mogą być przypisywane do złych źródeł.

9. **SMS: 0 transakcji z 1 735 sesji** — prawdopodobnie brak UTM tracking lub linki SMS nie działają poprawnie.

10. **login event: 459 045** — potencjalnie triggerowany wielokrotnie per sesję dla zalogowanych użytkowników.
