# AUDYT MARTECH — MODNAKIECKA.PL
## Raport Szczegółowy | Kwiecień 2026

**Klient:** modnakiecka.pl
**Data audytu:** 07.04.2026
**Audytor:** Adrian Andrzejczyk
**Okres analizy:** 30 dni (8.03.2026 – 7.04.2026)
**GA4 Property ID:** 291537403 (G-6S5QRBJ4EF)
**Platforma sklepu:** Shoper
**Typ biznesu:** E-commerce — moda damska (sukienki, komplety, okrycia)

> **Dostępy użyte w audycie:** GA4 Data API (pełny), analiza HTML strony (poprzedni audyt 2026-04-03).
> **Brak dostępu:** GTM Admin, Google Ads, BigQuery. Sekcje wymagające tych dostępów oznaczono 🔒.

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE

### KPI — Wyniki sklepu (30 dni, 8.03–7.04.2026)

| Wskaźnik | Wartość | Kontekst |
|---|---|---|
| Sesje łącznie | **1 858 660** | Duży ruch — ok. 62 tys. sesji dziennie |
| Zakupy (purchase events) | **31 090** | ~1 036 zakupów dziennie |
| Przychód | **6 842 880 PLN** | ~228 tys. PLN dziennie |
| Średnia wartość zamówienia (AOV) | **220,10 PLN** | Typowe dla fashion mid-market |
| Współczynnik konwersji (CR) | **1,67%** | Dobry wynik dla e-commerce fashion |
| Powracający klienci | **73,4% zakupów** | Silna baza lojalnościowa |
| Główny kanał sesji | Paid Social (33,4%) | Meta Ads dominuje ruchem |
| Najefektywniejszy kanał | Paid Search (9,27 PLN/sesja) | 3,1× lepszy niż Paid Social |

### Wyniki audytu per sekcja

| Sekcja | Wynik | Ocena |
|--------|-------|-------|
| 1. Infrastruktura śledzenia | 58% | ⚠️ Wymaga poprawy |
| 2. Zgodność z prawem (Consent Mode) | 100% sprawdzalnych | 🔒 Wymaga weryfikacji z GTM |
| 3. Konfiguracja GA4 i GTM | 28% | ❌ Krytyczny |
| 4. Jakość danych analitycznych | 97% | ✅ Bardzo dobra |
| 5. Oznaczenia UTM / źródła ruchu | 60% | ⚠️ Wymaga poprawy |
| 6. Analiza produktów (BCG) | N/A | ➖ Brak dostępu Ads + brak items[] |
| 7. Lejki zakupowe per kanał | 63% | ⚠️ Wymaga poprawy |
| 8. Integracja GA4 ↔ Google Ads | N/A | ➖ Brak dostępu Google Ads |
| 9. Analiza efektywności kanałów | 79% | ⚠️ Dobry, z rezerwami |
| 10. Google Ads | N/A | ➖ Brak dostępu Google Ads |
| **ŁĄCZNIE (sprawdzalne)** | **74%** | **⚠️ Wymaga poprawy** |

### Kluczowe wnioski — 5 najważniejszych problemów

**🚨 Problem 1 — Brak danych produktowych w zakupach**
GA4 rejestruje 31 090 zakupów i 6,84 mln PLN przychodu, ale **żaden produkt nie ma przypisanej sprzedaży**. Oznacza to, że platforma analityczna "wie" ile sprzedano, ale nie "wie" CO sprzedano. Niemożliwa jest analiza bestsellerów, optymalizacja reklam produktowych, ani personalizacja w SALESmanago na podstawie zakupionych produktów.

**🚨 Problem 2 — Zduplikowane kontenery GTM (2×) powodują wielokrotne rejestrowanie zakupów**
Na stronie działają jednocześnie dwa systemy zarządzania tagami: kontener agencji (GTM-N4D6KSC) i kontener automatycznie dodawany przez platformę Shoper (GTM-T68LWS). Jeden zakup jest rejestrowany nawet **12 razy** (potwierdzone dla ID=14564069). W GA4 jest to naprawiane, ale systemy reklamowe Meta i Google Ads "widzą" każde zdarzenie osobno — co zawyża ich ROAS i prowadzi do błędnej optymalizacji stawek.

**🚨 Problem 3 — Tylko 38% klientów, którzy zaczynają kasę, finalizuje zakup**
Z 81 640 klientów, którzy rozpoczęli proces zakupu, tylko 31 090 (38%) go finalizuje. Benchmark dla dobrego sklepu: 60-80%. Możliwe przyczyny: błąd techniczny (tagi nie strzelają), problem z kasą na urządzeniach mobilnych, lub ograniczona oferta metod płatności. Przy poprawie do 50%: **+3,3 mln PLN przychodu miesięcznie**.

**⚠️ Problem 4 — Mobile konwertuje 2,1× gorzej niż desktop mimo 89% udziału w ruchu**
89,3% odwiedzin pochodzi z telefonów (1,66 mln sesji), ale CR na mobile to 1,50% vs 3,19% na desktop. Przy tak dużym wolumenie mobilnym każde 0,5 punktu procentowego poprawy CR = **+1,75 mln PLN miesięcznie**.

**⚠️ Problem 5 — Fragmentation UTM: Meta Ads "rozpada się" na 14 wariantów**
Ruch z Facebooka jest rozbity na 14 różnych źródeł w GA4 (facebook, m.facebook.com, fb, lm.facebook.com, l.facebook.com itd.). 156 280 sesji Meta (22,3%) jest błędnie klasyfikowanych jako "polecenia" zamiast płatne kampanie. Prawdziwy ROAS Meta jest wyższy niż pokazuje GA4, co może prowadzić do błędnych decyzji budżetowych.

---

## CZĘŚĆ II — WYNIKI AUDYTU PER SEKCJA

---

### SEKCJA 1 — INFRASTRUKTURA ŚLEDZENIA (Audyt Wstępny)

#### Czym jest i dlaczego sprawdzamy

Infrastruktura śledzenia to fundament całej analityki cyfrowej. Składa się z systemu zarządzania tagami (Google Tag Manager — GTM), tagów pomiarowych (Google Analytics 4, Meta Pixel, tagi konwersji), oraz kodu strony. Podobnie jak w fabryce — jeśli czujniki pomiarowe są wadliwe lub zdublowane, wszystkie odczyty produkcji są nieprawidłowe. Niesprawna infrastruktura = błędne dane = złe decyzje biznesowe.

