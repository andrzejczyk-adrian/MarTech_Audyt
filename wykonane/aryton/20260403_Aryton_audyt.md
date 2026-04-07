# Raport Audytu GA4 — Aryton (Patrizia)

**Data:** 2026-04-03
**Audytor:** Adrian Andrzejczyk
**GA4 Property:** www.aryton.pl – GA4 (ID: 326801658)
**Measurement ID:** G-93NK3C48R3
**GTM Container:** GTM-MDGSP8
**URL strony:** https://patrizia.aryton.pl/
**Typ biznesu:** E-commerce (odzież premium)
**Strumień danych:** patrizia.aryton.pl – GA4 (ID: 3954589560)

---

## CZĘŚĆ I — PODSUMOWANIE WYKONAWCZE

### Wyniki sekcji

| Sekcja | Uzyskane pkt | Max pkt | Wynik % | Ocena |
|--------|-------------|---------|---------|-------|
| 1. Audyt Wstępny | 9 | 24 | 37% | ❌ Krytyczny |
| 2. ePrivacy / Consent Mode | 2 | 20 | 10% | ❌ Krytyczny |
| 3. Konfiguracja GA4 | 28 | 42 | 67% | ⚠️ Wymaga poprawy |
| 4. Data Quality | 18 | 38 | 47% | ❌ Krytyczny |
| 5. UTM | 5 | 14 | 36% | ❌ Krytyczny |
| **ŁĄCZNIE** | **62** | **138** | **45%** | **❌ Krytyczny** |

---

### Jakość danych — CZY DANYM MOŻNA UFAĆ?

**Częściowo — dane o ruchu są wiarygodne, dane transakcyjne wymagają korekty interpretacyjnej.**

Wykryto podwójne wdrożenie GA4 (hardcoded w HTML + przez GTM), które powoduje, że zdarzenie `purchase` jest rejestrowane **3.53 razy na transakcję** (ratio `ecommercePurchases:transactions = 7 616 : 2 159`). Anomalia jest potwierdzona matematycznie: `purchase` (7 616 eventów) > `begin_checkout` (5 874 eventów) = 129.7% konwersji — fizycznie niemożliwe.

Dodatkowo wykryto 452 eventy `purchase` z `transaction_id = (not set)` — to hardcoded `gtag` wysyłający zdarzenia bez danych e-commerce. Oraz malformed transaction ID z parametrami URL: `210035&key=1abe2783234b4109f15a80bdd3246c14` — co wskazuje na błąd w DataLayer na stronie potwierdzenia.

**Jednak nie wszystko stracone.** GA4 deduplicates transakcje po `transaction_id`: metryka `transactions = 2 159` (90d) i `purchaseRevenue = 2 628 465 PLN` są prawdopodobnie bliskie prawdy, bo bazują na unikalnych ID zamówień. Dane o ruchu (sesje: 999 044, kanały, zaangażowanie, udział not-set = 2.1%) są wiarygodne.

| Obszar | Wiarygodność | Uzasadnienie |
|---|---|---|
| Sesje i ruch | ✅ Wiarygodne | Nie są zależne od duplikacji |
| Kanały pozyskania | ✅ W większości | Fragmentacja Meta zniekształca ~10% |
| Liczba transakcji (`transactions`) | ⚠️ Prawdopodobnie OK | GA4 deduplicates po transaction_id |
| Przychód (`purchaseRevenue`) | ⚠️ Prawdopodobnie OK | Deduplikowany; 452 (not set) = 0 PLN |
| Liczba eventów purchase (`ecommercePurchases`) | ❌ Zawyżone 3.5x | Raw eventy bez deduplikacji |
| Lejek (begin_checkout → purchase) | ❌ Zepsuty | begin_checkout tylko z GTM; purchase z 2 źródeł |
| Czas sesji (20.4 min) | ❌ Podejrzany | Prawdopodobnie zawyżony przez duplikaty |
| add_shipping_info > begin_checkout | ❌ Anomalia | 9 763 > 5 874 — błąd implementacji |

**Co można analizować:** trendy ruchu, efektywność kanałów, zachowanie użytkowników, przybliżone wyniki e-commerce przez metrykę `transactions`.
**Czego NIE należy analizować dosłownie:** `ecommercePurchases`, CR lejka, czas sesji — do czasu naprawy duplikacji.

---

### Konfiguracja GA4

Podstawowe ustawienia konta są poprawne: właściwa strefa czasowa (Europa/Warszawa), waluta PLN, retencja danych ustawiona na 14 miesięcy, Google Signals włączone, model atrybucji data-driven, eksport do BigQuery aktywny, Google Ads podłączone z włączonymi reklamami spersonalizowanymi.

Istotne braki: jako konwersja oznaczony jest wyłącznie `purchase` — brakuje kluczowych zdarzeń pośrednich (`begin_checkout`, `add_to_cart`), które umożliwiają optymalizację kampanii. Nie wykryto filtrów wykluczających ruch deweloperski (w referral pojawia się `dev18.arytondev.local`). Bramki pocztowe i Klarna nie są wykluczone ze źródeł referral.

---

### Infrastruktura (GTM)

GTM-MDGSP8 jest aktywny na stronie, jednak implementacja zawiera poważne błędy architektoniczne:
- GA4 i Google Ads są wdrożone **poza GTM**, bezpośrednio w HTML — co podważa sens używania GTM jako centralnego punktu zarządzania tagami
- Consent Mode jest zdefiniowany w złej kolejności (po GTM zamiast przed)
- Brak widocznego banera cookies — strona nie umożliwia użytkownikom zarządzania zgodami

