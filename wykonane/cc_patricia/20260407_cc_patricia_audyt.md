# Audyt MarTech — Patrizia Aryton (patrizia.aryton.pl)

**Data audytu:** 07.04.2026
**Audytor:** Adrian Andrzejczyk
**GA4 Property ID:** 326801658 | **Measurement ID:** G-93NK3C48R3
**GTM Container:** GTM-MDGSP8
**URL strony:** https://patrizia.aryton.pl/
**Typ biznesu:** E-commerce premium (odzież damska)
**Platforma:** PrestaShop
**Okres analizy danych:** 08.03.2026 – 07.04.2026 (30 dni)
**Poprzedni audyt:** 03.04.2026 — wynik: 62/138 pkt (45%) ❌ Krytyczny

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE

### Wyniki sekcji

| Sekcja | Uzyskane | Max (dostępne) | Wynik % | Ocena |
|--------|---------|----------------|---------|-------|
| 1. Audyt Wstępny | 11 | 27 | 41% | ❌ Krytyczny |
| 2. ePrivacy / Consent Mode | 18 | 45 | 40% | ❌ Krytyczny |
| 3. Konfiguracja GA4 + GTM | 17 | 54 | 31% | ❌ Krytyczny |
| 4. Data Quality | 40 | 75 | 53% | ⚠️ Wymaga poprawy |
| 5. UTM | 13 | 18 | 72% | ⚠️ Wymaga poprawy |
| 6. BCG | — | — | 🔒 Brak dostępu | — |
| 7. Lejki | 3 | 8 | 38% | ❌ Krytyczny |
| 8. GA4↔Ads | — | — | 🔒 Brak dostępu | — |
| 9. Analiza | — | — | ⚠️ Ograniczone | — |
| 10. Google Ads | — | — | 🔒 Brak dostępu | — |
| **ŁĄCZNIE** | **102** | **227** | **45%** | **❌ Krytyczny** |

### CZY DANYM MOŻNA UFAĆ?

**Nie — dane e-commerce są systemowo zaburzone i wymagają natychmiastowej naprawy.**

Wykryto trzy nakładające się na siebie problemy krytyczne, które łącznie uniemożliwiają wiarygodną analizę wyników sprzedaży:

**1. Duplikacja zdarzenia purchase (ratio 3.83x)** — hardcoded tag GA4 w kodzie HTML PrestaShop PLUS tag GA4 przez GTM powoduje, że każde zdarzenie `purchase` jest wysyłane do GA4 wielokrotnie. Ratio ecommercePurchases:transactions = 3.83x (wykryty w audycie 03.04 jako 3.53x — problem nie naprawiony, a ratio wzrosło).

**2. 72.4% malformed transaction IDs** — PrestaShop przekazuje do systemu śledzenia URL strony potwierdzenia zamówienia (np. `210032&key=1abe2783...`) zamiast samego numeru zamówienia. W efekcie 1 088 z 1 503 unikalnych transakcji jest nieidentyfikowalnych i nieanalizowalnych w GA4.

**3. Dane produktowe całkowicie zepsute** — `itemsPurchased = 0` i `itemRevenue = 0` dla wszystkich 2 691 produktów w bazie przez 30 dni. Niemożliwa jakakolwiek analiza produktowa.

| Obszar | Wiarygodność | Uzasadnienie |
|---|---|---|
| Sesje i ruch | ✅ Wiarygodne | Niezależne od duplikacji purchase |
| Kanały pozyskania | ⚠️ Częściowo | Fragmentacja Meta, webmaile w referral |
| Liczba transakcji (`transactions`) | ⚠️ Zaniżone | 72.4% malformed ID = niepoliczalne |
| Przychód (`purchaseRevenue`) | ⚠️ Zaniżone | Część bez ID → revenue = 0 |
| Liczba eventów purchase | ❌ Zawyżone 3.83x | Duplikacja |
| Lejek e-commerce | ❌ Zepsuty | purchase > begin_checkout |
| Dane produktowe | ❌ Całkowicie zepsute | 0 purchased dla wszystkich produktów |