Audyt infrastruktury sprawdza: czy na stronie nie ma zbędnych lub zduplikowanych skryptów, czy narzędzia śledzące są poprawnie wdrożone i czy mierzą to, co powinny mierzyć.

#### Wyniki

**1.2 — Dwa kontenery GTM działają równolegle ❌**

Na stronie modnakiecka.pl jednocześnie działają dwa kontenery GTM:
- **GTM-N4D6KSC** — kontener zarządzany przez agencję/właściciela. Zawiera konfigurację śledzenia zamówień i inne zdarzenia e-commerce.
- **GTM-T68LWS** — kontener automatycznie wstrzykiwany przez platformę Shoper. Shoper od wersji 2.x wbudował własne zdarzenia GA4 (purchase, add_to_cart, view_item itp.) i uruchamia je niezależnie od kontenera agencji.

**Skutek:** Oba kontenery strzelają tymi samymi zdarzeniami w tym samym czasie. Jeden zakup rejestrowany jest kilkukrotnie. Weryfikacja z danych GA4: transactionID=14564069 pojawił się 12 razy w ciągu 30 dni; z próbki 200 transakcji — 49,5% (99 transakcji) ma zduplikowane hity. GA4 "naprawia" to na poziomie metryki `ecommercePurchases`, ale zewnętrzne systemy reklamowe (Meta Pixel, Google Ads Conversion Tag) nie mają tej korekcji i liczą każde zdarzenie osobno.

**Co to oznacza dla biznesu:** Meta Ads "widzi" np. 12 zakupów o wartości 12 × 430 PLN = 5 160 PLN zamiast jednego zakupu za 430 PLN. ROAS w panelu Meta jest zawyżony. Algorytmy optymalizacyjne Meta i Google uczą się na błędnych danych — dobierają odbiorców i stawki na podstawie fałszywych sygnałów.

**1.7 — Martwy tag Universal Analytics (UA) w kodzie strony ❌**

W kodzie HTML strony nadal obecny jest tag `UA-82686028-1` (Universal Analytics). UA zakończyło zbieranie danych w lipcu 2023 r. Tag ładuje się przy każdym odsłonie strony i niepotrzebnie zwalnia jej ładowanie (dodaje request do przestarzałego skryptu analytics.js). Nie jest to krytyczny problem, ale jest "bałaganem technicznym" obniżającym wydajność.

**1.9 — Brak danych produktowych w zdarzeniu zakupu ❌ KRYTYCZNY**

Każdy zakup w GA4 powinien zawierać informację o zakupionych produktach (tzw. tablica `items[]`): identyfikator produktu, nazwa, kategoria, cena, ilość. W modnakiecka.pl zdarzenie `purchase` (zakup) jest wysyłane, ale **bez danych o produktach**. Efekt: GA4 wie że nastąpił zakup za X złotych, ale nie wie jakie produkty zostały kupione.

Potwierdzenie z danych: TOP 20 produktów wg wyświetleń — wszystkie mają `itemsPurchased = 0` i `itemRevenue = 0 PLN`, mimo że strona wygenerowała 6 842 880 PLN przychodu. Zdarzenia `view_item` (oglądanie produktu) działają poprawnie — Beżowy Trencz ma 26 523 wyświetleń. Ale zakupy tych produktów nie są rejestrowane.

**Prawdopodobna przyczyna:** Kontener Shopera (GTM-T68LWS) wysyła zdarzenie `purchase` bez tablicy produktów lub z niezgodnymi identyfikatorami produktów. Kontener agencji (GTM-N4D6KSC) mógłby naprawić ten problem, ale z powodu konfliktów między kontenerami nie działa prawidłowo.

**Co to oznacza dla biznesu:**
- Niemożliwa analiza bestsellerów i słabo sprzedających się produktów
- Niemożliwa optymalizacja kampanii Shopping/PMax po produktach (brak danych o konwersjach per produkt)
- Niemożliwa personalizacja w SALESmanago (np. "klientka kupiła sukienkę X, pokaż jej pasujące akcesoria")
- Brak możliwości identyfikacji produktów z problemem (dużo wyświetleń, 0 zakupów)

**1.13 — Meta Pixel ✅**
Meta Pixel ID 973622559419130 aktywny. Generuje 703 013 sesji i ok. 1 981 000 PLN atrybuowanego przychodu w 30 dniach. Pixel działa, jednak ze względu na problem duplikacji tagów (pkt 1.2) może raportować zawyżone konwersje.

**1.16 — Pinterest Tag ✅**
Pinterest aktywny — kampanie CPC z 6 151 sesjami i 22 transakcjami.

**1.19 — Bing/Microsoft Ads ✅**
Bing Ads aktywne — 10 657 sesji, 376 transakcji, 100 306 PLN. Dobrze konwertujący kanał (CR 3,5%).

**1.22 — Criteo ✅**
Criteo Retargeting aktywny — 93 208 sesji łącznie, 216 357 PLN przychodu.

**1.23 — RTB House ✅**
RTB House aktywny (marginalny wolumen).

#### Scoring sekcji 1

| Element | Status | Punkty |
|---------|--------|--------|
| Dwa kontenery GTM | ❌ | 0/3 |
| Universal Analytics w kodzie | ❌ | 0/1 |
| Brak items[] w purchase | ❌ | 0/3 |
| Consent Mode — własny CMP | ⚠️ | 1/2 |
| Meta Pixel | ✅ | 3/3 |
| Pinterest Tag | ✅ | 3/3 |
| Bing/Microsoft Ads | ✅ | 2/2 |
| TikTok Pixel | ⚠️ | 1/3 |
| Criteo | ✅ | 2/2 |
| RTB House | ✅ | 2/2 |
| **Sprawdzalne** | | **14/24 pkt (58%)** |

---

### SEKCJA 2 — ZGODNOŚĆ Z PRAWEM (ePrivacy / Consent Mode)

#### Czym jest i dlaczego sprawdzamy

Consent Mode (tryb zgody) to system, który decyduje kiedy tagi analityczne i reklamowe mogą zbierać dane użytkowników. Od 2024 roku (wymóg Google i przepisy UE) każdy sklep internetowy musi implementować Consent Mode v2 — mechanizm, który pyta użytkownika o zgodę na pliki cookies i blokuje tagi przed jej udzieleniem.

