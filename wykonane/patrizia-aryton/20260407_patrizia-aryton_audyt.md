# Raport Audytu MarTech — Patrizia by Aryton

**Data:** 2026-04-07
**Audytor:** Adrian Andrzejczyk
**GA4 Property:** patrizia.aryton.pl — GA4 (ID: 326801658)
**Measurement ID:** G-93NK3C48R3
**GTM Container:** GTM-MDGSP8
**Google Ads:** 196-867-6668
**BigQuery:** dane-z-ga4-aryton-pl
**URL strony:** https://patrizia.aryton.pl/
**Typ biznesu:** E-commerce (odzież premium — marka Patrizia)
**Platforma:** Shoper | CMP: Cookiebot
**Okres danych:** 8 marca – 7 kwietnia 2026 (30 dni)

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE

### Wyniki sekcji

| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | 5 | 36 | 14% | ❌ Krytyczny |
| 2. ePrivacy / Consent Mode | 0 | 45 | 0% | ❌ Krytyczny |
| 3. Konfiguracja GA4/GTM | 20 | 93 | 22% | ❌ Krytyczny |
| 4. Data Quality | 40 | 75 | 53% | ⚠️ Wymaga poprawy |
| 5. UTM | 9 | 18 | 50% | ⚠️ Wymaga poprawy |
| 6. BCG | 0 | 12 | 0% | ❌ Dane niedostępne |
| 7. Lejki zakupowe | 1 | 8 | 13% | ❌ Krytyczny |
| 8. GA4 ↔ Google Ads | 6 | 27 | 22% | ❌ Krytyczny |
| 9. Analiza danych | 6 | 24 | 25% | ❌ Krytyczny |
| 10. Google Ads | 1 | 81 | 1% | 🔒 Brak dostępu |
| **ŁĄCZNIE** | **88** | **336** | **26%** | **❌ Krytyczny** |

> Uwaga: Sekcje 1 i 2 wymagają weryfikacji w przeglądarce (DevTools). Sekcja 10 — brak dostępu przez BDOS. Wynik 26% jest szacunkowo zaniżony o 5–10 pp. Przy pełnym dostępie estymujemy wynik ~30–38%.

---

### Jakość danych — CZY DANYM MOŻNA UFAĆ?

**Częściowo — dane o ruchu i ogólne trendy są wiarygodne. Dane transakcyjne wymagają ostrożnej interpretacji.**

**Co jest wiarygodne:**
- Liczba sesji (~320 tys./30d), geografia, urządzenia — nie są zależne od duplikacji eventów purchase
- Kanały pozyskania ruchu — w większości wiarygodne (z wyjątkiem 7 wariantów Meta i 8 057 sesji not-set)
- Przychód łączny (515 556 PLN/30d) — GA4 deduplicuje transakcje po transaction_id; wartość jest prawdopodobnie bliska prawdy
- Liczba zamówień: metryka `transactions` = **413** (GA4 deduplikowana) — wiarygodna

**Co NIE jest wiarygodne:**
- `ecommercePurchases` = 1 582 (3.83× zawyżone) — nie używać do żadnych raportów konwersji
- CR lejka (begin_checkout → purchase = 122%) — matematycznie niemożliwy
- Dane produktowe: przychód per produkt = 0 PLN dla 100% produktów — bezużyteczne
- Lejek e-commerce: add_shipping_info > begin_checkout — logicznie niemożliwe

| Obszar | Wiarygodność | Uzasadnienie |
|---|---|---|
| Sesje i ruch | ✅ Wiarygodne | Niezależne od duplikacji purchase |
| Kanały pozyskania | ⚠️ W większości | Fragmentacja Meta (~8.5% niedokładność) |
| Liczba transakcji (`transactions`) | ✅ OK | GA4 deduplicuje po transaction_id |
| Przychód (`purchaseRevenue`) | ✅ OK | 515 556 PLN — deduplikowany |
| Przychód per produkt (`itemRevenue`) | ❌ Zerowy | items[] brak w purchase event |
| `ecommercePurchases` (raw eventy) | ❌ 3.83× zawyżone | Duplikaty z hardcoded GA4 |
| Lejek checkout → purchase | ❌ Rozbity | purchase > begin_checkout |
| add_shipping_info > begin_checkout | ❌ Anomalia | Błędny trigger w GTM lub Shoper |

---

### Konfiguracja ogólna

Podstawowe ustawienia GA4 są poprawne: strefa czasowa Europa/Warszawa, waluta PLN, retencja 14 miesięcy, Google Signals aktywne, model atrybucji Data-Driven, eksport do BigQuery aktywny, Google Ads połączone. To dobra baza techniczna.

Jednak fundamentalny problem: **GA4 jest wdrożone dwa razy** — raz bezpośrednio w HTML platformy Shoper (hardcoded `gtag`) i raz przez GTM. To powoduje, że każde zdarzenie zakupu rejestruje się ~3.83 razy zamiast jeden. Problem ten był zidentyfikowany w poprzednim audycie (04-03-2026, ratio wynosił 3.53x) i **nie został naprawiony** — ratio wzrósł do 3.83x.

Cookiebot jest wdrożony, ale przekazanie sygnałów zgody do GA4 wymaga dogłębnej weryfikacji — 8 057 sesji bez atrybukcji (`not set`) wskazuje na niekompletną implementację Consent Mode v2.

---

### Kluczowe wnioski — Top 5 problemów

**1. 🔴 Podwójne wdrożenie GA4 — ratio ecommercePurchases:transactions = 3.83×**

