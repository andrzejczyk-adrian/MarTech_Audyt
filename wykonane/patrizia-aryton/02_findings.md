# Findings: patrizia-aryton — 2026-04-07
> Źródło danych: GA4 API (Property 326801658), dane z poprzedniego audytu 2026-04-03
> Okres danych: 30 dni (8 marca – 7 kwietnia 2026)
> Legenda: ✅ OK | ❌ Błąd | ⚠️ Do weryfikacji | ➖ Nie dotyczy | 🔒 Brak dostępu

---

## SEKCJA 1 — Audyt Wstępny

*Uwaga: Punkty wymagające DevTools/Tag Assistant/TagHound oznaczone 🔒 lub potwierdzone z poprzedniego audytu 2026-04-03.*

### 1.1 Adnotacje w GA4
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt
- **Komentarz**: Brak dostępu do panelu GA4 Admin w trybie edycji. Z poprzedniego audytu (04-03) nie wykryto adnotacji przy wdrożeniu. Nie można zweryfikować bieżącego stanu.
- **Rekomendacja**: Sprawdzić GA4 → Admin → Adnotacje; dodać adnotację przy każdej zmianie konfiguracji.

### 1.2 Kolejność skryptów HTML
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Z poprzedniego audytu (04-03) potwierdzone podwójne wdrożenie GA4: hardcoded `gtag` bezpośrednio w HTML **ORAZ** tag GA4 przez GTM. Oznacza to, że skrypt GA4 jest wywoływany co najmniej 2 razy. Platforma Shoper wstrzykuje własny snippet GA4 hardcoded — jest to prawdopodobna przyczyna. Ratio 3.83x w danych transakcyjnych jest bezpośrednim dowodem tej anomalii.
- **Impact PLN**: Duplikaty zawyżają `ecommercePurchases` 3.83x — fałszywe dane w raportach konwersji, błędna optymalizacja kampanii PMax/Ads.
- **Rekomendacja**: Wyłączyć hardcoded GA4 w Shoper (Panel → Integracje → Analityka → wyłącz wbudowany GA4); pozostawić TYLKO tag GTM.

### 1.3 Przegląd podstron
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt
- **Komentarz**: Brak możliwości inspekcji DevTools. Z danych GA4 wnioskujemy: brak błędów krytycznych w śledzeniu page_view (1,383,032 per 30d — wolumen normalny). Jednak anomalie lejkowe (add_shipping_info > begin_checkout) wskazują na błędy JS w triggerach GTM.
- **Rekomendacja**: Przeprowadzić ręczny przegląd DevTools na stronie produktu i potwierdzenia zamówienia.

### 1.4 Google Tag Assistant
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/1 pkt
- **Rekomendacja**: Uruchomić tagassistant.google.com na homepage i stronie koszyka.

### 1.5 TagHound
- **Status**: ❌ Błąd (potwierdzone z danych)
- **Wynik**: 0/3 pkt
- **Komentarz**: Dane GA4 jednoznacznie potwierdzają podwójne tagi GA4. Ratio ecommercePurchases:transactions = 3.83x — nie jest to możliwe przy jednym aktywnym tagu GA4. TagHound wykryłby dwa tagi GA4 Configuration na stronie.
- **Impact PLN**: Każdy zakup generuje 3.83 eventów purchase — wszystkie raporty konwersji są ponad 3× zawyżone.
- **Rekomendacja**: Usunąć hardcoded GA4 snippet z HTML Shopera; zostawić tylko GTM.

### 1.6 Consent Mode — wstępna weryfikacja
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: Cookiebot jest wdrożony (zgodnie z briefem). Jednak 8,057 sesji (2.52%) przypisanych do `(not set)/(not set)` sugeruje niepełną implementację Consent Mode v2. Baner prawdopodobnie wyświetla się poprawnie, ale przekazanie sygnałów zgodny do GA4 jest niekompletne.
- **Rekomendacja**: Szczegółowy audyt w Sekcji 2.

### 1.7 Brak starych kodów UA
- **Status**: ✅ OK
- **Wynik**: 1/1 pkt
- **Komentarz**: Brak zdarzeń charakterystycznych dla Universal Analytics w danych GA4. Property używa nowego GA4 schema. Brak wskaźników UA w strukturze danych.

### 1.8 DataLayer — poprawność
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Dane GA4 wykazują krytyczną anomalię w DataLayer: event `purchase` jest generowany bez poprawnej tablicy `items[]` — 100% produktów ma `itemRevenue = 0 PLN` i `itemsPurchased = 0`. Mimo że zdarzenie purchase trafia do GA4 (1,582 eventów) z transaction_id i revenue na poziomie transakcji, brak danych item-level wskazuje na niepoprawny push do DataLayer — brak `ecommerce.items[]` lub pusty `items[]` w momencie zakupu.
- **Impact PLN**: Niemożliwa jakakolwiek analiza produktowa. 515,556 PLN przychodu nie jest przypisane do żadnego produktu.
- **Rekomendacja**: Na stronie potwierdzenia zamówienia (order/thank-you) zweryfikować w DevTools strukturę `dataLayer.push` — sprawdzić czy `ecommerce.items[]` zawiera `item_id`, `item_name`, `price`, `quantity`.

### 1.9 DataLayer GA4 — struktura e-commerce
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: **itemRevenue = 0 PLN dla 100% z 50 sprawdzonych produktów** (TOP 50 według "przychodu"). Prawidłowa struktura wymaga tablicy `items: [{item_id, item_name, price, quantity}]` wypełnionej przy zdarzeniu `purchase`. Dane wskazują że albo: (a) `items[]` jest pusta przy purchase, (b) `price = 0` dla wszystkich itemów, lub (c) event purchase jest wysyłany z tagu hardcoded bez danych e-commerce (tylko transaction-level).
- **Impact PLN**: Analiza BCG, produktowa, kategorialna — całkowicie niemożliwa. Merchant Center nie może optymalizować feedu na podstawie danych GA4.
- **Rekomendacja**: Deweloper → strona thank-you → sprawdź `dataLayer` push przy purchase → uzupełnić `items[]` z cenami i ilościami.

