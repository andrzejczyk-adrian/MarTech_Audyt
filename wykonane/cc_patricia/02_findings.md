# Findings: patrizia.aryton.pl — 20260407

> **Źródła danych:** GA4 API (property 326801658), WebFetch HTML (patrizia.aryton.pl), poprzedni audyt 2026-04-03
> **Brak dostępu:** GTM Admin, GA4 Admin panel, Google Ads

---

## SEKCJA 1 — Audyt Wstępny

### 1.1 Adnotacje w GA4
- **Status:** 🔒 Brak dostępu do GA4 Admin
- **Wynik:** 0/3 pkt
- **Komentarz:** Brak dostępu do panelu GA4 Admin → weryfikacja niemożliwa. Poprzedni audyt (03.04) nie odnotował informacji o adnotacjach. Przy skali problemów (duplikacja purchase, malformed IDs, items[] broken) adnotacje byłyby kluczowe do śledzenia zmian wdrożeniowych.
- **Rekomendacja:** Zapewnić dostęp Viewer do GA4 Admin. Dodać adnotacje przy każdej zmianie GTM.

### 1.2 Kolejność skryptów HTML
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** Z analizy HTML wynika że GA4 jest wdrożone podwójnie: hardcoded `gtag('config', 'G-93NK3C48R3')` bezpośrednio w HTML ORAZ przez GTM-MDGSP8. Consent Mode `gtag('consent', 'default', {...})` jest obecny jako pierwszy element (poprawnie), jednak po nim pojawia się bezpośredni tag GA4 poza GTM. Taka konfiguracja narusza zasadę jednego źródła prawdy i jest bezpośrednią przyczyną ratio 3.83x.
- **Rekomendacja:** Usunąć hardcoded `gtag('config', 'G-93NK3C48R3')` z HTML PrestaShop. GA4 powinno być wyłącznie przez GTM. Zostawić tylko `gtag('consent', 'default', {...})` jako inicjalizację Consent Mode.

### 1.3 Przegląd podstron (ograniczony — WebFetch)
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/3 pkt
- **Komentarz:** Weryfikacja przez WebFetch (statyczny HTML, bez JS execution) zamiast DevTools. Na stronie głównej brak krytycznych błędów w HTML. Jednak pośredni dowód problemów JS: items[] w purchase events zepsuty (0 itemsPurchased dla 2 691 produktów) = błąd w DataLayer na stronie potwierdzenia zamówienia. Weryfikacja DevTools przez klienta wymagana.
- **Rekomendacja:** Klient powinien otworzyć DevTools → Console na stronie thank-you i sprawdzić zawartość `dataLayer` po zakupie, szczególnie pole `ecommerce.items[]`.

### 1.4 Google Tag Assistant
- **Status:** 🔒 Brak dostępu
- **Wynik:** 0/1 pkt
- **Komentarz:** Wymaga weryfikacji po stronie klienta lub agencji.

### 1.5 TagHound
- **Status:** ❌ Błąd (pośredni dowód z danych)
- **Wynik:** 0/3 pkt
- **Komentarz:** Dane GA4 potwierdzają duplikację GA4: ratio ecommercePurchases:transactions = 3.83x. TagHound potwierdziłby podwójne ładowanie tagu G-93NK3C48R3 na każdej podstronie. Na stronie głównej wykryto GTM-MDGSP8 + hardcoded gtag = 2 instancje GA4 na każdej stronie.
- **Rekomendacja:** Uruchomić TagHound na: homepage, kategoria, produkt, koszyk, thank-you. Oczekiwany wynik: podwójny tag GA4.

### 1.6 Consent Mode — wstępna weryfikacja
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/2 pkt
- **Komentarz:** W HTML strony brak jakiegokolwiek widocznego bannera zgody cookie. Consent Mode v2 jest implementowany technicznie (wszystkie kategorie `denied` by default, `wait_for_update: 500ms`), jednak bez banera CMP użytkownicy nie mogą wyrazić ani odmówić zgody. W praktyce: `analytics_storage` pozostaje `denied` dla wszystkich użytkowników na zawsze → GA4 zbiera wyłącznie modelowane dane anonimowe. Widoczne w danych: 2 302 sesji jako "data not available" (modelowane bez zgody).
- **Impact PLN:** Ryzyko RODO: brak możliwości zbierania danych bez mechanizmu zgody = niezgodność z UODO. Potencjalna kara do 20 mln EUR lub 4% obrotu.
- **Rekomendacja:** Natychmiastowe wdrożenie bannera CMP (Cookiebot / OneTrust / Usercentrics) lub naprawa modułu psgdpr PrestaShop który ma renderować baner.