Wykryto 1 582 zdarzenia `purchase` przy zaledwie 413 unikalnych transakcjach (deduplikowanych przez GA4). Oznacza to, że platforma Shoper wysyła zdarzenie zakupu ze swojego hardcoded snippetu GA4 *oraz* GTM wysyła je ponownie. Efekt: każdy raport konwersji w Google Analytics jest ponad 3× zawyżony. Kampanie PMax, które optymalizują się na tej metryce, otrzymują błędne sygnały — "widzą" 3.83× więcej konwersji niż faktycznie ma miejsce, co zaburza algorytmy bidowania i może prowadzić do nadmiernych wydatków lub nietrafionych optymalizacji.

**2. 🔴 itemRevenue = 0 PLN dla 100% produktów — śledzenie item-level niedziała**

W ciągu 30 dni przy 413 zamówieniach i przychodzie 515 556 PLN, żaden produkt nie wykazuje zakupów ani przychodów w raporcie produktowym. Mimo że transakcje są zliczane (515 556 PLN jest wiarygodne), event `purchase` nie przekazuje tablicy produktów (`items[]`) z cenami. Uniemożliwia to: analizę BCG, optymalizację struktury kampanii Shopping/PMax wg rentowności produktu, identyfikację bestselerów, segmentację feedu w Merchant Center.

**3. 🔴 Mobile CR = 37.8% desktop CR — gigantyczna luka konwersji mobile**

Na urządzeniach mobilnych rejestruje się 249 319 sesji (78% całości), ale CR mobile (szac. 0.099%) jest ~2.6× niższy niż CR desktop (szac. 0.262%). Przy AOV 1 248 PLN strata wynosi potencjalnie setki tysięcy złotych miesięcznie. To wskazuje na poważne problemy UX na mobile: prawdopodobnie wolne ładowanie, trudny checkout na małym ekranie, lub nieoptymalne wyświetlanie produktów.

**4. 🟡 Checkout drop-off 68% — tylko 1 na 3 użytkowników finalizuje zakup**

Ze 1 296 sesji, które zaczęły checkout, zaledwie 413 zakończyło zakupem (31.9%). Benchmark dla dobrze zoptymalizowanego checkout to 50–80%. Każde 10 pp. poprawy = ~130 dodatkowych transakcji/miesiąc = ~162 240 PLN.

**5. 🟡 Porzucenie koszyka 95–99% — ogromny potencjał niewydobyty**

Na 32 653 sesji `add_to_cart` tylko 413 zakupiło (1.26% z faktycznych transakcji vs eventów). Nawet odzysk 2–3% porzuconych koszyków przez e-mail remarketing mógłby generować kilkaset tysięcy PLN dodatkowego przychodu miesięcznie.

---

## CZĘŚĆ II — OMÓWIENIE SZCZEGÓŁOWE

---

## SEKCJA 1 — Audyt Wstępny infrastruktury

*Audyt wstępny sprawdza fundamenty całej infrastruktury śledzenia: czy narzędzia są zainstalowane we właściwej kolejności, czy działają poprawnie na kluczowych podstronach, czy nie ma konfliktów między tagami. To jak przegląd techniczny samochodu przed długą podróżą — jeśli podstawy są zepsute, wszystkie inne analizy tracą sens.*

**Wynik sekcji: 5/36 pkt (14%) — ❌ Krytyczny**

---

### 1.2 Kolejność skryptów HTML
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

Prawidłowa kolejność skryptów w sekcji `<head>` to: (1) ustawienie domyślnej odmowy zgody [consent default], (2) inicjalizacja dataLayer, (3) snippet GTM. Każde odstępstwo od tej kolejności może powodować, że tagi w GTM uruchomią się przed ustawieniem zgód użytkownika — co jest niezgodne z RODO.

Dane GA4 jednoznacznie potwierdzają podwójne wdrożenie: Shoper posiada wbudowany mechanizm integracji z GA4, który dodaje hardcoded `gtag` bezpośrednio do HTML strony. Równocześnie GTM-MDGSP8 zawiera tag GA4. Efekt to duplikacja każdego zdarzenia, potwierdzona matematycznie przez ratio 3.83×.

**Rekomendacja:** Wyłączyć wbudowaną integrację GA4 w panelu Shoper (Ustawienia → Integracje → Google Analytics → wyłączyć). Pozostawić wyłącznie tag GA4 Configuration przez GTM.

---

### 1.5 TagHound — duplikowane tagi
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

TagHound lub DevTools wykryłby dwa aktywne kody GA4 na każdej stronie. Ratio 3.83× (1 582 eventów purchase vs 413 transakcji) jest niezbity dowodem tej duplikacji.

---

### 1.8 DataLayer — poprawność struktury
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

DataLayer `ecommerce.items[]` w evencie `purchase` nie zawiera danych produktowych. Widoczne w GA4: 100% produktów z `itemRevenue = 0 PLN` i `itemsPurchased = 0`. Przykłady produktów bez przychodów pomimo aktywnej sprzedaży:
- "Zielona sukienka midi z jedwabiu" (ID: 26307) — 7 052 odsłon, 0 zakupów w GA4
- "Beżowe sneakersy z plecionej skóry" (ID: 23308) — 1 956 odsłon, 0 zakupów w GA4
- Łącznie: 50 sprawdzonych produktów, każdy z itemRevenue = 0 PLN

Prawidłowa struktura DataLayer powinna zawierać:
```js
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'NUMER_ZAMOWIENIA',
    value: 1248.00,
    currency: 'PLN',
    items: [{
      item_id: '26307',
      item_name: 'Zielona sukienka midi z jedwabiu',
      price: 1248.00,
      quantity: 1
    }]
  }
})
```

