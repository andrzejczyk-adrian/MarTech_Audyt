# Raport Audytu GA4 / MarTech
> **Ten szablon generuje DWA pliki:**
> - `Plik 1 — Podsumowanie` (sekcje oznaczone `[KRÓTKI]`) — 2–3 strony, dla właściciela/dyrektora
> - `Plik 2 — Raport szczegółowy` (wszystkie sekcje) — pełna analiza, bez ograniczeń objętości
>
> Tryb multi-konto: CZĘŚĆ 0 wypełnij gdy audytujesz >1 kont GA4/Ads. Dla 1 konta → pomiń CZĘŚĆ 0.

**Klient:** _______________
**Data:** _______________ | **Okres analizy:** _______________
**Audytor:** Adrian Andrzejczyk
**Liczba kont:** ___ (GA4: ___ | Google Ads: ___)
**MCC ID:** _______________ | **GA4 Property ID(s):** _______________
**Typ biznesu:** e-commerce / lead gen / SaaS / mix
**URL(y) strony:** _______________

---

## CZĘŚĆ 0 — TABELA PRZESTAWNA KONT `[KRÓTKI]` _(tryb multi-konto)_

> Pomiń jeśli audytujesz tylko 1 konto. Wypełnij automatycznie z Google Ads API.

### 0.1 — Dane portfela

| Metryka | Wartość |
|---------|---------|
| Kont łącznie w MCC | |
| Kont aktywnych (z wydatkami) | |
| Kont nieaktywnych | |
| Łączne wydatki 30d (PLN) | |
| Łączne konwersje 30d | |
| Łączna wartość konwersji 30d (PLN) | |
| ROAS portfela (aktywne konta e-comm) | x |

### 0.2 — Tabela przestawna kont aktywnych `[KRÓTKI]`

| # | Konto | Wydatki 30d | ROAS | Konwersje | Kamp. bez konw. | Niski ROAS | Wysoki CPA | Niski QS | GA4 | Status |
|---|-------|------------|------|-----------|-----------------|------------|------------|---------|-----|--------|
| 1 | | PLN | x | | ✅/⚠️ | ✅/🔴 | ✅/🔴 | ✅/🔴 | ✅/❌ | ✅/⚠️/🔴 |
| 2 | | PLN | x | | | | | | | |
| 3 | | PLN | x | | | | | | | |
| ... | | | | | | | | | | |

**Legenda:** ✅ OK | ⚠️ Uwaga | 🔴 Problem | ℹ️ Lead gen | 💤 Nieaktywne

### 0.3 — Wyniki kampanii per konto (top konta wg wydatków) `[KRÓTKI]`

| # | Konto | Wydatki | Kliknięcia | Konwersje | Wart. konw. | ROAS | CPA | Avg QS | Typy kampanii |
|---|-------|---------|-----------|----------|------------|------|-----|--------|--------------|
| 1 | | PLN | | | PLN | x | PLN | /10 | |
| 2 | | PLN | | | PLN | x | PLN | /10 | |
| ... | | | | | | | | | |

### 0.4 — Segmentacja portfela i problemy `[KRÓTKI]`

**Podział na segmenty:**
```
✅ OK:      N kont | łączne wydatki: PLN
⚠️ Uwaga:  N kont
🔴 Problem: N kont | szacowany koszt strat: PLN/msc
ℹ️ Lead gen: N kont
💤 Nieaktywne: N kont
```

**Top problemy (posortowane wg kosztu/wpływu):**

**1. 🔴 Konta e-commerce z ROAS < 2x**
| Konto | Wydatki | ROAS |
|-------|---------|------|
| | PLN | x |
**Łącznie: PLN/msc przy negatywnym lub śladowym zwrocie**

**2. ⚠️ Kampanie bez konwersji (drenaż budżetu)**
- Konto A: N kampanii, PLN drenażu/msc
- Konto B: N kampanii, PLN drenażu/msc

**3. 🔴 Konta z 0 konwersjami na całym koncie**
| Konto | Wydatki | Kampanie aktywne |
|-------|---------|-----------------|
| | PLN | N |

**4. ℹ️ Konta lead gen bez wartości konwersji**
Lista: _______________ (do weryfikacji z klientem)

**5. 💤 Konta nieaktywne do weryfikacji**
Lista: _______________

### 0.5 — Ocena portfela per konto `[KRÓTKI]`

| Konto | Ocena specjalisty | Najważniejszy problem | Priorytet działania |
|-------|------------------|----------------------|---------------------|
| | ⭐⭐ (2/5) | | 🔴/🟡/🟢 |
| | ⭐⭐⭐ (3/5) | | |

---

## CZĘŚĆ 0B — ANALIZA BŁĘDÓW POWTARZALNYCH (CROSS-ACCOUNT) `[KRÓTKI]` _(tryb multi-konto)_

> Pomiń jeśli audytujesz tylko 1 konto.
> Cel: identyfikacja błędów, które powtarzają się u wielu klientów — to sygnał problemu systemowego.

### Macierz powtarzalności błędów

Legenda: ❌ Błąd wykryty | ✅ OK | ➖ Nie dotyczy / Brak dostępu

| Błąd / Problem | [Klient 1] | [Klient 2] | [Klient 3] | [Klient 4] | [Klient 5] | Razem | % klientów |
|----------------|-----------|-----------|-----------|-----------|-----------|-------|------------|
| **GA4** | | | | | | | |
| Brak GA4 lub brak dostępu | | | | | | | |
| Brak połączenia GA4 ↔ Ads | | | | | | | |
| Delta przychodów GA4 vs Ads > 15% | | | | | | | |
| **ePrivacy / Consent** | | | | | | | |
| Brak Consent Mode v2 | | | | | | | |
| Brak możliwości odrzucenia zgód | | | | | | | |
| Tagi odpalają się przed zgodą | | | | | | | |
| **GTM / Implementacja** | | | | | | | |
| Duplikacja tagu GA4 | | | | | | | |
| Zła kolejność skryptów | | | | | | | |
| Błędy w DataLayer (e-commerce) | | | | | | | |
| Stare kody UA na stronie | | | | | | | |
| **Data Quality** | | | | | | | |
| Udział (not set) > 20% | | | | | | | |
| Duplikaty transakcji | | | | | | | |
| Niska jakość źródeł ruchu | | | | | | | |
| **UTM** | | | | | | | |
| Nieoznaczone kampanie paid | | | | | | | |
| Fragmentacja UTM (np. facebook vs facebook.com) | | | | | | | |
| **Google Ads** | | | | | | | |
| Niski QS (< 5.0 avg) | | | | | | | |
| Kampanie bez konwersji (> 300 PLN, 0 konw.) | | | | | | | |
| Brak Enhanced Conversions | | | | | | | |
| Błędna konfiguracja konwersji (mikrokonwersje) | | | | | | | |
| Brak Customer Match | | | | | | | |
| Brak RLSA / list remarketingowych | | | | | | | |
| Manual CPC zamiast smart bidding | | | | | | | |
| Brak kampanii brand | | | | | | | |
| Auto-apply recommendations włączone | | | | | | | |
| **Feed / Merchant Center** | | | | | | | |
| Brak GTIN w feedzie | | | | | | | |
| Niezoptymalizowane tytuły produktów | | | | | | | |
| Wysoki udział produktów "Psy" BCG (>70%) | | | | | | | |

### Błędy systemowe (u >50% klientów) `[KRÓTKI]`

> Błędy powtarzające się u większości klientów wskazują na wspólną przyczynę: ten sam szablon GTM, ten sam dostawca CMP, ta sama procedura wdrożeniowa.

| # | Błąd | Klientów z błędem | Prawdopodobna wspólna przyczyna |
|---|------|------------------|-------------------------------|
| 1 | | N/N (___%) | |
| 2 | | N/N (___%) | |
| 3 | | N/N (___%) | |

**Wniosek:** _______________

### Błędy indywidualne (u pojedynczych klientów)

| Klient | Błąd unikatowy | Priorytet |
|--------|---------------|-----------|
| | | 🔴/🟡 |
| | | |

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE `[KRÓTKI]`

### Wyniki sekcji

| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | | | | |
| 2. ePrivacy / Consent Mode | | | | |
| 3. Konfiguracja | | | | |
| 3K. BigQuery Export _(jeśli dostępny)_ | | | | |
| 4. Data Quality | | | | |
| 5. UTM | | | | |
| 6. Macierz BCG _(tylko e-commerce)_ | | | | |
| 7. Lejki per kampania _(tylko e-commerce)_ | | | | |
| 8. Spójność GA4 ↔ Google Ads _(jeśli połączone)_ | | | | |
| 9. Analiza danych | | | | |
| 10. Google Ads _(jeśli dostęp do konta)_ | | | | |
| **ŁĄCZNIE** | | | | |

### Jakość danych

_Czy danym w GA4 można ufać? W jakim zakresie?_

_______________

### Konfiguracja GA4

_Czy GA4 jest dobrze skonfigurowane? Czy wykorzystujemy pełny potencjał narzędzia?_

_______________

### Infrastruktura (GTM / Server Side)

_Czy infrastruktura śledzenia jest nowoczesna i odporna?_

_______________

### Kluczowe wnioski

1. _______________
2. _______________
3. _______________

---

## CZĘŚĆ II — OMÓWIENIE SZCZEGÓŁOWE

### SEKCJA 1 — Audyt Wstępny

#### 1.1 Adnotacje
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 1.2 Kod HTML — kolejność skryptów
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 1.3 Przegląd wybranych podstron
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 1.4 Google Tag Assistant
**Wynik:** ___
**Komentarz:** _______________

#### 1.5 TagHound
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 1.6 Consent Mode — wstępna weryfikacja
**Wynik:** ___
**Komentarz:** _______________

#### 1.7 Brak starych kodów UA
**Wynik:** ___
**Komentarz:** _______________