### 1.7 Brak starych kodów UA
- **Status:** ✅ OK
- **Wynik:** 1/1 pkt
- **Komentarz:** W HTML strony brak identyfikatorów Universal Analytics (UA-XXXXXX) i requestów do analytics.js. GA4 wdrożone jako jedyna platforma GA. Poprawa względem starszych wdrożeń Aryton.

### 1.8 DataLayer — poprawność
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/3 pkt
- **Komentarz:** `window.dataLayer = window.dataLayer || []` widoczny w HTML. Zdarzenia push-owane przez GTM. Jednak pośredni dowód problemu: items[] w purchase events całkowicie puste (0 itemsPurchased dla wszystkich 2 691 produktów) → DataLayer push na stronie thank-you prawdopodobnie nie zawiera tablicy `ecommerce.items[]`. Bezpośrednia weryfikacja przez DevTools wymagana.
- **Rekomendacja:** Sprawdzić `dataLayer` na stronie potwierdzenia zamówienia: `dataLayer.filter(e => e.event === 'purchase')` → czy pole `ecommerce.items` jest wypełnione.

### 1.9 DataLayer GA4 — struktura e-commerce
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** `itemsPurchased = 0` i `itemRevenue = 0` dla WSZYSTKICH 2 691 unikalnych produktów w bazie GA4 przez 30 dni. Oznacza to, że tablica `items[]` w zdarzeniu `purchase` jest albo pusta, albo w ogóle nie wysyłana do GA4. Możliwa przyczyna: hardcoded `gtag('event', 'purchase')` wysyła purchase bez `ecommerce.items[]`, podczas gdy GTM próbuje pobrać items z DataLayer który jest pusty lub niepoprawny.
- **Impact PLN:** Niemożliwa analiza: które produkty się sprzedają, które kategorie generują przychód, jakie marże, feed reklamowy produktowy. To uniemożliwia optymalizację kampanii Shopping i PMax.
- **Rekomendacja:** Sprawdzić DataLayer na thank-you page. Upewnić się że `ecommerce.items[]` zawiera: `item_id`, `item_name`, `price`, `quantity`. Usunąć hardcoded purchase event bez items.

### 1.11 Remarketing Google Ads
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** Conversion tag Google Ads `AW-769585117` wykryty w HTML (`gtag('config', 'AW-769585117')`). Remarketing aktywny.

### 1.12 Konwersje Google Ads w GTM
- **Status:** 🔒 Brak dostępu do GTM
- **Wynik:** 0/3 pkt

### 1.13 Meta Pixel
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** Meta Pixel ID `268133950519975` wykryty w HTML z prawidłową inicjalizacją `fbq('init', ...)`. Zdarzenia: AddToCart, PageView, Pagetime (co 30 sekund). Pixel działa.

### 1.14 Meta — API konwersji (CAPI)
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** Server-side tracking przez AJAX do endpointu `/module/facebookconversiontrackingplus/` — to jest CAPI przez moduł PrestaShop Facebook Conversions API. Implementacja po stronie serwera = prawidłowe zduplikowanie eventów client-side + server-side.

### 1.19 Bing/Microsoft Ads
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/2 pkt
- **Komentarz:** Bing organic widoczny w GA4: 2 801 sesji, 46 purchases, 26 428 PLN revenue (3. kanał organiczny). Świadczy o obecności na Bing. Jednak tag UET (Universal Event Tracking) Bing Ads nie wykryty w HTML → możliwe że brak kampanii Bing lub brak tagu.
- **Rekomendacja:** Sprawdzić czy prowadzone są kampanie Bing Ads. Jeśli tak — wdrożyć UET tag przez GTM.

**Sekcja 1 — Łącznie:** ~11/27 pkt dostępnych = ~41% ❌

---

## SEKCJA 2 — ePrivacy / Consent Mode

### 2.1 Personalizacja wyboru zgód
- **Status:** ❌ Błąd
- **Wynik:** 0/1 pkt
- **Komentarz:** Brak bannera CMP → brak możliwości personalizacji zgód.

### 2.2 Możliwość odrzucenia wszystkich zgód
- **Status:** ❌ Błąd
- **Wynik:** 0/1 pkt
- **Komentarz:** Brak bannera = brak przycisku odrzucenia.

### 2.3 Strona domyślnie zablokowana
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** Brak bannera CMP = brak blokady strony przed decyzją użytkownika. Użytkownik może przeglądać stronę bez jakiejkolwiek interakcji z mechanizmem zgody.

### 2.4 Poprawnie blokuje pliki cookies po odmowie
- **Status:** ⚠️ Częściowo
- **Wynik:** 1/3 pkt
- **Komentarz:** Technicznie Consent Mode v2 ma `analytics_storage: denied` by default → GA4 nie ustawia cookies _ga/_gid bez zgody. Jednak: (1) brak bannera = nikt nie może wyrazić zgody, (2) nie wiadomo czy Meta Pixel i Google Ads są blokowane bez zgody (wymaga DevTools). Pozytywne: hardcoded `gtag('consent', 'default', {...denied...})` jako pierwszy element HTML = prawidłowa kolejność techniczna.