---

## CZĘŚĆ II — WYNIKI AUDYTU PER SEKCJA

---

### SEKCJA 1 — Audyt Wstępny (11/27 pkt = 41% ❌)

#### Co sprawdzamy i dlaczego

Sekcja 1 to przegląd podstaw infrastruktury śledzenia: jakie narzędzia marketingowe są zainstalowane na stronie, czy działają poprawnie, czy nie ma konfliktów technicznych i czy konfiguracja odpowiada dobrym praktykom. To odpowiednik przeglądu technicznego samochodu przed sezonem — identyfikujemy co jest sprawne, co wymaga regulacji i co jest zepsute.

#### Kluczowe ustalenia

**Duplikacja GA4 — bezpośrednia przyczyna ratio 3.83x**

Na stronie patrizia.aryton.pl GA4 jest wdrożone na dwa różne sposoby jednocześnie:
- Bezpośrednio w kodzie HTML PrestaShop: `gtag('config', 'G-93NK3C48R3', {'send_page_view': true})`
- Przez kontener Google Tag Manager (GTM-MDGSP8)

To jak posiadanie dwóch kasjerów rejestrujących tę samą sprzedaż — każda transakcja pojawia się w systemie dwa lub więcej razy. W efekcie zdarzenie `purchase` odpala się 3.83 razy per unikalną transakcję. Wszystkie raporty e-commerce w GA4 pokazują fałszywe wartości.

**Brak bannera zgody cookie — naruszenie RODO**

W kodzie HTML strony nie ma widocznego bannera CMP (Cookie Management Platform). Wprawdzie Consent Mode v2 jest technicznie skonfigurowany (wszystkie kategorie domyślnie "odmówione"), ale bez bannera użytkownik nie może ani wyrazić, ani odmówić zgody. Efekt: system nigdy nie przechodzi w tryb "zgoda udzielona" → GA4 zbiera wyłącznie zamodelowane dane anonimowe. Moduł psgdpr (PrestaShop GDPR) jest zainstalowany, ale banner nie wyświetla się.

**Struktura danych e-commerce (DataLayer) — zepsuta tablica produktów**

Dla 30 dni audytu: `itemsPurchased = 0` i `itemRevenue = 0` dla wszystkich 2 691 produktów w bazie GA4. Tablica `items[]` w zdarzeniu `purchase` jest prawdopodobnie pusta lub w ogóle nie wysyłana. Może to wynikać z konfliktu między hardcoded `gtag('event', 'purchase')` (który nie zawiera danych produktowych) a wersją przez GTM.

**Co działa dobrze:**
- Jeden kontener GTM (GTM-MDGSP8) — bez duplikacji GTM ✅
- Brak Universal Analytics (UA) — czysty stack GA4 ✅
- Meta Pixel 268133950519975 aktywny + CAPI (server-side tracking) ✅
- Google Ads conversion tag AW-769585117 aktywny ✅
- Google Ads + Meta = kompletna infrastruktura reklamowa ✅

---

### SEKCJA 2 — ePrivacy / Consent Mode (18/45 pkt = 40% ❌)

#### Co sprawdzamy i dlaczego

ePrivacy to obszar zgodności z prawem unijnym — RODO i ePrivacy Directive. Chodzi o to czy strona respektuje prawo użytkownika do decydowania o tym, jakie dane o nim zbieramy. Consent Mode v2 to techniczny mechanizm Google, który pozwala "rozmawiać" systemowi śledzenia z decyzją użytkownika wyrażoną przez baner cookie. Bez prawidłowej implementacji firma naraża się na kary UODO (do 4% rocznego obrotu lub 20 mln EUR) i traci wiarygodne dane analityczne.

#### Kluczowe ustalenia

**Consent Mode v2 — implementacja techniczna poprawna, praktyczna zepsuta**