#### 1.8 DataLayer — poprawność
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 1.9 DataLayer GA4 — struktura e-commerce
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 1.10–1.20 Integracje wykryte na stronie
**Wykryte narzędzia:** _______________
**Komentarz:** _______________

---

### SEKCJA 2 — ePrivacy / Consent Mode

#### 2.1 Personalizacja wyboru zgód
**Wynik:** ___
**Komentarz:** _______________

#### 2.2 Możliwość odrzucenia wszystkich zgód
**Wynik:** ___
**Komentarz:** _______________

#### 2.3 Strona domyślnie zablokowana
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 2.4 Skuteczne blokowanie cookies
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 2.5 Możliwość zmiany decyzji
**Wynik:** ___
**Komentarz:** _______________

#### 2.6–2.7 Ustawienia domyślne przy pierwszej wizycie
**Wynik:** ___
**Komentarz:** _______________

#### 2.8 Consent update w DataLayer
**Wynik:** ___
**Komentarz:** _______________

#### 2.9 Brak odświeżania po zgodzie
**Wynik:** ___
**Komentarz:** _______________

#### 2.10 Tagi wywołują się po zgodzie
**Wynik:** ___
**Komentarz:** _______________

#### 2.11–2.16 Konfiguracja Consent Mode w GTM
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 2.17 url_passthrough
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

#### 2.18–2.20 Dane wrażliwe
**Wynik:** ___
**Komentarz:** _______________
**Rekomendacja:** _______________

---

### SEKCJA 3 — Konfiguracja

#### 3A — GTM

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| 3.1 Walidacja GTM | | |
| 3.2 Brak błędów w GTM | | |
| 3.3 Consent dla wszystkich tagów | | |
| 3.4 Conversion Linker | | |
| 3.5 Zasięg tagu | | |
| 3.6 Wersje z tytułami | | |
| 3.7 Brak kodów UA | | |
| 3.8 GA4 przez GTM | | |

#### 3A2 — GTM Container Health Score

| Kryterium | Wynik | Ocena (max) |
|-----------|-------|-------------|
| Tagi łącznie (< 50 = OK, 50–100 = ⚠️, > 100 = ❌) | | /2 |
| Konwencja nazewnictwa tagów: [Tool] - [Action] - [Trigger] | | /2 |
| Triggery martwe (tag z triggerem = 0 odpalenia / 30d) | | /2 |
| Zmienne DataLayer (preferowane nad DOM/JS) | | /2 |
| Zmienne nieużywane (> 20% = ❌) | | /1 |
| Wersje kontenerów z opisem (nie "Published") | | /2 |
| Testy Preview Mode — strona główna, PDP, koszyk, checkout | | /3 |
| Brak UA / starych tagów po migracji | | /2 |
| **ŁĄCZNIE** | | **/16** |

**GTM Health Score:** ___/16 — (✅ ≥13 / ⚠️ 8–12 / ❌ <8)

**Tagi wykryte (wg typu):**

| Typ narzędzia | Liczba tagów | Przykłady |
|---------------|-------------|-----------|
| GA4 | | |
| Google Ads | | |
| Meta Pixel / CAPI | | |
| Consent / CMP | | |
| Inne | | |
| **Łącznie** | | |

#### 3B — GTM Server Side
_(pomiń jeśli nie dotyczy)_

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| 3.9 sGTM włączony i aktywny | | |
| Własna domena sGTM (nie googletagmanager.com) | | |
| GA4 Client skonfigurowany po stronie serwera | | |
| Google Ads Conversion Tag po stronie serwera | | |
| Meta CAPI (Conversions API) skonfigurowane | | |
| GCP Cloud Run: status aktywny, bez błędów | | |
| Preview Mode sGTM: testy ręczne wykonane | | |

**First-party cookies — weryfikacja:**

| Cookie | Domena ustawiana przez | Czas życia | Status |
|--------|----------------------|-----------|--------|
| `_ga` | sGTM (1st-party) / gtm.js (3rd-party) | 2 lata | |
| `_ga_XXXXX` (property) | sGTM / gtm.js | 2 lata | |
| `_gcl_aw` (Google Ads) | sGTM / tag.js | 90 dni | |
| `_fbc` / `_fbp` (Meta) | sGTM / pixel.js | 2 lata | |

> ✅ sGTM ustawia cookies z własnej domeny = 1st-party (dłuższe ITP)
> ❌ gtm.js ustawia z googletagmanager.com = 3rd-party (Safari: 7 dni)

**sGTM Score:** ___/10 — (✅ ≥8 / ⚠️ 4–7 / ❌ <4)

---

### SEKCJA 3K — BigQuery Export Audit
_(pomiń jeśli BigQuery nieaktywny)_

#### 3K.1 — Health check (świeżość danych)

| Metryka | Wynik | Ocena |
|---------|-------|-------|
| Ostatni dzień danych | | |
| Opóźnienie eksportu (days_lag) | | |
| Eksport streaming (intraday) | | |

#### 3K.2 — Wolumen i anomalie

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| Anomalie wolumenu (drop > 30%) | | |
| Dni z purchases = 0 przy normalnym ruchu | | |

#### 3K.3–3K.4 — Jakość schematu i items[]

| Pole | % null/(not set) | Ocena |
|------|-----------------|-------|
| `user_pseudo_id` | | |
| `ecommerce.transaction_id` (przy purchase) | | |
| `items[].item_id` | | |
| `items[].item_name` | | |
| `items[].price` | | |
| `items[].quantity` | | |
| `items[].item_category` | | |
| `collected_traffic_source` | | |

#### 3K.5 — Duplikaty transakcji (BQ)

| Metryka | Wynik | Ocena |
|---------|-------|-------|
| % zduplikowanych transaction_id | | |
| Szacowany zawyżony przychód | | |

#### 3K.6–3K.7 — Source/Medium i User-ID

| Metryka | Wynik | Ocena |
|---------|-------|-------|
| % sesji z (not set) source | | |
| User-ID coverage % | | |
| % kupujących z User-ID | | |

#### 3K.8 — Delta BQ vs GA4 UI

| Metryka (30d) | BQ | GA4 UI | Delta % | Ocena |
|--------------|-----|--------|---------|-------|
| Transakcje | | | | |
| Przychód | | | | |

#### 3K.9 — Analiza ścieżek (opcjonalnie)

| Obserwacja | Wynik |
|-----------|-------|
| Mediana sesji przed zakupem | |
| % impulse buyers (1 sesja) | |
| Mediana dni od wizyty do zakupu | |

**Łącznie sekcja 3K:** ___/20

#### 3C–3J — GA4 Konfiguracja

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| 3.21 Alerty i powiadomienia | | |
| 3.24 Uprawnienia konta | | |
| 3.28 Waluta | | |
| 3.30 Google Signals | | |
| 3.31 User-ID | | |
| 3.34 Przechowywanie danych 14M | | |
| 3.36 Filtrowanie ruchu wewnętrznego | | |
| 3.37–3.39 Strumienie danych | | |
| 3.45 Cross-domain tracking | | |
| 3.49 Ignorowanie duplikatów | | |
| 3.53 Wykluczenie bramek płatności | | |
| 3.54 Wykluczenie botów CMP | | |
| 3.55 Czas trwania sesji | | |
| 3.58 Zdarzenia jako konwersje | | |
| 3.64 Model atrybucji | | |
| 3.68–3.71 Integracje obligatoryjne | | |
| 3.77–3.78 Alerty o anomaliach | | |

---

### SEKCJA 4 — Data Quality

#### Przegląd ruchu

| Wymiar | Wynik | % (not set) | Komentarz |
|--------|-------|-------------|-----------|
| Sesje — (not set) | | | |
| Pierwsze źródło — (not set) | | | |
| Bramki płatności w referral | | | |
| Bramki pocztowe w referral | | | |

#### Analiza (not set) — wymiary

| Wymiar | Wynik | % | Komentarz |
|--------|-------|---|-----------|
| source/medium | | | |
| Transakcje | | | |
| Nazwa produktu | | | |
| Kategoria produktu | | | |

#### Transakcje — atrybucja

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| Udział (not set) w transakcjach | | |
| Udział direct w transakcjach | | |
| Łączny not set + direct | | |
| Trend transakcji | | |

#### Transakcje — duplikaty i parametry

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| Duplikaty transaction_id (%) | | |
| `transaction_id` wypełnione (nie null/undefined) | | |
| `value` > 0 przy purchase | | |
| `currency` ustawione | | |
| `tax` i `shipping` obecne | | |

#### Parametry items[] przy purchase

| Pole | Status | % null | Komentarz |
|------|--------|--------|-----------|
| `item_id` | | | |
| `item_name` | | | |
| `price` (number, nie string) | | | |
| `quantity` | | | |
| `item_category` | | | |
| `item_brand` | | | |
| `discount` | | | |

#### Zdarzenia e-commerce — kompletność i parametry

**Ścieżka zakupowa:**

| Zdarzenie | Wdrożone | currency OK | value > 0 | items[] OK | Komentarz |
|-----------|----------|------------|-----------|-----------|-----------|
| `view_item_list` | | — | — | ☐ | |
| `select_item` | | — | — | ☐ | |
| `view_item` | | ☐ | ☐ | ☐ | |
| `add_to_cart` | | ☐ | ☐ | ☐ | |
| `remove_from_cart` | | ☐ | ☐ | ☐ | |
| `view_cart` | | ☐ | ☐ | ☐ | |
| `begin_checkout` | | ☐ | ☐ | ☐ | |
| `add_shipping_info` | | ☐ | ☐ | ☐ | |
| `add_payment_info` | | ☐ | ☐ | ☐ | |
| `purchase` | | ☐ | ☐ | ☐ | |
| `refund` | | ☐ | ☐ | opcjonalne | |
| `view_promotion` | | — | — | ☐ | |
| `select_promotion` | | — | — | ☐ | |