Brak prawidłowego Consent Mode to ryzyko kary RODO (do 20 mln EUR lub 4% rocznego obrotu), a jednocześnie problem jakości danych — jeśli tagi strzelają przed zgodą użytkownika, dane są "zanieczyszczone" botami i niezamierzonymi zdarzeniami.

#### Wyniki

Weryfikacja Consent Mode wymaga dostępu do GTM Admin (do sprawdzenia ustawień consent każdego tagu) oraz DevTools w przeglądarce (do sprawdzenia co się dzieje po kliknięciu "Odrzuć"). **Brak dostępu do GTM Admin uniemożliwia pełną weryfikację tej sekcji.**

Elementy możliwe do sprawdzenia z GA4 API:

**2.18 — Brak danych osobowych w URL-ach stron ✅**
Analiza ścieżek URL (top strony wg sesji) nie wykazała adresów email, numerów telefonów ani innych danych osobowych w parametrach URL. Prawidłowe.

**2.19 — Brak danych osobowych w UTM ✅**
Analiza 200+ wariantów source/medium nie wykazała PII (Personally Identifiable Information) w parametrach UTM. Prawidłowe.

**Elementy nieweryfikowalne bez GTM Admin:**
Blokowanie tagów przed zgodą, sekwencja consent_default/consent_update w DataLayer, url_passthrough, maskowanie cookies po odmowie — wymagają sesji z dostępem do GTM Preview Mode i DevTools.

**Ważna rekomendacja dotycząca CMP:** Modnakiecka.pl korzysta z własnego rozwiązania zarządzania zgodami (`window.customerPrivacy` — wbudowane w Shoper). Własne implementacje CMP są trudniejsze w utrzymaniu i częściej mają luki. Zaleca się weryfikację przez zewnętrznego audytora ds. RODO lub wdrożenie certyfikowanego CMP (Cookiebot, Usercentrics) który automatycznie spełnia wymogi Consent Mode v2.

#### Scoring sekcji 2

| Element | Status | Punkty |
|---------|--------|--------|
| Consent Mode — weryfikacja GTM | 🔒 | 0/38 |
| Brak PII w URL | ✅ | 3/3 |
| Brak PII w UTM | ✅ | 3/3 |
| **Sprawdzalne** | | **6/6 pkt (100%)** |

---

### SEKCJA 3 — KONFIGURACJA GTM I GA4

#### Czym jest i dlaczego sprawdzamy

Konfiguracja narzędzi analitycznych to jak kalibracja wagi w magazynie. Nawet jeśli waga jest obecna i włączona, nieprawidłowa kalibracja daje błędne odczyty. GA4 i GTM mają kilkadziesiąt ustawień, które wpływają na jakość zbieranych danych: filtrowanie własnego ruchu pracowników, czas trwania sesji, wykluczanie zewnętrznych bramek płatności z powodujących fałszywy ruch.

#### Wyniki

**3A.1 / 3A.10 — Dwa kontenery GTM / Duplikacja tagów ❌ KRYTYCZNY**
(Opis rozwinięty w Sekcji 1.2 powyżej.) Konfiguracja GTM z dwoma kontenerami prowadzi do duplikacji zdarzeń e-commerce. Prawidłowe rozwiązanie: jeden aktywny kontener GTM odpowiedzialny za całe śledzenie.

**3A.7 — Tag Universal Analytics w GTM ❌**
Tag UA-82686028-1 obecny w kodzie. Wymaga usunięcia z kontenera GTM lub kodu strony.

**3C.3 — Waluta PLN ✅**
GA4 prawidłowo skonfigurowane na walutę PLN. Przychody raportowane poprawnie.

**3C.9 — Strumień danych aktywny ✅**
Dane napływają normalnie: 1 858 660 sesji w 30 dniach.

**3C.10 — Cross-domain tracking (bramki płatności) ⚠️**
Na stronie aktywne dwie bramki płatności: **Przelewy24** i **PayPo** (BNPL — kup teraz, zapłać później). Bez poprawnej konfiguracji cross-domain, kliknięcie "Zapłać" i przejście na stronę bramki płatności tworzy nową sesję z source=przelewy24. Klient wraca na stronę potwierdzenia jako "nowa sesja" z "nowym źródłem". To zaburza:
- Atrybucję źródeł (zakup atrybuowany bramce zamiast reklamie, która sprowadziła klienta)
- Metryki sesji (jedna wizyta liczona jako dwie)
- Dane CR (jeden zakup może być liczony w dwóch sesjach)

Symptomy problemu niewidoczne bezpośrednio w source/medium (bramki nie pojawiają się znacząco), ale wymaga potwierdzenia w GA4 Admin → Strumień → Konfigurowanie domen.

**3C.11 — Ignorowanie zduplikowanych tagów GA4 ❌**
Przy dwóch aktywnych kontenerach GTM (oba potencjalnie z tagiem GA4) i możliwym hardcoded GA4 w HTML strony, opcja "Ignoruj zduplikowane konfiguracje" w GA4 jest kluczowa. Bez niej każda sesja może być ładowana przez dwie instancje GA4 jednocześnie, podwajając page_view i inne zdarzenia. Potwierdzenie problemu: page_view = 17 750 478 w 30 dniach przy 1 858 660 sesjach = 9,55 page_view/sesję. Dla sklepu fashion ta liczba może być normalną (użytkownicy przeglądają wiele produktów), ale wymaga weryfikacji.

**3C.19 — Brak eksportu do BigQuery ❌**
BigQuery nie jest podłączony. BigQuery to bezpłatny (w podstawowym zakresie) eksport surowych danych GA4 do bazy danych, umożliwiający zaawansowane analizy: customer lifetime value, atrybucja wielodotykowa, segmentacja RFM, korelacja zakupów. Przy 6,84 mln PLN miesięcznego przychodu brak BigQuery oznacza brak możliwości analiz, które mogłyby zidentyfikować kolejne dźwignie wzrostu.

#### Scoring sekcji 3

| Element | Status | Punkty |
|---------|--------|--------|
| Dwa GTM / duplikacja tagów | ❌ | 0/3 |
| UA w GTM | ❌ | 0/3 |
| Ignorowanie duplikatów GA4 | ❌ | 0/3 |
| Waluta PLN | ✅ | 2/2 |
| Strumień aktywny | ✅ | 3/3 |
| Cross-domain tracking | ⚠️ | 0/3 |
| BigQuery | ❌ | 0/3 |
| Konwersje w GA4 | ✅ | 2/2 |
| **Sprawdzalne** | | **7/25 pkt (28%)** |