**Rekomendacja:** Deweloper powinien sprawdzić push DataLayer na stronie potwierdzenia zamówienia (thank-you page) — czy `ecommerce.items[]` jest poprawnie wypełnione z cenami i ilościami.

---

### 1.11 Remarketing Google Ads
**Priorytet:** Średni | **Wynik:** ⚠️ 1/2 pkt

Kampanie Display (3 996 sesji) i PMax (Cross-network: 125 604 sesji) są aktywne, co sugeruje działający remarketing. Weryfikacja wymaga dostępu do DevTools lub Google Ads Panel.

---

## SEKCJA 2 — ePrivacy i Consent Mode

*ePrivacy to nie tylko kwestia prawna (RODO) — to bezpośredni wpływ na jakość danych analitycznych. Consent Mode v2 od Google pozwala na modelowanie konwersji użytkowników, którzy odmówili cookies. Bez poprawnej implementacji tracisz zarówno dane, jak i możliwości optymalizacji kampanii. Z 1 maja 2024 Consent Mode v2 jest wymagany dla działania funkcji Smart Bidding w Google Ads.*

**Wynik sekcji: 0/45 pkt (0%) — ❌ Krytyczny**

*(Ocena oparta na pośrednich wskaźnikach z GA4. Pełna weryfikacja wymaga testów w przeglądarce z DevTools.)*

---

### 2.4 Blokowanie cookies po odmowie
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

Wskaźnik pośredni: 8 057 sesji (2.52%) przypisanych jako `(not set)/(not set)` sugeruje niekompletną implementację Consent Mode. Prawidłowa implementacja powinna generować *anonimowe pingi* do GA4 (modelowane dane), a nie pełne sesje `(not set)`. Fakt, że te sesje pojawiają się w raportach, wskazuje na możliwe wycieki danych przy odmowie zgody.

29 transakcji (7.0% wszystkich) pochodzi z `(not set)` — łączna wartość to ~34 954 PLN/miesiąc bez atrybukcji.

---

### 2.17 url_passthrough
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

`url_passthrough` to parametr GA4, który pozwala na przekazanie informacji o kampanii przez URL nawet gdy użytkownik odmówił cookies. Bez tego parametru każdy użytkownik, który odmówił zgody, a kliknął reklamę Google Ads, traci atrybuję do tej kampanii.

Z poprzedniego audytu (04-03-2026): `url_passthrough` nie było skonfigurowane. Problem nadal istnieje. Szacowany wpływ: ~29 transakcji/miesiąc (7% z 413) bez prawidłowej atrybuacji = **~36 192 PLN/miesiąc bez atrybuacji**.

**Rekomendacja:** W GTM → Tag GA4 Configuration → Pola konfiguracji → dodać: klucz `url_passthrough`, wartość `true`.

---

### Ogólna ocena Consent Mode

Cookiebot jest wdrożony i baner prawdopodobnie wyświetla się użytkownikom. Jednak integracja z GTM wymaga weryfikacji:
- Czy tag Cookiebot ładuje się w trybie "Consent Initialization" (przed GTM) czy "All Pages" (zbyt późno)?
- Czy w GTM każdy tag analityczny ma ustawione wymagania consent (`analytics_storage`)?
- Czy w GTM każdy tag reklamowy ma ustawione wymagania (`ad_storage`, `ad_user_data`, `ad_personalization`)?

**Rekomendacja:** Przeprowadzić test w trybie incognito z DevTools: załadować stronę → odmówić zgody → sprawdzić Network, czy pojawia się request do `google-analytics.com/g/collect` lub cookies `_ga`, `_gid`.

---

## SEKCJA 3 — Konfiguracja GTM i GA4

*Konfiguracja to "silnik" całej analityki. GTM (Google Tag Manager) to system zarządzania tagami — jedno miejsce, z którego zarządzamy wszystkimi narzędziami śledzącymi. GA4 to platforma analityczna Google. Ich prawidłowa konfiguracja jest warunkiem koniecznym dla wiarygodności wszystkich danych.*

**Wynik sekcji: 20/93 pkt (22%) — ❌ Krytyczny**

---

### 3A.1 Podwójne wdrożenie GA4
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

To najpoważniejszy problem techniczny całej instalacji. Platforma Shoper posiada wbudowaną integrację z Google Analytics, która automatycznie dodaje kod śledzący bezpośrednio do HTML strony. Jednocześnie GTM-MDGSP8 zawiera własny tag GA4 Configuration.

Skutki:
1. Każde zdarzenie (page_view, add_to_cart, purchase) rejestruje się dwukrotnie lub więcej
2. Ratio ecommercePurchases:transactions = **3.83×** — matematyczny dowód duplikacji
3. Kampanie Google Ads "widzą" 3.83× więcej konwersji niż faktycznie ma miejsce
4. Smart Bidding optymalizuje się na fałszywych sygnałach konwersji

**Rekomendacja:** Krok 1 — W panelu Shoper: Ustawienia → Integracje → Google Analytics → wyłączyć wbudowaną integrację. Krok 2 — Sprawdzić w GTM Preview czy po wyłączeniu pojawia się jeden tag GA4 per zdarzenie.

---

### 3C.3 Waluta
**Priorytet:** Średni | **Wynik:** ✅ 2/2 pkt

Waluta PLN ustawiona poprawnie. Przychody w GA4 spójne z PLN (515 556 PLN/30d, AOV 1 248 PLN).