**Brakujące zdarzenia:** _______________
**Zdarzenia z błędnymi parametrami:** _______________
**Lejek wygląda naturalnie (każdy krok ↓):** ___
**AOV spójne dla różnych źródeł:** ___

---

### SEKCJA 5 — UTM

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| Standaryzacja UTM | | |
| Google Ads — UTM source/medium | | |
| Google Ads — UTM kampanii | | |
| Facebook Ads — UTM | | |
| Organiczne social | | |
| Email marketing | | |
| Wizytówka Google | | |

---

### SEKCJA 6 — Macierz BCG: Analiza produktów i segmentów

> _(Tylko dla e-commerce z kampaniami Shopping lub PMax z feedem produktowym ORAZ dostępem do GA4)_

#### Dane wejściowe

| Parametr | Wartość |
|----------|---------|
| Liczba produktów w feedzie | |
| Liczba produktów z konwersjami (30d) | |
| Źródło danych BCG | ☐ Google Ads (shopping_performance) ☐ GA4 (itemId) |

#### Klasyfikacja BCG — podział produktów

| Segment | Produkty | % portfela | Przychód Ads | % przychodu |
|---------|----------|------------|--------------|-------------|
| ⭐ Gwiazdy (Stars) | | | | |
| 🐄 Dojne Krowy (Cash Cows) | | | | |
| ❓ Znaki Zapytania (Question Marks) | | | | |
| 🐕 Psy (Dogs) | | | | |
| ⚫ Nieaktywne | | | | |

_Kryterium podziału: X = udział w przychodzie vs mediana konta, Y = ROAS produktu vs mediana ROAS konta_

#### GA4 per segment BCG (wszystkie kanały, 30d)

| Segment | Odsłony | Dodania do koszyka | Zakupy | Purchase Rate | Cart Rate | Przychód GA4 |
|---------|---------|-------------------|--------|---------------|-----------|--------------|
| ⭐ Gwiazdy | | | | | | |
| 🐄 Dojne Krowy | | | | | | |
| ❓ Znaki Zapytania | | | | | | |
| 🐕 Psy | | | | | | |

#### Spójność Ads vs GA4 (CPC, 30d)

| Segment | Przychód Ads | Przychód GA4/cpc | Delta % | Ocena |
|---------|-------------|------------------|---------|-------|
| ⭐ Gwiazdy | | | | |
| 🐄 Dojne Krowy | | | | |
| ❓ Znaki Zapytania | | | | |
| 🐕 Psy | | | | |
| **Łącznie** | | | | |

_Delta ≤15% ✅ | 15–30% ⚠️ | >30% 🔴_

#### Ocena struktury kampanii vs BCG

| Pytanie | Odpowiedź | Wynik |
|---------|-----------|-------|
| Gwiazdy mają wydzielone kampanie lub osobne asset groups? | | /3 |
| Dojne Krowy mają ograniczony ROAS lub CPC cap? | | /2 |
| Psy są wykluczone lub ograniczone budżetowo? | | /2 |
| Znaki Zapytania mają dedykowany test lub wydzieloną grupę? | | /2 |

**Łącznie sekcja 6:** ___/9

#### Psy organiczne (Dog w Ads, ale sprzedają się z innych kanałów)

| Produkt | Przychód GA4 (all) | Przychód GA4 (cpc) | Wniosek |
|---------|--------------------|--------------------|---------|
| | | | |

#### Kluczowe wnioski

- _______________
- _______________

---

### SEKCJA 7 — Lejki zachowań użytkowników per typ kampanii

> _(Tylko dla e-commerce. Wymaga GA4 z wdrożonymi zdarzeniami e-commerce: view_item, add_to_cart, begin_checkout, purchase)_

#### Dostępność zdarzeń lejka

| Zdarzenie | Wdrożone | Uwagi |
|-----------|----------|-------|
| view_item | ☐ | |
| add_to_cart | ☐ | |
| begin_checkout | ☐ | |
| purchase | ☐ | |

#### Lejek per typ kampanii (30d)

| Kanał / Typ | view_item | → koszyk % | → checkout % | → zakup % | CR całkowity | Przychód |
|-------------|-----------|------------|--------------|-----------|--------------|----------|
| Paid Search (CPC) | | | | | | |
| Shopping | | | | | | |
| Performance Max | | | | | | |
| Display | | | | | | |
| Demand Gen | | | | | | |
| Organic Search | | | | | | |
| Direct | | | | | | |

_% = przejście do kolejnego kroku lejka_

#### Analiza odpadów — najsłabsze przejście per kanał

| Kanał | Najsłabsze przejście | Wartość % | Benchmark | Ocena |
|-------|---------------------|-----------|-----------|-------|
| Paid Search | | | view→koszyk 5–15% | |
| Shopping | | | view→koszyk 8–20% | |
| Performance Max | | | view→koszyk 6–18% | |
| Display | | | view→koszyk 1–5% | |
| Demand Gen | | | view→koszyk 2–8% | |

#### Porównanie jakości ruchu Paid vs Organic

| Metryka | Paid (CPC) | Organic | Stosunek Paid/Org |
|---------|-----------|---------|-------------------|
| CR (view→purchase) | | | |
| AOV | | | |
| Cart Rate | | | |

#### Ocena lejków

| Pytanie | Wynik |
|---------|-------|
| Wszystkie 4 zdarzenia e-commerce wdrożone poprawnie | /2 |
| CR paid ≥ 50% CR organic (ruch płatny konwertuje sensownie) | /2 |
| Brak kanału z CR < 0,1% przy wydatkach > 1000 PLN | /2 |
| Checkout drop-off ≤ 40% (begin_checkout → purchase ≥ 60%) | /2 |

**Łącznie sekcja 7:** ___/8

#### Wnioski

- _______________
- _______________

---

### SEKCJA 8 — Spójność GA4 ↔ Google Ads + Enhanced Conversions
_(pomiń jeśli brak połączenia GA4↔Ads)_

#### 8.1 — Status połączenia

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| Połączenie GA4↔Ads aktywne (weryfikacja przez API) | | |
| Reklamy spersonalizowane włączone | | |
| Konwersje GA4 widoczne w Google Ads | | |

#### 8.2 — Delta przychodów GA4 vs Google Ads (30d)

| Metryka | GA4 (CPC/Cross-network) | Google Ads | Delta % | Ocena |
|---------|------------------------|------------|---------|-------|
| Transakcje | | | | |
| Przychód | | | | |
| ROAS | | | | |

#### 8.3 — Konwersje importowane z GA4

| Konwersja | Źródło | Kategoria | Wartość (stała/dynamiczna) | Błędy | Status |
|-----------|--------|-----------|--------------------------|-------|--------|
| | | | | | |
| | | | | | |

#### 8.4 — Smart bidding

| Punkt | Wynik |
|-------|-------|
| Konwersje wartościowe (nie 1 zł) dla kampanii ROAS | |
| Purchase jako konwersja Primary | |
| Brak duplikatów (tag Ads + import GA4) | |
| Enhanced Conversions włączone | |

#### 8.5 — Enhanced Conversions — jakość matchingu

| # | Punkt | Status | Wynik | Komentarz |
|---|-------|--------|-------|-----------|
| 8.5.1 | Enhanced Conversions włączone w Google Ads | | | |
| 8.5.2 | EC skonfigurowane w GTM (pola: email, phone) | | | |
| 8.5.3 | Match rate > 40% | | | |
| 8.5.4 | Dane hashowane SHA-256 | | | |
| 8.5.5 | EC obejmuje konwersję purchase (primary) | | | |

#### 8.6 — Audience Lists — eksport do Google Ads

| Lista odbiorców | Okno | Rozmiar (Ads) | Używana w Ads? | Ocena |
|-----------------|------|--------------|---------------|-------|
| Wszyscy użytkownicy (All Users) | 30d | | | |
| Porzucający koszyk (add_to_cart bez purchase) | 30d | | | |
| Oglądający produkt bez zakupu | 14d | | | |
| Kupujący — powracający (purchase 180d) | 180d | | | |
| Niestandardowe segmenty | — | | | |

#### 8.7 — Conversion Value Rules

| Pytanie | Wynik |
|---------|-------|
| Skonfigurowane reguły wartości konwersji? | |
| Nowi klienci (new customer) z wyższym mnożnikiem? | |
| Reguła geograficzna (jeśli dotyczy)? | |
| Reguła urządzenie skonfigurowana? | |

#### 8.8 — Audience Audit — pełna weryfikacja list odbiorców

| Lista odbiorców | Źródło | Rozmiar (GA4) | Rozmiar (Ads) | Używana w kampaniach | Match rate | Ocena |
|-----------------|--------|--------------|--------------|---------------------|------------|-------|
| Wszyscy odwiedzający (30d) | GA4 | | | | — | |
| Porzucający koszyk | GA4 | | | | — | |
| Oglądający produkt bez zakupu | GA4 | | | | — | |
| Kupujący (30d) — up/cross sell | GA4 | | | | — | |
| Kupujący (180d) — retention | GA4 | | | | — | |
| Odwiedzający checkout bez zakupu | GA4 | | | | — | |
| Strona kategorii X (segment) | GA4 | | | | — | |
| Customer Match — baza CRM | CRM → Ads | — | | | % | |
| Customer Match — buyers only | CRM → Ads | — | | | % | |
| Lookalike / Similar Audiences | Ads | — | | | — | |

**Minima operacyjne:**
- Remarketing Display: min. 100 użytkowników _(< 100 = ❌ lista nieaktywna)_
- RLSA (Search): min. 1 000 użytkowników _(< 1000 = ❌)_
- Customer Match: min. 1 000 dopasowanych _(< 1000 = ❌)_
- Match rate CM: > 30% _(< 20% = ❌ niska jakość listy emaili)_

**Szacowany wpływ finansowy Customer Match:**