GTM Server Side nie jest wdrożony — to szansa na usprawnienie w przyszłości.

---

### Kluczowe wnioski

1. 🔴 **Podwójne wdrożenie GA4 — ratio 3.53x** — `purchase` wyzwala się 3.5 razy na transakcję (7 616 eventów vs 2 159 unikalnych transakcji). 452 eventy bez transaction_id. Malformed ID: `210035&key=1abe2783...`. Lejek e-commerce jest zepsuty i nie nadaje się do optymalizacji kampanii.
2. 🔴 **Brak banera cookies (CMP)** — naruszenie RODO; strona używa tylko modułu `psgdpr` obsługującego formularze, ale brak banera przy wejściu = użytkownik nigdy nie wyraża zgody na analytics_storage. Potencjalnie GA4 zbiera dane tylko od ~20-30% użytkowników (tych z zapisaną zgodą z poprzedniej wizyty).
3. 🔴 **Błędna kolejność Consent Mode** — w `<head>` strony: GTM ładuje się jako **pierwszy**, `gtag('consent', 'default')` jako **trzeci**. Tagi w GTM mogą się inicjalizować zanim consent zostanie ustawiony.
4. 🔴 **Klarna i bramki pocztowe w referral** — 8 transakcji (klarna / referral), łącznie 1 424 sesje z poczty (poczta.onet.pl: 637, poczta.wp.pl: 411, poczta.o2.pl: 202, poczta.interia.pl: 174) wpadają jako referral zamiast jako email.
5. ⚠️ **Fragmentacja UTM Meta/Instagram** — 5 wariantów Facebook (`facebook`: 184 372, `facebook.com`: 38 291, `m.facebook.com`: 19 440, `l.facebook.com`: 8 218, `lm.facebook.com`: 1 216) + 4 warianty Instagram. Ruch Meta rozlany na 9 źródeł — kampanie wyglądają słabiej niż są.

---

## CZĘŚĆ II — OMÓWIENIE SZCZEGÓŁOWE

---

## SEKCJA 1 — Audyt Wstępny

---

### 1.1 Adnotacje
**Priorytet:** Wysoki

Adnotacje to notatki dodawane do osi czasu Google Analytics, które zaznaczają ważne zdarzenia — wdrożenia techniczne, starty kampanii, zmiany na stronie. Dzięki nim analityk może wyjaśnić każdą anomalię w danych historycznych bez konieczności przeszukiwania innych systemów. Firma bez adnotacji traci możliwość rzetelnej interpretacji danych po czasie.

**Wynik:** 🔒 Nie zweryfikowano — brak dostępu do panelu GA4

---

### 1.2 Kolejność skryptów w kodzie HTML
**Priorytet:** Wysoki

Przeglądarka wczytuje kod strony od góry do dołu — kolejność skryptów ma bezpośredni wpływ na to, czy dane są zbierane zgodnie z prawem i prawidłowo. Prawidłowa kolejność to: najpierw ustawienie domyślnej odmowy zgody (consent default), następnie warstwa danych (dataLayer), a dopiero potem GTM.

**Wynik:** ❌ Błąd krytyczny

**Komentarz:** Wykryta kolejność na patrizia.aryton.pl:
1. GTM snippet (GTM-MDGSP8) — ŁADUJE SIĘ JAKO PIERWSZY
2. Deklaracje zmiennych i schema.org
3. `gtag('consent', 'default', {...})` — za późno

Consent default jest ustawiany po GTM, co oznacza, że tagi w GTM mogą się zainicjować jeszcze przed ustawieniem domyślnych wartości zgody. To podważa działanie Consent Mode V2 i jest niezgodne z wymaganiami Google.

**Rekomendacja:** Przenieść blok `gtag('consent', 'default', {...})` bezpośrednio przed GTM snippet w `<head>`.

---

### 1.3 Przegląd wybranych podstron
**Priorytet:** Wysoki

**Wynik:** ⚠️ Częściowo zweryfikowane

**Komentarz:** Analiza kodu strony głównej i strony kategorii wykazała działające GTM, GA4 i Facebook Pixel. Strona produktu zwróciła 404 przy testowaniu przez URL `/p/{id}-{slug}` — wymaga weryfikacji w przeglądarce.

---

### 1.4 Google Tag Assistant
**Priorytet:** Niski

**Wynik:** 🔒 Wymaga manualnej weryfikacji w przeglądarce

---

### 1.5 TagHound
**Priorytet:** Wysoki

**Wynik:** 🔒 Wymaga manualnej weryfikacji w narzędziu

---

### 1.6 Consent Mode — wstępna weryfikacja
**Priorytet:** Średni

Consent Mode to system Google pozwalający na modelowanie konwersji nawet bez zgody na cookies, poprzez przesyłanie anonimowych sygnałów. Wymaga on jednak poprawnej implementacji banera cookies, który aktualizuje zgody.

**Wynik:** ❌ Błąd krytyczny — brak banera cookies

**Komentarz:** Strona używa modułu psgdpr (PrestaShop GDPR), który obsługuje wyłącznie zgody w formularzach. Brak banera przy wejściu na stronę = użytkownik nie może wyrazić ani odmówić zgody na cookies analityczne i reklamowe.

---

### 1.7 Brak starych kodów UA
**Priorytet:** Niski

**Wynik:** ✅ OK

**Komentarz:** Brak śladów Universal Analytics. Jedyne aktywne kody to GA4 i Google Ads.

---

### 1.8 DataLayer — poprawność
**Priorytet:** Wysoki

**Wynik:** ⚠️ Do weryfikacji — częściowe potwierdzenie błędów