### 2.5 Możliwość zmiany decyzji
- **Status:** ❌ Błąd
- **Wynik:** 0/1 pkt
- **Komentarz:** Brak bannera = brak możliwości zmiany decyzji.

### 2.6 Ustawienia domyślne — wymuszony wybór
- **Status:** ✅ OK (technicznie)
- **Wynik:** 2/2 pkt
- **Komentarz:** `gtag('consent', 'default', {ad_storage: 'denied', analytics_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied', wait_for_update: 500})` — wszystkie kategorie denied by default. To jest poprawna implementacja techniczna Consent Mode v2. Problem: brak bannera sprawia że to ustawienie nigdy nie jest zmieniane na 'granted'.

### 2.7 Brak cookies przed decyzją
- **Status:** ⚠️ Prawdopodobnie OK
- **Wynik:** 1/2 pkt
- **Komentarz:** Przy `analytics_storage: denied` domyślnie, GA4 nie powinien ustawiać _ga/_gid przed zgodą. Weryfikacja przez DevTools → Application → Storage wymagana.

### 2.8 Wywołanie consent update w DataLayer
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/2 pkt
- **Komentarz:** Consent default present. Sekwencja: `consent default` → brak bannera → brak `consent update`. Technicznie prawidłowa inicjalizacja, praktycznie niepełna bez CMP.

### 2.9 Brak odświeżania strony po zgodzie
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 0/2 pkt
- **Komentarz:** Brak bannera uniemożliwia test. Moduł psgdpr PrestaShop historycznie wymaga reload po zmianie zgód — do weryfikacji po naprawie bannera.

### 2.10 GA4 wywołuje się po zgodzie
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/3 pkt
- **Komentarz:** Przy prawidłowej implementacji Consent Mode v2 GA4 powinien oczekiwać na `consent update`. `wait_for_update: 500ms` jest ustawiony. Jednak duplikacja tagu GA4 (hardcoded + GTM) może powodować że jedno z wywołań ignoruje consent.

### 2.11 Brak podwójnego user_engagement po zgodzie
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/1 pkt (brak dowodów na problem)

### 2.12–2.15 (GTM consent settings)
- **Status:** 🔒 Brak dostępu do GTM
- **Wynik:** 0/9 pkt łącznie

### 2.16 PING w Consent Mode
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** W danych GA4 widoczne 2 302 sesji oznaczone jako "data not available" w source/medium — to anonimowe pinge GA4 wysyłane po odmowie zgody. Consent Mode modeluje te sesje. Mechanizm działa technicznie.

### 2.17 url_passthrough
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** `url_passthrough` nie wykryty w HTML (`gtag('set', 'url_passthrough', true)` ani w konfiguracji GTM). Bez url_passthrough użytkownicy odmawiający cookies nie są atrybowani do kampanii reklamowych → ROAS kampanii jest zaniżany dla użytkowników bez zgody. Przy braku bannera (0% użytkowników daje zgodę) = zaniżenie ROAS dla 100% ruchu.
- **Impact PLN:** Niedoszacowanie ROAS kampanii → błędne decyzje budżetowe.
- **Rekomendacja:** Dodać `url_passthrough: true` w tag GA4 Configuration w GTM.

### 2.18–2.20 Brak danych wrażliwych
- **Status:** ✅ ✅ ✅
- **Wynik:** 9/9 pkt
- **Komentarz:** Brak danych osobowych wykrytych w URL-ach, UTM-ach ani zdarzeniach GA4 w analizowanych danych.

**Sekcja 2 — Łącznie:** ~18/45 pkt = ~40% ❌

---

## SEKCJA 3 — Konfiguracja GTM i GA4

### 3A.1 Walidacja GTM
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** GTM-MDGSP8 wykryty jako jedyny kontener. `gtm.js?id=GTM-MDGSP8` ładowany asynchronicznie. Jeden kontener — prawidłowo.

### 3A.2 Błędy w GTM / 3A.3 Consent tagów / 3A.4–3A.6 / 3A.9 / 3A.11–3A.12
- **Status:** 🔒 Brak dostępu do GTM
- **Wynik:** 0 pkt łącznie

### 3A.7 Brak UA w GTM
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** Brak tagów Universal Analytics w kodzie HTML. GA4 jedyną platformą GA.