---

### SEKCJA 4 — JAKOŚĆ DANYCH ANALITYCZNYCH

#### Czym jest i dlaczego sprawdzamy

Jakość danych to odpowiedź na pytanie: "czy liczby w GA4 odzwierciedlają rzeczywistość?". Sklep może mieć doskonale skonfigurowane narzędzia, ale jeśli dane są "zanieczyszczone" fałszywym ruchem, zduplikowanymi transakcjami czy niezidentyfikowanymi źródłami — podejmowane decyzje będą błędne. Ta sekcja weryfikuje spójność i wiarygodność danych.

#### Wyniki

**Jakość źródeł ruchu — ocena ogólna ✅**

Dane źródłowe GA4 są w dobrej kondycji. Ruch (not set) wynosi zaledwie **3,3% sesji** (61 232 / 1 858 660) — wyraźnie poniżej alarmowego progu 15%. Direct/(none) to tylko 3,5% — bardzo niski poziom dla sklepu tej wielkości (typowo 15-30%). Ruch wewnętrzny pracowników nie zaburza danych (Warszawa CR = 1,67% = dokładnie tyle co średnia konta).

**Dystrybucja nowych użytkowników — naturalna ✅**

Pierwsze źródło nowych użytkowników: google/cpc (218 087) → facebook/cpc (147 883) → google/organic (64 454) → direct (38 873). Naturalna hierarchia dla sklepu z aktywnymi kampaniami Google i Meta.

**Fragmentacja Facebook — krytyczny problem UTM ❌**

Choć jakość danych per se jest dobra (niskie (not set)), ruch z Facebooka/Meta jest rozbity na **14 różnych wariantów source/medium** generujących 703 013 sesji łącznie:

| Wariant | Sesje | Problem |
|---------|-------|---------|
| facebook/cpc | 546 733 | ✅ Poprawny |
| m.facebook.com/referral | 51 530 | ❌ Mobile bez UTM |
| fb/paid | 48 461 | ❌ Niestandardowy format |
| lm.facebook.com/referral | 28 769 | ❌ Referral zamiast paid |
| facebook/traffic | 16 365 | ❌ Medium "traffic" zamiast "cpc" |
| l.facebook.com/referral | 8 171 | ❌ Referral zamiast paid |
| + 8 dalszych wariantów | 3 014 | ❌ |

Łącznie: **156 280 sesji Meta (22,3%) z błędnym source/medium**, co zaniża mierzony ROAS Meta w GA4 o ~322 719 PLN/msc niezakwalifikowanych do kanału "Paid Social".

**Kompletność lejka e-commerce ✅ (z zastrzeżeniami)**

Wszystkie 4 standardowe zdarzenia GA4 e-commerce są wdrożone i działają:
- `view_item`: 4 629 750 (6,65/użytkownik — aktywne przeglądanie produktów)
- `add_to_cart`: 249 979 (3,13/użytkownik)
- `begin_checkout`: 81 640 (2,29/użytkownik)
- `purchase`: 31 090 (1,12/użytkownik)

Lejek jest fizycznie spójny (każdy krok mniejszy od poprzedniego). JEDNAK: dodatkowe zdarzenie `złożenie_zamówienia` (custom event Shopera) = **76 136 trafień** przy `purchase` = 31 090 — różnica 2,45×. Oznacza to, że system Shopera rejestruje ~76 tys. "złożeń zamówień", podczas gdy GA4 purchase event rejestruje tylko ~31 tys. Jedna z interpretacji: purchase event nie odpala się przy wszystkich zamówieniach (np. przy błędzie JS, szybkim kliknięciu "wstecz", lub specyficznych metodach płatności). Wymaga natychmiastowej weryfikacji w panelu Shopera.

**Jakość transakcji ✅**

- Ratio ecommercePurchases/transactions = 1,00 (GA4 prawidłowo deduplikuje zakupy po ID transakcji)
- 0% transakcji bez identyfikatora (wszystkie zakupy mają przypisany numer zamówienia)
- Brak "malformed" ID (numery zamówień są poprawnym formatem numerycznym Shopera)
- AOV = 220,10 PLN — spójny per kanał: Paid Search (249,7 PLN), Organic (230,5 PLN), Paid Social (194,2 PLN)

**Powracający klienci — doskonały wynik ✅**

- Powracający użytkownicy: 1 156 169 sesji (61,7%), 22 790 zakupów, CR = 1,97%
- Nowi użytkownicy: 663 262 sesji (35,4%), 8 249 zakupów, CR = 1,24%
- Powracający generują **73,4% zakupów** i **73,8% przychodu** (5 035 969 PLN)
- CR powracających 1,59× wyższy niż nowych — silna baza lojalnych klientów

**Engagement rate — doskonały ✅**

Engagement rate (% sesji z interakcją >10s) per kanał: Paid Search 92,7%, Paid Shopping 91,5%, Email 90,6%, Organic Search 90,4%, Paid Social 89,0%. Wszystkie główne kanały >84%. Ruch jest bardzo zaangażowany. Wyjątek: kanał "Unassigned" (62,5%) — niższy engagement potwierdza problem z identyfikacją tego ruchu.

#### Scoring sekcji 4

| Element | Status | Punkty |
|---------|--------|--------|
| First user (not set) | ✅ | 3/3 |
| First user — naturalna dystrybucja | ✅ | 3/3 |
| Sesje (not set) <5% | ✅ | 3/3 |
| Ruch wygląda naturalnie | ✅ | 3/3 |
| Brak spamu | ✅ | 2/2 |
| Bramki płatności poza ścieżką | ✅ | 3/3 |
| Bramki pocztowe | ✅ | 3/3 |
| Facebook fragmentacja | ❌ | 0/2 |
| Ruch z Polski | ✅ | 2/2 |
| CR naturalny | ✅ | 2/2 |
| (not set) <5% | ✅ | 3/3 |
| Direct <30% | ✅ | 3/3 |
| Not set + direct <40% | ✅ | 3/3 |
| Trans. (not set) | ✅ | 3/3 |
| Ratio EP:TR | ✅ | 3/3 |
| Brak null ID | ✅ | 3/3 |
| Brak malformed ID | ✅ | 3/3 |
| value >0 | ✅ | 3/3 |
| view_item | ✅ | 3/3 |
| add_to_cart | ✅ | 3/3 |
| begin_checkout | ✅ | 3/3 |
| purchase | ✅ | 3/3 |
| Lejek naturalny | ⚠️ | 2/3 |
| AOV spójny | ✅ | 2/2 |
| **ŁĄCZNIE** | | **63/65 pkt (97%)** |