### 1.10 Google Analytics 360
- **Status**: ➖ Nie dotyczy
- **Wynik**: ➖

### 1.11 Remarketing Google Ads
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: Konto Google Ads 196-867-6668 aktywne. Kampanie PMax (Cross-network: 125,604 sesji) i Display (3,996 sesji) aktywne — remarketing prawdopodobnie działa. Brak możliwości weryfikacji DevTools.
- **Rekomendacja**: Sprawdzić Google Ads → Odbiorcy → listy remarketingowe.

### 1.12 Konwersje Google Ads w GTM
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt
- **Rekomendacja**: Zweryfikować w GTM czy Conversion Tracking Tag jest aktywny.

### 1.13 Meta (Facebook) Pixel
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: Kampanie Meta Ads aktywne (facebook/cpc: 57,699 sesji, 25 transakcji). Pixel prawdopodobnie wdrożony, ale brak weryfikacji przez DevTools. Fragmentacja źródeł Meta (7 wariantów) może wskazywać na problemy z UTM, nie z pixelem.
- **Rekomendacja**: Zweryfikować pixel Meta przez Facebook Pixel Helper.

### 1.14 Meta — API konwersji (CAPI)
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt
- **Rekomendacja**: Sprawdzić GTM → Tagi → Facebook Conversions API lub Server-Side GTM.

### 1.15–1.17 LinkedIn / Pinterest / Yandex
- **Status**: ➖ Nie dotyczy
- **Wynik**: ➖

### 1.18 Microsoft Clarity
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt
- **Rekomendacja**: Sprawdzić DevTools → Network → clarity.ms.

### 1.19 Bing/Microsoft Ads
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: Bing organic: 2,801 sesji, 22 transakcje, 26,428 PLN. Brak widocznego bing/cpc → prawdopodobnie brak kampanii Bing Ads.
- **Rekomendacja**: Potwierdzić czy Bing Ads jest używany.

### 1.20–1.24 TikTok / Hotjar / Criteo / RTB House / Allegro
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/15 pkt (wymaga DevTools)
- **Rekomendacja**: Przeprowadzić przegląd DevTools Network.

**Sekcja 1 — Wynik szacunkowy: 5/36 pkt = 14%**

---

## SEKCJA 2 — ePrivacy / Consent Mode

*Uwaga: Ocena oparta na danych GA4 (pośrednie wskaźniki) i kontekście poprzedniego audytu.*

### 2.1–2.3 Personalizacja i blokowanie
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/5 pkt
- **Komentarz**: Cookiebot jest wdrożony. Z poprzedniego audytu: baner był widoczny. Szczegółowa weryfikacja blokowania wymaga testu w przeglądarce.

### 2.4 Poprawne blokowanie cookies po odmowie
- **Status**: ❌ Błąd (pośrednio)
- **Wynik**: 0/3 pkt
- **Komentarz**: (not set)/(not set): 8,057 sesji (2.52%) — użytkownicy, którzy odmówili zgody, ale ich sesje są częściowo widoczne w GA4 jako `(not set)`. Prawidłowy Consent Mode v2 powinien generować anonimowe pingi (modelowane dane) a nie pełne (not set) sesje. Wskazuje to na niekompletną implementację.
- **Impact PLN**: 8,057 sesji z nieznanym źródłem = ok. 34,954 PLN przychodów bez atrybukcji/miesiąc.
- **Rekomendacja**: Sprawdzić w GTM → Cookiebot tag → czy ustawiony w Consent Initialization; zweryfikować sekwencję consent_default → consent_update.

### 2.5–2.16 Zmiana decyzji, brak reload, tagi po zgodzie
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/17 pkt
- **Rekomendacja**: Szczegółowy test z incognito + DevTools.

### 2.17 url_passthrough
- **Status**: ❌ Błąd (potwierdzone z poprzedniego audytu)
- **Wynik**: 0/3 pkt
- **Komentarz**: Z poprzedniego audytu 04-03: `url_passthrough` nie było skonfigurowane. Problem nadal istnieje — bez url_passthrough użytkownicy odmawiający cookies są traceni dla celów atrybucji kampanii.
- **Impact PLN**: Każdy użytkownik bez cookies = nieprzypisana konwersja. Przy 2.52% (not set) i AOV 1,248 PLN: ~29 transakcji/miesiąc bez atrybukcji = ~36,192 PLN/msc.
- **Rekomendacja**: GTM → Tag GA4 Config → Pola konfiguracji → dodać `url_passthrough: true`.

### 2.18–2.20 Dane wrażliwe
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/9 pkt
- **Rekomendacja**: Weryfikacja przez GA4 → Eksploracje → URL parameters + event parameters.

**Sekcja 2 — Wynik szacunkowy: 0/45 pkt = 0–5% (minimum bez dostępu)**

---

## SEKCJA 3 — Konfiguracja GTM i GA4

### 3A.1 Walidacja GTM
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Potwierdzone z poprzedniego audytu i z danych: GA4 jest wdrożone ZARÓWNO przez GTM jak i hardcoded w HTML. To narusza zasadę "GTM jako jedyny kontener". Shoper wstrzykuje własny snippet GA4.
- **Rekomendacja**: Wyłączyć wbudowany GA4 w panelu Shoper.

### 3A.2 Brak błędów w GTM
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3A.3 Consent dla wszystkich tagów
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: Cookiebot sugeruje konfigurację consent. Jednak 8,057 sesji (not set) wskazuje, że nie wszystkie tagi są prawidłowo zblokowane.