| Parametr | Wartość |
|----------|---------|
| Rozmiar bazy (emaili) | |
| Match rate % | |
| Dopasowanych użytkowników | |
| Szacowana aktywność zakupowa (5%) | |
| AOV (PLN) | |
| Potencjalny przychód remarketing CM/msc | |

#### 8.9 — Model atrybucji — porównanie (30 dni)

| Model | Sesje CPC | Transakcje | Przychód (PLN) | ROAS | Delta vs Last Click |
|-------|-----------|-----------|----------------|------|---------------------|
| Last Click | | | | x | baseline |
| Data-Driven (DDA) | | | | x | ___% |
| Linear | | | | x | ___% |
| Time Decay | | | | x | ___% |
| First Click | | | | x | ___% |

**Kanały „przegrane" przez Last Click (assist > last):** ___
**Rekomendowany model:** ___
**Uzasadnienie:** ___

**Łącznie sekcja 8:** ___/12 + ___/8 (audience) = ___/20

---

### SEKCJA 9 — Analiza danych

> _(Tylko gdy masz dostęp do GA4 API. Wypełniaj na podstawie danych z ostatnich 30 i 90 dni.)_

#### 9.1 — Efektywność kanałów (90 dni)

| Kanał | Sesje | CVR | Przychód (PLN) | Rev/sesja | Engagement rate | Ocena |
|-------|-------|-----|----------------|-----------|-----------------|-------|
| Organic Search | | | | | | |
| Paid Search | | | | | | |
| Cross-network (PMax) | | | | | | |
| Paid Social | | | | | | |
| Email | | | | | | |
| Display | | | | | | |
| Direct | | | | | | |
| SMS | | | | | | |
| Referral | | | | | | |

**CVR paid / CVR organic:** ___ (benchmark ≥ 50%)
**Najlepszy kanał wg Rev/sesja:** ___
**Najgorszy kanał płatny wg CVR:** ___

#### 9.2 — Analiza urządzeń

| Urządzenie | Sesje | % | CVR | Przychód | Rev/sesja | Engagement |
|------------|-------|---|-----|----------|-----------|------------|
| Mobile | | | | | | |
| Desktop | | | | | | |
| Tablet | | | | | | |

**Mobile/Desktop CVR ratio:** ___ (sygnał alarmu jeśli < 50%)
**Szacunkowy potencjał przychodowy przy wyrównaniu CVR do 80% desktop:** ___ PLN

#### 9.3 — Trend ruchu i zaangażowania (ostatnie 90 dni)

| Miesiąc / Okres | Sesje/dzień (śr.) | Eng. rate | Avg Session Duration | Trend |
|-----------------|-------------------|-----------|----------------------|-------|
| | | | | |
| | | | | |
| | | | | |

**Anomalie / szczyty ruchu (daty i możliwe przyczyny):** ___
**Trend jakości ruchu (↑ / ↓ / stabilny):** ___

#### 9.4 — Wartość zamówienia i struktura sprzedaży (90 dni)

| Metryka | Wartość |
|---------|---------|
| Transakcje łącznie | |
| Przychód łącznie (PLN) | |
| AOV — średnia wartość zamówienia | |
| Najwyższy dzienny przychód (data + PLN) | |
| Najniższy dzienny przychód (data + PLN) | |
| % przychodu z top 3 kanałów | |

#### 9.5 — Lejek porzuceń (behawioralny)

| Etap | Zdarzenia | Konwersja do nast. | Komentarz |
|------|-----------|--------------------|-----------|
| view_item | | — | |
| add_to_cart | | % view→cart | |
| begin_checkout | | % cart→checkout | |
| purchase | | % checkout→purchase | |

**Porzucenie koszyka (add_to_cart → purchase):** ___%
**Kluczowy punkt odpadania:** ___

#### 9.6 — Sygnały omnichannel i lojalność

| Zdarzenie / Wskaźnik | Liczba (90d) | Komentarz |
|----------------------|--------------|-----------|
| Eventy wskazujące interes offline (np. "znajdź w salonie") | | |
| Dołączenia do programu lojalnościowego | | |
| Alerty cenowe / mail alert clicks | | |
| Login events | | |
| Add to wishlist | | |

**Wnioski omnichannel:** ___

#### 9.7 — Analiza geograficzna

| Kraj | Sesje | % | Transakcje | CVR | Przychód | Ocena |
|------|-------|---|------------|-----|----------|-------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

**Rynek główny:** ___ (___% przychodu)
**Podejrzany ruch (kraj z 0 transakcji, duży wolumen):** ___

#### 9.8 — Ukryte możliwości i quick wins

| Obserwacja | Dane | Rekomendacja |
|-----------|------|--------------|
| Kanały organiczne z wysokim CVR bez wsparcia płatnego | | |
| Referral z wysokim CVR | | |
| Bramki płatności / webmaile w referral (do wykluczenia) | | |
| Kanały płatne z CVR < 30% organic | | |
| Inne | | |

#### 9.9 — Retencja i LTV per kanał

| Kanał | Sesje | Użytkownicy | Zakupy | Zakupy/użytk. | Revenue/użytk. | % powracających | Ocena LTV |
|-------|-------|------------|--------|--------------|---------------|----------------|-----------|
| Organic Search | | | | | | | |
| Email | | | | | | | |
| Paid Search | | | | | | | |
| Cross-network (PMax) | | | | | | |
| Direct | | | | | | |
| Paid Social | | | | | | |

**Kanał z najwyższym LTV (zakupy/użytk.):** ___
**Kanał z najniższym LTV (jednorazowi):** ___

#### 9.10 — Wyszukiwania wewnętrzne
_(pomiń jeśli event `search` nie jest wdrożony)_

| Top fraza | Liczba wyszukiwań (90d) | CVR | Przychód | Insight |
|-----------|------------------------|-----|---------|---------|
| | | | | |
| | | | | |
| | | | | |

**Frazy z wysoką liczbą i CVR = 0% (brakujący produkt):** ___
**Frazy z CVR > 2% (materiał na słowa kluczowe Search):** ___

#### 9.11 — Analiza kohortowa: powracający kupujący

| Segment | Transakcje | % łącznych | Revenue | Avg CVR | Komentarz |
|---------|-----------|------------|---------|---------|-----------|
| Nowi klienci (first purchase) | | | | | |
| Powracający (repeat purchase) | | | | | |

**% transakcji od powracających:** ___ (benchmark: > 20%)
**Kanał z najwyższą retencją powracających:** ___
**Wnioski dot. CRM / email retencji:** ___

#### 9.12 — Ścieżki konwersji wielodotykowe

| Kanał | Rola wspomagająca (assisted conv.) | Rola domykająca (last-click) | Stosunek assist./last-click | Interpretacja |
|-------|-----------------------------------|-----------------------------|-----------------------------|---------------|
| Organic Search | | | | |
| Paid Search | | | | |
| Cross-network | | | | |
| Email | | | | |
| Paid Social | | | | |
| Direct | | | | |

**Kanały niedocenione przez last-click (assist > last-click):** ___
**Wnioski dot. atrybucji:** ___

#### 9.13 — ROAS per kategoria produktu (itemCategory × shopping_performance)
_(tylko e-commerce z Shopping/PMax i feedem Merchant Center)_

| Kategoria | Wydatki (PLN) | Przychód (PLN) | ROAS | % budżetu | % przychodu | BCG Kwadrant | Działanie |
|-----------|--------------|----------------|------|-----------|-------------|-------------|-----------|
| | | | x | | | ⭐/🐄/❓/🐕 | |
| | | | x | | | | |
| | | | x | | | | |
| | | | x | | | | |
| **ŁĄCZNIE** | | | x | 100% | 100% | | |

**Kategorie niedoinwestowane (wysoki ROAS, niski % budżetu):** ___
**Kategorie do ograniczenia (ROAS < 1x, wysoki % budżetu):** ___
**Potencjał realokacji:** ___ PLN/msc (z Psów na Znaki Zapytania)

#### 9.14 — Upper Funnel — Display / Demand Gen / YouTube
_(pomiń jeśli brak kampanii Display/DG/Video)_

| Kampania | Typ | Wydatki (PLN) | VCR (%) | CTR (%) | Assisted conv. | Brand Search Lift | Ocena |
|----------|-----|--------------|---------|---------|----------------|------------------|-------|
| | Display | | — | | | — | |
| | Demand Gen | | — | | | — | |
| | YouTube | | | | | | |

**Uwaga:** Upper Funnel NIE ocenia się przez ROAS last-click — używaj Assisted Conversions i Brand Search Lift jako KPI.
**VCR benchmark YouTube:** > 25% (unskippable), > 15% (skippable)
**Assisted/Last-click ratio:** > 1.5x = kanał wspierający, warto utrzymać

**Łącznie sekcja 9:** ___/26 + ___/10 (kategorie + upper funnel) = ___/36

---

### SEKCJA 10 — Audyt Google Ads

> _(Pomiń jeśli klient nie ma konta Google Ads lub brak dostępu API. Wymaga BDOS connect do konta.)_

---

#### 10.0 — KPI konta (30 dni) — metryki zbiorcze

| Metryka | Wartość (30d) | Poprzednie 30d | Trend | Ocena |
|---------|---------------|----------------|-------|-------|
| Wydatki łączne (PLN) | | | ↑/→/↓ | |
| Kliknięcia | | | | |
| Wyświetlenia | | | | |
| CTR (%) | | | | |
| Avg CPC (PLN) | | | | |
| Konwersje łączne | | | | |
| Wartość konwersji (PLN) | | | | |
| ROAS (%) | | | | |
| CPA (PLN) | | | | |
| Avg Quality Score | | | | |
| Kampanie aktywne | | | | |
| Kampanie bez konwersji | | | | |