### 3A.8 GA4 przez GTM
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/1 pkt
- **Komentarz:** GA4 NIE jest wdrożone wyłącznie przez GTM. Hardcoded `gtag('config', 'G-93NK3C48R3', {'send_page_view': true})` bezpośrednio w HTML PrestaShop PLUS tag GA4 przez GTM-MDGSP8 = dwa aktywne tagi GA4 na każdej stronie. To bezpośrednia przyczyna duplikacji purchase events (ratio 3.83x). Problem identyczny jak w audycie 03.04 (było 3.53x) — **nie został naprawiony, a ratio wzrosło**.

### 3A.10 Brak zduplikowanych tagów
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** GA4 G-93NK3C48R3 jest zduplikowany: (1) hardcoded `gtag('config', 'G-93NK3C48R3')` w HTML + (2) tag GA4 Configuration w GTM. Każde zdarzenie (w tym `purchase`) jest wysyłane 2–4 razy do GA4. Ratio 3.83x sugeruje że purchase event odpala się nawet więcej niż 2 razy — możliwa dodatkowa duplikacja w samym GTM (trigger firing multiple times).
- **Impact PLN:** Wszystkie metryki e-commerce są zaburzone. Niemożliwa wiarygodna analiza CR, ROAS, lejka.

### 3C.3 Waluta PLN
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** `gtag('set', {'currency': "PLN", 'country': "PL"})` w HTML.

### 3C.4 Google Signals / 3C.2 / 3C.5–3C.7 / 3C.17 / 3C.20–3C.21
- **Status:** 🔒 Brak dostępu do GA4 Admin
- **Wynik:** 0 pkt (weryfikacja przez panel)
- **Komentarz:** Na podstawie poprzedniego audytu (03.04): Google Signals aktywne ✅, retencja 14 mies ✅, model DDA ✅, BigQuery aktywny ✅, Google Ads połączone ✅.

### 3C.8 Filtrowanie ruchu wewnętrznego
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** W danych GA4 widoczne 2 źródła ruchu wewnętrznego: `dev18.arytondev.local / referral` (10 sesji) i `arytonpl.sharepoint.com / referral` (28 sesji). Łącznie 38 sesji ze środowiska deweloperskiego i korporacyjnego SharePoint Aryton w danych produkcyjnych. Brak filtru IP w GA4 lub filtr niekompletny.
- **Rekomendacja:** GA4 → Admin → Filtry danych → dodać filtry dla IP biura Aryton, IP agencji i subdomen wewnętrznych.

### 3C.9 Strumień Web
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** Dane napływają regularnie — 30 dni danych bez przerwy.

### 3C.10 Cross-domain tracking
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** Klarna widoczna jako referral z 71 sesjami i 1 purchase = bramka płatności nie jest wykluczona z cross-domain tracking. Po powrocie z Klarna tworzona jest nowa sesja przypisana do `klarna/referral` zamiast do oryginalnego źródła. Klarna powinna być na liście referral exclusions.
- **Rekomendacja:** GA4 → Strumień → Konfigurowanie tagów → Referral exclusion → dodać: `klarna.com`, `pay.klarna.com`.

### 3C.11 Ignorowanie zduplikowanych konfiguracji
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** Przy duplikacji GA4 (hardcoded + GTM) ustawienie "Ignoruj duplikaty" w GA4 → Strumień → Zarządzaj tagiem powinno być włączone aby zapobiec podwójnemu liczeniu. Jeśli nie jest włączone, każde page_view i purchase liczy się 2x. Ratio 3.83x (a nie 2x) sugeruje że problem jest głębszy (trigger w GTM odpala purchase event wielokrotnie) ale "Ignoruj duplikaty" to pierwsza linia obrony.
- **Rekomendacja:** GA4 → Strumień → Zarządzaj tagiem → Zduplikowane konfiguracje → Ignoruj. ORAZ usunąć hardcoded tag z HTML.

### 3C.12 Wykluczenie bramek płatności
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** Klarna widoczna w referral (71 sesji, 1 purchase z revenue = 0 PLN). Brak wykluczenia w referral exclusion list. W danych brak innych bramek płatności (PayU, Przelewy24) co sugeruje że albo są wykluczone albo nieużywane.
- **Rekomendacja:** GA4 → Strumień → Referral exclusion → dodać wszystkie używane bramki płatności.

### 3C.13 Wykluczenie bramek pocztowych
- **Status:** ❌ Błąd
- **Wynik:** 0/2 pkt
- **Komentarz:** W referral widoczne 4 webmaile: `poczta.onet.pl` (198 sesji, 3 purchases), `poczta.interia.pl` (80 sesji, 2 purchases), `poczta.wp.pl` (46 sesji, 3 purchases), `poczta.o2.pl` (46 sesji, 1 purchase). Łącznie 370 sesji z poczty internetowej = ruch z emaili marketingowych eDrone/SMS trafia jako referral zamiast do kanału Email. Zaniżenie attribution email marketing.
- **Impact PLN:** 370 sesji z 9 purchases nieprawidłowo przypisanych = zakłócenie ROI email channel.
- **Rekomendacja:** GA4 → Referral exclusion → dodać: `wp.pl`, `onet.pl`, `interia.pl`, `o2.pl`.