---

### SEKCJA 5 — OZNACZENIA UTM / ŹRÓDŁA RUCHU

#### Czym jest i dlaczego sprawdzamy

UTM (Urchin Tracking Module) to parametry dodawane do linków w kampaniach reklamowych i emailach, które informują GA4 skąd pochodzi odwiedzający. Bez UTM GA4 nie wie że kliknięcie w reklamę Facebook to reklama — widzi je jako "polecenie z m.facebook.com". Prawidłowe UTM to warunek konieczny właściwego pomiaru ROI z każdego kanału.

#### Wyniki

**5.1 — Standaryzacja UTM ❌**

Fragmentacja UTM na wielu kanałach:

**Facebook/Meta — 14 wariantów** (opisane w sekcji 4). 156 280 sesji (22,3% ruchu Meta) bez poprawnych UTM.

**TikTok — 7 wariantów:**
- tiktok/paid: 10 112 sesji ✅
- tiktok/cpc: 5 317 sesji ⚠️ (inny format niż "paid")
- tiktok/traffic: 3 784 sesji ❌ (engagement campaign, nie zakupowa)
- tiktok/(not set): 311 sesji ❌
- tiktok.com/referral: 184 sesji ❌ (kliknięcia bez UTM)
- tiktok/referral: 76 sesji ❌
- `tiktok?utm_id`/paid: 12 sesji ❌ (malformed URL — `utm_id` w source zamiast w parametrze!)

Ostatni wariant `tiktok?utm_id` to technicznie malformed URL gdzie parametr `utm_id` wpadł do nazwy source zamiast być osobnym parametrem URL. Wskazuje to na błąd w konfiguracji kampanii TikTok.

**SALESmanago — 9 mediums:**
Ruch z SALESmanago jest stosunkowo dobrze oznaczony (sms, newsletter, email_confirmation, email, workflow). Problem: `salesmanago.pl/referral` = 20 410 sesji — to wiadomości lub powiadomienia SALESmanago bez UTM, klasyfikowane jako referral zamiast email/push. 924 transakcje (283 728 PLN) atrybuowane do "referral" zamiast do właściwego kanału email.

**5.4 — Meta Ads UTM ⚠️**
Główny wariant facebook/cpc (546 733 sesji) ma poprawne UTM. Problem: kampanie oznaczone medium=traffic (16 365 sesji, tylko 20 transakcji = CR 0,12%) — kampanie "traffic" to kampanie zasięgowe/angażujące, nie konwersyjne. Ich wyniki nie powinny być mieszane z kampaniami konwersyjnymi w analizie.

**5.7 — Email marketing — UTM ✅**
SALESmanago używa różnorodnych UTM dla kanałów email: sms, newsletter, email_confirmation, email, workflow. Łącznie 45 981 sesji, 1 499 transakcji, 413 399 PLN.

**5.10 — PWA bez UTM ⚠️**
`pwa/(not set)` = 23 019 sesji, 731 transakcji, 171 877 PLN — ruch z Progressive Web App (wersja aplikacyjna sklepu) bez żadnego oznaczenia UTM. 171 877 PLN miesięcznie generowane przez PWA, ale nie wiadomo skąd użytkownicy trafiają do PWA (z reklamy? z organic? z push notification?).

#### Scoring sekcji 5

| Element | Status | Punkty |
|---------|--------|--------|
| Standaryzacja UTM | ❌ | 0/1 |
| Meta UTM (częściowe) | ⚠️ | 2/3 |
| Organic social UTM | ⚠️ | 1/2 |
| Email UTM | ✅ | 2/2 |
| Pozostałe płatne | ⚠️ | 1/2 |
| **Sprawdzalne** | | **6/10 pkt (60%)** |

---

### SEKCJA 6 — ANALIZA PRODUKTÓW (BCG)

#### Czym jest i dlaczego sprawdzamy

Macierz BCG to narzędzie klasyfikacji produktów na 4 kategorie:
- ⭐ Gwiazdy: wysokie przychody + wysoki ROAS (skaluj budżet)
- 🐄 Dojne Krowy: wysokie przychody + niski ROAS (utrzymuj, nie przepłacaj)
- ❓ Znaki Zapytania: niskie przychody + wysoki ROAS (testuj)
- 🐕 Psy: niskie przychody + niski ROAS (ogranicz wydatki)

Analiza BCG pozwala alokować budżet reklamowy do produktów, które faktycznie na siebie zarabiają.

#### Wyniki

**➖ Analiza niemożliwa — dwa powody:**

1. **Brak dostępu do Google Ads** — brak danych o wydatkach i przychodach per produkt z kampanii Shopping/PMax
2. **Brak item-level danych GA4** — jak opisano w pkt 1.9, zdarzenie `purchase` nie zawiera tablicy produktów. Wszystkie produkty w GA4 mają `itemRevenue = 0`, `itemsPurchased = 0`.

Bez naprawienia problemu z items[] (pkt 1.9) analiza BCG nie będzie możliwa nawet po uzyskaniu dostępu Google Ads. **Naprawa items[] jest warunkiem wstępnym przeprowadzenia analizy BCG.**

Pośrednia obserwacja z danych: TOP 20 produktów wg wyświetleń to Okrycia Wierzchnie (Beżowy Trencz — 26 523 wyświetleń), Komplety Marynarka+Spodnie, Sukienki Eleganckie. To typowe kategorie dla sprzedaży wiosna 2026 w fashion damskim.

---

### SEKCJA 7 — LEJKI ZAKUPOWE PER KANAŁ

#### Czym jest i dlaczego sprawdzamy

Lejek zakupowy to ścieżka klienta od pierwszego wejścia na stronę do finalizacji zakupu. W e-commerce standardowy lejek to: wejście → oglądanie produktu → dodanie do koszyka → rozpoczęcie kasy → zakup. Analiza lejka pozwala znaleźć "wąskie gardła" — etapy, na których klienci rezygnują z zakupu. Nawet małe usprawnienie na etapie kasy (np. dodanie metody płatności BLIK) może znacząco zwiększyć sprzedaż.

#### Wyniki