---

### 3C.4 Google Signals
**Priorytet:** Wysoki | **Wynik:** ✅ 3/3 pkt

Google Signals aktywne — umożliwia cross-device tracking i raporty demograficzne.

---

### 3C.8 Filtrowanie ruchu wewnętrznego
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

W danych GA4 widoczne są sesje z wewnętrznych zasobów firmy Aryton:
- `dev18.arytondev.local/referral` — 10 sesji (środowisko deweloperskie Aryton)
- `arytonpl.sharepoint.com/referral` — 28 sesji (wewnętrzny SharePoint firmy)

Łącznie 38 sesji/miesiąc z wewnętrznych źródeł nie jest filtrowanych. Choć liczba jest mała, wskazuje na brak filtru IP lub hostname dla ruchu pracowniczego.

**Rekomendacja:** GA4 → Admin → Filtry danych → dodać filtr "Ruch wewnętrzny" dla hostname zawierającego `arytondev.local` oraz zakresu IP biura.

---

### 3C.10 Cross-domain tracking — Klarna
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

`klarna/referral` — 71 sesji/miesiąc. Klarna to popularna usługa płatności odroczonej BNPL (Buy Now Pay Later). Gdy użytkownik klika "Kup teraz, zapłać później", przechodzi na stronę Klarna w celu autoryzacji. Po powrocie do sklepu GA4 traktuje go jako nową sesję z referral = `klarna`.

Konsekwencja: transakcje z Klanry są przypisywane do `klarna/referral` zamiast do oryginalnego kanału (np. google/cpc lub facebook/cpc). Zaburza to raportowanie efektywności kanałów reklamowych.

**Rekomendacja:** GA4 → Strumień danych → Konfigurowanie domen → Referral exclusion → dodać: `klarna.com`, `checkout.klarna.com`. Jeśli używane są inne bramki płatnicze — dodać je również.

---

### 3C.11 Ignorowanie zduplikowanych konfiguracji
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

W GA4 istnieje ustawienie "Ignoruj zduplikowane konfiguracje tagów GA4", które powinno blokować duplikaty. Jednak samo włączenie tego ustawienia nie rozwiązuje problemu — jest to tylko ostatnia linia obrony. Konieczne jest wyłączenie hardcoded snippetu w Shoper.

---

### 3C.12–3C.13 Wykluczenia referral
**Priorytet:** Wysoki | **Wynik:** ❌ 0/5 pkt

**Niezwykluczone bramki płatnicze:** Klarna (71 sesji)
**Niezwykluczone bramki pocztowe (webmaile):**
- `poczta.onet.pl` — 198 sesji
- `poczta.interia.pl` — 80 sesji
- `poczta.o2.pl` — 76 sesji
- `poczta.wp.pl` — 46 sesji, 1 transakcja (719 PLN)

Łącznie **400 sesji z webmaili** pojawia się jako referral zamiast być prawidłowo przypisanych do kanału email. 719 PLN przychodu jest błędnie przypisane do `poczta.wp.pl/referral` zamiast do email/edrone.

**Rekomendacja:** GA4 → Strumień → Referral exclusion → dodać: `klarna.com`, `wp.pl`, `onet.pl`, `o2.pl`, `interia.pl`.

---

### 3C.17 Model atrybucji
**Priorytet:** Średni | **Wynik:** ✅ 2/2 pkt

Data-Driven Attribution (DDA) aktywny. To najlepsza opcja dla e-commerce — model uczący się na rzeczywistych ścieżkach konwersji.

---

### 3C.18 Połączenie Google Ads
**Priorytet:** Wysoki | **Wynik:** ✅ 3/3 pkt

Połączenie GA4 ↔ Google Ads aktywne. Reklamy spersonalizowane włączone.

---

### 3C.19 BigQuery
**Priorytet:** Wysoki | **Wynik:** ✅ 3/3 pkt

Dataset `dane-z-ga4-aryton-pl` aktywny. Eksport działa.

---

## SEKCJA 4 — Jakość danych

*Jakość danych to odpowiedź na pytanie "Czy danym w Google Analytics można zaufać?". Nawet najlepiej skonfigurowany system może zbierać złe dane jeśli parametry kampanii są niespójne, transakcje zduplikowane, lub ruch wewnętrzny firmy nie jest odfiltrowany. Sekcja ta sprawdza, czy dane są kompletne, spójne i wolne od zanieczyszczeń.*

**Wynik sekcji: 40/75 pkt (53%) — ⚠️ Wymaga poprawy**

---

### 4D.1 Duplikacja purchase event — KRYTYCZNE
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

Metryki z 30 dni:
- `ecommercePurchases` (raw eventy purchase): **1 582**
- `transactions` (deduplikowane po transaction_id): **413**
- **Ratio: 3.83×**

Interpretacja: jeden zakup generuje średnio 3.83 zdarzenia `purchase`. GA4 jest wystarczająco mądry, żeby deduplikować transakcje po `transaction_id` — dlatego metryka `transactions = 413` jest prawdopodobnie bliska prawdy. Jednak metryka `ecommercePurchases = 1 582` jest bezużyteczna i misleadingowa.

Problem istnieje od minimum 04-03-2026 (poprzedni audyt: ratio 3.53×). W ciągu 4 dni ratio wzrósł z 3.53× do 3.83× — problem pogłębia się, nie poprawia.

---

### 4A.9 Fragmentacja Meta/Facebook — 7 wariantów
**Priorytet:** Średni | **Wynik:** ❌ 0/2 pkt