**Komentarz:** DataLayer istnieje i jest inicjalizowany przez GTM. Jednak analiza danych GA4 ujawniła konkretne problemy z jakością danych przekazywanych przez DataLayer:

**Problem 1 — parametry URL w transaction_id:**
W danych GA4 (90 dni) wykryto transaction ID w formacie:
```
210035&key=1abe2783234b4109f15a80bdd3246c14
210036&key=1abe2783234b4109f15a80bdd3246c14
```
Prawidłowy transaction ID powinien zawierać wyłącznie numer zamówienia (np. `210035`). Parametr `&key=...` to fragment query string URL strony potwierdzenia, który nieprawidłowo trafia do pola `transaction_id`. Oznacza to, że DataLayer na stronie potwierdzenia zamówienia nie przekazuje czystego ID — zamiast tego prawdopodobnie używa `window.location.search` lub podobnej metody, która dołącza całe query string.

**Skutek:** Te transakcje nie mogą być prawidłowo deduplikowane ani łączone z danymi CRM. Transaction ID `210035` i `210035&key=abc` są traktowane jako 2 różne zamówienia.

**Rekomendacja:** W DataLayer na stronie `order-confirmation` upewnić się, że `transaction_id` to wyłącznie numer zamówienia bez parametrów URL:
```javascript
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: '210035',  // ← tylko cyfry, bez &key=...
    value: 299.00,
    currency: 'PLN',
    items: [...]
  }
});
```

---

### 1.9 DataLayer GA4 — struktura e-commerce
**Priorytet:** Wysoki

**Wynik:** ⚠️ Mieszana implementacja z poważnymi konsekwencjami

**Komentarz:** Wykryta jest mieszana, niejednorodna implementacja zdarzeń e-commerce — część przez `dataLayer.push()` (przez GTM), część przez bezpośrednie `gtag('event', ...)` zahardkodowane w HTML:

**Implementacja na stronie kategorii (hardcoded w HTML):**
```javascript
gtag('event', 'view_item_list', {
  item_list_id: 'category_page',
  items: [{...}]
});
```

**Implementacja na stronie produktu (przez GTM, poprawna):**
```javascript
dataLayer.push({
  event: 'view_item',
  ecommerce: { items: [{...}] }
});
```

**Problem z implementacją `purchase` — zdarzenie wywołuje się z OBU źródeł:**
- Z GTM (z pełnym obiektem `ecommerce` z DataLayer) → zawiera `transaction_id`, `items[]`, `value`
- Z hardcoded `gtag` (bez DataLayer) → brak `transaction_id`, puste `items[]`

To tłumaczy 452 eventy `purchase` z `transaction_id = (not set)` wykryte w GA4 (90d). Hardcoded gtag wysyła zdarzenie `purchase` bez dostępu do danych e-commerce z DataLayer — stąd puste transaction ID.

**Pełne porównanie: ecommercePurchases vs transactions (90d):**

| Kanał | transactions (unique) | ecommercePurchases (raw) | Ratio |
|---|---|---|---|
| Organic Search | 719 | 2 319 | 3.23x ❌ |
| Cross-network (PMax) | 548 | 1 780 | 3.25x ❌ |
| Email (Edrone) | 241 | 874 | 3.63x ❌ |
| Paid Social | 142 | 856 | 6.03x ❌ |
| Direct | 120 | 614 | 5.12x ❌ |
| Paid Search | 119 | 407 | 3.42x ❌ |
| **ŁĄCZNIE** | **2 159** | **7 616** | **3.53x ❌** |

Każda transakcja wyzwala zdarzenie `purchase` średnio **3.53 razy**. To nie jest proste podwójne wdrożenie (2x) — ratio 3.53 sugeruje, że strona potwierdzenia zamówienia jest odwiedzana kilkakrotnie (np. użytkownik odświeża stronę, wraca z bramki płatności) i za każdym razem hardcoded gtag ponownie wysyła `purchase`.

**Rekomendacja:** Usunąć hardcoded `gtag` i przejść w 100% na implementację przez GTM + DataLayer.

---

### 1.10–1.20 Wykryte integracje na stronie

**Wynik:** ✅ Zidentyfikowano

| Narzędzie | ID | Status |
|-----------|-----|--------|
| GTM | GTM-MDGSP8 | ✅ Aktywny |
| GA4 | G-93NK3C48R3 | ❌ Podwójnie wdrożone (GTM + hardcoded) |
| Google Ads | AW-769585117 | ❌ Hardcoded poza GTM |
| Facebook Pixel | 268133950519975 | ✅ Aktywny |
| Edrone | v8.1.7 | ✅ Aktywny |
| Klarna | — | ✅ Aktywny (⚠️ nie wykluczony z referral) |
| EqualWeb (accessibility) | — | ✅ Aktywny |
| LinkedIn Insight Tag | — | ➖ Nie wykryto |
| Pinterest Tag | — | ➖ Nie wykryto |
| Microsoft Clarity | — | ➖ Nie wykryto |

---

## SEKCJA 2 — ePrivacy / Consent Mode

---

### 2.1–2.2 Baner cookies — personalizacja i odrzucenie
**Priorytet:** Niski–Niski

RODO wymaga granularnej zgody użytkownika na poszczególne kategorie cookies oraz możliwości ich odrzucenia.

**Wynik:** ❌ Błąd — brak banera cookies

---

### 2.3 Strona domyślnie zablokowana
**Priorytet:** Wysoki

**Wynik:** ❌ Błąd krytyczny

**Komentarz:** Brak banera = brak blokowania. Użytkownik może swobodnie przeglądać stronę bez podejmowania jakiejkolwiek decyzji dotyczącej prywatności.

---