### 3A.4 Tag łączący konwersje (Conversion Linker)
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3A.5–3A.12 Inne GTM
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/15 pkt

### 3B.1–3B.6 GTM Server Side
- **Status**: ➖ Nie dotyczy (brak sGTM w konfiguracji)
- **Wynik**: ➖

### 3C.1 Alerty GA4
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3C.2 Uprawnienia
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3C.3 Waluta
- **Status**: ✅ OK (potwierdzone)
- **Wynik**: 2/2 pkt
- **Komentarz**: Z poprzedniego audytu: waluta PLN ustawiona poprawnie. Przychody w danych GA4 spójne z PLN.

### 3C.4 Google Signals
- **Status**: ✅ OK (potwierdzone)
- **Wynik**: 3/3 pkt
- **Komentarz**: Z poprzedniego audytu 04-03: Google Signals włączone i aktywne.

### 3C.5 User-ID
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: `login` event: 459,045 (30d) — bardzo wysoki wolumen przy ~316k sesjach sugeruje, że event `login` triggeruje się przy każdym załadowaniu strony dla zalogowanych użytkowników (nie tylko przy faktycznym logowaniu). Jeśli User-ID jest włączone, to jest problem z jakością danych User-ID.
- **Rekomendacja**: Sprawdzić trigger dla eventu `login` — powinien triggerować tylko przy faktycznym logowaniu, nie przy każdej sesji.

### 3C.6 Import danych
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/2 pkt

### 3C.7 Retencja 14 miesięcy
- **Status**: ✅ OK (potwierdzone)
- **Wynik**: 1/1 pkt
- **Komentarz**: Z poprzedniego audytu: retencja 14 miesięcy.

### 3C.8 Filtrowanie ruchu wewnętrznego
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: W danych source/medium widoczne: `dev18.arytondev.local/referral` (10 sesji) i `arytonpl.sharepoint.com/referral` (28 sesji). Łącznie 38 sesji z wewnętrznych zasobów firmy. Filtr IP lub hostname nie jest skonfigurowany lub jest niekompletny.
- **Impact PLN**: Zanieczyszczenie danych analitycznych. Przy niskim CR z tych źródeł = obniżenie średniego CR konta.
- **Rekomendacja**: GA4 → Admin → Filtry danych → dodać filtr dla hostname `arytondev.local` + wykluczyć zakresy IP biura.

### 3C.9 Strumień Web
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Dane napływające — 1,383,032 page_view w 30 dniach. Strumień aktywny.

### 3C.10 Cross-domain tracking
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: W source/medium widoczna `klarna/referral` (71 sesji) — Klarna jako bramka płatnicza nie jest wykluczona z referrali. Oznacza to, że użytkownicy wracający z płatności Klarna generują nową sesję z referral=klarna zamiast kontynuować oryginalną sesję (np. z google/cpc).
- **Impact PLN**: Transakcje mogą być przypisane do Klarna zamiast do pierwotnego kanału pozyskania.
- **Rekomendacja**: GA4 → Strumień → Konfigurowanie domen → dodać `klarna.com` + inne bramki płatnicze.

### 3C.11 Ignorowanie zduplikowanych konfiguracji
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Podwójne wdrożenie GA4 (hardcoded + GTM) = ustawienie "Ignoruj duplikaty" powinno być włączone, ale samo w sobie nie rozwiązuje problemu. Potwierdzone: zduplikowane zliczanie purchase (ratio 3.83x).
- **Rekomendacja**: Włączyć "Ignoruj zduplikowane konfiguracje" w GA4 Strumień → Zarządzaj tagiem, ORAZ wyłączyć hardcoded snippet.

### 3C.12 Wykluczono bramki płatności
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: `klarna/referral` (71 sesji) potwierdza brak wykluczenia Klarna. Z poprzedniego audytu: bramki płatnicze nie były wykluczone.
- **Rekomendacja**: GA4 → Strumień → Referral exclusion → dodać: klarna.com, payu.pl, przelewy24.pl.

### 3C.13 Wykluczono bramki pocztowe
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: W danych: poczta.onet.pl (198 sesji), poczta.interia.pl (80), poczta.o2.pl (76), poczta.wp.pl (46) — łącznie **400 sesji** z bramek pocztowych jako referral. Email marketing (edrone) jest osobno, ale linki w emailach kierują do sklepu przez webmaile.
- **Impact PLN**: 400 sesji/msc potencjalnie niepoprawnie atrybucjonowane.
- **Rekomendacja**: Dodać do Referral exclusion: onet.pl, interia.pl, o2.pl, wp.pl.

### 3C.14 Wykluczono boty CMP
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3C.15 Czas trwania sesji
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/2 pkt
- **Rekomendacja**: Dla e-commerce ustawić co najmniej 5 godzin w GA4 → Strumień.

### 3C.16 Zdarzenia jako konwersje
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: Z poprzedniego audytu: `purchase` oznaczony jako konwersja. Brakuje jednak `begin_checkout` i `add_to_cart` jako konwersji — niezbędnych do optymalizacji kampanii Smart.
- **Rekomendacja**: Oznaczyć `begin_checkout` i `add_to_cart` jako konwersje pomocnicze.

### 3C.17 Model atrybucji
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Z poprzedniego audytu: Data-Driven Attribution (DDA) aktywny.

### 3C.18 Połączenie Google Ads
- **Status**: ✅ OK (potwierdzone)
- **Wynik**: 3/3 pkt
- **Komentarz**: Z poprzedniego audytu: Google Ads połączone z GA4, reklamy spersonalizowane włączone.

### 3C.19 BigQuery
- **Status**: ✅ OK (potwierdzone)
- **Wynik**: 3/3 pkt
- **Komentarz**: Dataset `dane-z-ga4-aryton-pl` aktywny. Eksport skonfigurowany.