**Ocena ogólna:** ✅ Dobry (ROAS > 300%) / ⚠️ Do optymalizacji (150–300%) / ❌ Krytyczny (< 150%)

#### 10.0B — Szczegółowy przegląd per kampania (wszystkie aktywne, 30d)

| Kampania | Typ | Wydatki | Kliknięcia | Konw. | Wart. konw. | ROAS% | Budżet/d | Strategia | Ocena |
|----------|-----|---------|-----------|-------|------------|-------|---------|-----------|-------|
| | PMax | | | | | | | | |
| | PMax | | | | | | | | |
| | Search | | | | | | | | |
| | Shopping | | | | | | | | |
| | Display | | | | | | | | |
| | DemGen | | | | | | | | |
| | Video | | | | | | | | |
| **ŁĄCZNIE** | | | | | | | | | |

**Kampanie bez konwersji (> 300 PLN / 30d, konwersje = 0):**

| Kampania | Typ | Wydatki 30d | Szacowany drenaż/msc | Diagnoza |
|----------|-----|-------------|---------------------|---------|
| | | | | |
| **ŁĄCZNIE drenażu** | | PLN | | |

---

#### 10A — Struktura konta i kampanii

**Typy kampanii i podział budżetu (30d):**

| Typ kampanii | Liczba | Aktywne | Wydatki 30d (PLN) | % budżetu |
|--------------|--------|---------|-------------------|-----------|
| Performance Max | | | | |
| Search | | | | |
| Shopping standard | | | | |
| Display | | | | |
| Demand Gen | | | | |
| Video | | | | |
| **Łącznie** | | | | |

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.1 Żadna aktywna kampania nie ma 0 konwersji przez >30 dni przy wydatkach > 500 PLN | Wysoki | | |
| 10.2 Brand i non-brand wydzielone w osobne kampanie | Wysoki | | |
| 10.3 Brak kampanii wstrzymanych z historycznie dobrymi wynikami bez uzasadnienia | Średni | | |
| 10.4 Naming convention kampanii — spójna i czytelna | Niski | | |
| 10.5 Automatic recommendations (auto-apply) wyłączone | Wysoki | | |

**Łącznie 10A:** ___/12

---

#### 10B — Konwersje i śledzenie

**Lista konwersji skonfigurowanych na koncie:**

| Nazwa konwersji | Kategoria | Źródło (tag/GA4) | Wartość | Primary / Secondary | Counting | Status |
|-----------------|-----------|------------------|---------|---------------------|----------|--------|
| | | | | | | |
| | | | | | | |
| | | | | | | |

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.6 Konwersja Primary ustawiona (purchase dla e-com / lead dla lead gen) | Wysoki | | |
| 10.7 Wartości konwersji dynamiczne, nie stała kwota (1 PLN = błąd) | Wysoki | | |
| 10.8 Brak duplikacji śledzenia: tag Google Ads i import GA4 jednocześnie dla tej samej akcji | Wysoki | | |
| 10.9 Enhanced Conversions włączone i dane hashe przekazywane | Średni | | |
| 10.10 Conversion window: e-com 30d klik / 1d view, lead gen 60–90d klik | Średni | | |
| 10.11 Model atrybucji: Data-Driven lub Last Click (nie First Click / Linear / Time Decay) | Średni | | |
| 10.12 Konwersja Secondary nie jest używana jako cel biddingowy | Średni | | |

**Łącznie 10B:** ___/19

---

#### 10C — Strategie bidding

**Strategie na koncie:**

| Kampania | Strategia | Target (ROAS / CPA) | Osiągany ROAS (30d) | Status | Komentarz |
|----------|-----------|---------------------|---------------------|--------|-----------|
| | | | | | |
| | | | | | |

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.13 Target ROAS / CPA ustawiony (nie "Maximize" bez celu) | Wysoki | | |
| 10.14 Target ROAS ≤ 1.5× osiągalnego ROAS z ostatnich 30d (nie zbyt ambitny) | Wysoki | | |
| 10.15 Brak kampanii w Learning period >14 dni bez wyraźnego powodu | Średni | | |
| 10.16 Brak zmian budżetu >30% w jednym kroku (destabilizacja Smart Bidding) | Wysoki | | |
| 10.17 Brak kampanii z Maximize Clicks bez CPC max cap | Średni | | |
| 10.18 Portfolio bidding strategy użyta gdy wiele kampanii z tym samym celem | Niski | | |

**Łącznie 10C:** ___/16

---

#### 10D — Kampanie Performance Max

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.19 Typ PMax rozpoznany: Feed-Only / Full / Mixed / No-Feed | Wysoki | | |
| 10.20 Asset groups segmentowane wg kategorii lub marki (nie jedna "Wszystkie produkty") | Wysoki | | |
| 10.21 Gwiazdy BCG i Dojne Krowy w osobnych asset groups z wyższym target ROAS | Wysoki | | |
| 10.22 Psy BCG wykluczone z PMax lub izolowane w osobnej nisko-budżetowej kampanii | Wysoki | | |
| 10.23 Listing group filters na poziomie product_type lub item_id (nie flat All Products) | Wysoki | | |
| 10.24 Negative keywords na kampanię PMax (ochrona brandu, SEO overlap) | Wysoki | | |
| 10.25 Brand exclusion w ustawieniach kampanii lub brand terms w listach wykluczeń | Wysoki | | |
| 10.26 PMax nie kanibaluje kampanii Search (Impression Share brand zbadane) | Wysoki | | |
| 10.27 URL expansion: wyłączone lub zawężone do konkretnych kategorii URL | Średni | | |
| 10.28 Assety tekstowe: 15 nagłówków, 4+ opisy, >3 warianty grafik | Średni | | |
| 10.29 Video asset: własne video lub auto-generated z wyłączonym jeśli słabej jakości | Niski | | |

**Asset groups — lista:**

| Asset Group | Kampania | Typ | Target ROAS | Wydatki 30d | Segment produktów | Opis listing group |
|-------------|----------|-----|-------------|-------------|-------------------|-------------------|
| | | | | | | |
| | | | | | | |

**Łącznie 10D:** ___/30

---

#### 10E — Kampanie Search

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.30 Kampania brandowa wydzielona z własnym budżetem i bid strategy | Wysoki | | |
| 10.31 Impression Share brand Search ≥ 70% | Wysoki | | |
| 10.32 Match type: Exact + Phrase dominują; broad match tylko z kontekstem i zgodą | Wysoki | | |
| 10.33 Jakość reklam RSA: Ad Strength Good lub Excellent (min 70% reklam) | Średni | | |
| 10.34 Pinned assets: nagłówek 1 lub 2 pinned (marka / kluczowe USP) | Niski | | |
| 10.35 Negative keywords na kampanię i na poziomie konta (shared lists) | Wysoki | | |
| 10.36 Search Terms raport — negatywy dodawane regularnie (brak irrelewantnych fraz) | Wysoki | | |
| 10.37 Zduplikowane keywords między kampaniami (kanibalizacja) — brak lub świadome | Średni | | |
| 10.38 AI Max for Search — jeśli włączony: URL expansion i keyword expansion zbadane | Średni | | |
| 10.39 Kampania generyczna non-brand wydzielona od brand | Sredni | | |

**Reklamy RSA — jakość (top kampanie Search):**

| Kampania | Ad Group | Ad Strength | Pinnione nagłówki | Wynik |
|----------|----------|-------------|-------------------|-------|
| | | | | |
| | | | | |

**Łącznie 10E:** ___/26

---

#### 10F — Targeting geo i harmonogram

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.40 Geo targeting ustawione na wszystkich kampaniach (brak "Wszystkie kraje i terytoria") | Wysoki | | |
| 10.41 Targeting method: PRESENCE (fizyczna obecność) — nie PRESENCE_OR_INTEREST (zainteresowanie) | Wysoki | | |
| 10.42 Targetowane lokalizacje odpowiadają obszarowi dostawy lub działalności | Średni | | |
| 10.43 Wykluczenia mobile app categories (kampanie Display / PMax z Display) | Średni | | |
| 10.44 Harmonogram reklam dopasowany do godzin konwersji, jeśli analiza potwierdza zasadność | Niski | | |
| 10.45 Device bid adjustments lub obserwacje — brak niedopasowania mobile/desktop | Średni | | |

**Łącznie 10F:** ___/14

---

#### 10G — Feed produktowy i Merchant Center

_(pomiń jeśli brak kampanii Shopping / PMax)_

**Stan feedu w Merchant Center:**

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| Produkty łącznie w feedzie | | |
| Eligible (Active) | | |
| Disapproved | | |
| Pending (oczekuje na review) | | |
| In Stock | | |
| Out of Stock | | |

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.46 Produkty Eligible > 90% feedu | Wysoki | | |
| 10.47 Produkty Disapproved < 5% feedu | Wysoki | | |
| 10.48 Tytuły: keyword + marka + kolor/rozmiar/model — nie "Produkt 123" | Średni | | |
| 10.49 Custom labels (0–4): wypełnione (sezon / marża / BCG / bestseller) | Średni | | |
| 10.50 item_id spójny między MC ↔ GA4 ↔ arkuszem zamówień | Wysoki | | |
| 10.51 Supplemental feed do nadpisywania tytułów (jeśli tytuły systemowe słabe) | Niski | | |
| 10.52 Free Listings włączone i aktywne | Niski | | |
| 10.53 Price Insights / Competitive Visibility sprawdzone | Niski | | |

**Łącznie 10G:** ___/20

---

#### 10H — Diagnostyka kampanii i jakość konta