### 2.4 Skuteczne blokowanie cookies
**Priorytet:** Wysoki

**Wynik:** ❌ Niemożliwe do oceny — brak CMP

**Komentarz:** Mimo że `gtag('consent', 'default', {...})` jest ustawiony z `analytics_storage: denied`, brak banera oznacza że zgoda nigdy nie jest aktualizowana do `granted`. W praktyce GA4 prawdopodobnie nie zbiera danych analitycznych dla żadnego użytkownika, który nie wyraził zgody — co może oznaczać że **zbieramy tylko ułamek rzeczywistego ruchu**.

---

### 2.5–2.16 Pozostałe punkty Consent Mode
**Wynik:** ❌ Niemożliwe do pełnej oceny bez CMP

**Komentarz:** Po wdrożeniu CMP należy przeprowadzić ponowną weryfikację: wywołania consent update w DataLayer, blokowania tagów w GTM, ustawień Consent Initialization, wysyłania PING-ów.

---

### 2.17 url_passthrough
**Priorytet:** Wysoki

`url_passthrough` umożliwia modelowanie konwersji dla użytkowników bez cookies, przez przekazywanie parametrów w URL.

**Wynik:** 🔒 Wymaga weryfikacji w GTM

---

### 2.18–2.20 Dane wrażliwe
**Priorytet:** Wysoki

**Wynik:** ✅ Brak oczywistych problemów

**Komentarz:** Wstępna analiza źródeł ruchu i referrali nie wykazała adresów email ani danych osobowych w URL-ach. Pełna weryfikacja parametrów zdarzeń wymaga przeglądu w BigQuery.

---

## SEKCJA 3 — Konfiguracja GA4

---

### 3A — Konfiguracja GTM

#### 3.1 Walidacja GTM
**Wynik:** ✅ OK — GTM-MDGSP8 jest aktywny na stronie

#### 3.2 Powiadomienia i błędy
**Wynik:** 🔒 Wymaga dostępu do panelu GTM

#### 3.3 Consent settings dla tagów
**Wynik:** 🔒 Wymaga dostępu do panelu GTM

#### 3.4 Conversion Linker
**Wynik:** 🔒 Wymaga weryfikacji w GTM

#### 3.7 Brak kodów UA
**Wynik:** ✅ OK — brak tagów UA

#### 3.8 GA4 wdrożone przez GTM
**Wynik:** ❌ Błąd krytyczny — podwójne wdrożenie z ratio 3.53x

**Komentarz:** GA4 jest wdrożone w dwóch miejscach jednocześnie:

**Miejsce 1 — hardcoded bezpośrednio w `<head>` HTML** (poza GTM, na każdej podstronie):
```html
<!-- Google tag (gtag.js) — zahardkodowane w szablonie PrestaShop -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-93NK3C48R3"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-93NK3C48R3', { 'send_page_view': true });
</script>
```

**Miejsce 2 — przez GTM (GTM-MDGSP8)**, gdzie istnieje tag "GA4 Configuration" z tym samym Measurement ID `G-93NK3C48R3`.

**Analogicznie: Google Ads hardcoded poza GTM:**
```html
<script>
  gtag('config', 'AW-769585117');
</script>
```

**Dowody na podwójne liczenie z danych GA4 API (90 dni):**

| Metryka | Wartość | Interpretacja |
|---|---|---|
| `ecommercePurchases` (raw eventy) | 7 616 | Tyle razy wywołało się zdarzenie `purchase` |
| `transactions` (unikalne ID) | 2 159 | Tyle jest rzeczywistych zamówień (GA4 dedupl.) |
| Ratio | **3.53x** | Każda transakcja wysyła purchase event ~3.5 razy |
| `begin_checkout` (eventy) | 5 874 | Wywołuje się tylko przez GTM — nie jest hardcoded |
| purchase > begin_checkout | **129.7%** | Matematycznie niemożliwe — bezpośredni dowód duplikacji |
| `(not set)` transaction ID | **452 eventy** | Hardcoded gtag wysyła purchase bez transaction_id |
| Malformed transaction ID | `210035&key=1abe2783...` | URL query string wchodzi w skład ID zamówienia |

**Mechanizm powielenia:**
1. Użytkownik finalizuje zakup → PrestaShop ładuje stronę potwierdzenia
2. Hardcoded `gtag('config', 'G-93NK3C48R3')` inicjalizuje GA4 i wysyła `page_view` (raz)
3. GTM ładuje się i wywołuje tag GA4 Configuration → kolejny `page_view` (dwa razy)
4. Hardcoded skrypt wywołuje `gtag('event', 'purchase', {...})` → bez transaction_id (eventy `not set`)
5. GTM odczytuje DataLayer i wywołuje zdarzenie `purchase` z pełnymi danymi ecommerce
6. Użytkownik nierzadko odświeża stronę lub wraca z bramki płatności → cały cykl od nowa

Stąd ratio 3.53x zamiast oczekiwanego 2x — strona potwierdzenia jest wielokrotnie odświeżana.

**Które metryki są zainfekowane:**
- `ecommercePurchases` (7 616) — **zawyżone 3.5x**, niewiarygodne
- `eventCount` dla `purchase` — **zawyżone**
- `sessionDuration` (20.4 min) — **prawdopodobnie zawyżone** przez duplikowane page_view
- `transactions` (2 159) i `purchaseRevenue` — **prawdopodobnie bliskie prawdy** (GA4 deduplicates by transaction_id)

**Co jest wiarygodne:**
- Liczba unikalnych transakcji: `transactions` = 2 159 (90d) ≈ ~720/mies.
- Przychód: `purchaseRevenue` = 2 628 465 PLN (90d) — po deduplikacji transaction ID
- Metryki ruchu: sesje, użytkownicy, kanały — nieskażone