**7.1 — Wszystkie 4 zdarzenia e-commerce aktywne ✅**
view_item, add_to_cart, begin_checkout, purchase — wszystkie działają. Uzupełniająco aktywne: add_shipping_info (80 967) i add_payment_info (81 130) — szczegółowy lejek kasy jest wdrożony.

**7.2 — CR płatny ≥ 50% CR organiczny ✅**
google/cpc: CR = 12 129 / 623 547 = **1,95%**
google/organic: CR = 1 595 / 136 835 = **1,17%**
Ratio: 1,95 / 1,17 = 167% — ruch płatny konwertuje 1,67× lepiej niż organiczny. Dobry sygnał jakości kampanii Google.

**7.4 — Checkout drop-off 61,9% ❌ KRYTYCZNY**

To najważniejszy problem lejkowy. Porównanie:

| Etap lejka | Zdarzenia | Przejście |
|---|---|---|
| add_to_cart | 249 979 | — |
| begin_checkout | 81 640 | 32,7% (z ATC) |
| add_shipping_info | 80 967 | 99,2% ✅ |
| add_payment_info | 81 130 | 100,2% ✅ |
| złożenie_zamówienia (Shoper) | **76 136** | 93,3% ✅ |
| **purchase (GA4)** | **31 090** | **38,1%** ❌ |

Kluczowa obserwacja: etapy add_shipping_info (80 967) i add_payment_info (81 130) są niemal identyczne z begin_checkout (81 640) — prawie wszyscy, którzy zaczęli kasę, wypełnili dane. Nawet zdarzenie Shopera `złożenie_zamówienia` pokazuje 76 136 "zamówień złożonych" — tylko 7% drop-off z begin_checkout. Ale `purchase` w GA4 = tylko 31 090.

**Wniosek:** Problem nie leży w UX kasy (użytkownicy wypełniają dane), ale w **niekompletnym firowaniu zdarzenia `purchase`**. Prawdopodobne: purchase event nie odpala się dla ok. 45 000 zakupów miesięcznie. Możliwe przyczyny: błąd JavaScript na stronie potwierdzenia, tag w GTM strzelający tylko przy pewnych metodach płatności, lub konflikt między dwoma kontenerami GTM.

**Natychmiastowa weryfikacja:** Porównaj liczbę zamówień w panelu Shopera (liczba rzeczywistych zamówień) z purchase events w GA4 za ten sam okres. Jeśli panel Shoper pokazuje ~70 000 zamówień a GA4 ~31 000 — brakuje 45 000 zarejestrowanych zakupów miesięcznie.

**Potencjalny impact:** Jeśli purchase event jest zaniżony o ~45 000 zakupów/msc × 220 PLN = ~9 900 000 PLN/msc niezidentyfikowanych konwersji. Smart Bidding Google Ads i optymalizacja Meta Advantage+ działają na połowie rzeczywistych danych → algorytmy uczą się na niekompletnych sygnałach → kampanie są nieefektywne.

**Lejek per kanał — kluczowe obserwacje:**

| Kanał | Sesje | CR | Rev/sesja | Czas sesji |
|-------|-------|----|-----------|----|
| Paid Search | 168 729 | **3,71%** | **9,27 PLN** | 597s |
| Referral | 24 198 | **4,15%** | 12,71 PLN | 651s |
| Paid Shopping | 25 149 | 2,43% | 5,24 PLN | 484s |
| Direct | 64 812 | 1,95% | 4,34 PLN | 266s |
| Organic Search | 143 668 | 1,29% | 2,98 PLN | 339s |
| Cross-network | 442 595 | 1,31% | 2,78 PLN | 309s |
| **Paid Social** | **620 375** | **1,40%** | **2,71 PLN** | **220s** |
| Unassigned | 82 600 | 1,94% | 4,50 PLN | 496s |

Paid Social (głównie Meta) to największy kanał sesji (33,4%) ale **najniższy czas sesji** (220s) i przychód/sesję (2,71 PLN). Paid Search mimo 9× mniejszego wolumenu generuje 3,1× więcej przychodu per sesję.

#### Scoring sekcji 7

| Element | Status | Punkty |
|---------|--------|--------|
| Cztery zdarzenia aktywne | ✅ | 2/2 |
| CR paid vs organic | ✅ | 2/2 |
| CR <0.1% kanały | ⚠️ | 1/2 |
| Checkout drop-off | ❌ | 0/2 |
| **ŁĄCZNIE** | | **5/8 pkt (63%)** |

---

### SEKCJA 9 — ANALIZA EFEKTYWNOŚCI KANAŁÓW

#### Czym jest i dlaczego sprawdzamy

Analiza efektywności kanałów to odpowiedź na pytanie: "który kanał marketingowy przynosi najlepszy zwrot z inwestycji?". Przy wielu aktywnych kanałach (Google Ads, Meta Ads, TikTok, Bing, Criteo, SALESmanago, Referral) kluczowe jest wiedzieć, gdzie każda zainwestowana złotówka przynosi największy efekt.

#### Wyniki

**9.1 — CR paid vs organic ✅**
Kanały płatne Google konwertują lepiej niż organiczne (167% ratio) — ruch płatny jest właściwie targetowany.

**9.2 — Ranking kanałów wg Rev/sesja**

| Ranking | Kanał | Rev/sesja | Sesje | Ocena |
|---------|-------|-----------|-------|-------|
| 🥇 1 | Referral | **12,71 PLN** | 24 198 | Niedoinwestowany! |
| 🥈 2 | Paid Search | **9,27 PLN** | 168 729 | Skalować! |
| 🥉 3 | Direct | 4,34 PLN | 64 812 | OK |
| 4 | Organic Search | 2,98 PLN | 143 668 | OK |
| 5 | Cross-network | 2,78 PLN | 442 595 | Do optymalizacji |
| 6 | **Paid Social** | **2,71 PLN** | **620 375** | **Najdroższy, najgorzej konwertuje** |
| 7 | Display | 2,22 PLN | 73 711 | Słaby |
| 8 | SMS | 1,89 PLN | 9 839 | Do oceny per kampania |

**Kluczowy wniosek:** Referral (partnerzy, afiliacja, PR) generuje 12,71 PLN/sesję przy CR 4,15% — **4,7× więcej niż Paid Social**. Program afiliacyjny Wedare osiąga CR ~24%. To potężnie niedoinwestowany kanał.