### 3C.20 Search Console
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3C.21 Alerty z emailem
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/3 pkt

### 3K.1–3K.7 BigQuery (wymagają zapytań BQ)
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/21 pkt
- **Komentarz**: Dataset istnieje. Wymagane bezpośrednie zapytania SQL. Z danych GA4 API można pośrednio wnioskować że 3K.4 (jakość items[]) = ❌ (price=0 dla 100% produktów).

**Sekcja 3 — Wynik szacunkowy: ~20/93 pkt = 22%**

---

## SEKCJA 4 — Data Quality

### 4A.1 Udział sesji (not set) <5%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set)/(not set): 8,057 sesji z ~319,640 łącznie = **2.52%**. Poniżej progu 5%.

### 4A.2 Udział pierwszego źródła (not set) <5%
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: Brak bezpośredniego raportu "pierwsze źródło" w pobranych danych. Na podstawie source/medium sesji: (not set) = 2.52%, ale pierwsze źródło użytkownika może różnić się od źródła sesji.
- **Rekomendacja**: Sprawdzić GA4 → Raporty → Pozyskiwanie → Pozyskiwanie użytkowników → First user source.

### 4A.3 Pierwsze źródło wygląda naturalnie
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Dystrybucja sesji: google/cpc (41.4%), google/organic (23.2%), facebook/cpc (18.0%), edrone/email (5.5%), direct/none (5.1%). Naturalna dystrybucja e-commerce odzieżowego. Brak anomalii dominacji jednego kanału.

### 4A.4 Ruch wygląda naturalnie
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Kanały z sensownymi metrykami. Organic CR (0.86%) przewyższa CPC (0.07% z source/medium — ale to prawdopodobnie ze względu na różne definicje sessions vs transakcji).

### 4A.5 Cross-domain — własne domeny w referral
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: `arytonpl.sharepoint.com/referral` (28 sesji) — wewnętrzna domena Aryona jako referral. Może wskazywać na linki z wewnętrznych dokumentów Sharepoint do strony sklepu.
- **Rekomendacja**: Jeśli subdomena aryton.pl jest innym serwisem, skonfigurować cross-domain tracking.

### 4A.6 Brak ruchu spamowego
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Podejrzane domeny: `825cfeb46b5e71bf82a61c1f8ffafe7c.safeframe.googlesyndication.com` (8 sesji), `1e2b4c34a385aa2ec922d31a31b5c732.safeframe.googlesyndication.com` (7 sesji) — to automaty Google SafeFrame z Display/PMax (normalny ruch). `metric.picodi.com` (8 sesji) — agregator zniżek. Łączny spam <0.1%.

### 4A.7 Bramki płatności poza ścieżką
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: `klarna/referral`: 71 sesji. Klarna to bramka BNPL (buy now pay later) — użytkownicy wracający z Klarna po autoryzacji płatności są traktowani jako nowa sesja z referral Klarna. W skrajnym przypadku konwersja jest przypisana do Klarna zamiast do oryginalnego kanału.
- **Impact PLN**: Szacunkowo kilka transakcji/miesiąc przypisanych błędnie.
- **Rekomendacja**: Dodać `klarna.com` do Referral exclusion.

### 4A.8 Bramki pocztowe poza ścieżką
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Bramki pocztowe jako referral: poczta.onet.pl (198 sesji, 0 transakcji), poczta.interia.pl (80), poczta.o2.pl (76), poczta.wp.pl (46, 1 transakcja). Łącznie **400 sesji i 1 transakcja (719 PLN)** z webmaili. Sesje te powinny być przypisane do email/edrone, a nie referral.
- **Impact PLN**: Nieidentyfikowalny ruch emailowy przychodzi jako referral zamiast email.
- **Rekomendacja**: Wykluczyć bramki pocztowe z referral exclusion.

### 4A.9 Facebook/Meta — dane unifikowane
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: **7 wariantów source dla Meta:**
  - `facebook/cpc`: 57,699 sesji (UTM)
  - `m.facebook.com/referral`: 1,722 sesji
  - `l.instagram.com/referral`: 1,645 sesji
  - `l.facebook.com/referral`: 690 sesji
  - `lm.facebook.com/referral`: 381 sesji
  - `facebook/referral`: 363 sesji
  - `facebook.com/referral`: 86 sesji
  - `pl-pl.facebook.com/referral`: 4 sesje
  - **Łącznie: ~62,590 sesji w 7 silosach.** GA4 traktuje je jako 7 różnych źródeł.
- **Impact PLN**: ROAS Meta obliczany tylko na 57,699 sesjach zamiast 62,590 = zaniżony o ~8.5%. Przy przychodzie ~34,433 PLN z facebook/cpc: realne przychody Meta mogą być o ~3,000–5,000 PLN wyższe ale nieprzypisane.
- **Rekomendacja**: GA4 → Strumień → Grupowanie kanałów niestandardowych → połączyć wszystkie warianty Meta; LUB skonfigurować UTM na wszystkich linach Facebook organicznych.

### 4A.10 Ruch międzynarodowy
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: TOP 20 miast to polskie miasta. Brak anomalii z zagranicznych lokalizacji.

### 4B.1 Czas trwania sesji naturalny
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: Brak danych avg session duration w pobranych danych. Z wolumenu `user_engagement` (853,971) vs `session_start` (675,526) — ratio ~1.26x sugeruje że większość sesji ma zaangażowanie. Login (459,045) na poziomie zbliżonym do session_start sugeruje że wielu użytkowników jest zalogowanych.
- **Rekomendacja**: Sprawdzić GA4 → Raporty → Sesje → Czas trwania.

### 4B.2 Engagement rate naturalny
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Engagement rate nie jest bezpośrednio w danych, ale `user_engagement` (853,971) przy 675,526 sesjach = ratio > 1 = sesje zaangażowane. Wolumen `scroll` (238,296) i `menu_click` (152,646) potwierdza aktywność użytkowników.