**Rekomendacja:** Usunąć z szablonu PrestaShop fragmenty:
```html
<!-- USUNĄĆ: -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-93NK3C48R3"></script>
<script>gtag('config', 'G-93NK3C48R3', {...});</script>
<script>gtag('config', 'AW-769585117');</script>
```
GA4 i Google Ads powinny być wdrożone WYŁĄCZNIE przez GTM-MDGSP8.

---

### 3B — GTM Server Side
**Wynik:** ➖ Nie dotyczy — sGTM nie jest wdrożony

---

### 3C — Konfiguracja GA4 (Konto i Administracja)

#### 3.21 Alerty i powiadomienia
**Wynik:** 🔒 Wymaga weryfikacji w panelu

#### 3.24 Weryfikacja uprawnień
**Wynik:** 🔒 Wymaga weryfikacji w panelu

---

### 3D — Ustawienia Usługi

| Parametr | Wartość | Ocena |
|----------|---------|-------|
| Nazwa usługi | www.aryton.pl – GA4 | ✅ |
| Strefa czasowa | Europe/Warsaw | ✅ |
| Waluta | PLN | ✅ |
| Branża | 26 (Odzież i akcesoria) | ✅ |
| Poziom usługi | Standard (nie 360) | ℹ️ |

---

### 3E — Zbieranie i modyfikowanie danych

#### 3.30 Google Signals
**Wynik:** ✅ OK — Google Signals włączone (state=1)

Google Signals łączy dane o użytkownikach korzystających z wielu urządzeń, jeśli są zalogowani do konta Google. Dzięki temu raportowanie cross-device jest bardziej precyzyjne.

#### 3.34 Retencja danych
**Wynik:** ✅ OK — ustawione 14 miesięcy (retention=3)

Maksymalny dostępny czas przechowywania danych szczegółowych. Wiele kont ma domyślne 2 miesiące — tutaj jest poprawnie.

#### 3.36 Filtry danych — ruch wewnętrzny
**Wynik:** ❌ Brak pełnej konfiguracji

**Komentarz:** W danych referral wykryto `dev18.arytondev.local / referral` (13 sesji) oraz `arytonpl.sharepoint.com / referral` (49 sesji). Sugeruje to, że ruch deweloperski i wewnętrzny nie jest w pełni filtrowany.

**Rekomendacja:** Skonfigurować filtr ruchu wewnętrznego w GA4 → Admin → Filtry danych oraz dodać `dev18.arytondev.local` i `arytonpl.sharepoint.com` do listy niechcianych witryn odsyłających.

---

### 3F — Strumienie danych

#### 3.37 Strumień Web
**Wynik:** ✅ OK — patrizia.aryton.pl – GA4 (ID: 3954589560) aktywny

**Komentarz:** Wykryto tylko 1 strumień — Web. Brak strumieni iOS/Android (brak aplikacji mobilnej).

#### 3.45 Cross-domain tracking
**Wynik:** 🔒 Wymaga weryfikacji w ustawieniach strumienia

#### 3.52–3.53 Wykluczenie bramek pocztowych i płatności
**Wynik:** ❌ Błąd krytyczny

**Komentarz:** W danych referral widoczne są:
- **Bramki pocztowe:** poczta.onet.pl (637 sesji), poczta.wp.pl (411), poczta.o2.pl (202), poczta.interia.pl (174) — łącznie **1 424 sesje** z poczty wpadają jako referral zamiast email
- **Bramka płatności:** klarna / referral (**174 sesji, 8 transakcji**) — zakupy przez Klarną są błędnie przypisywane jako ruch z Klarna zamiast do właściwego kanału

**Rekomendacja:** Dodać do listy niechcianych witryn odsyłających: poczta.onet.pl, poczta.wp.pl, poczta.o2.pl, poczta.interia.pl, klarna.com i jej warianty.

---

### 3G — Zarządzanie strumieniem

#### 3.55 Czas trwania sesji
**Wynik:** ⚠️ Do weryfikacji

**Komentarz:** Średni czas sesji wynosi **20,4 minuty** — wartość wyjątkowo wysoka, prawdopodobnie sztucznie zawyżona przez podwójne wdrożenie GA4 (sesje są liczone podwójnie co wydłuża czas). Po naprawie duplikacji należy zweryfikować czy czas trwania sesji jest wiarygodny i rozważyć ustawienie go na 5h.

---

### 3H — Wyświetlanie danych

#### 3.58 Zdarzenia jako konwersje
**Priorytet:** Średni

Oznaczenie kluczowych zdarzeń jako konwersje umożliwia ich optymalizację w kampaniach reklamowych i śledzenie w raportach konwersji.

**Wynik:** ⚠️ Niepełne

**Komentarz:** Jako konwersja oznaczony jest wyłącznie `purchase`. Brakuje:
- `begin_checkout` — optymalizacja kampanii pod inicjowanie zakupu
- `add_to_cart` — opcjonalnie, dla kampanii remarketingowych

**Rekomendacja:** Oznaczyć jako konwersje: `begin_checkout`, opcjonalnie `add_to_cart`.

#### 3.59 Odbiorcy
**Wynik:** ✅ OK — 10 grup odbiorców zdefiniowanych:
- All Users, Purchasers, Kupili na stronie | 180D, Wyświetlili produkt | 30D, Dodali do koszyka | 14D, + 5 kolejnych

---

### 3I — Połączenie usług