### 3C.16 Zdarzenia jako konwersje
- **Status:** ⚠️ Częściowo
- **Wynik:** 1/2 pkt
- **Komentarz:** Na podstawie poprzedniego audytu: tylko `purchase` oznaczony jako konwersja. Brak `begin_checkout` i `add_to_cart` jako konwersji → niemożliwa optymalizacja kampanii na wcześniejsze etapy lejka. Dla PMax i Smart Bidding ważne są mikro-konwersje.
- **Rekomendacja:** Oznaczyć jako konwersje: `add_to_cart`, `begin_checkout`, `purchase` (z wartościami).

### 3C.18 Połączenie Google Ads
- **Status:** ✅ OK (wg poprzedniego audytu)
- **Wynik:** 3/3 pkt

### 3C.19 BigQuery
- **Status:** ✅ OK (wg poprzedniego audytu)
- **Wynik:** 3/3 pkt

### 3K BigQuery Quality
- **Status:** 🔒 Brak dostępu do BigQuery
- **Wynik:** 0/21 pkt

**Sekcja 3 — Łącznie (z dostępnych danych):** ~17/54 pkt dostępnych = ~31% ❌

---

## SEKCJA 4 — Data Quality

### 4A.1 Udział sesji (not set) <5%
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** `(not set)/(not set)` = 8 053 sesji / 320 607 łącznie = **2,5%**. Poniżej progu 5%. Akceptowalny poziom.

### 4A.4 Ruch wygląda naturalnie
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/3 pkt
- **Komentarz:** **Cross-network = 125 584 sesji (39,2% całego ruchu)** — największy kanał z najkrótszym czasem sesji (5:52) i najniższym CR (0,20%). To anomalia. Cross-network w GA4 = głównie PMax i Discovery. Przy 39% ruchu z avg session 5:52 (vs 21:42 dla organic) ruch jest mało zaangażowany. Wymaga weryfikacji czy kampanie PMax są właściwie skonfigurowane.

### 4A.5 Cross-domain własne domeny w referral
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** Brak własnych subdomen Aryton jako referral (za wyjątkiem dev i SharePoint — to ruch wewnętrzny, nie cross-domain).

### 4A.6 Ruch spamowy
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** Brak typowych domen spamowych. Rabatio.com (38 sesji), mariagajek.pl (35 sesji) — naturalne referrale porównywarkowe / lifestyle.

### 4A.7 Bramki płatności poza ścieżką
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** `klarna / referral` = 71 sesji, 1 purchase. Klarna jest aktywną bramką płatności i pojawia się w referral źródłach → nie jest wykluczona z referral exclusion.

### 4A.8 Bramki pocztowe poza ścieżką
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** `poczta.onet.pl` (198 sesji, 3 purch), `poczta.interia.pl` (80, 2), `poczta.wp.pl` (46, 3), `poczta.o2.pl` (46, 1). Łącznie **370 sesji / 9 purchases** z webmaili jako referral. Ruch z kliknięcia w link z webmaila powinien być przypisany do email/eDrone, nie referral.

### 4A.9 Facebook/Meta — unifikacja
- **Status:** ❌ Błąd
- **Wynik:** 0/2 pkt
- **Komentarz:** Meta widoczna jako **6 wariantów source/medium**: `facebook/cpc` (57 699 sesji) + `m.facebook.com/referral` (1 722) + `l.facebook.com/referral` (690) + `lm.facebook.com/referral` (381) + `facebook/referral` (363) + `facebook.com/referral` (86). Razem **60 941 sesji rozbitych na 6 wierszy**. GA4 traktuje je jako 6 różnych kanałów → zaniżone metryki Paid Social.
- **Impact PLN:** Rzeczywiste sesje Meta ~60 941 vs widoczne 57 699 → ~5,5% ruchu Meta nieprzypisane → zaniżone ROAS Facebook.

### 4B.1 Czas trwania sesji naturalny
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** Najniższy avg session duration: Cross-network 5:52 (352s). Referral 42:49 (2569s). Wartości powyżej 20s dla wszystkich kanałów → brak ruchu botowego.

### 4B.2 Engagement rate naturalny
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** Cross-network: 54 065/125 584 = 43% (OK). Organic: 46 536/79 134 = 59% ✅. Email: 10 104/17 470 = 58% ✅. Brak kanału poniżej 20%.