### 4B.3 CR naturalny
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: CR = transactions/sessions = 413/~319,640 = **0.13%**. To poniżej benchmarku 0.5–3%. Jednak CR organic (168/74,329 = **0.23%**) i email (40/17,457 = **0.23%**) są w akceptowalnych granicach. Całościowy niski CR wynika z dominacji Cross-network PMax (255/125,604 = **0.20%**) i CPC Search (91/132,384 = **0.07%**) — sugeruje że kanały płatne mają słabą jakość ruchu.
- **Impact PLN**: Gdyby google/cpc miał CR organic (0.23% vs 0.07%), przychody wzrosłyby o ~95,560 × (0.23/0.07 - 1) = ~243% więcej z CPC.

### 4C.1 source/medium not set <5%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set)/(not set): 2.52% < 5%.

### 4C.2 direct/none <30%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: direct/(none): 16,376 sesji = **5.12%** z ~319,640. Zdrowy poziom.

### 4C.3 Łączny not set + direct <40%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: (not set) 2.52% + direct 5.12% = **7.64%** < 40%. ✅

### 4C.4 Transakcje (not set) <10%
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: (not set) source/medium: 29 transakcji z 413 = **7.0%**. Między progiem ostrzegawczym (5%) a krytycznym (10%). To 29 zamówień o łącznej wartości ~34,954 PLN bez atrybukcji.
- **Impact PLN**: 34,954 PLN/miesiąc bez przypisanego kanału = ~419,448 PLN/rok.
- **Rekomendacja**: Naprawić Consent Mode i url_passthrough.

### 4D.1 Ratio ecommercePurchases:transactions ≤1.1
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: **Ratio = 1582 / 413 = 3.83x** — to PONAD 3× przekroczenie progu ostrzegawczego (>1.5x). To identyczny problem jak w poprzednim audycie z 04-03 (ratio był 3.53x). Problem **NIE ZOSTAŁ NAPRAWIONY** w ciągu 4 dni. Każdy zakup rejestruje ~3.83 zdarzenia `purchase`. Wynika to z podwójnego tagu GA4 (hardcoded Shoper + GTM).
- **Impact PLN**: Wszelkie raporty konwersji są 3.83× zawyżone. Kampanie PMax optymalizują się na fałszywych danych konwersji.

### 4D.2 % transakcji bez transactionId <2%
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: not_set_count = 1 z 1503 unikalnych IDs = **0.07%**. Doskonały wynik.

### 4D.3 Brak malformed transaction_id
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Wykryto malformed source zawierający pełen URL z parametrami kampanii Google Ads:
  - `google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|_Aryton&utm_id=19091733253&utm_term=kurtka patrizia aryton&...` — jako `sessionSource` (3 sesje)
  - `google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|_Aryton&...płaszcze patrizia aryton...` — 2 sesje
  - Sugeruje broken URL encoding w linkach Google Ads lub błąd w przetwarzaniu URL przez Shoper. Choć dotyczy to `sessionSource` a nie `transactionId`, wskazuje na systemowy problem z URL handling.
- **Rekomendacja**: Sprawdzić URL templates w Google Ads — użyć {lpurl} zamiast manualnych URL.

### 4D.4 value >0 przy purchase
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: Suma purchaseRevenue = 515,556 PLN z 1,582 raw eventów = średnio 325 PLN/event. Jednak per transakcję (413 unikalnych) AOV = 1,248 PLN. 1 not_set transaction może mieć value=0. Nie można zweryfikować % zdarzeń z value=0 bez BQ.
- **Rekomendacja**: Sprawdzić w BigQuery: `SELECT COUNT(*) FROM events WHERE event_name='purchase' AND ecommerce.purchase_revenue = 0`.

### 4D.5 currency ustawione
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: purchaseRevenue w PLN (515,556 PLN) — waluta spójna.

### 4E.1 view_item wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: view_item: 590,185 eventów/30d. ✅

### 4E.2 add_to_cart wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: add_to_cart: 32,653 eventów/30d. ✅

### 4E.3 begin_checkout wdrożone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: begin_checkout: 1,296 eventów/30d. ✅

### 4E.4 purchase wdrożone
- **Status**: ✅ OK (z zastrzeżeniem duplikacji)
- **Wynik**: 2/3 pkt
- **Komentarz**: purchase: 1,582 eventów. Wdrożone, ale zduplikowane 3.83×.

### 4E.5 Lejek wygląda naturalnie
- **Status**: ❌ Błąd KRYTYCZNY
- **Wynik**: 0/3 pkt
- **Komentarz**: **Lejek jest rozbity na dwóch poziomach:**
  - `add_shipping_info` (2,132) > `begin_checkout` (1,296) — matematycznie niemożliwe. Użytkownik nie może przejść do shipping info bez checkout.
  - `purchase` (1,582) > `add_payment_info` (806) — niemożliwe.
  - `purchase` (1,582) > `begin_checkout` (1,296) — niemożliwe.
  - Diagram prawidłowego lejka: view_item (590k) → add_to_cart (32k) → begin_checkout (1,296) → add_shipping_info (2,132❌) → add_payment_info (806) → purchase (1,582❌)
  - Widoczne: dwa zdarzenia purchase docierają z różnych źródeł (hardcoded GA4 na stronie thank-you + GTM).

### 4E.6 AOV naturalny i spójny
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: AOV = 515,556 PLN / 413 transakcji = **1,248 PLN**. To wysoki AOV dla odzieży premium — Patrizia to marka luxury, więc jest uzasadniony. Jednak anomalie per miasto: Bydgoszcz AOV 39 PLN (36 zakupów, 1,408 PLN = ~39 PLN/zakup) i Lublin AOV 93 PLN są podejrzane. Mogą wskazywać na duplikacje lub test zakupów z niskimi cenami.