Technicznie Consent Mode v2 jest wdrożony wzorowo. W kodzie HTML jako PIERWSZY element pojawia się:
```javascript
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'analytics_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'wait_for_update': 500
})
```
To jest dokładnie taka kolejność i zawartość jaką rekomenduje Google. Wszystkie 4 kategorie zgód Consent Mode v2 są obecne.

**Problem: brak bannera = system nigdy nie przechodzi w tryb "granted"**

Bez wizualnego bannera użytkownik nie ma możliwości kliknięcia "Akceptuj" lub "Odmów". W efekcie `analytics_storage` pozostaje `denied` dla 100% użytkowników na zawsze. GA4 zbiera wyłącznie zamodelowane dane anonimowe — widoczne w GA4 jako 2 302 sesje oznaczone "(data not available)".

Moduł psgdpr (PrestaShop GDPR) jest zainstalowany w kodzie, ale banner nie renderuje się. Możliwe przyczyny: błąd konfiguracji modułu, konflikt z innym pluginem, wyłączony rendering bannera przez ustawienia sklepu.

**Brak url_passthrough — zaniżanie ROAS kampanii**

Bez włączonego `url_passthrough: true` użytkownicy, którzy odmówili zgody (czyli 100% przy braku bannera), nie przekazują parametrów kampanii przez URL do GA4. Oznacza to że cały ruch kampanii reklamowych jest zaniżony o zasięg użytkowników bez cookies. Przy skali kampanii Google Ads (132 384 sesji CPC) to istotne zaniżenie mierzalnego ROAS.

**Co działa:**
- Consent Mode v2 z 4 kategoriami zgód: domyślnie denied ✅
- Prawidłowa kolejność inicjalizacji w HTML (consent przed GTM) ✅
- Brak danych osobowych w URL-ach, UTM-ach i zdarzeniach ✅
- Anonimowe "pingi" GA4 po odmowie (modelowanie) działa ✅

---

### SEKCJA 3 — Konfiguracja GTM i GA4 (17/54 pkt = 31% ❌)

#### Co sprawdzamy i dlaczego

Konfiguracja GTM i GA4 to fundament całego systemu śledzenia. Nawet jeśli dane zbieramy i banery mamy poprawne, błędna konfiguracja może sprawić że dane trafiają do niewłaściwych miejsc, są zaburzone przez wewnętrzny ruch firmowy, lub że sesje z różnych źródeł są nieprawidłowo atrybowane. To jak sprawdzenie czy wszystkie rury w instalacji wodnej są prawidłowo podłączone — zatkana rura w jednym miejscu może zaburzyć przepływ w całym systemie.

#### Kluczowe ustalenia

**Problem 1: GA4 hardcoded + GTM = podwójna konfiguracja (KRYTYCZNE)**

Główna przyczyna wszystkich problemów z danymi e-commerce. Ustawienie "Ignorowanie zduplikowanych konfiguracji" w GA4 → Strumień → Zarządzaj tagiem ma być pierwszą linią obrony, ale nie zastępuje usunięcia hardcoded tagu. Kompletna naprawa wymaga dwóch kroków:
1. Usunięcie `gtag('config', 'G-93NK3C48R3')` z kodu HTML PrestaShop (moduł/template)
2. Upewnienie się że GA4 jest wysyłany wyłącznie przez GTM

**Problem 2: Klarna nie wykluczona z cross-domain / referral**

Klarna to bramka płatności działająca na osobnej domenie. Gdy klient wraca ze strony Klarna do patrizia.aryton.pl po sfinalizowaniu płatności, GA4 traktuje to jako nową sesję z referral źródła "klarna". W danych widoczne: 71 sesji klarna/referral, 1 purchase z revenue = 0 PLN. To oznacza że transakcja nie jest przypisana do oryginalnego kanału pozyskania (np. Google Ads CPC) ale do "klarna/referral".

Naprawa: GA4 → Strumień → Konfigurowanie tagów → Lista domen / Referral exclusion → dodać: `klarna.com`, `pay.klarna.com`.

**Problem 3: Webmaile w referral exclusion — brak wykluczeń**