### 4B.3 CR naturalny
- **Status:** ❌ Błąd
- **Wynik:** 0/2 pkt
- **Komentarz:** CR (transactions/sesje) = 413/320 607 = **0,13%** — poniżej benchmarku 0,5% dla e-commerce. Nawet dla premium fashion (AOV 1 249 PLN) oczekiwane minimum to 0,3-0,5%. Prawdopodobna przyczyna: tracking transakcji zaniżony — 72,4% malformed IDs nie jest liczonych jako `transactions` przez GA4. Rzeczywisty CR mógłby być 3–4x wyższy.

### 4C.1 source/medium (not set) <5%
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** 2,5% — poniżej progu.

### 4C.2 direct/none <30%
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** `(direct)/(none)` = 16 366/320 607 = **5,1%**. Bardzo dobry poziom.

### 4C.3 Łączny (not set) + direct <40%
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** 2,5% + 5,1% = **7,6%**. Znacznie poniżej progu 40%.

### 4C.4 Transakcje (not set) <10%
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** (not set) sessions = 8 053, purchases = 45. 45/1 582 = **2,8%** purchase eventów z (not set) source. Akceptowalne.

### 4D.1 Ratio ecommercePurchases:transactions ≤1.1
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** Ratio = 1 582 / 413 = **3,83x** (benchmark ≤1.1). Każda unikalna transakcja generuje średnio 3,83 zdarzenia `purchase` w GA4. Ten sam błąd co w audycie 03.04 (było 3,53x) — **problem nie tylko nie naprawiony, ale ratio wzrosło o 0.3x w ciągu 4 dni**. Wzrost może wskazywać na dodatkową duplikację po stronie GTM (nowy trigger lub modyfikacja tagu).
- **Impact PLN:** Wszystkie metryki e-commerce (ecommercePurchases, CR, lejek) są zaburzone 3.83x. Kampanie optymalizowane na zawyżone dane = przepalone budżety.

### 4D.2 % transakcji bez transactionId <2%
- **Status:** ❌ Błąd
- **Wynik:** 0/3 pkt
- **Komentarz:** `(not set)` transactionId = 1 wiersz w danych → **92 purchase events bez ID** = 92/1 582 = **5,8%** (benchmark <2%). 92 eventów `purchase` wysłanych bez żadnych danych transakcyjnych. Prawdopodobnie hardcoded `gtag('event', 'purchase')` bez parametrów ecommerce.

### 4D.3 Brak malformed transactionId
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** **1 088 z 1 503 wierszy (72,4%) ma malformed transactionId**. Format: `210032&key=1abe2783234b4109f15a80bdd3246c14` — PrestaShop przekazuje do DataLayer URL strony potwierdzenia zamiast czystego ID zamówienia. URL zawiera `?id_order=210032&key=...`. Skrypt JS pobiera `window.location.search` lub `document.referrer` i przekazuje cały string. GA4 nie liczy tych transakcji jako deduplikowane `transactions` (metryka = 0 dla malformed IDs).
- **Impact PLN:** **1 088 transakcji bez możliwości analizy produktowej, segmentacyjnej, lifetime value**. Revenue z malformed IDs nieweryfikowalne.

### 4D.4 value >0 przy purchase
- **Status:** ⚠️ Częściowo
- **Wynik:** 1/3 pkt
- **Komentarz:** 92 purchase events z (not set) transactionId → revenue = 0 PLN (5,8% eventów). SMS channel: 5 purchases z revenue = 0 PLN. Łącznie ~6-7% eventów z value=0. Przekracza próg 1% ale nie 5%.

### 4D.5 Currency ustawione
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** `currency: PLN` ustawione w HTML (`gtag('set', {'currency': "PLN"}`).

### 4E.1–4E.4 Zdarzenia e-commerce
- **Status:** ✅ ✅ ✅ ✅
- **Wynik:** 12/12 pkt
- **Komentarz:** Wszystkie 4 zdarzenia wdrożone: `view_item` (590 146), `add_to_cart` (32 652), `begin_checkout` (1 296), `purchase` (1 582).

### 4E.5 Lejek wygląda naturalnie
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/3 pkt
- **Komentarz:** **purchase (1 582) > begin_checkout (1 296) = 122,1%** — fizycznie niemożliwe. Potwierdza że purchase event odpala się wielokrotnie per sesja. Dodatkowo: `add_shipping_info` (2 131) > `begin_checkout` (1 296) → kolejność zdarzeń lejka jest odwrócona lub shipping_info odpala się poza lejkiem. `add_payment_info` (806) < `begin_checkout` (1 296) = drop 37,8% między checkout a payment — kolejna anomalia.

### 4E.6 AOV naturalny
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** AOV = 515 556 PLN / 413 transakcji = **1 249 PLN**. Spójne z segmentem premium fashion. Organic: 234 013 PLN / 608 events ≈ 385 PLN (na ecommercePurchases) lub ok. 780 PLN per transaction — spójne.