**9.3 — Mobile/Desktop CVR ratio ⚠️**

To jeden z najważniejszych problemów operacyjnych sklepu:

| Urządzenie | Sesje | Zakupy | CR | AOV |
|------------|-------|--------|----|-----|
| **Mobile** | 1 658 971 (89,3%) | 24 900 (80,1%) | **1,50%** | 210,9 PLN |
| **Desktop** | 188 525 (10,1%) | 6 013 (19,3%) | **3,19%** | 258,2 PLN |
| Tablet | 21 481 (1,2%) | 177 (0,6%) | 0,82% | 215,6 PLN |

Mobile stanowi 89,3% ruchu ale CR jest 2,13× niższy niż desktop. AOV na desktop jest o 47 PLN wyższy (+22%). Desktop generuje zakupy 2,1× efektywniej mimo zaledwie 10% wolumenu.

**Wycena potencjału mobile (ostrożna):**
- Gdyby mobile CR wzrósł o 0,5pp (z 1,50% do 2,00%):
- +1 658 971 × 0,50% = **+8 295 dodatkowych zakupów × 210,9 PLN = +1 749 000 PLN/msc**
- Gdyby wzrósł o 1pp: **+3 499 000 PLN/msc**

**9.5 — Porzucenie koszyka 87,6% ❌**

Z 249 979 dodań do koszyka tylko 31 090 (12,4%) kończy się zakupem. Porzucenie koszyka = 87,6%.

Benchmark dla e-commerce fashion PL: 75-85%. modnakiecka.pl jest na granicy lub powyżej normy, ale absolutna skala jest ogromna: **218 889 porzuconych koszyków miesięcznie**.

Przy kosztu ponownego dotarcia do 5% porzuconych koszyków przez remarketing (SALESmanago, Criteo, Meta):
- 218 889 × 5% = 10 944 odzyskanych koszyków × 220 PLN = **+2 407 680 PLN/msc potencjał**

Aktualny remarketing Criteo generuje 203 948 PLN z 73 105 sesji. Intensyfikacja retargetingu powinna być priorytetem.

**9.7 — Ruch wewnętrzny nie zaburza danych ✅**
Warszawa (siedziba firmy): CR = 1,67% = identyczny ze średnią konta. Ruch wewnętrzny pracowników jest filtrowany prawidłowo lub jest pomijalnie mały.

**9.8 — Quick wins — kanały z wysokim CR ✅**
- zasobygwp.pl/referral: 39 sesji, 5 transakcji, 5 823 PLN → CR **12,8%** → wart eksploracji partnerstwa
- wedare_*/cps (affiliate): ~575 sesji, ~141 transakcji → CR ~24,5% → skalować afiliację!
- pl.search.yahoo.com/referral: 744 sesji, 29 transakcji → CR 3,9%

**9.9 — Bramki płatności w referral ✅**
Przelewy24, PayPo nieobecne jako źródła ruchu z istotnym wolumenem. Brak problemu.

**9.10 — Retencja — doskonały wskaźnik ✅**
Powracający: 1 156 169 sesji, CR = 1,97%, 5 035 969 PLN (73,8% przychodu). Silna baza stałych klientek jest fundamentem stabilności biznesu. Koszt pozyskania powracającego klienta jest wielokrotnie niższy niż nowego.

#### Scoring sekcji 9

| Element | Status | Punkty |
|---------|--------|--------|
| CVR paid vs organic | ✅ | 3/3 |
| Rev/sesja per kanał | ✅ | 2/2 |
| Mobile/Desktop CVR | ⚠️ | 1/3 |
| Engagement rate | ✅ | 2/2 |
| Porzucenie koszyka | ❌ | 0/3 |
| Anomalie ruchu | ✅ | 2/2 |
| Ruch wewnętrzny | ✅ | 3/3 |
| Referral quick wins | ✅ | 1/1 |
| Bramki w referral | ✅ | 3/3 |
| Retencja | ✅ | 2/2 |
| **ŁĄCZNIE** | | **19/24 pkt (79%)** |

---

## CZĘŚĆ II.B — IMPACT FINANSOWY (PODSUMOWANIE)

### Problemy techniczne — bezpośrednie straty

| Problem | Opis | Szacunek PLN/msc | Priorytet |
|---------|------|-----------------|-----------|
| Brak purchase events (45k zakupów) | purchase event nie odpalał się przy części zamówień → Smart Bidding uczy się na 50% danych | Potencjalnie 9 900 000 PLN brakujących sygnałów konwersji | 🔴 NATYCHMIAST |
| Duplikacja tagów → zawyżony ROAS Meta/GAds | algorytmy reklamowe uczą się na błędnych danych → błędna optymalizacja stawek | Szacunkowo 10-20% nieefektywności budżetu reklamowego | 🔴 NATYCHMIAST |
| Brak items[] → brak optymalizacji produktowej | brak BCG, brak personalizacji, brak feed produktowy z konwersjami | Blokuje 6 842 880 PLN/msc danych produktowych | 🔴 NATYCHMIAST |

### Optymalizacje — potencjał wzrostu

| Optymalizacja | Metodologia | Szacunek PLN/msc | Horyzont |
|---|---|---|---|
| Poprawa mobile CR o 0,5pp | 1 658 971 ses × 0,5% × 210,9 PLN | **+1 749 000 PLN** | Miesiąc 1-2 |
| Odratowanie 5% porzuconych koszyków | 218 889 × 5% × 220 PLN | **+2 408 000 PLN** | Miesiąc 1 |
| Poprawa checkout drop-off o 10pp | 81 640 × 10% × 220 PLN | **+1 796 000 PLN** | Miesiąc 1-3 |
| Skalowanie afiliacji Wedare (24% CR) | Podwojenie wolumenu (575→1150 ses) | **+30 000 PLN** | Miesiąc 2 |
| Poprawne UTM Meta (+22% atryb.) | 156 280 ses z poprawną atrybucją | Lepsza alokacja budżetu (nie PLN bezp.) | Tydzień 1 |
| **Łączny potencjał (realistyczny)** | | **+5 953 000 PLN/msc** | **+71 436 000 PLN/rok** |

---

## CZĘŚĆ III — PLAN DZIAŁANIA

### 🔴 Natychmiast (0–7 dni) — zatamowanie strat