| Punkt | Priorytet | Wynik | Komentarz |
|-------|-----------|-------|-----------|
| 10.54 Impression Share (IS) kampanii niebrandowych ≥ 30% (nie ograniczone budżetem) | Wysoki | | |
| 10.55 Kampanie z IS Lost (Budget) > 30% — budżet za niski | Średni | | |
| 10.56 Kampanie z IS Lost (Rank) > 50% — bid za niski lub jakość reklamy | Średni | | |
| 10.57 Brak kampanii z ROAS < 1× (traci więcej niż zarabia) bez planu naprawy | Wysoki | | |
| 10.58 Konto nie ma >15 kampanii w Learning period jednocześnie | Średni | | |
| 10.59 Serving status kampanii zbadany (SERVING / SUSPENDED / PENDING) | Średni | | |
| 10.60 Etykiety datowane (np. BDOS:22.04) na kampaniach po optymalizacjach | Niski | | |

**Kampanie problematyczne — lista:**

| Kampania | Problem | ROAS (30d) | IS | Wydatki | Rekomendacja |
|----------|---------|------------|-----|---------|--------------|
| | | | | | |
| | | | | | |

**Łącznie 10H:** ___/18

---

#### 10I — Quality Score — rozkład (Search)

| Zakres QS | Liczba słów kluczowych | % całości | Szacowany nadkoszt CPC |
|-----------|----------------------|-----------|----------------------|
| QS 9–10 | | | oszczędność |
| QS 7–8 | | | bazowy |
| QS 5–6 | | | +20–40% |
| QS 3–4 | | | +50–80% |
| QS 1–2 | | | +100–200% |

**Kampanie z Avg QS < 5:**

| Kampania | Avg QS | Najsłabszy komponent | Akcja naprawcza |
|----------|--------|---------------------|-----------------|
| | | | |

---

#### 10J — Search Terms — kategorie zapytań (Search + PMax)

| Kategoria | Unikalne zapytania | % wydatków | Konwersje | Rekomendacja |
|-----------|------------------|-----------|-----------|--------------|
| Branded (własna marka) | | | | Wyodrębnij do brand |
| Competitor (marka konkurencji) | | | | Decyzja: tak/nie |
| Informacyjne (brak intencji) | | | | Wyklucz |
| Produktowe (wysoka intencja) | | | | Dodaj Exact match |
| Kategoriowe | | | | Monitoruj CVR |
| Spam / brak sensu | | | | Wyklucz |

**Top 5 fraz do natychmiastowego wykluczenia:** ___

---

#### 10K — Customer Match i Audience Lists

| Lista | Rozmiar | Match rate | Używana w PMax | Używana w RLSA | Ocena |
|-------|---------|------------|---------------|---------------|-------|
| Customer Match (baza CRM) | | | | | |
| Porzucający koszyk (GA4) | | | | | |
| Oglądający produkt (GA4) | | | | | |
| Kupujący 30d (GA4) | | | | | |
| Kupujący 180d (GA4) | | | | | |

---

#### 10L — Ocena specjalisty prowadzącego konto

| Obszar | Ocena /5 | Komentarz |
|--------|---------|-----------|
| Trend ROAS (ostatnie 3 miesiące) | | ↑ / → / ↓ |
| Struktura kampanii (nazewnictwo, segmentacja) | | |
| Aktywność optymalizacyjna (ostatnie 30 dni) | | |
| Jakość wykluczeń i negatywów | | |
| Użycie zaawansowanych funkcji (EC, CM, CL, IS) | | |
| Reakcja na kampanie bez konwersji | | |

**Łączna ocena specjalisty:** ⭐⭐⭐⭐⭐ (___/5)
**Narracja:** _______________

---

#### 10M — Performance Max — Zaawansowany audyt
_(pomiń jeśli brak kampanii PMax)_

**Asset Groups — jakość:**

| Asset Group | Ad Strength | Nagłówki | Obrazy | Wideo | Konwersje | Koszt | Działanie |
|-------------|------------|----------|--------|-------|-----------|-------|-----------|
| AG 1 — | Doskonała/Dobra/Słaba | /15 | / | tak/nie | | | |
| AG 2 — | | /15 | / | | | | |

**Listing Groups — segmentacja:**

| Asset Group | Segmentacja | Custom Label BCG | Psy wykluczone | Ocena |
|-------------|------------|-----------------|---------------|-------|
| AG 1 | Brak / Kategoria / Marka / Label | tak/nie | tak/nie | |
| AG 2 | | | | |

**Audience Signals:**

| Typ sygnału | Skonfigurowany | Szczegóły | Ocena |
|-------------|---------------|-----------|-------|
| Customer Match | tak/nie | rozmiar: ___ | |
| Niestandardowe segmenty (słowa kluczowe) | tak/nie | | |
| Remarketing GA4 | tak/nie | | |
| In-market audiences | tak/nie | | |

**Kanibalizacja PMax:**

| Sprawdzenie | Wynik | Działanie |
|-------------|-------|-----------|
| PMax przechwytuje branded queries? | tak/nie | |
| Brand exclusions skonfigurowane? | tak/nie | |
| Oddzielna kampania Search Brand? | tak/nie | |
| Impression Share kampanii branded ↓ po wdrożeniu PMax? | tak/nie | |

**Search Themes:**

| Punkt | Wynik | Ocena |
|-------|-------|-------|
| Search Themes skonfigurowane (min. 5 per AG) | | |
| Pokrywają główne intencje zakupowe | | |
| Nie nakładają się na branded queries | | |

**URL Expansion:** włączone / wyłączone / z wykluczeniami: ___
**Najczęściej wybierane URL przez Google:** ___

**PMax — Performance per Asset Group:**

| Asset Group | Wydatki | Konwersje | Wartość | ROAS | Status | Działanie |
|-------------|---------|-----------|---------|------|--------|-----------|
| AG 1 | | | | x | Learning/Active | |
| AG 2 | | | | x | | |

**PMax Zaawansowany Score:** ___/19

---

**Łącznie SEKCJA 10 — Google Ads (1 konto):** ___/54 (+ ___/19 PMax)

**Wynik sekcji punktowanych:** ___% — _(✅ ≥80% / ⚠️ 50–79% / ❌ <50%)_

#### Kluczowe wnioski Google Ads

- _______________
- _______________
- _______________

---

## ROZDZIAŁY PER KLIENT _(tryb multi-konto)_

> Pomiń całą tę sekcję jeśli audytujesz tylko 1 konto — powyższe sekcje 1–10 już pokrywają jedynego klienta.
>
> **Zasada:** Każdy klient = osobny rozdział z PEŁNYM audytem MarTech (Sekcje 1–10).
> Kopiuj cały blok `## KLIENT [N]` tyle razy ile klientów audytujesz.
> Każdy blok jest identyczny strukturą z audytem dla 1 konta — nie skracaj sekcji.

---

# KLIENT 1 — [Nazwa klienta]

**GA4 Property ID:** ___ | **Google Ads ID:** ___ | **URL:** ___
**Typ biznesu:** e-commerce / lead gen / SaaS
**Okres analizy:** _______________

## SEKCJA 1 — Audyt Wstępny _(Klient 1)_

> Wypełnij identycznie jak dla audytu 1 konta. Patrz: instrukcje Sekcja 1.

#### 1.1 Adnotacje
**Wynik:** ___ | **Komentarz:** _______________ | **Rekomendacja:** _______________

#### 1.2 Kolejność skryptów HTML
**Wynik:** ___ | **Komentarz:** _______________ | **Rekomendacja:** _______________

#### 1.3 Przegląd wybranych podstron
**Wynik:** ___ | **Komentarz:** _______________ | **Rekomendacja:** _______________

#### 1.4 Google Tag Assistant
**Wynik:** ___ | **Komentarz:** _______________

#### 1.5 TagHound
**Wynik:** ___ | **Komentarz:** _______________ | **Rekomendacja:** _______________

#### 1.6 Consent Mode — wstępna weryfikacja
**Wynik:** ___ | **Komentarz:** _______________

#### 1.7 Brak starych kodów UA
**Wynik:** ___ | **Komentarz:** _______________

#### 1.8 DataLayer — poprawność
**Wynik:** ___ | **Komentarz:** _______________ | **Rekomendacja:** _______________

#### 1.9 DataLayer GA4 — struktura e-commerce
**Wynik:** ___ | **Komentarz:** _______________ | **Rekomendacja:** _______________

#### 1.10–1.20 Integracje wykryte na stronie
**Wykryte narzędzia:** _______________ | **Komentarz:** _______________

**Łącznie Sekcja 1:** ___/___

---

## SEKCJA 2 — ePrivacy / Consent Mode _(Klient 1)_

#### 2.1 Personalizacja wyboru zgód
**Wynik:** ___ | **Komentarz:** _______________

#### 2.2 Możliwość odrzucenia wszystkich zgód
**Wynik:** ___ | **Komentarz:** _______________

#### 2.3 Strona domyślnie zablokowana
**Wynik:** ___ | **Komentarz:** _______________

#### 2.4 Skuteczne blokowanie cookies
**Wynik:** ___ | **Komentarz:** _______________

#### 2.5 Możliwość zmiany decyzji
**Wynik:** ___ | **Komentarz:** _______________

#### 2.6–2.20 Pozostałe punkty ePrivacy
_(wypełnij wg sekcji 2 z instrukcji)_

**Łącznie Sekcja 2:** ___/___

---

## SEKCJA 3 — Konfiguracja _(Klient 1)_

_(wypełnij wg sekcji 3 z instrukcji — 3A GTM, 3B sGTM, 3C GA4 admin, 3D–3J pozostałe)_

**Łącznie Sekcja 3:** ___/___

---

## SEKCJA 3K — BigQuery Export _(Klient 1, jeśli dostępny)_

_(pomiń jeśli brak eksportu BQ)_

**Łącznie Sekcja 3K:** ___/___ lub ➖ nie dotyczy

---

## SEKCJA 4 — Data Quality _(Klient 1)_

#### 4.1–4.2 Udział (not set)

| Wymiar | (not set) | % sesji | Ocena |
|--------|-----------|---------|-------|
| source / medium | | % | ✅/⚠️/❌ |
| sessionDefaultChannelGroup | | % | ✅/⚠️/❌ |
| itemId | | % | ✅/⚠️/❌ |