**Sekcja 4 — Łącznie:** ~40/75 pkt = **53%** ⚠️

---

## SEKCJA 5 — UTM

### 5.1 Standaryzacja UTM
- **Status:** ❌ Błąd
- **Wynik:** 0/1 pkt
- **Komentarz:** Meta/Facebook: **6 wariantów** zamiast max 2: `facebook/cpc`, `m.facebook.com/referral`, `l.facebook.com/referral`, `lm.facebook.com/referral`, `facebook/referral`, `facebook.com/referral`. Brak jednolitej konwencji UTM dla kampanii Meta.

### 5.2 Google Ads — UTM source/medium
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** `google/cpc` = 132 384 sesji — Google Ads poprawnie oznakowane.

### 5.3 Google Ads — UTM kampanii
- **Status:** 🔒 Brak dostępu do GA4 raportów kampanii
- **Wynik:** 0/3 pkt

### 5.4 Meta/Facebook — UTM
- **Status:** ✅ OK
- **Wynik:** 3/3 pkt
- **Komentarz:** `facebook/cpc` = 57 699 sesji — kampanie Meta Ads widoczne z UTM. Problem: 3 242 sesji Meta bez UTM (referral warianty) = 5,3% ruchu Meta bez tagowania.

### 5.5 Meta — ID kampanii w UTM
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/2 pkt
- **Komentarz:** Brak dostępu do szczegółowych raportów UTM content/id.

### 5.6 Organiczne social — UTM
- **Status:** ⚠️ Częściowo
- **Wynik:** 1/2 pkt
- **Komentarz:** `ig/social` = 112 sesji, `instagram/referral` = 54 sesji. Częściowe UTM na Instagram. Brak spójnego oznakowania postów organicznych.

### 5.7 Email marketing — UTM
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** `edrone/email` = 17 457 sesji — eDrone poprawnie konfiguruje UTM. `sms/smsapi` = 1 735 sesji — SMS canal oznakowany, ale revenue = 0 (problem tracking, nie UTM).

### 5.8 Wizytówka Google — UTM
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** `google/maps` = 540 sesji — ruch z Google Maps / Google Business Profile widoczny jako oddzielna pozycja. Prawidłowe oznakowanie.

### 5.10 Pozostałe kanały płatne
- **Status:** ⚠️ Częściowo
- **Wynik:** 1/2 pkt
- **Komentarz:** SMS channel: `sms/smsapi` widoczny (1 735 sesji) ale revenue = 0 PLN dla 5 purchases = problem tracking e-commerce dla SMS, nie UTM.

**Sekcja 5 — Łącznie:** ~13/18 pkt = **72%** ⚠️

---

## SEKCJA 7 — Lejki zakupowych

### 7.1 Wszystkie 4 zdarzenia e-commerce wdrożone
- **Status:** ✅ OK
- **Wynik:** 2/2 pkt
- **Komentarz:** `view_item`, `add_to_cart`, `begin_checkout`, `purchase` — wszystkie 4 aktywne.

### 7.2 CR paid ≥50% CR organic
- **Status:** ❌ Błąd
- **Wynik:** 0/2 pkt
- **Komentarz:** CR organic (ecommercePurchases): 608/74 329 = **0,82%**. CR Google CPC: 320/132 384 = **0,24%** → 0,24/0,82 = **29%** (benchmark ≥50%). CR Meta paid: 186/57 699 = 0,32% → 39% organic. Ruch płatny jest słabej jakości lub targeting wymaga optymalizacji. Uwaga: dane zaburzone przez duplikację — rzeczywisty CR może być inny.

### 7.3 Brak kanału z CR <0.1% przy wydatkach >1000 PLN
- **Status:** ⚠️ Do weryfikacji
- **Wynik:** 1/2 pkt
- **Komentarz:** Cross-network CR: 255/125 584 = 0,20% (powyżej 0,1%). Bez dostępu do Google Ads niemożliwe pełne wyliczenie kosztu kampanii.

### 7.4 Checkout drop-off ≤40%
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/2 pkt
- **Komentarz:** Dane zduplikowane uniemożliwiają rzetelną ocenę. Jeśli użyć `transactions` (deduplikowane): 413/1 296 = **31,9% checkout kończy się purchase** (benchmark ≥60%). Tylko 1 na 3 klientów który zaczął checkout finalizuje zakup → potencjalny problem z UX kasy, bramką płatności lub zbyt małą liczbą metod płatności. Możliwy też błąd tracking (begin_checkout zbyt mało odpalany ze względu na duplikację purchase).