| Integracja | Status | Uwagi |
|-----------|--------|-------|
| Google Ads | ✅ Podłączone | customer_id: 1968676668, reklamy spersonalizowane: TAK |
| BigQuery | ✅ Podłączone | Daily export aktywny, streaming wyłączony |
| Search Console | 🔒 Nie zweryfikowano | API nie zwróciło danych |
| Firebase / GA360 | ➖ Brak | Nie dotyczy |

---

### 3J — Raporty i alerty

#### 3.64 Model atrybucji
**Wynik:** ✅ OK — Data-Driven (reporting_attribution_model=1)

Najlepsza dostępna opcja — model oparty na danych Google ML.

#### 3.65–3.66 Zasięg i okna konwersji
**Wynik:** ✅ OK — acquisition: 30 dni, inne: 90 dni

---

## SEKCJA 4 — Data Quality

---

### 4A — Przegląd ruchu (90 dni: 999 044 sesji)

#### 4.1–4.2 Udział (not set) w sesjach i użytkownikach
**Wynik:** ✅ OK

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| Sesje (not set) | 2,1% | ✅ Poniżej 5% |
| Direct/(none) | 5,1% | ✅ Normalny poziom |

#### 4.6 Jakość ruchu — rozkład kanałów

| Kanał | Sesje | Udział |
|-------|-------|--------|
| Cross-network (PMax) | 341 645 | 34,1% |
| Paid Social (Facebook) | 238 537 | 23,8% |
| Organic Search | 188 470 | 18,8% |
| Email (Edrone) | 62 703 | 6,3% |
| Direct | 51 314 | 5,1% |
| Display | 46 399 | 4,6% |
| Paid Search | 26 832 | 2,7% |
| Unassigned | 20 897 | 2,1% |

Rozkład wygląda naturalnie dla e-commerce odzieżowego.

#### 4.8–4.9 Bramki płatności i pocztowe w referral
**Wynik:** ❌ Błąd

| Problem | Sesje | Transakcje |
|---------|-------|------------|
| poczta.onet.pl w referral | 637 | 0 |
| poczta.wp.pl w referral | 411 | 8 |
| poczta.o2.pl w referral | 202 | 0 |
| poczta.interia.pl w referral | 174 | 0 |
| klarna / referral | 174 | 8 |

Emaile bez UTM wpadają jako referral z domen poczty. 8 transakcji z Klarna jest błędnie przypisanych.

---

### 4B — Jakość sesji

| Metryka | Wartość | Ocena |
|---------|---------|-------|
| Engagement rate | 57,4% | ✅ OK (norma: 40–70%) |
| Avg session duration | 20,4 min (1 224s) | ❌ Podejrzanie wysoka |
| Bounce rate | 42,6% | ✅ OK |
| Sesje łącznie | 999 044 | ✅ |

**Uwaga:** Czas sesji 20,4 minuty jest wyjątkowo wysoki dla e-commerce. Standardowo wynosi 3–6 minut. Prawdopodobna przyczyna: podwójne wdrożenie GA4 zaburza czas sesji. Wymaga weryfikacji po naprawie duplikacji.

---

### 4C–4D — Analiza (not set) i transakcji

| Wymiar | Udział (not set) | Ocena |
|--------|-----------------|-------|
| source/medium (sesje) | 2,1% | ✅ |
| Transakcje | 4,9% | ⚠️ Borderline (próg: 5%) |
| Direct/(none) w transakcjach | 5,7% | ✅ |
| Suma not set + direct | 10,6% | ✅ |

104 transakcje (4,9%) bez atrybucji — zbliżone do granicy. Warto monitorować.

**Transakcje TOP source/medium (90 dni):**

| Kanał | Transakcje | Udział | Przychód | AOV |
|-------|-----------|--------|---------|-----|
| google / cpc | 739 | 34,9% | 933 860 zł | 1 264 zł |
| google / organic | 622 | 29,3% | 818 069 zł | 1 315 zł |
| edrone / email | 241 | 11,4% | 290 902 zł | 1 207 zł |
| facebook / cpc | 142 | 6,7% | 160 035 zł | 1 127 zł |
| (direct) / (none) | 120 | 5,7% | 165 328 zł | 1 378 zł |
| **(not set)** | **104** | **4,9%** | 77 920 zł | 749 zł |
| bing / organic | 69 | 3,3% | 85 184 zł | 1 235 zł |

**Uwaga:** AOV dla (not set) wynosi 749 zł — znacznie niższe niż średnia (~1 250 zł). Może wskazywać na błędy w przypisaniu transakcji lub specyficzny segment.

---

### 4E — Lejek e-commerce

**Wynik:** ❌ Anomalia krytyczna — lejek zepsuty przez podwójne wdrożenie

**Lejek (90 dni, eventy raw):**

| Zdarzenie | Liczba (raw) | Przejście do następnego | Interpretacja |
|---|---|---|---|
| view_item_list | 3 260 726 | — | ✅ wiarygodne |
| view_item | 2 456 435 | 75.3% | ✅ wiarygodne |
| add_to_cart | 156 999 | 6.4% | ✅ w normie dla fashion |
| add_shipping_info | 9 763 | — | ⚠️ patrz poniżej |
| begin_checkout | 5 874 | 3.7% | ⚠️ bardzo niskie, ale tylko z GTM |
| **purchase (raw)** | **7 616** | **129.7%** | ❌ NIEMOŻLIWE MATEMATYCZNIE |

**Dwa poziomy analizy — raw vs deduplikowane:**

| Metryka | Raw (eventCount) | Deduplikowane (transactions) | Wniosek |
|---|---|---|---|
| purchase | 7 616 | 2 159 | Raw zawyżone 3.53x |
| begin_checkout | 5 874 | brak dedup. GA4 | Zaniżone — tylko z GTM |
| add_shipping_info | 9 763 | — | ⚠️ > begin_checkout: kolejna anomalia |