| # | Działanie | Cel | Odpowiedzialny |
|---|-----------|-----|----------------|
| 1 | **Wyjaśnij rozbieżność `złożenie_zamówienia` (76k) vs `purchase` (31k)**: porównaj z panelem Shopera | Ustal czy mamy ~45k niezarejestrowanych zakupów/msc | Dev/GTM |
| 2 | **Zidentyfikuj duplikację w GTM**: otwórz DevTools na stronie potwierdzenia zamówienia, sprawdź ile razy odpala się purchase event | Potwierdzenie źródła duplikacji | Dev/GTM |
| 3 | **Zatrzymaj duplikację tagów**: wyłącz tagi GA4 e-commerce z kontenera agencji (GTM-N4D6KSC) jeśli Shoper GTM (GTM-T68LWS) je już wysyła — LUB wyłącz kontener Shopera i przenieś wszystko do kontenera agencji | 1 aktywny tag purchase = prawidłowe dane | Dev/GTM |
| 4 | **Włącz automatyczne UTM Meta**: Meta Ads Manager → Ustawienia konta → Automatyczne UTM | Koniec fragmentacji na 14 wariantów | PPC Manager |

### 🟡 Miesiąc 1 — Naprawa i optymalizacja

| # | Działanie | Cel | Odpowiedzialny |
|---|-----------|-----|----------------|
| 1 | **Napraw items[] w purchase event**: sprawdź DataLayer na stronie potwierdzenia, dodaj tablicę products/items do GA4 purchase event | Dane produktowe w GA4, możliwa analiza BCG | Dev/GTM |
| 2 | **Aktywuj kampanię retargetingową porzuconych koszyków w SALESmanago**: 3 emaile (1h, 24h, 72h po porzuceniu) z dynamicznymi produktami | Odratowanie koszyków, est. +2,4 mln PLN/msc | Email Marketing |
| 3 | **Diagnostyka UX mobile**: wdrożyć Microsoft Clarity lub Hotjar, nagrać sesje mobilne, zidentyfikować elementy blokujące zakup na telefonie | Identyfikacja barier mobile CR | UX/Dev |
| 4 | **Podłącz BigQuery**: GA4 Admin → Połączone usługi → BigQuery Export → włącz eksport dzienny | Pełne dane historyczne do analiz zaawansowanych | Analytics |
| 5 | **Skonfiguruj cross-domain dla Przelewy24 i PayPo**: GA4 Admin → Strumień → Konfigurowanie domen → dodaj przelewy24.pl, paypo.pl | Prawidłowa atrybucja zakupów przez bramki | GA4 Admin |
| 6 | **Standaryzuj UTM TikTok**: jeden format (source=tiktok, medium=paid_social lub cpc), usuń warianty traffic/referral | Spójne dane TikTok w GA4 | PPC Manager |
| 7 | **Dodaj UTM do PWA/push notifications SALESmanago** | Identyfikacja 23 019 sesji PWA, 731 zakupów | Email/Dev |

### 🟢 Miesiąc 2–3 — Skalowanie i strategia

| # | Działanie | Cel | Odpowiedzialny |
|---|-----------|-----|----------------|
| 1 | **Analiza BCG produktów** (po naprawieniu items[]): zidentyfikuj Gwiazdy (wysokie obroty + wysoki ROAS), Dojne Krowy, Psy. Wyklucz Psy z kampanii Shopping/PMax | Alokacja budżetu do produktów z najwyższym zwrotem | Analytics + PPC |
| 2 | **Skaluj program afiliacją Wedare**: CR ~24,5% to wyjątkowo wysokie wyniki. Zwiększ wolumen partnerów, zrekrutuj nowe kanały afiliacjne | Est. potencjał przy 5× wolumenie: +150 000 PLN/msc | Partnership Manager |
| 3 | **Zoptymalizuj podział budżetu Google Ads**: przesuń budżet z Cross-network/Display (2,78-2,22 PLN/sesja) do Paid Search (9,27 PLN/sesja) | Wzrost efektywności bez zwiększania budżetu | PPC Manager |
| 4 | **Wdrożyć Meta CAPI** (Conversions API): server-side lub przez GTM → wysyła dane konwersji do Meta poza przeglądarką użytkownika → odporność na iOS 14+ | +15-30% widoczności konwersji Meta | Dev/GTM |
| 5 | **Weryfikacja Consent Mode** z dostępem GTM Admin: sprawdź czy wszystkie tagi są blokowane przed zgodą, dodaj url_passthrough | Zgodność z RODO, lepsza atrybucja po odmowie cookies | GTM/Legal |
| 6 | **Rozważ wdrożenie Clarity**: bezpłatne nagrania sesji, heatmapy, rage clicks — szczególnie wartościowe dla diagnostyki mobile | Ciągła diagnostyka UX | UX/Dev |
| 7 | **Usuń martwy tag UA-82686028-1** z kodu strony | Higiena techniczna, minimalne przyspieszenie ładowania | Dev |

---

## PODSUMOWANIE PUNKTACJI

| Sekcja | Uzyskane | Max sprawdzalne | Wynik % | Ocena |
|--------|----------|-----------------|---------|-------|
| 1. Audyt Wstępny | 14 | 24 | 58% | ⚠️ |
| 2. ePrivacy | 6 | 6 | 100% | ✅ (reszta 🔒) |
| 3. Konfiguracja | 7 | 25 | 28% | ❌ |
| 4. Data Quality | 63 | 65 | 97% | ✅ |
| 5. UTM | 6 | 10 | 60% | ⚠️ |
| 6. BCG | ➖ | ➖ | N/A | ➖ |
| 7. Lejki | 5 | 8 | 63% | ⚠️ |
| 8. GA4↔Ads | ➖ | ➖ | N/A | ➖ |
| 9. Analiza | 19 | 24 | 79% | ⚠️ |
| 10. Google Ads | ➖ | ➖ | N/A | ➖ |
| **ŁĄCZNIE** | **120** | **162** | **74%** | ⚠️ Wymaga poprawy |

**Ocena ogólna:** Modnakiecka.pl ma doskonałą bazę danych analitycznych (jakość 97%) i silne wyniki biznesowe (6,84 mln PLN/msc, CR 1,67%, 73% powracających), ale trzy krytyczne błędy techniczne (duplikacja tagów, brak items[], możliwe niedoreje`strowanie zakupów) zagrażają niezawodności danych i efektywności kampanii reklamowych. Naprawienie tych błędów w ciągu 7 dni jest warunkiem koniecznym prawidłowej optymalizacji konta.