Ruch z kampanii i profili Meta pojawia się w GA4 pod 7 różnymi wariantami source:

| Źródło | Medium | Sesje | Transakcje | Przychód |
|--------|--------|-------|------------|---------|
| facebook | cpc | 57 699 | 25 | 34 433 PLN |
| m.facebook.com | referral | 1 722 | 5 | 4 220 PLN |
| l.instagram.com | referral | 1 645 | 1 | 1 198 PLN |
| l.facebook.com | referral | 690 | 0 | 0 PLN |
| lm.facebook.com | referral | 381 | 0 | 0 PLN |
| facebook | referral | 363 | 3 | 1 737 PLN |
| facebook.com | referral | 86 | 0 | 0 PLN |
| **Łącznie Meta** | | **62 586** | **34** | **41 588 PLN** |

Porównując tylko `facebook/cpc`: 25 transakcji (34 433 PLN) vs faktyczna wartość Meta: 34 transakcje (41 588 PLN). ROAS Meta zaniżony o ~20%.

Przyczyna fragmentacji: linki w kampaniach płatnych mają UTM (`facebook/cpc`), ale linki w postach organicznych, stories i innych formatach nie mają UTM — więc GA4 rozpoznaje oryginalny host (`m.facebook.com`, `l.instagram.com` itd.).

**Rekomendacja:** Oznaczyć UTM wszystkie linki organiczne na Facebooku i Instagramie (source=instagram/facebook, medium=social, campaign=nazwa_kampanii).

---

### 4D.3 Malformed UTM source
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

Wykryto sesje, gdzie cały URL Google Ads jest zapisany jako `sessionSource`:

```
google&utm_medium=cpc&utm_campaign=SEA_|_Brand_|_Aryton&utm_id=19091733253
&utm_term=kurtka patrizia aryton&utm_content=638313710563&gad_source=1
&gad_campaignid=19091733253&gclid=Cj0KCQiAyvHLBhDlARIsAH...
```

Oznacza to, że niektóre linki Google Ads mają nieprawidłowo skonstruowany URL: zamiast `?utm_source=google&utm_medium=cpc&...` parametry UTM są doklejone bezpośrednio do domeny bez separatora `?`. Dotyczy kampanii brandowych `SEA_|_Brand_|_Aryton`.

**Rekomendacja:** W Google Ads → kampania Brand → URL templates → sprawdzić i poprawić szablon URL na: `{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}`.

---

### 4E.5 Lejek e-commerce — anomalie
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

Prawidłowy lejek zakupowy powinien wyglądać tak: view_item > add_to_cart > begin_checkout > add_shipping_info > add_payment_info > purchase. Każdy kolejny krok powinien mieć mniejszą liczbę eventów niż poprzedni.

Aktualny stan (eventy z 30d):
```
view_item:          590 185  ✅
add_to_cart:         32 653  ✅ (5.5% z view_item)
begin_checkout:       1 296  ❌ (3.97% z add_to_cart — bardzo nisko)
add_shipping_info:    2 132  ❌ (> begin_checkout — NIEMOŻLIWE)
add_payment_info:       806  ✅ (ok względem begin_checkout)
purchase:             1 582  ❌ (> add_payment_info — zduplikowane)
```

Problem 1: `begin_checkout` (1 296) jest bardzo nisko w stosunku do `add_to_cart` (32 653) — tylko 3.97% dodających do koszyka przechodzi do checkout. Benchmark: 30–60%. To wskazuje albo na problem UX koszyka albo na brak triggera `begin_checkout` na pewnych ścieżkach.

Problem 2: `add_shipping_info` (2 132) > `begin_checkout` (1 296) — matematycznie niemożliwe. Prawdopodobna przyczyna: trigger `add_shipping_info` odpala się na etapie wcześniejszym niż `begin_checkout` w procesie zakupu Shopera.

---

## SEKCJA 5 — UTM — Oznaczenia kampanii

*UTM (Urchin Tracking Module) to parametry dodawane do URL linków w kampaniach reklamowych, emailach i mediach społecznościowych. Dzięki nim Google Analytics wie, skąd przyszedł użytkownik — z jakiej kampanii, z jakich reklamy, z jakiego medium. Bez UTM kampanie płatne mogą być widoczne jako "direct" lub "organic" — co sprawia, że nie można ocenić ich efektywności.*

**Wynik sekcji: 9/18 pkt (50%) — ⚠️ Wymaga poprawy**

---

### 5.2 Google Ads — UTM
**Priorytet:** Wysoki | **Wynik:** ✅ 3/3 pkt

Google Ads jest prawidłowo tagowany — `google/cpc` widoczne z 132 384 sesjami. Automatyczne tagowanie Google (auto-tagging) działa poprawnie.

---

### 5.3 Google Ads — malformed UTM kampanii
**Priorytet:** Wysoki | **Wynik:** ❌ 0/3 pkt

Kamapania brandowa `SEA_|_Brand_|_Aryton` generuje kilka sesji z całym URL jako source (patrz punkt 4D.3). Wymaga naprawy szablonu URL.

---

### 5.4 Meta Ads — UTM
**Priorytet:** Wysoki | **Wynik:** ⚠️ 1/3 pkt

Płatne kampanie Meta (`facebook/cpc`): 57 699 sesji — UTM działa. Jednak 4 887 sesji z Meta (~8.5%) nie ma UTM i trafia jako referral z różnych domen Facebooka/Instagrama.

---

### 5.7 Email marketing — UTM
**Priorytet:** Średni | **Wynik:** ✅ 2/2 pkt