**Sekcja 4 — Wynik: ~40/75 pkt = 53%**

---

## SEKCJA 5 — UTM

### 5.1 Standaryzacja UTM
- **Status**: ❌ Błąd
- **Wynik**: 0/1 pkt
- **Komentarz**: Meta: 7 wariantów source (facebook, m.facebook.com, l.facebook.com, l.instagram.com, lm.facebook.com, facebook.com, pl-pl.facebook.com). To skrajny przykład fragmentacji.

### 5.2 Google Ads — UTM source/medium
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: google/cpc: 132,384 sesji. Google Ads jest prawidłowo tagowany.

### 5.3 Google Ads — UTM kampanii
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Wykryto malformed UTM source (cały URL z parametrami jako source): `google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|_Aryton&utm_id=19091733253&utm_term=kurtka patrizia aryton&utm_content=638313710563&...`. To wskazuje że część linków Google Ads ma broken URL — URL nie jest enkodowany, parametry UTM są doklejone do domeny bez `?`. Choć dotyczy tylko 3–5 sesji, sugeruje błąd w szablonach URL kampanii.
- **Impact PLN**: Kilka kliknięć/miesiąc traci atrybucję.
- **Rekomendacja**: Sprawdzić URL templates w kampaniach SEA|Brand — użyć `{lpurl}?utm_source=google&utm_medium=cpc&...` z poprawnym separatorem `?`.

### 5.4 Meta/Facebook Ads — UTM
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: facebook/cpc: 57,699 sesji — główna kampania Meta z UTM. Jednak tylko 57,699 z ~62,590 sesji Meta (~92%) ma poprawne UTM. Reszta (8%) przypisana jako referral bez UTM.
- **Impact PLN**: 4,891 sesji bez UTM = ~2,660 PLN przychodów niezidentyfikowanych jako Meta.

### 5.5 Meta Ads — ID kampanii w UTM
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/2 pkt

### 5.6 Organiczne social media — UTM
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: `l.instagram.com/referral` (1,645 sesji) — posty organiczne Instagram bez UTM. `ig/social` (112 sesji) — próba oznaczenia ale tylko 112 sesji. Łącznie ~4,879 sesji Organic Social (~4,521 bez UTM) trafia jako referral zamiast oznaczonego social/organic.

### 5.7 Email marketing — UTM
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: edrone/email: 17,457 sesji, 40 transakcji, 51,771 PLN. edrone prawidłowo tagowane.

### 5.8 Wizytówka Google — UTM
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: google/maps: 540 sesji, 2 transakcje, 3,527 PLN. Ruch z Google Maps jest widoczny. Brak potwierdzenia czy UTM jest na wizytówce.

### 5.9 Linki SEO — UTM
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: google/organic: 74,329 sesji naturalny.

### 5.10 SMS — UTM
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: `sms/smsapi`: 1,735 sesji, **0 transakcji, 0 PLN przychodów**. Pomimo 1,735 sesji z kampanii SMS, żadna nie konwertuje. To wskazuje na problem UTM (user ląduje na złej stronie lub bez product context) albo linki SMS nie zawierają odpowiednich UTM — ewentualnie błąd w zliczaniu konwersji z tych sesji.
- **Impact PLN**: Jeśli SMS ma CR jak email (0.23%), powinno generować ~4 transakcje/miesiąc × 1,248 PLN = ~5,000 PLN. Strata z powodu niedziałającego śledzenia.
- **Rekomendacja**: Sprawdzić landing page z linków SMS — czy strona ładuje się poprawnie; sprawdzić UTM params na linkach SMS.

**Sekcja 5 — Wynik: 9/18 pkt = 50%**

---

## SEKCJA 6 — Macierz BCG

### 6.1–6.5 Analiza BCG
- **Status**: ❌ Niemożliwa
- **Wynik**: 0/12 pkt
- **Komentarz**: **Analiza BCG jest całkowicie niemożliwa** ze względu na `itemRevenue = 0 PLN` i `itemsPurchased = 0` dla 100% produktów w GA4. Brak danych o przychodach per produkt uniemożliwia obliczenie revenue_share i ROAS per produkt. Google Ads Shopping/PMax bez segmentacji BCG = brak kontroli nad alokacją budżetu.

Sekcja 6 wymaga dostępu do Google Ads (BDOS). Bez BDOS: 🔒 Brak dostępu do kampanii Shopping.

**Sekcja 6 — Wynik: 0/12 pkt = 0%**

---

## SEKCJA 7 — Lejki zakupowe

### 7.1 Wszystkie 4 zdarzenia wdrożone
- **Status**: ✅ OK (z zastrzeżeniem)
- **Wynik**: 1/2 pkt
- **Komentarz**: Wszystkie 4 zdarzenia aktywne: view_item (590,185), add_to_cart (32,653), begin_checkout (1,296), purchase (1,582). Jednak anomalie wskazują na błędy wdrożenia.

### 7.2 CR paid ≥50% CR organic
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: CR google/cpc = 91/132,384 = **0.069%**. CR google/organic = 168/74,329 = **0.226%**. Ratio = 0.069/0.226 = **30.5%** < 50%.
- **Impact PLN**: Gdyby google/cpc miał CR = 50% organic (0.113%), przy 132,384 sesjach = ~149 transakcji zamiast 91 = +58 transakcji/miesiąc × 1,248 PLN = **+72,384 PLN/miesiąc**.
- **Rekomendacja**: Audyt jakości landing pages dla kampanii CPC; sprawdzić dopasowanie reklama→landing page.

### 7.3 Brak kanału z CR <0.1% przy wydatkach >1000 PLN
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: google/cpc: 132,384 sesji, 91 transakcji, CR = **0.069%** < 0.1% — przy szacunkowych wydatkach PMax prawdopodobnie >10,000 PLN/miesiąc. Cross-network (PMax): 125,604 sesji, CR = 0.20% (ok), ale zawiera zduplikowane purchase.
- **Impact PLN**: CPC z bardzo niskim CR = przepalony budżet.