#### 4.3–4.6 Jakość ruchu
**Wynik:** ___ | **Komentarz:** _______________

#### 4D — Weryfikacja transakcji

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| ecommercePurchases | | |
| transactions | | |
| Ratio purchase:transaction | | ✅ <1.1 / ⚠️ 1.1–2x / ❌ >2x |
| Duplikaty transaction_id | | |

**Łącznie Sekcja 4:** ___/___

---

## SEKCJA 5 — UTM _(Klient 1)_

| Źródło | Sesje | % bez UTM | Ocena |
|--------|-------|-----------|-------|
| Google Ads | | % | |
| Meta Ads | | % | |
| Email | | % | |
| Inne paid | | % | |

**Łącznie Sekcja 5:** ___/___

---

## SEKCJA 6 — Macierz BCG _(Klient 1, tylko e-commerce)_

_(wypełnij wg sekcji 6 z instrukcji)_

**Łącznie Sekcja 6:** ___/___ lub ➖ nie dotyczy

---

## SEKCJA 7 — Lejki per kampania _(Klient 1, tylko e-commerce)_

| Kanał / kampania | Sesje | Add to cart | Checkout | Purchase | CR sesja→zakup |
|-----------------|-------|------------|---------|---------|----------------|
| | | | | | % |

**Łącznie Sekcja 7:** ___/___ lub ➖ nie dotyczy

---

## SEKCJA 8 — Spójność GA4 ↔ Google Ads _(Klient 1)_

| Punkt | Wynik | Komentarz |
|-------|-------|-----------|
| 8.1 Status połączenia GA4 ↔ Ads | ✅/❌ | |
| 8.2 Delta przychodów GA4 vs Ads | ___% | ✅ <15% / ⚠️ 15–30% / ❌ >30% |
| 8.3 Konwersje importowane z GA4 | ✅/❌ | |
| 8.4 Smart bidding — jakość sygnałów | ✅/⚠️/❌ | |
| 8.5 Enhanced Conversions | ✅/❌ | match rate: % |
| 8.6 Audience Lists eksport | ✅/⚠️/❌ | |
| 8.7 Conversion Value Rules | ✅/➖ | |

**Łącznie Sekcja 8:** ___/___

---

## SEKCJA 9 — Analiza danych _(Klient 1)_

#### 9.1 Efektywność kanałów (90 dni)

| Kanał | Sesje | Transakcje | ROAS | AOV | CR |
|-------|-------|-----------|------|-----|-----|
| Paid Search | | | x | PLN | % |
| Paid Shopping | | | x | PLN | % |
| Organic | | | — | PLN | % |
| Direct | | | — | PLN | % |
| Email | | | — | PLN | % |

#### 9.2 Analiza urządzeń
| Urządzenie | Sesje | Transakcje | CR | AOV |
|-----------|-------|-----------|-----|-----|
| Desktop | | | % | PLN |
| Mobile | | | % | PLN |
| Tablet | | | % | PLN |

#### 9.3–9.12 Pozostałe analizy
_(wypełnij wg sekcji 9 z instrukcji)_

**Łącznie Sekcja 9:** ___/___

---

## SEKCJA 10 — Audyt Google Ads _(Klient 1)_

#### 10.0 — KPI konta (30 dni)

| Metryka | Wartość (30d) | Poprzednie 30d | Trend | Ocena |
|---------|---------------|----------------|-------|-------|
| Wydatki łączne (PLN) | | | ↑/→/↓ | |
| Kliknięcia | | | | |
| Wyświetlenia | | | | |
| CTR (%) | | | | |
| Avg CPC (PLN) | | | | |
| Konwersje łączne | | | | |
| Wartość konwersji (PLN) | | | | |
| ROAS | x | x | | ✅/>3x / ⚠️/2-3x / ❌/<2x |
| CPA (PLN) | | | | |
| Avg Quality Score | | | | ✅/>7 / ⚠️/5-7 / ❌/<5 |
| Kampanie aktywne | | | | |
| Kampanie bez konwersji | | | | |

**Ocena ogólna:** ✅ Dobry (ROAS > 300%) / ⚠️ Do optymalizacji (150–300%) / ❌ Krytyczny (< 150%)

#### 10.0B — Przegląd per kampania

| Kampania | Typ | Wydatki | Kliknięcia | Konw. | Wart. konw. | ROAS% | Budżet/d | Strategia | Ocena |
|----------|-----|---------|-----------|-------|------------|-------|---------|-----------|-------|
| | PMax | | | | | | | | |
| | Search | | | | | | | | |
| **ŁĄCZNIE** | | | | | | | | | |

**Kampanie bez konwersji (drenaż):**

| Kampania | Typ | Wydatki 30d | Diagnoza |
|----------|-----|-------------|---------|
| | | PLN | |

_(wypełnij dalej wg sekcji 10A–10H z instrukcji i szablonu)_

**Łącznie Sekcja 10:** ___/54

---

### Podsumowanie Klienta 1

| Sekcja | Pkt | Max | % | Ocena |
|--------|-----|-----|---|-------|
| 1. Audyt Wstępny | | | | |
| 2. ePrivacy | | | | |
| 3. Konfiguracja | | | | |
| 4. Data Quality | | | | |
| 5. UTM | | | | |
| 6. BCG | | | | |
| 7. Lejki | | | | |
| 8. GA4 ↔ Ads | | | | |
| 9. Analiza danych | | | | |
| 10. Google Ads | | | | |
| **ŁĄCZNIE** | | | **%** | |

**Ocena specjalisty:** ⭐⭐⭐ (___/5) — _______________

**Top 3 priorytety dla tego klienta:**
1. _______________
2. _______________
3. _______________

---

---

# KLIENT 2 — [Nazwa klienta]

**GA4 Property ID:** ___ | **Google Ads ID:** ___ | **URL:** ___
**Typ biznesu:** e-commerce / lead gen / SaaS

_(kopiuj kompletny blok KLIENT 1 powyżej — wszystkie sekcje 1–10 + podsumowanie)_

---

# KLIENT 3 — [Nazwa klienta]

_(kopiuj kompletny blok KLIENT 1 powyżej)_

---

## KONTO 1 — [Nazwa konta]

**ID konta:** ___ | **MCC:** ___ | **GA4 Property:** ___ | **Typ:** e-commerce / lead gen
**Alias BDOS:** ___

#### Wyniki kampanii Google Ads (ostatnie 30 dni)

| Metryka | Wartość |
|---------|--------|
| Wydatki łączne | PLN |
| Kliknięcia | |
| Wyświetlenia | |
| CTR | % |
| Avg. CPC | PLN |
| Konwersje | |
| Wartość konwersji | PLN |
| ROAS | x |
| CPA | PLN |
| Kampanii łącznie | (aktywne: N) |
| Słów kluczowych | |
| Avg. Quality Score | /10 |

**Typy kampanii:** PMax: N, Search: N, Shopping: N, Display: N, DemGen: N, Video: N
**Strategie bidowania:** Nx maximize conversion value, Nx target roas, Nx maximize conversions, Nx target impression share

#### Kampanie (ostatnie 30 dni)

| Kampania | Typ | Wydatki | Konw. | ROAS% | Budżet/d | Strategia | Ocena |
|----------|-----|---------|-------|-------|---------|-----------|-------|
| | PMax | PLN | | % | PLN | | ✅/⚠️/🔴 |
| | Search | PLN | | % | PLN | | |
| | Shopping | PLN | | % | PLN | | |
| **ŁĄCZNIE** | | PLN | | % | | | |

**Kampanie bez konwersji (> 300 PLN, 0 konwersji):**

| Kampania | Typ | Wydatki 30d | Diagnoza |
|----------|-----|-------------|---------|
| | | PLN | |
| **Łącznie drenażu** | | PLN | |

#### Analiza danych GA4

> ⚠️ Brak dostępu do GA4 — wymaga autoryzacji `bdos auth --add analytics`.
> Do weryfikacji po autoryzacji:
> - Czy GA4 property jest połączone z tym kontem Google Ads?
> - Czy kluczowe eventy są oznaczone jako konwersje?
> - Czy dane GA4 są zgodne z danymi Google Ads? (delta < 15% akceptowalna)
> - Bounce rate i czas sesji z kampanii płatnych vs organic?
> - Udział (not set) w source/medium?

#### Błędy w konfiguracji

- Niski Quality Score — sprawdź relevance słów kluczowych / LP
- Kampanie z wydatkami ale bez konwersji: [lista nazw]
- Strategia Maximize Clicks na koncie e-commerce — powinna być Maximize Conv. Value
- Nie wykryto krytycznych błędów konfiguracji

#### Analiza trackingu

- ✅/❌ Konwersje śledzone (___ konwersji w 30 dniach)
- ✅/❌ Wartości konwersji aktywne: PLN
- ✅/❌ Enhanced Conversions skonfigurowane
- ✅/❌ GA4 połączone z kontem Ads
- ✅/❌ Brak duplikacji konwersji
- ℹ️ Uwagi: ___

#### Sugestie i rekomendacje

- Przeanalizuj kampanie z najwyższymi wydatkami i najniższym ROAS
- Rozważ wyłączenie lub zmianę strategii kampanii nieopłacalnych
- Popraw dopasowanie słów kluczowych do treści reklam i stron docelowych
- Przeanalizuj N kampanię/kampanie z wydatkami bez konwersji

#### Ogólna ocena konta

⚠️ niski ROAS | 📉 niski QS | ❌ brak konwersji | ✅ Brak krytycznych problemów | ℹ️ lead gen

_(zostaw tylko pasujące flagi, pozostałe usuń)_