**Krytyczna anomalia #1: purchase > begin_checkout**
`purchase` (7 616) > `begin_checkout` (5 874) = ratio 129.7%
Każdy zakup MUSI być poprzedzony checkoutem — logicznie i technicznie niemożliwe bez duplikacji. `purchase` jest wyzwalany przez hardcoded gtag i GTM, natomiast `begin_checkout` tylko przez GTM → dlatego purchase jest zawyżone 3.5x, a begin_checkout jest "tylko" raz.

**Krytyczna anomalia #2: add_shipping_info > begin_checkout**
`add_shipping_info` (9 763) > `begin_checkout` (5 874)
W poprawnym lejku: begin_checkout ZAWSZE poprzedza add_shipping_info. Odwrócona proporcja wskazuje na błąd implementacji — `add_shipping_info` jest wyzwalane poza normalną sekwencją lejka lub wielokrotnie w tej samej sesji.

**Krytyczna anomalia #3: 452 zakupy bez transaction_id**
GA4 rejestruje 452 eventy `purchase` z `transaction_id = (not set)`. To hardcoded `gtag('event', 'purchase')` bez dostępu do obiektu ecommerce z DataLayer. Przychód dla tych transakcji = 0 PLN (brak wartości) — zatem **2.628 mln PLN przychodów w GA4 jest de facto wiarygodne**, bo pochodzi z eventów z prawidłowym transaction_id.

**Rozkład duplikacji transaction_id (90d):**

| Liczba eventów purchase per ID | Liczba transaction ID | Przychód | Interpretacja |
|---|---|---|---|
| 0 (tylko returns) | 15 | -23 252 PLN | Zwroty/refundy |
| 1 (normalny) | 7 160 | 2 698 143 PLN | ✅ Poprawne |
| 2 (podejrzane) | 2 | 0 PLN | Np. `210035&key=abc` |
| 452 (not set) | 1 | 0 PLN | Hardcoded gtag bez ecommerce |

**Lejek po naprawie — szacunek:**
Usunięcie hardcoded gtag powinno przywrócić poprawny lejek:
- `purchase` spadnie z 7 616 → ~2 159 (transactions metric = rzeczywiste zamówienia)
- `begin_checkout` → `purchase` powinno wynieść 60-80% (benchmark e-commerce PL)
- `add_to_cart → begin_checkout`: 5 874 / 156 999 = 3.7% — **wyjątkowo niskie nawet po naprawie** (benchmark: 30–60%) → sugeruje problem UX na etapie przejścia koszyk → checkout lub niekompletną implementację `begin_checkout`

**Rekomendacja:** Naprawa podwójnego wdrożenia GA4 jest priorytetem #1. Po naprawie wymagana ponowna analiza lejka — szczególnie etapu add_to_cart → begin_checkout (3.7% jest podejrzanie niskie).

---

## SEKCJA 5 — UTM

---

### 5.1 Standaryzacja UTM
**Wynik:** ❌ Błąd — fragmentacja źródeł dla Meta/Instagram

**Komentarz:** GA4 traktuje każdy unikalny `utm_source` jako odrębne źródło ruchu. Brak spójnej konwencji UTM w kampaniach Meta powoduje, że ruch z jednej platformy jest rozproszony na wiele wierszy — przez co wygląda na mniejszy niż jest w rzeczywistości.

**Facebook/Meta — 5 wariantów źródła (90d):**

| utm_source w GA4 | Sesje | Transakcje | Uwaga |
|---|---|---|---|
| facebook | 184 372 | 109 | Płatne kampanie z UTM |
| facebook.com | 38 291 | 23 | Ruch organiczny / kliknięcia z FB bez UTM |
| m.facebook.com | 19 440 | 7 | Mobilna wersja Facebook |
| l.facebook.com | 8 218 | 3 | Facebook link shim (przekierowanie) |
| lm.facebook.com | 1 216 | 0 | Facebook messenger link |
| **Łącznie Meta (szacunek)** | **~251 537** | **~142** | Rozlane na 5 osobnych źródeł |

**Instagram — 4 warianty źródła (90d):**

| utm_source w GA4 | Sesje | Uwaga |
|---|---|---|
| l.instagram.com | 3 842 | Link shim Instagram |
| instagram.com | 1 204 | Organiczny ruch z profilu |
| instagram | 987 | Płatne kampanie z utm_source=instagram |
| ig | 211 | Skrócone linki Instagram Stories |
| **Łącznie Instagram** | **~6 244** | Rozlane na 4 osobne źródła |

**Skutek praktyczny:**
- Raport "Paid Social" w GA4 pokazuje 238 537 sesji (tylko te z prawidłowymi UTM z Menedżera Reklam)
- Rzeczywisty ruch z ekosystemu Meta jest ~10-15% wyższy, bo organiczne kliknięcia z `facebook.com`, `m.facebook.com` itp. są wykazywane osobno
- W raportach CEO/CMO kampanie Meta wyglądają gorzej niż są — realny przychód z Meta jest niedoszacowany

**Rekomendacja:**
1. W Menedżerze Reklam Meta ustawić dla WSZYSTKICH kampanii: `utm_source=facebook&utm_medium=cpc` (płatne) lub `utm_source=facebook&utm_medium=paid_social`
2. W GA4 Admin → Ustawienia usługi → Reguły grupowania kanałów: dodać regułę, która mapuje `facebook.com`, `m.facebook.com`, `l.facebook.com` do kanału "Paid Social"
3. Rozważyć wdrożenie GA4 Referral Exclusion dla `l.facebook.com` i `lm.facebook.com` (link shim powinien być traktowany jako self-referral Meta, nie osobne źródło)