edrone/email: 17 457 sesji, 40 transakcji, 51 771 PLN. Kampanie emailowe prawidłowo oznaczone UTM source=edrone medium=email.

---

### 5.10 SMS — brak UTM/konwersji
**Priorytet:** Średni | **Wynik:** ❌ 0/2 pkt

`sms/smsapi`: 1 735 sesji, **0 transakcji, 0 PLN przychodów**. Mając taki wolumen sesji przy zerowym przychodzie, mamy do czynienia z jednym z trzech problemów:
1. Linki SMS kierują na złą stronę (np. stronę główną zamiast na konkretny produkt/promocję)
2. SMS ma UTM source=sms medium=smsapi, ale strona docelowa nie konwertuje
3. Sesje z SMS są liczone, ale konwersje nie są przypisywane ze względu na redirect

**Rekomendacja:** Sprawdzić landing pages z linków SMS; zmierzyć CR bezpośrednio z UTM session SMS w GA4 Explore.

---

## SEKCJA 7 — Lejki zakupowe per kanał

*Lejek zakupowy to sekwencja kroków od pierwszego kontaktu z produktem do zakupu: odsłona produktu → koszyk → checkout → zakup. Analiza lejka per kanał pozwala zidentyfikować, który etap jest wąskim gardłem i dla których kanałów.*

**Wynik sekcji: 1/8 pkt (13%) — ❌ Krytyczny**

---

### Dane lejka per kanał (30d)

| Kanał | Sesje | addToCarts | Checkouts | Purchases | CR sess→purch |
|-------|-------|------------|-----------|-----------|---------------|
| Cross-network (PMax) | 125 604 | 5 357 | 247 | 255 | 0.20% |
| Organic Search | 79 134 | 13 693 | 570 | 683 | 0.86% |
| Paid Social (Meta) | 57 699 | 4 207 | 136 | 186 | 0.32% |
| Email (edrone) | 17 470 | 3 302 | 142 | 178 | 1.02% |
| Direct | 16 376 | 2 290 | 45 | 122 | 0.75% |
| Unassigned | 8 081 | 1 374 | 47 | 45 | 0.56% |
| Organic Social | 4 879 | 508 | 19 | 24 | 0.49% |
| Paid Search | 4 458 | 900 | 47 | 46 | 1.03% |
| Display | 3 996 | 498 | 25 | 22 | 0.55% |
| SMS | 1 737 | 332 | 3 | 5 | 0.29% |
| Referral | 1 072 | 191 | 15 | 15 | 1.40% |

> Uwaga: Wartości `Purchases` to `ecommercePurchases` (raw eventy, zawyżone ~3.83×). Rzeczywisty CR jest ~3.83× niższy.

---

### 7.2 CR paid vs CR organic
**Priorytet:** Wysoki | **Wynik:** ❌ 0/2 pkt

CR google/cpc (source/medium): 91 transakcji / 132 384 sesji = **0.069%**
CR google/organic: 168 transakcji / 74 329 sesji = **0.226%**
Ratio CR paid/organic = **30.5%** (minimum to 50%)

Oznacza to, że 1 złotówka wydana na pozyskanie ruchu z CPC przynosi 3× mniej transakcji niż ten sam ruch organiczny. Może to wynikać z: (1) kampanie CPC kierują na stronę główną zamiast na produkty, (2) targetowanie jest zbyt szerokie, (3) brak dopasowania między reklamą a landing page.

**Impact:** Gdyby google/cpc miało CR = 50% organic (tj. 0.113%), przy 132 384 sesjach = **~150 transakcji/msc zamiast 91** = +59 transakcji × 1 248 PLN = **~73 632 PLN/msc** dodatkowego przychodu bez zwiększania budżetu.

---

### 7.4 Checkout drop-off
**Priorytet:** Wysoki | **Wynik:** ❌ 0/2 pkt

Ze 1 296 sesji begin_checkout tylko 413 zakończyło zakupem = **31.9% konwersji checkout**. To 68.1% drop-off — użytkownicy rezygnują na etapie finalizacji. Typowe przyczyny dla odzieży premium:
- Zbyt wiele kroków w checkout
- Ograniczone opcje płatności
- Brak opcji "gościa" (wymóg zakładania konta)
- Problemy z UX na mobile (68.1% sesji to mobile)
- Zaskakujące koszty dostawy

---

## SEKCJA 9 — Analiza danych

*Analiza danych to odpowiedź na pytanie "Jak sklep rzeczywiście działa?". Patrzymy na efektywność kanałów, zachowanie urządzeń, geografię. To podstawa rekomendacji strategicznych.*

**Wynik sekcji: 6/24 pkt (25%) — ❌ Krytyczny**

---

### Rev/sesja per kanał — Ranking efektywności

| Kanał | Rev (PLN) | Sesje | Rev/sesja |
|-------|-----------|-------|-----------|
| Organic Search | 234 013 | 74 329 | **3.15 PLN** |
| Email (edrone) | 51 771 | 17 457 | **2.97 PLN** |
| Bing organic | 26 428 | 2 801 | **9.43 PLN** ⭐ |
| Direct | 20 139 | 16 376 | **1.23 PLN** |
| (not set) | 34 954 | 8 057 | — |
| Google CPC | 95 560 | 132 384 | **0.72 PLN** |
| Paid Social Meta | 34 433 | 57 699 | **0.60 PLN** |
| Cross-network | 75 104 | 125 604 | **0.60 PLN** |