- ❌ Bardzo niski ROAS: __x (poniżej progu rentowności 3x dla e-commerce)
- ⚠️ Niski wynik jakości: __ /10
- ⚠️ Kampanie bez konwersji: N kampanii, PLN drenażu/msc
- ✅ Konwersje śledzone i wartości aktywne

#### Ocena specjalisty prowadzącego konto

⭐⭐ (2/5) — [komentarz jedno zdanie]

| Ocena | Opis |
|-------|------|
| ⭐ (1/5) | Konto w katastrofalnym stanie — straty, brak konwersji, błędy strukturalne |
| ⭐⭐ (2/5) | Kampanie generują straty lub marnują budżet — wymagana pilna optymalizacja |
| ⭐⭐⭐ (3/5) | Wyniki do oceny, brak danych o wartości konwersji (lead gen) / konto działa ale jest dużo do poprawy |
| ⭐⭐⭐⭐ (4/5) | Konto w dobrej kondycji — drobne optymalizacje |
| ⭐⭐⭐⭐⭐ (5/5) | Konto w doskonałej kondycji — benchmark dla innych |

---

### KONTO 2 — [Nazwa konta]

_[kopiuj blok KONTO 1 powyżej — wszystkie pola]_

---

### KONTO 3 — [Nazwa konta]

_[kopiuj blok KONTO 1 powyżej]_

---

## CZĘŚĆ 3 — KONTA NIEAKTYWNE _(tryb MCC, pomiń dla 1 konta)_

> Lista wszystkich kont w MCC bez wydatków w ostatnich 30 dniach. Źródło: BDOS MCC lub Google Ads UI → konta → filtr: wydatki = 0.

| # | Nazwa konta | ID konta | Status | Rekomendacja |
|---|------------|---------|--------|--------------|
| 1 | | | ⛔ Brak aktywności | Zarchiwizuj / Przerwa sezonowa / Weryfikacja kontraktu |
| 2 | | | ⛔ Brak aktywności | |
| 3 | | | ⛔ Brak aktywności | |
| ... | | | | |

> **Rekomendacja ogólna:** Sprawdź czy kampanie są wstrzymane, czy konto jest archiwalne, czy trwa przerwa sezonowa. Konta nieaktywne przez >3 miesiące bez przyczyny powinny zostać zarchiwizowane w BDOS i zweryfikowane z klientem pod kątem statusu kontraktu.

---

## CZĘŚĆ 4 — PODSUMOWANIE WYKONAWCZE MCC _(tryb MCC)_

### Statystyki globalne MCC (ostatnie 30 dni)

| Metryka | Wartość |
|---------|---------|
| Łączne wydatki (aktywne konta) | PLN |
| Łączne kliknięcia | |
| Łączne konwersje | |
| Łączna wartość konwersji | PLN |
| Średni ROAS portfela (konta e-comm) | x |
| Kont aktywnych | |
| Kont nieaktywnych | |
| Kont z problemami krytycznymi | |
| Kont bez problemów | |

### TOP 5 kont wg wydatków

| # | Konto | Wydatki | ROAS | Konwersje |
|---|-------|---------|------|-----------|
| 1 | | PLN | x | |
| 2 | | PLN | x | |
| 3 | | PLN | x | |
| 4 | | PLN | x | |
| 5 | | PLN | x | |

### Priorytety działań

**PILNE (do tygodnia):**

- [Konto]: Brak konwersji przy N PLN wydatków — sprawdź tracking
- [Konto]: ROAS __x — diagnoza kampanii

**DO OPTYMALIZACJI (do miesiąca):**

- [Konto]: ROAS __x | CPA __ PLN — optymalizacja bidów i struktury

---

## SEKCJA 11 — BCG cross-account _(tryb multi-konto, tylko e-commerce z feedem)_

> Pomiń jeśli brak danych produktowych lub 1 konto.

### Łączna baza produktowa

| Metryka | Wartość |
|---------|---------|
| Kont z danymi produktowymi | |
| Wszystkich produktów (unikalne item_id) | |
| Produktów aktywnych (min. 10 kliknięć) | |
| Łączna wartość konwersji (30d) | PLN |
| Łączne wydatki (30d) | PLN |
| ROAS portfela | x |

### Rozkład BCG — wszystkie konta

| Kwadrant | Produkty | % aktywnych | Wydatki | Przychód | ROAS | Śr. CTR | Śr. CR |
|----------|----------|-------------|---------|----------|------|---------|--------|
| ⭐ Gwiazdy | | % | PLN | PLN | x | % | % |
| 🐄 Dojne Krowy | | % | PLN | PLN | x | % | % |
| ❓ Znaki Zapytania | | % | PLN | PLN | x | % | % |
| 🐕 Psy | | % | PLN | PLN | x | % | % |

**Kluczowe insighty BCG:**
- Gwiazdy generują ___% przychodów przy ___% wydatków
- Znaki Zapytania: ROAS ___x, niedoinwestowane (___% budżetu)
- Psy: ___% budżetu przy ROAS ___x — potencjał optymalizacji

**Konta z dominacją Psów (>70% produktów):**

| Konto | % Psów | Wydatki | ROAS | Działanie |
|-------|--------|---------|------|-----------|
| | % | PLN | x | Feed audit |

**Konta z największym potencjałem ZQ:**

| Konto | ZQ z wzrostem >20% | Wydatki | Akcja |
|-------|-------------------|---------|-------|
| | | PLN | Wydziel / zwiększ budżet |

---

## CZĘŚĆ II.B — IMPACT FINANSOWY (PLN)

> Każdy wykryty problem wyceniony w złotówkach. Metodologia: patrz Sekcja F instrukcji.

| # | Problem | Formuła | Koszt miesięczny (PLN) | Koszt roczny (PLN) | Priorytet |
|---|---------|---------|----------------------|-------------------|-----------|
| 1 | Zduplikowane transakcje GA4 (zawyżony ROAS/przychód) | `duplikaty × AOV` | | | 🔴 |
| 2 | Kampanie bez konwersji (zmarnowany budżet) | `ad_spend_0conv` | | | 🔴 |
| 3 | Niski QS — przepłacony CPC | `spend × QS_penalty%` | | | 🟡 |
| 4 | Psy BCG — nieefektywny budżet feedu | `spend_Psy × (1 - ROAS_Psy)` | | | 🟡 |
| 5 | Niedoinwestowani liderzy (ROAS>10x, niski budżet) | `dodatkowy_budżet × ROAS` | | | 🟡 |
| 6 | Brak Customer Match | `lista × match_rate × CVR_boost × AOV` | | | 🟢 |
| 7 | Błędna atrybucja (Last Click vs DDA) | `budżet × delta_ROAS%` | | | 🟢 |
| 8 | Brak Enhanced Conversions | szacunek | | | 🟢 |
| 9 | Kanibalizacja PMax (branded) | `branded_CPC_delta × kliki` | | | 🟡 |
| 10 | Inne: ___ | | | | |
| **ŁĄCZNIE strat/szans** | | | **PLN** | **PLN** | |

**Potencjał wzrostu przychodów bez zwiększania budżetu:** ___% (~___ PLN/msc)
**Priorytetowy quick win (najwyższy ROI naprawy):** ___

---

## CZĘŚĆ III — REKOMENDACJE `[KRÓTKI]`

> W trybie multi-konto: oznacz przy każdej rekomendacji którego konta dotyczy. Format: **[Konto]** Opis.

### 🔴 Natychmiast (0–7 dni) — zatamowanie strat

| # | Działanie | Konto | Efekt | Odpowiedzialny |
|---|-----------|-------|-------|----------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

**Przykłady:**
- Wstrzymaj kampanie z >300 PLN i 0 konwersji: [Konto] — kampanie: [lista]
- Natychmiastowa diagnostyka śledzenia: [Konto] — konwersje liczą mikroeventy
- Zakończ lub przebuduj konta z ROAS <0.5x: [Konto]

### 🟡 Miesiąc 1 — optymalizacja i naprawa

| # | Działanie | Konto | Efekt szacowany | Priorytet |
|---|-----------|-------|----------------|-----------|
| 1 | Poprawa Quality Score | | niższy CPC o ~10–15% | Wysoki |
| 2 | Feed audit — Psy BCG | | ROAS +20–40% | Wysoki |
| 3 | Wydziel Znaki Zapytania do osobnych kampanii | | dostęp do ROAS 15–20x | Wysoki |
| 4 | | | | |
| 5 | | | | |

### 🟢 Miesiąc 2–3 — skalowanie i strategia

| # | Działanie | Konto | Efekt |
|---|-----------|-------|-------|
| 1 | Skalowanie liderów (ROAS >10x) | | +X PLN przychodów/msc |
| 2 | Enhanced Conversions | | lepsze sygnały Smart Bidding |
| 3 | Customer Match z bazą CRM | | ROAS +10–20% |
| 4 | GA4 integracja / autoryzacja API | | pełny cross-platform audit |
| 5 | Wartości konwersji dla lead gen | | optymalizacja Target CPA |

---

### Potencjał skalowania — konta z wysokim ROAS i niskim budżetem

_(wypełnij gdy zidentyfikujesz konta z ROAS >10x i budżetem poniżej potencjału IS)_

| Konto | ROAS | Obecny budżet/msc | Zalecany budżet | Szacowany wzrost przychodów |
|-------|------|-------------------|----------------|---------------------------|
| | x | PLN | PLN | PLN |

---

**Łączna ocena klientów / audytu:**

| Obszar | Ocena | Komentarz |
|--------|-------|-----------|
| ROAS portfela | ✅/⚠️/❌ | |
| Monitoring kont | ✅/⚠️/❌ | |
| Konfiguracja konwersji | ✅/⚠️/❌ | |
| Jakość feedów (BCG) | ✅/⚠️/❌ | |
| Quality Score | ✅/⚠️/❌ | |
| Skalowanie liderów | ✅/⚠️/❌ | |

**Ocena ogólna:** ⭐⭐⭐ (___/5) — _______________