### 7.4 Checkout drop-off ≤40%
- **Status**: ❌ Błąd
- **Wynik**: 0/2 pkt
- **Komentarz**: begin_checkout: 1,296, transactions (real): 413 → checkout→purchase: 413/1,296 = **31.9%** < 40%. Tylko 32% użytkowników, którzy zaczęli checkout, finalizuje zakup. Benchmark: 50–80%.
- **Impact PLN**: Gdyby drop-off wynosił 40% (zamiast 68%), dodatkowych transakcji = (1,296 × 60%) - 413 = 778 - 413 = +365 transakcji/miesiąc × 1,248 PLN = **~455,520 PLN/miesiąc**. Nawet połowa tej wartości = ogromna szansa.
- **Rekomendacja**: Audyt UX koszyka i procesu checkout: liczba kroków, opcje płatności, koszt dostawy.

### 7.5 Lejek wygląda naturalnie
- **Status**: ❌ Błąd (pokrywa się z 4E.5)
- **Komentarz**: add_shipping_info (2,132) > begin_checkout (1,296) — lejek rozbity.

**Sekcja 7 — Wynik: 1/8 pkt = 13%**

---

## SEKCJA 8 — GA4 ↔ Google Ads

### 8.1 Połączenie GA4↔Ads aktywne
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt
- **Komentarz**: Z poprzedniego audytu: połączenie aktywne. Reklamy spersonalizowane włączone.

### 8.2 Reklamy spersonalizowane włączone
- **Status**: ✅ OK
- **Wynik**: 3/3 pkt

### 8.3–8.10 Konwersje, Enhanced Conversions, listy
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/21 pkt
- **Komentarz**: Wymagany dostęp do Google Ads Panel. Brak BDOS (dostęp tylko przez email osobisty).

**Sekcja 8 — Wynik: 6/27 pkt = 22%**

---

## SEKCJA 9 — Analiza danych

### 9.1 CVR paid ≥50% CVR organic
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: CVR google/cpc (0.069%) vs google/organic (0.226%) = 30.5% ← poniżej 50% minimum.

### 9.2 Najlepszy kanał wg Rev/sesja
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: Rev/sesja per kanał:
  | Kanał | Rev/sesja |
  |-------|-----------|
  | Organic Search | 3.42 PLN |
  | Email (edrone) | 2.97 PLN |
  | Direct | 1.23 PLN |
  | CPC (google) | 0.72 PLN |
  | Paid Social (Meta) | 0.60 PLN |
  | Cross-network | 0.60 PLN |
  
  **Organic Search** i **Email** to najefektywniejsze kanały wg Rev/sesja. Google CPC jest 4.7× mniej efektywny niż organic.

### 9.3 Mobile/Desktop CVR ratio
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Mobile CR (szac.): 247/249,319 = **0.099%**. Desktop CR (szac.): 165/62,954 = **0.262%**. Ratio mobile/desktop = **37.8%** < 50%.
- **Impact PLN**: Potencjał mobile przy CR = 50% desktop: (249,319 × 0.131%) × 1,248 = **~407,530 PLN/miesiąc** dodatkowego przychodu. To wskazuje na poważny problem UX mobile.
- **Rekomendacja**: Audyt UX mobile: szybkość strony (Core Web Vitals), przycisk CTA mobile, checkout na mobile.

### 9.4 Engagement rate naturalny
- **Status**: ✅ OK
- **Wynik**: 2/2 pkt
- **Komentarz**: user_engagement (853,971) vs session_start (675,526) = naturalny. Scroll (238,296), menu_click (152,646) = aktywni użytkownicy.

### 9.5 Porzucenie koszyka <80%
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Cart abandonment = 1 - (purchase_raw/add_to_cart) = 1 - (1,582/32,653) = **95.2%**. Nawet biorąc deduplikowane transactions: 1 - (413/32,653) = **98.7%**. Benchmark: <80%.
- **Impact PLN**: 32,240 użytkowników dodało do koszyka ale nie kupiło. Przy AOV 1,248 PLN i 5% odzysku = 32,240 × 5% × 1,248 = **~2,011,800 PLN/rok** potencjał z abandoned cart.
- **Rekomendacja**: Wdrożyć abandoned cart emails w edrone; remarketing z produktami z koszyka; uproszczenie procesu zakupu.

### 9.6 Anomalie ruchu
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/2 pkt
- **Komentarz**: Brak danych dziennych do analizy trendów. Cross-network (PMax) dominuje z 125,604 sesjami — anomalnie wysoka dominacja jednego kanału. SMS/smsapi: 1,735 sesji z 0 konwersji = anomalia.

### 9.7 Ruch wewnętrzny nie zaburza danych
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: dev18.arytondev.local (10 sesji referral) + arytonpl.sharepoint.com (28 sesji referral) = **38 sesji/miesiąc z wewnętrznych źródeł**. Filtr IP/hostname niekompletny.

### 9.8 Referral z wysokim CVR
- **Status**: ✅ OK
- **Wynik**: 1/1 pkt
- **Komentarz**: ntp.msn.com (88 sesji, 3 transakcje, 3,121 PLN) = CVR 3.4% — wysoki. pl.search.yahoo.com (615 sesji, 2 transakcje) = CVR 0.33%. zasobygwp.pl (78 sesji, 1 transakcja) — niszowe ale konwertuje.

### 9.9 Bramki płatności/webmaile w referral
- **Status**: ❌ Błąd
- **Wynik**: 0/3 pkt
- **Komentarz**: Klarna (71 sesji) + webmaile (400 sesji) = **471 sesji** z bramek i pocztowych referrali. Pokrywa się z 4A.7 i 4A.8.