### 7.5 Lejek naturalny
- **Status:** ❌ Błąd krytyczny
- **Wynik:** 0/2 pkt (szacunek)
- **Komentarz:** `add_to_cart` (32 652) → `view_cart` (5 281) = 16,2% view_cart/ATC. `begin_checkout` (1 296) / `add_to_cart` (32 652) = 3,97% → bardzo niski (benchmark 30–60%). `purchase` (1 582) / `begin_checkout` (1 296) = **122,1%** → NIEMOŻLIWE. `add_shipping_info` (2 131) > `begin_checkout` (1 296) → zdarzenia w złej kolejności.

**Sekcja 7 — Łącznie:** ~3/8 pkt = **38%** ❌

---

## SEKCJA 6, 8, 10 — Google Ads / BCG
- **Status:** 🔒 Brak dostępu (Customer ID Google Ads)
- **Wynik:** 0/[max] pkt

---

## Punktacja

| Sekcja | Uzyskane pkt | Max pkt (dostępne) | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | 11 | 27 | 41% | ❌ Krytyczny |
| 2. ePrivacy | 18 | 45 | 40% | ❌ Krytyczny |
| 3. Konfiguracja | 17 | 54 | 31% | ❌ Krytyczny |
| 4. Data Quality | 40 | 75 | 53% | ⚠️ Wymaga poprawy |
| 5. UTM | 13 | 18 | 72% | ⚠️ Wymaga poprawy |
| 6. BCG | 0 | 0 | 🔒 — | 🔒 Brak dostępu |
| 7. Lejki | 3 | 8 | 38% | ❌ Krytyczny |
| 8. GA4↔Ads | 0 | 0 | 🔒 — | 🔒 Brak dostępu |
| 9. Analiza | — | — | ⚠️ — | ⚠️ Ograniczone dane |
| 10. Google Ads | 0 | 0 | 🔒 — | 🔒 Brak dostępu |
| **ŁĄCZNIE** | **102** | **227** | **45%** | **❌ Krytyczny** |

---

## Impact finansowy (podsumowanie)

| Problem | Szacunek PLN/msc | Priorytet |
|---------|-----------------|-----------|
| Duplikacja purchase 3.83x → błędne decyzje budżetowe kampanii | Niepoliczalny (zakłóca ROAS) | 🔴 Natychmiastowy |
| Items[] zepsute → niemożliwa analiza produktowa i optymalizacja Shopping/PMax | Niepoliczalny (zepsuta optymalizacja) | 🔴 Natychmiastowy |
| Malformed transactionId (72,4%) → 1 088 transakcji bez analizy | ~135 000 PLN/msc bez wglądu | 🔴 Natychmiastowy |
| Brak bannera CMP → ryzyko RODO | Do 20 mln EUR kara | 🔴 Natychmiastowy |
| Checkout drop-off 68% (1 na 3 kończy zakup) → UX problem | ~100 000 PLN/msc strat | 🔴 Natychmiastowy |
| Webmaile w referral (370 sesji, 9 purchases) → błędna atrybucja email | ~2 700 PLN/msc | 🟡 Miesiąc 1 |
| Meta fragmentacja (6 wariantów) → zaniżony ROAS Meta | ~1 500 PLN/msc | 🟡 Miesiąc 1 |
| Brak url_passthrough → zaniżenie ROAS przy braku zgody | Niepoliczalny (bez bannera = 100% bez zgody) | 🟡 Miesiąc 1 |
| Ruch wewnętrzny (38 sesji) → zaburzone metryki | Pomijalny | 🟢 Miesiąc 2–3 |

---

## Top 5 problemów

1. **Duplikacja GA4 3.83x** — hardcoded `gtag()` + GTM = każde purchase event odpala ~4 razy. Wszystkie metryki e-commerce są fałszywe. Ten sam problem wykryty 4 dni temu (03.04) → nie naprawiony, ratio wzrosło.

2. **72,4% malformed transactionId** — PrestaShop przekazuje URL z `&key=...` zamiast czystego ID zamówienia. 1 088 z 1 503 transakcji jest niezidentyfikowanych w GA4. Niemożliwa analiza per zamówienie.

3. **items[] całkowicie zepsute** — 0 itemsPurchased, 0 itemRevenue dla wszystkich 2 691 produktów przez 30 dni. Brak shopping analytics = niemożliwa optymalizacja kampanii produktowych.

4. **Brak bannera CMP** — Consent Mode v2 skonfigurowany technicznie (denied by default), ale brak wizualnego bannera. Użytkownicy nie mogą wyrazić zgody → GA4 zbiera wyłącznie zamodelowane anonimowe dane. Ryzyko RODO.

5. **Checkout drop-off 68%** — tylko 31,9% klientów którzy zaczęli checkout finalizuje zakup (benchmark ≥60%). Przy 515 556 PLN/msc revenue: poprawa CR checkout z 32% do 50% = potencjalnie +280 000 PLN/msc dodatkowego przychodu.