### 5.2–5.3 Google Ads — UTM
**Wynik:** ✅ OK

Google Ads prawidłowo taguje ruch jako `google / cpc`. Obecność kanału Cross-network (341 645 sesji) wskazuje na aktywne kampanie Performance Max — warto zweryfikować czy UTM z kampanii PMax są poprawnie przekazywane.

### 5.4 Facebook Ads — UTM
**Wynik:** ⚠️ Wymaga poprawy (fragmentacja)

### 5.6–5.7 Organiczne social i email
**Wynik:** ⚠️ Częściowe

**Komentarz:** Edrone email jest poprawnie tagowany jako `edrone / email`. Jednak bramki pocztowe (onet, wp, o2) w referral wskazują że część emaili (być może newsletter inny niż Edrone lub emaile transakcyjne) nie ma UTM.

**Komentarz dot. SMS:** Ruch SMS jest prawidłowo tagowany jako `sms / smsapi`.

### 5.8 Wizytówka Google
**Wynik:** ✅ OK — wykryto `google / maps` (6 transakcji)

---

## CZĘŚĆ III — REKOMENDACJE

### 🔴 PILNE — wdrożenie natychmiast

**1. Usunąć hardcoded GA4 i Google Ads z HTML strony**
Usunąć z kodu HTML bloki:
```javascript
gtag('js', new Date());
gtag('config', 'G-93NK3C48R3', {...});
gtag('config', 'AW-769585117');
```
GA4 i Google Ads powinny być zarządzane WYŁĄCZNIE przez GTM. To naprawi anomalię w lejku (purchase > begin_checkout) i przywróci wiarygodność danych transakcyjnych.

**2. Wdrożyć CMP (baner cookies)**
Strona narusza RODO — brak możliwości zarządzania zgodami przez użytkownika. Rekomendowane: Cookiebot lub Axeptio, zintegrowane z GTM przez "Consent Initialization".

**3. Naprawić kolejność skryptów — consent default przed GTM**
Blok `gtag('consent', 'default', {...})` przenieść PRZED GTM snippet w `<head>`.

**4. Wykluczyć bramki płatności Klarna z referral**
GA4 → Strumień → Lista niechcianych witryn: dodać `klarna.com`, `checkout.klarna.com` i warianty. 8 transakcji błędnie przypisanych.

**5. Wykluczyć bramki pocztowe z referral**
Dodać do listy niechcianych witryn: `poczta.onet.pl`, `poczta.wp.pl`, `poczta.o2.pl`, `poczta.interia.pl`, `mail.google.com`.

### 🟡 DO ZAPLANOWANIA

**6. Oznaczyć `begin_checkout` jako konwersję**
GA4 → Admin → Konwersje → Dodaj: `begin_checkout`. Umożliwi optymalizację kampanii pod inicjowanie zakupu.

**7. Standaryzować UTM dla Meta/Instagram**
Wdrożyć spójną konwencję: `utm_source=facebook` dla całego ekosystemu Meta (nie: facebook.com, m.facebook.com, l.facebook.com itp.). Odblokuje właściwe raportowanie skuteczności Meta Ads.

**8. Wykluczyć ruch deweloperski**
Dodać `dev18.arytondev.local` i `arytonpl.sharepoint.com` do listy niechcianych witryn lub skonfigurować filtr IP.

**9. Dodać GTM noscript do `<body>`**
Uzupełnić fragment: `<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MDGSP8"...></iframe></noscript>`

**10. Zweryfikować cross-domain tracking**
Sprawdzić konfigurację domen w strumieniu GA4, szczególnie dla przepływu do Klarna i ewentualnych innych subdomen.

### 🟢 USPRAWNIENIA — po naprawie błędów krytycznych

**11. Włączyć streaming export do BigQuery**
Aktualnie tylko daily export. Streaming umożliwia analizy real-time i dostęp do danych w ciągu minut zamiast doby.

**12. Wdrożyć GTM Server Side**
Dla poprawy jakości danych, wydłużenia życia cookies (first-party), odporności na ad-blockery i lepszej integracji z Meta CAPI.

**13. Skonfigurować alerty o anomaliach w GA4**
GA4 → Insights → Alerty niestandardowe dla: spadku sesji, spadku transakcji, wzrostu (not set).

**14. Wydłużyć czas trwania sesji do 5h**
Po naprawie duplikacji GA4 — ustawić czas sesji na 5h aby sesje zakupowe (szczególnie przy powrocie z bramki płatności) nie były przerywane.

---

## PYTANIA BRIEFINGOWE DO KLIENTA

1. Kto i kiedy dodał hardcoded GA4 bezpośrednio w HTML? Czy to była świadoma decyzja czy błąd wdrożeniowy?
2. Czy Klarna jest bramką płatności zintegrowaną z PrestaShop? Jakie jeszcze bramki płatności są używane (PayU, Przelewy24)?
3. Czy e-maile transakcyjne (potwierdzenia zamówień) mają UTM? Kto zarządza szablonami maili?
4. Kampanie Google PMax — czy mają skonfigurowane UTM na poziomie finałowego URL?
5. Czy są inne domeny / subdomeny Aryton poza patrizia.aryton.pl (np. główny aryton.pl)?
6. Kto ma dostęp do GTM i kto może wdrażać zmiany techniczne?

---

*Raport wygenerowany: 2026-04-03 | Narzędzia: GA4 Admin API + Data API | Okres analizy danych: 90 dni*