### 9.10 Retencja — % powracających kupujących
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/2 pkt
- **Rekomendacja**: Sprawdzić GA4 → Raporty → Retencja → New vs Returning.

**Sekcja 9 — Wynik: 6/24 pkt = 25%**

---

## SEKCJA 10 — Google Ads

*Brak dostępu przez BDOS. Ocena na podstawie danych GA4 (pośrednia).*

### 10A.1 Brak kampanii z 0 konwersji >30d
- **Status**: ⚠️ Do weryfikacji
- **Wynik**: 1/3 pkt
- **Komentarz**: Z GA4 source/medium: `sms/smsapi` (1,735 sesji, 0 transakcji) — to jednak nie jest Google Ads. Z GA4 kanały: Display (3,996 sesji, 22 zakupy raw) = ok. Brak danych o konkretnych kampaniach Google Ads.
- **Rekomendacja**: Sprawdzić w Google Ads Panel → Kampanie → filtruj Konwersje = 0 za ostatnie 30 dni.

### 10A.2–10G.3 Pozostałe kryteria Google Ads
- **Status**: 🔒 Brak dostępu
- **Wynik**: 0/78 pkt
- **Komentarz**: Wymagany dostęp przez BDOS lub Google Ads Panel. Brak dostępu przez service account.

**Sekcja 10 — Wynik: 1/81 pkt = 1%**

---

## Punktacja

| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | 5 | 36 | 14% | ❌ Krytyczny |
| 2. ePrivacy | 0 | 45 | 0% | ❌ Krytyczny |
| 3. Konfiguracja | 20 | 93 | 22% | ❌ Krytyczny |
| 3K. BigQuery | 0 | 21 | 0% | 🔒 Brak dostępu |
| 4. Data Quality | 40 | 75 | 53% | ⚠️ Wymaga poprawy |
| 5. UTM | 9 | 18 | 50% | ⚠️ Wymaga poprawy |
| 6. BCG | 0 | 12 | 0% | ❌ Dane niedostępne |
| 7. Lejki | 1 | 8 | 13% | ❌ Krytyczny |
| 8. GA4↔Ads | 6 | 27 | 22% | ❌ Krytyczny |
| 9. Analiza danych | 6 | 24 | 25% | ❌ Krytyczny |
| 10. Google Ads | 1 | 81 | 1% | 🔒 Brak dostępu |
| **ŁĄCZNIE (bez sekcji z 🔒)** | **88** | **336** | **26%** | **❌ Krytyczny** |

*Uwaga: Sekcje 1 i 2 wymagają dostępu do DevTools/GTM Panel. Sekcje 8 i 10 wymagają BDOS. Wynik 26% jest zaniżony — przy pełnym dostępie szacujemy wynik 30–40%.*

---

## Impact finansowy (podsumowanie)

| Problem | Szacunek PLN/msc | Priorytet |
|---------|-----------------|-----------|
| Duplikaty purchase (3.83x) — błędna optymalizacja kampanii | ~50,000+ (przepalony budżet Ads) | 🔴 Natychmiast |
| itemRevenue=0 — brak optymalizacji produktowej | Niezmierzalny (analiza niemożliwa) | 🔴 Natychmiast |
| Mobile CVR 37.8% desktop — strata sprzedaży | ~200,000–500,000 PLN/msc | 🔴 Natychmiast |
| Checkout drop-off 68% — niedokończone zakupy | ~100,000–200,000 PLN/msc potencjał | 🟡 Miesiąc 1 |
| Porzucenie koszyka 95–99% | ~2,000,000 PLN/rok potencjał | 🟡 Miesiąc 1 |
| CR google/cpc 0.069% (30% organic) | ~72,000 PLN/msc stracone | 🟡 Miesiąc 1 |
| Meta fragmentation (7 źródeł) | ~5,000 PLN/msc niewidoczne | 🟡 Miesiąc 1 |
| (not set) transakcje 7% | ~34,954 PLN/msc bez atrybukcji | 🟡 Miesiąc 1 |
| SMS: 0 transakcji z 1,735 sesji | ~5,000 PLN/msc potencjał | 🟢 Miesiąc 2-3 |

---

## Top 5 problemów

1. **❌ Duplikaty purchase event (ratio 3.83x)** — hardcoded GA4 w Shoper + GTM = każdy zakup liczy się 3.83×. Wszystkie raporty konwersji fałszywe. Kampanie PMax optymalizują się na błędnych danych. Problem istnieje od minimum 04-03-2026 i nie został naprawiony. **Szacunkowy koszt: setki tysięcy PLN rocznie w błędnych decyzjach optymalizacyjnych.**

2. **❌ itemRevenue = 0 PLN dla 100% produktów** — event `purchase` nie przekazuje tablicy `items[]` z cenami. Analiza produktowa, BCG, category performance — całkowicie niemożliwe. Merchant Center nie ma danych o przychodach produktowych. **Impact: niemożliwa optymalizacja feedu i struktury kampanii Shopping/PMax.**

3. **❌ Mobile CVR 37.8% desktop** — 249,319 sesji mobile z CR 0.099% vs 62,954 sesji desktop CR 0.262%. Luka **~200,000–500,000 PLN/miesiąc** w przychodach jeśli mobile miałoby CR równy choćby 50% desktop.

4. **❌ Checkout drop-off 68%** — tylko 31.9% użytkowników, którzy zaczęli checkout, finalizuje zamówienie. Benchmark to 50–80%. Potencjał optymalizacji: **~100,000–200,000 PLN/miesiąc**.

5. **❌ Lejek rozbity + brak danych produktowych** — add_shipping_info (2,132) > begin_checkout (1,296): niemożliwe. Analiza lejka per etap jest bezużyteczna. Niemożliwa identyfikacja wąskiego gardła w procesie zakupu.