W danych GA4 widoczne cztery serwisy poczty internetowej jako źródła ruchu (referral):
- poczta.onet.pl: 198 sesji, 3 purchases, 0 PLN revenue
- poczta.interia.pl: 80 sesji, 2 purchases, 0 PLN revenue
- poczta.wp.pl: 46 sesji, 3 purchases, 719 PLN revenue
- poczta.o2.pl: 46 sesji, 1 purchase, 0 PLN revenue

Łącznie 370 sesji i 9 zakupów nieprawidłowo przypisanych do referral zamiast do kanału email (eDrone). Użytkownik klikający link w emailu na onet.pl jest traktowany jako przychodzący z onet.pl (referral), nie z eDrone (email). Zaniżenie skuteczności email marketingu.

**Problem 4: Ruch wewnętrzny nie filtrowany**

W danych GA4 widoczne dwa źródła wewnętrzne:
- `dev18.arytondev.local / referral`: 10 sesji — środowisko deweloperskie PrestaShop
- `arytonpl.sharepoint.com / referral`: 28 sesji — wewnętrzny SharePoint Aryton (pracownicy)

Łącznie 38 sesji ze źródeł firmowych zaburza dane. Brak filtra IP w GA4 → Admin → Filtry danych.

**Problem 5: Brak mikro-konwersji**

Na podstawie poprzedniego audytu: jako konwersje w GA4 oznaczony jest wyłącznie `purchase`. Brak `add_to_cart` i `begin_checkout` jako konwersji pośrednich uniemożliwia algorytmom Google Smart Bidding optymalizację kampanii na wcześniejsze etapy lejka zakupowego. Szczególnie ważne dla kampanii PMax, które stanowią ~39% całego ruchu (Cross-network: 125 584 sesji).

**Co działa dobrze:**
- Jeden kontener GTM — bez duplikacji GTM ✅
- Waluta PLN ustawiona ✅
- BigQuery eksport aktywny ✅
- Google Ads połączone z GA4 ✅
- Model atrybucji Data-Driven (DDA) ✅
- Brak Universal Analytics ✅

---

### SEKCJA 4 — Data Quality (40/75 pkt = 53% ⚠️)

#### Co sprawdzamy i dlaczego

Jakość danych to serce każdego audytu MarTech. Najlepsza konfiguracja techniczna jest bezużyteczna jeśli dane które zbieramy są nieprawidłowe, zduplikowane lub niekompletne. Sprawdzamy czy liczby w GA4 odzwierciedlają rzeczywistość: czy transakcje są prawidłowo liczone, czy ID zamówień są unikalne i poprawne, czy lejek zakupowy ma sens logiczny, czy atrybucja kanałów jest właściwa.

#### Kluczowe ustalenia

**KPI ogólne (30 dni, 08.03–07.04.2026):**

| Wskaźnik | Wartość | Ocena |
|---|---|---|
| Sesje łącznie | 320 607 | ✅ |
| ecommercePurchases (raw, zduplikowane) | 1 582 | ❌ zawyżone 3.83x |
| Transakcje (unikalne, deduplikowane) | 413 | ⚠️ zaniżone 72% malformed |
| Przychód | 515 556 PLN | ⚠️ częściowy |
| addToCarts | 32 652 | ✅ |
| begin_checkout | 1 296 | ✅ |
| CR (transactions/sesje) | 0,13% | ❌ za niskie |
| AOV | 1 249 PLN | ✅ spójne z premium |

**Analiza duplikacji transaction ID:**

Z 1 503 unikalnych transaction ID w bazie GA4:
- 1 088 (72,4%) — malformed: format `210032&key=1abe2783234b4109f15a80bdd3246c14`
- 414 (27,5%) — czyste ID zamówień (np. `210032`)
- 1 (0,1%) — (not set): 92 purchase events bez ID

**Skąd bierze się malformed ID?** PrestaShop na stronie potwierdzenia zamówienia (thank-you page) generuje URL w formacie: `https://patrizia.aryton.pl/zamowienie-potwierdzenie?id_order=210032&key=1abe2783...`. Skrypt zbierający transaction ID pobiera cały ciąg `id_order=210032&key=...` zamiast tylko `210032`. Prawdopodobna przyczyna: GTM Variable pobierający `Page URL` lub `Query String` zamiast właściwej zmiennej DataLayer.