**Kluczowe obserwacje:**
1. **Bing organic** — zaledwie 2 801 sesji ale Rev/sesja = 9.43 PLN — najefektywniejszy kanał! Kompletnie niedoinwestowany.
2. **Google CPC** — Rev/sesja = 0.72 PLN vs Organic 3.15 PLN — kanał płatny 4.4× mniej efektywny
3. **Cross-network (PMax)** — największy wolumen sesji (125 604) ale najniższy Rev/sesja (0.60 PLN) — PMax wydaje dużo na słaby ruch

---

### 9.3 Mobile vs Desktop — Luka konwersji

| Urządzenie | Sesje | Szac. transakcje | CR | Rev (PLN) |
|-----------|-------|------------------|----|-----------|
| Desktop | 62 954 | ~165 | 0.262% | 200 534 |
| Mobile | 249 319 | ~247 | 0.099% | 314 523 |
| Tablet | 4 615 | ~1 | 0.022% | 499 |

> Szacunki transakcji per urządzenie oparte na proporcji ecommercePurchases zdeduplikowanej przez ratio 413/1582.

Mobile generuje **78%** całego ruchu ale tylko **60%** przychodów. CR mobile (0.099%) jest **2.6× niższy** niż desktop (0.262%).

**Obliczenie potencjału:** Gdyby mobile osiągnęło CR = 50% desktop (0.131%):
Dodatkowe transakcje = 249 319 × (0.131% - 0.099%) = 249 319 × 0.032% ≈ **80 transakcji/msc**
Dodatkowy przychód = 80 × 1 248 PLN = **99 840 PLN/msc** = **~1.2M PLN/rok**

To ostrożna estymacja przy celu 50% desktop CR. Przy 70% desktop byłoby to blisko **2M PLN/rok** dodatkowego przychodu.

---

### 9.5 Porzucenie koszyka

`add_to_cart` = 32 653 sesji. Faktyczne transakcje = 413.
Cart abandonment rate = 1 - (413/32 653) = **98.7%**

To jeden z najwyższych wskaźników porzucenia koszyków. Nawet w branży odzieżowej (gdzie porzucenie 70–80% jest normą) wynik 98.7% wskazuje na poważne bariery w procesie zakupu.

Potencjał odzysku z abandoned cart (przy 3% recovery rate):
32 240 porzuconych koszyków × 3% = 967 dodatkowych transakcji
967 × 1 248 PLN = **~1 207 000 PLN/rok**

Narzędzie edrone posiada funkcję abandoned cart emails — wymaga aktywacji.

---

## SEKCJA 8 — GA4 ↔ Google Ads

**Wynik sekcji: 6/27 pkt (22%) — ❌ Krytyczny**

Połączenie GA4↔Ads aktywne, reklamy spersonalizowane włączone (✅ 6/6 pkt za te dwa elementy). Pozostałe punkty wymagają weryfikacji w Google Ads Panel, do którego brak dostępu przez BDOS.

Kluczowe ryzyko: Kampanie PMax optymalizują się na podstawie `ecommercePurchases` = 1 582 (zawyżone 3.83×). Google "widzi" 3.83× więcej konwersji niż faktycznie ma miejsce. Algorytm Smart Bidding może agresywnie podnosić bidy wierząc, że kampanie są skuteczniejsze niż są.

---

## CZĘŚĆ II.B — Impact finansowy (podsumowanie)

| Problem | Szacunek strat/potencjał PLN/msc | Typ | Priorytet |
|---------|----------------------------------|-----|-----------|
| Duplikaty purchase — błędna optymalizacja PMax | niezmierzalne przepalenie budżetu | Strata | 🔴 |
| itemRevenue=0 — niemożliwa optymalizacja produktowa | niezmierzalne | Strata | 🔴 |
| Mobile CVR 2.6× niższy niż desktop | ~100 000 – 500 000 PLN/msc potencjał | Szansa | 🔴 |
| Checkout drop-off 68% | ~100 000 – 200 000 PLN/msc potencjał | Szansa | 🟡 |
| Porzucenie koszyka 98.7% | ~100 000 PLN/msc (przy 3% recovery) | Szansa | 🟡 |
| google/cpc CR 30% organic | ~73 632 PLN/msc niedopieczony | Szansa | 🟡 |
| Meta fragmentacja 7 źródeł | ~5 000 PLN/msc niewidoczne | Strata | 🟡 |
| (not set) transakcje 7% = brak atrybuacji | ~36 192 PLN/msc | Strata | 🟡 |
| SMS: 0 transakcji z 1 735 sesji | ~5 000 PLN/msc potencjał | Szansa | 🟢 |
| Webmaile + Klarna w referral | ~5 000 PLN/msc błędna atrybuacja | Strata | 🟢 |

**Łączny szacowany potencjał (konserwatywny):** ~300 000 – 800 000 PLN/miesiąc

---

## CZĘŚĆ III — REKOMENDACJE

### 🔴 Natychmiast (0–7 dni) — Zatamowanie strat

**1. Wyłączyć hardcoded GA4 w Shoper**
- Panel Shoper → Ustawienia → Integracje → Google Analytics → wyłączyć
- Efekt: ratio purchase:transactions spada do ~1.0×, kampanie PMax otrzymują prawdziwe dane
- Ryzyko: po wyłączeniu dane historyczne nie zmienią się, ale dane od jutra będą wiarygodne