**Krytyczna anomalia produktowa:**

W 30-dniowym oknie analizy, dla wszystkich 2 691 produktów w katalogu:
- `itemsPurchased` = 0
- `itemRevenue` = 0

To nie jest przypadkowy błąd jednego produktu — to systemowe niefunkcjonowanie tablicy `items[]` w zdarzeniu `purchase`. Możliwe przyczyny:
1. Hardcoded `gtag('event', 'purchase')` wysyła purchase bez parametrów ecommerce
2. GTM pobiera items z DataLayer który jest pusty lub ma inną strukturę niż oczekiwana
3. Konflikt między dwoma instancjami GA4 powoduje że items z jednej instancji "przepadają"

**Anomalie lejka zakupowego:**

| Etap | Zdarzenia | Przejście | Benchmark | Status |
|------|-----------|-----------|-----------|--------|
| add_to_cart | 32 652 | — | — | ✅ |
| view_cart | 5 281 | 16,2% | 10-30% | ✅ |
| begin_checkout | 1 296 | 3,97% ATC→CO | 30-60% | ❌ Bardzo niski |
| add_payment_info | 806 | 62,2% CO→PA | 70-90% | ⚠️ |
| purchase (events) | 1 582 | 122,1% CO→PU | 50-80% | ❌ NIEMOŻLIWE |
| transactions | 413 | 31,9% CO→TRX | 50-80% | ❌ |

Krok `add_to_cart → begin_checkout` = 3,97% (32 652 → 1 296) jest drastycznie poniżej benchmarku 30-60%. Oznacza to że tylko 4 z 100 klientów którzy dodali produkt do koszyka przechodzi do realizacji zamówienia. Możliwe przyczyny:
- Koszyk niewidoczny lub trudny w użyciu
- Begin_checkout nie odpalany na właściwym etapie (zbyt późno w procesie)
- Klienci porzucają koszyk i wracają do zakupów przez inne kanały
- Usterka w triggerze GTM dla begin_checkout

**Struktura ruchu — kanały:**

| Kanał | Sesje | % | CR (ecommPurch) | Avg Duration |
|-------|-------|---|---------|------|
| Cross-network (PMax) | 125 584 | **39,2%** | 0,20% | 5:52 |
| Organic Search | 79 134 | 24,7% | 0,82% | 21:42 |
| Paid Social | 57 699 | 18,0% | 0,32% | 12:01 |
| Email | 17 470 | 5,5% | 1,02% | 32:23 |
| Direct | 16 366 | 5,1% | 0,75% | 26:46 |

Dominacja Cross-network (39% ruchu) z bardzo niskim zaangażowaniem (5:52 avg duration, CR 0,20%) sugeruje że kampanie PMax przyciągają ruch słabej jakości lub są skierowane na zbyt szerokie audience. Email marketing wykazuje najwyższy CR (1,02%) przy solidnej liczbie sesji (17 470) — to kanał wymagający skalowania.

---

### SEKCJA 5 — UTM (13/18 pkt = 72% ⚠️)

#### Co sprawdzamy i dlaczego

UTM (Urchin Tracking Module) to "metki" przyklejane do linków reklamowych, które pozwalają GA4 zidentyfikować skąd pochodzi każdy użytkownik. Bez prawidłowych UTM-ów nie wiemy czy klient przyszedł z reklamy Facebook, emaila czy posta organicznego. To bezpośrednio wpływa na możliwość obliczenia ROI każdego kanału marketingowego i podejmowania decyzji budżetowych.

#### Kluczowe ustalenia

**Co działa poprawnie:**

- **Google Ads**: `google/cpc` = 132 384 sesji — kampanie Google Ads mają poprawne UTM. Ruch płatny Google jest identyfikowalny i atrybuowalny.
- **Email (eDrone)**: `edrone/email` = 17 457 sesji — eDrone prawidłowo taguje linki emailowe. Atrybuacja email marketingu działa.
- **Google Maps/GMB**: `google/maps` = 540 sesji — wizytówka Google Business Profile jest identyfikowalna. Rzadko spotykane, dobrze.
- **Facebook Ads**: `facebook/cpc` = 57 699 sesji — kampanie płatne Meta mają UTM.

**Problemy:**

**Fragmentacja Meta — 6 wariantów zamiast max 2:**

```
facebook / cpc          57 699 sesji  ✅ (kampanie z UTM)
m.facebook.com/referral  1 722 sesji  ❌ (mobile bez UTM)
l.facebook.com/referral    690 sesji  ❌ (link preview)
lm.facebook.com/referral   381 sesji  ❌ (link preview mobile)
facebook / referral        363 sesji  ❌ (kliknięcia bez UTM)
facebook.com / referral     86 sesji  ❌ (bez UTM)
```

Razem **3 242 sesji Meta bez UTM** (5,3% ruchu Meta). GA4 traktuje je jako 5 różnych źródeł, co zaniża mierzone metryki kampanii Facebook Ads.

**SMS channel — problem z revenue:**
`sms/smsapi` = 1 735 sesji, 5 purchases, revenue = 0 PLN. UTM jest prawidłowy (identyfikujemy kanał SMS), jednak system e-commerce nie przekazuje wartości zamówień dla sesji oznaczonych tym kanałem. Problem leży w tracking purchase, nie w UTM.

---

### SEKCJA 7 — Lejki zakupowe (3/8 pkt = 38% ❌)

#### Co sprawdzamy i dlaczego

Analiza lejków zakupowych to spojrzenie na "podróż klienta" od wejścia na stronę do finalizacji zakupu. Każdy etap (przeglądanie produktów → dodanie do koszyka → realizacja zamówienia → zakup) powinien mieć naturalną liczbę użytkowników — każdy kolejny krok musi być mniejszy od poprzedniego. Anomalie w lejku wskazują na problemy z UX, błędy w implementacji śledzenia lub źródła niejakościowego ruchu.

#### Kluczowe ustalenia

**Anomalia 1: purchase > begin_checkout (122.1%)**

Matematycznie niemożliwe aby więcej osób dokonało zakupu niż zaczęło proces realizacji zamówienia. Wynik 122.1% potwierdza że zdarzenie `purchase` odpala się wielokrotnie per transakcję — np. przy każdym odświeżeniu strony potwierdzenia, lub przez oba tagi GA4 (hardcoded + GTM). To główny dowód na duplikację.

**Anomalia 2: add_shipping_info > begin_checkout (2131 > 1296)**

Zdarzenie `add_shipping_info` (wybór metody dostawy) pojawia się w liczbie wyższej niż `begin_checkout` (wejście w checkout). To logicznie niemożliwe w prawidłowym lejku. Możliwa przyczyna: trigger dla `add_shipping_info` odpala się poza procesem checkout (np. na stronie koszyka przy każdym wyborze opcji) lub `begin_checkout` jest zbyt późno rejestrowany.

**Drop-off checkout (tylko 31.9% kończy zakup):**

Używając wiarygodnej metryki `transactions` (413) vs `begin_checkout` (1 296): tylko **31.9% klientów który zaczął checkout dokonuje zakupu** (benchmark: 50-80%). Co się stało z 68.1% (883 klientów)?

Możliwe przyczyny:
1. Problem z UX procesu zamówienia (zbyt wiele kroków, brak preferred payment methods)
2. Problemy techniczne z bramką Klarna
3. Wymagana rejestracja konta przed zakupem (checkout guest może być trudny)
4. Koszty dostawy widoczne dopiero w checkout (surprise shipping cost)
5. Brak zaufanych metod płatności

Przy obecnym revenue 515 556 PLN/msc: jeśli checkout drop-off poprawimy z 68% do 50% (realny cel), przychód wzrośnie proporcjonalnie o ~24% = **+123 000 PLN/msc**.