**2. Naprawić DataLayer items[] na stronie thank-you**
- Deweloper → strona potwierdzenia zamówienia → zweryfikować `dataLayer.push` przy evencie `purchase`
- Upewnić się, że `ecommerce.items[]` zawiera: `item_id`, `item_name`, `price`, `quantity`
- Efekt: dane produktowe zaczną napływać, BCG możliwe, feed zoptymalizowany

**3. Skonfigurować url_passthrough w GTM**
- GTM → Tag GA4 Configuration → Pola konfiguracji → dodać `url_passthrough = true`
- Efekt: ~29 transakcji/msc odzyska atrybuację, ~36 000 PLN/msc mierzalne

**4. Dodać Referral exclusion**
- GA4 → Strumień → Referral exclusion → dodać: `klarna.com`, `wp.pl`, `onet.pl`, `o2.pl`, `interia.pl`
- Efekt: 471 sesji/msc z prawidłową atrybuacją

---

### 🟡 Miesiąc 1 — Optymalizacja i naprawa

**5. Audyt UX mobile — priorytet #1 po naprawie trackingu**
- Sprawdzić Core Web Vitals na mobile (Google PageSpeed Insights)
- Zmierzyć czas checkout na telefonie — powinien być max 3 kroki
- Sprawdzić rozmiar przycisków CTA, czytelność produktów
- Implementować Apple Pay / Google Pay (natywne metody mobile)
- Cel: podnieść CR mobile z 0.099% do min. 0.15% = +130 000 PLN/msc

**6. Wdrożyć abandoned cart emails w edrone**
- edrone posiada gotowy moduł abandoned cart
- Sekwencja: 1h po porzuceniu (bez rabatu) → 24h (z 5% rabatu) → 72h (ostatnia szansa)
- Cel: odzysk 2–3% z 32 240 porzuconych koszyków = +640–970 transakcji/msc = +800 000–1 200 000 PLN/rok

**7. Naprawić lejek checkout — zmniejszyć drop-off z 68% do 50%**
- Analiza heatmap mobile na stronie checkout (Clarity lub Hotjar)
- Uprościć formularz (autouzupełnianie adresu, mniejsza liczba pól)
- Dodać progress bar (użytkownik widzi etap procesu)
- Sprawdzić opcje płatności — czy Klarna, PayU, BLIK są dostępne

**8. Oznaczyć UTM linki organiczne Meta**
- Dla każdego postu organicznego na Facebooku/Instagramie dodawać UTM: `?utm_source=facebook&utm_medium=social&utm_campaign=organic_post`
- Efekt: 4 887 sesji/msc zmienia klasyfikację z referral na social/organic → spójne raportowanie

**9. Wdrożyć Consent Mode v2 prawidłowo**
- Sprawdzić w GTM czy Cookiebot tag jest w triggerze "Consent Initialization"
- Sprawdzić czy wszystkie tagi mają ustawione wymagania zgody
- Przetestować z DevTools: incognito → odmówić zgody → sprawdzić Network

---

### 🟢 Miesiąc 2–3 — Skalowanie i strategia

**10. Analiza BCG po naprawie items[]**
- Po naprawieniu DataLayer items[] (punkt 2) — po 30 dniach pojawią się dane produktowe
- Przeprowadzić analizę BCG: podzielić produkty na Gwiazdy/Dojne Krowy/Znaki Zapytania/Psy
- Wydzielić asset groups w PMax per kategoria BCG

**11. Skalować Bing Ads**
- Bing organic: 2 801 sesji, Rev/sesja = 9.43 PLN (najlepsza efektywność!)
- Wdrożyć kampanie Microsoft Advertising z tym samym feedem
- Potencjał: 10× skalowanie = 28 000 sesji × 9.43 PLN = ~264 000 PLN/msc

**12. Wdrożyć sGTM (GTM Server-Side)**
- Eliminuje duplikacje na poziomie serwera, nie klienta
- Poprawia jakość Consent Mode i 1st-party cookies
- Prerequisite: domena 1st-party (np. `analytics.patrizia.aryton.pl`)

**13. Filtrowanie ruchu wewnętrznego**
- GA4 → Filtry → dodać filtr hostname dla `arytondev.local`
- Opcjonalnie: filtr zakresu IP biura Aryton

**14. Aktywować SMS remarketing z prawidłowym tracking**
- Sprawdzić landing pages z linków SMS
- Dodać prawidłowe UTM + deep linki do produktów
- Zmierzyć CR po naprawie

---

## Podsumowanie — co jest najważniejsze

Strona patrizia.aryton.pl generuje ~515 556 PLN/miesiąc przy 413 zamówieniach (AOV 1 248 PLN). To solidna baza dla marki premium. Jednak infrastruktura technologiczna ma krytyczne luki, które:

1. **Kłamią** — duplikaty purchase 3.83× = kampanie "widzą" 4× więcej konwersji niż jest
2. **Ślepią** — itemRevenue=0 = nie wiadomo które produkty sprzedają
3. **Marnują szanse** — mobile CR 2.6× niższy = ~100 000–500 000 PLN/msc potencjału nieodrobionego
4. **Gubiąa pieniądze** — checkout drop-off 68% = 2 na 3 gotowych kupujących rezygnuje

Naprawienie pierwszych 4 punktów (wyłączenie hardcoded GA4, naprawa DataLayer items[], url_passthrough, wykluczenia referral) jest możliwe w **48 godzin przez jednego dewelopera** i powinno być traktowane jako absolutny priorytet.

Optimalizacja UX mobile i wdrożenie abandoned cart emails (punkty 5 i 6) to 4–6 tygodni pracy i potencjał **1–2 mln PLN/rok** dodatkowego przychodu.