**CR paid vs. organic:**

- CR organic (Google): 608/74 329 = 0.82%
- CR Google CPC: 320/132 384 = 0.24% → tylko **29% CR organic**

Ruch płatny z Google konwertuje 3.4x gorzej niż ruch organiczny. Benchmark: ruch płatny powinien konwertować min 50% tyle co organiczny. Możliwe przyczyny: złe landing pages dla kampanii, zbyt szeroka publiczność w PMax, niedopasowanie reklamy do strony.

---

## CZĘŚĆ III — REKOMENDACJE

### 🔴 Natychmiast (0–7 dni) — zatamowanie strat

**1. Usunięcie hardcoded tagu GA4 z HTML PrestaShop**

To jest PRIORYTET nr 1 całego audytu. Wszystkie inne metryki e-commerce będą zaburzone dopóki ten problem nie zostanie naprawiony.

*Jak:* W szablonie PrestaShop (plik `header.tpl` lub moduł Google Analytics) znaleźć i usunąć linię `gtag('config', 'G-93NK3C48R3', {'send_page_view': true})`. Zachować tylko `gtag('consent', 'default', {...})` jako inicjalizację Consent Mode. GA4 powinno być wysyłane wyłącznie przez GTM.

*Weryfikacja:* Po wdrożeniu sprawdzić w GA4 Debug View czy ratio purchase:transakcje zbliży się do 1:1.

**2. Naprawa malformed transactionId w PrestaShop**

*Jak:* Na stronie potwierdzenia zamówienia (thank-you page) sprawdzić jak GTM pobiera transaction ID. Zamiast pobierać całą wartość `id_order=210032&key=...` z URL, skrypt powinien pobierać tylko wartość po `id_order=` i przed `&`. W GTM: zmienna JavaScript pobierająca `{{URL Query - id_order}}` (nie cały query string).

*Alternatywnie:* Deweloper PrestaShop powinien dodać do DataLayer push na stronie thank-you:
```javascript
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: '{{CZYSTE_ID_ZAMOWIENIA}}',  // np. '210032'
    value: {{WARTOSC_ZAMOWIENIA}},
    currency: 'PLN',
    items: [...]
  }
});
```

**3. Naprawa tablicy items[] w purchase event**

*Jak:* Na stronie potwierdzenia zamówienia PrestaShop musi pushować do DataLayer kompletne dane produktowe:
```javascript
ecommerce: {
  items: [{
    item_id: '26307',
    item_name: 'Zielona sukienka midi z jedwabiu',
    price: 599.00,
    quantity: 1,
    item_category: 'Odzież'
  }]
}
```
GTM następnie przesyła te dane do GA4. Bez tego niemożliwa optymalizacja kampanii Shopping/PMax.

**4. Wdrożenie bannera CMP**

*Jak:* Naprawić konfigurację modułu psgdpr lub zastąpić go certyfikowanym CMP (rekomendacja: Cookiebot — integracja z PrestaShop dostępna jako moduł, cena ~60-120 EUR/rok). Banner musi zawierać: kategorie zgód, opcję odrzucenia wszystkich, opcję zmiany decyzji w stopce.

---

### 🟡 Miesiąc 1 — optymalizacja i naprawa

**5. Dodanie referral exclusions**

GA4 → Strumień → Konfigurowanie tagów → Lista referrals do wykluczenia:
- `klarna.com`, `pay.klarna.com` (bramka płatności)
- `wp.pl`, `onet.pl`, `interia.pl`, `o2.pl` (webmaile)
- `arytonpl.sharepoint.com` (ruch wewnętrzny)

**6. Włączenie url_passthrough**

W GTM: Tag GA4 Configuration → dodać pole konfiguracji `url_passthrough: true`. Lub bezpośrednio w hardcoded gtag (po naprawie — tylko jeden tag powinien zostać).

**7. Filtry ruchu wewnętrznego**

GA4 → Admin → Filtry danych → Ruch wewnętrzny → dodać:
- Adresy IP biura Aryton
- IP agencji marketingowej
- Reguła dla arytonpl.sharepoint.com

**8. Ujednolicenie UTM dla Meta**

W panelu Meta Ads: upewnić się że WSZYSTKIE kampanie i zestawy reklam mają UTM: `utm_source=facebook&utm_medium=cpc`. Sprawdzić reklamy bez UTM (źródło fragmentacji na 5 wariantów referral).

**9. Dodanie mikro-konwersji w GA4**

GA4 → Admin → Konwersje → Oznacz jako konwersje: `add_to_cart` (wartość 0), `begin_checkout` (wartość 0). Poprawi optymalizację kampanii PMax i Smart Bidding.

**10. Analiza checkout drop-off**

Po naprawie duplikacji: uruchomić raport lejka w GA4 Explore → Funnel Exploration. Zidentyfikować dokładny krok gdzie odpada 68% klientów. Rozważyć:
- Włączenie guest checkout (bez rejestracji)
- Uproszczenie procesu do 2-3 kroków
- Dodanie popularnych metod płatności (BLIK, PayPo, Przelewy24)

---

### 🟢 Miesiąc 2–3 — skalowanie i strategia

**11. Analiza produktowa po naprawie items[]**

Po naprawie tablicy items: uruchomić raporty produktowe w GA4 → Zarabianie → E-commerce zakupy. Zidentyfikować top produkty, kategorie, bestsellery per kanał.

**12. Optymalizacja kampanii Cross-network/PMax**

Przy 39% ruchu i CR 0,20% (najniższy), kampanie PMax wymagają przeglądu:
- Weryfikacja audience signals
- Sprawdzenie asset groups i ich jakości
- Rozważenie podziału na oddzielne kampanie Shopping + Performance Max

**13. Skalowanie email marketingu**

Email wykazuje CR 1,02% (najwyższy z płatnych kanałów) przy 17 470 sesjach. Potencjał do skalowania bazy eDrone i zwiększenia częstotliwości wysyłek.

**14. Wdrożenie BigQuery Analytics**

BigQuery jest aktywny. Po naprawie jakości danych: zbudować raporty w Looker Studio łączące BigQuery + dane kosztowe Google Ads i Meta Ads → pełny widok ROAS per kanał, per kampania, per produkt.

---

## CZĘŚĆ IV — Aneks techniczny

### Stack MarTech (wykryty z HTML)

| Narzędzie | ID / Wersja | Status |
|-----------|------------|--------|
| Google Tag Manager | GTM-MDGSP8 | ✅ Aktywny |
| GA4 (GTM) | G-93NK3C48R3 | ✅ Aktywny |
| GA4 (hardcoded) | G-93NK3C48R3 | ❌ Duplikat — do usunięcia |
| Google Ads Conversion | AW-769585117 | ✅ Aktywny |
| Meta Pixel | 268133950519975 | ✅ Aktywny |
| Meta CAPI (server-side) | /module/facebookconversiontrackingplus/ | ✅ Aktywny |
| eDrone | appId: 626a8093e4423 | ✅ Aktywny |
| Klarna | clientId present | ✅ Aktywny |
| DPD | iframe widget | ✅ Aktywny |
| psgdpr | PrestaShop GDPR moduł | ⚠️ Baner niewidoczny |
| Universal Analytics | — | ✅ Usunięty |
| Consent Mode v2 | default: denied | ⚠️ Techniczny OK, brak CMP |

### Dane GA4 — Transakcje (30d)

| Metryka | Wartość |
|---|---|
| Unique transaction IDs | 1 503 |
| Z czego malformed (`&key=...`) | 1 088 (72,4%) |
| Z czego (not set) | 1 wiersz (92 purchase events) |
| Z czego czyste ID | 414 (27,5%) |
| ecommercePurchases (suma) | 1 582 |
| transactions (GA4 deduplikowane) | 413 |
| Ratio | **3,83x** |
| Revenue łączny | 515 556 PLN |
| AOV (per transaction) | 1 249 PLN |
