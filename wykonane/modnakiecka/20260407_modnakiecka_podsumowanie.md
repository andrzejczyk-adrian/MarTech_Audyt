# Audyt MarTech — Podsumowanie dla Właściciela

**Klient:** modnakiecka.pl
**Data:** 07.04.2026 | **Okres analizy:** 8.03–7.04.2026 (30 dni)
**Audytor:** Adrian Andrzejczyk
**Typ biznesu:** Sklep internetowy — moda damska (Shoper)

---

## Wyniki ogólne

| Obszar | Wynik | Ocena |
|--------|-------|-------|
| 1. Infrastruktura — tagi i skrypty | 58% | ⚠️ Wymaga naprawy |
| 2. Zgodność z prawem (pliki cookies) | 100% sprawdz. | 🔒 Wymaga weryfikacji |
| 3. Konfiguracja systemu analitycznego | 28% | ❌ Krytyczny |
| 4. Jakość zbieranych danych | 97% | ✅ Bardzo dobra |
| 5. Oznaczenia kampanii marketingowych | 60% | ⚠️ Wymaga poprawy |
| 7. Lejki zakupowe | 63% | ⚠️ Wymaga poprawy |
| 9. Analiza efektywności reklam | 79% | ⚠️ Dobry z rezerwami |
| **ŁĄCZNIE** | **74%** | **⚠️ Wymaga poprawy** |

**Ocena ogólna:** Sklep ma solidną bazę danych i świetne wyniki retencji klientów (73% zakupów to powracające klientki), ale trzy techniczne problemy w systemie śledzenia zamówień powodują, że kampanie reklamowe uczą się na niepełnych lub błędnych danych — co bezpośrednio kosztuje pieniądze.

---

## Najważniejsze problemy (z wyceną)

### 🔴 Problem 1 — System dwukrotnie liczy te same zakupy

**Co się dzieje:** Na stronie działają jednocześnie dwa systemy zarządzania tagami — jeden zarządzany przez agencję, drugi automatycznie dodawany przez platformę Shoper. Oba rejestrują zakupy w tym samym momencie. Jeden zakup jest zliczany nawet **12 razy** w systemach reklamowych Facebook i Google (konkretnie: zamówienie nr 14564069 zarejestrowano 12-krotnie).

**Co to znaczy w praktyce:** Jeśli klientka kupi sukienkę za 430 PLN, Facebook "widzi" sprzedaż za 5 160 PLN (430 × 12). Algorytm reklamowy uczy się, że ta konkretna reklama przynosi ogromny przychód i przydziela jej większy budżet — na podstawie fałszywych danych. Kampanie są optymalizowane błędnie.

**Szacowany koszt:** Trudny do precyzyjnego obliczenia, ale błędna optymalizacja stawek reklamowych może oznaczać 10-20% nieefektywności budżetu reklamowego.

---

### 🔴 Problem 2 — System nie wie co zostało sprzedane

**Co się dzieje:** Google Analytics 4 wie ile sprzedano (31 090 zamówień, 6 842 880 PLN w 30 dniach) ale **nie wie jakie konkretne produkty zostały sprzedane**. Dane o zakupach trafiają do systemu bez informacji o artykułach. TOP 20 produktów wg wyświetleń — Beżowy Trencz (26 523 wyświetleń), komplety, sukienki eleganckie — wszystkie mają 0 zł przypisanego przychodu.

**Co to znaczy w praktyce:**
- Nie można sprawdzić które produkty się sprzedają najlepiej
- Nie można zoptymalizować reklam Google Shopping po produktach (system nie wie co kupują klientki po kliknięciu reklamy)
- Nie można wysyłać personalizowanych emaili przez SALESmanago z "produktami podobnymi do zakupionych"

**Szacowany koszt:** 6 842 880 PLN miesięcznego przychodu generowanego "w ciemno" — bez możliwości analizy co napędza sprzedaż.

---

### 🔴 Problem 3 — Możliwe niezliczanie ~45 000 zamówień miesięcznie

**Co się dzieje:** System Shopera rejestruje **76 136 złożonych zamówień** w 30 dniach, podczas gdy Google Analytics rejestruje **31 090 zakupów**. Różnica: ~45 000 zamówień miesięcznie.

**Pilna weryfikacja:** Sprawdź w panelu Shopera ile rzeczywistych zamówień zostało złożonych w tym samym okresie. Jeśli liczba zbliżona do 76 000 — Google Analytics nie śledzi połowy zakupów. To oznacza, że algorytmy reklamowe Google i Meta "widzą" tylko część konwersji i optymalizują kampanie na podstawie niepełnych danych.

**Szacowany koszt:** Jeśli potwierdzony: brakuje sygnałów konwersji dla ok. 45 000 zakupów × 220 PLN = ~9 900 000 PLN miesięcznie niezarejestrowanego przychodu w systemach reklamowych.

---

### ⚠️ Problem 4 — Strona mobilna konwertuje 2× gorzej niż wersja na komputer

**Co się dzieje:** 89% odwiedzin modnakiecka.pl pochodzi z telefonów (1,66 mln sesji miesięcznie). Jednak klientki na telefonach kupują 2,1× rzadziej niż na komputerach: na telefonie co 67. klientka finalizuje zakup (CR 1,5%), na komputerze co 31. (CR 3,2%).

**Efekt w liczbach:**
- Przychód z mobile: 5 252 254 PLN (77% całości) przy 89% ruchu
- Gdyby mobile konwertowało tak samo jak desktop: ~10 880 000 PLN (+5,6 mln PLN)
- Realistyczny cel: poprawa CR mobile o 0,5 punktu procentowego = **+1 749 000 PLN miesięcznie**

**Co może powodować ten problem:** Utrudniony proces płatności na telefonie, za małe przyciski "kup teraz", wolne ładowanie strony na mobile, lub problemy z formularzem kasy na ekranach dotykowych.

---

### ⚠️ Problem 5 — 87% dodanych do koszyka produktów nie jest kupowanych

**Co się dzieje:** W ciągu 30 dni 249 979 razy klientki dodały produkt do koszyka. Tylko 31 090 (12,4%) zakończyło zakupem. **218 889 koszyków zostało porzuconych.**

**Szansa:** Automatyczne przypomnienia emailowe przez SALESmanago do klientek, które dodały produkt do koszyka ale nie kupiły (po 1 godzinie, po 24h, po 72h). Przy odratowaniu zaledwie 5% porzuconych koszyków: +10 944 zamówień × 220 PLN = **+2 408 000 PLN miesięcznie**.

---

## Mocne strony — co działa dobrze

✅ **Silna baza stałych klientek:** 73% zakupów to powracające klientki. Wskaźnik lojalności na poziomie premium sklepu. To rzadkość i ogromna przewaga.

✅ **Bardzo dobra jakość danych:** 97% punktów za jakość danych analitycznych — dane są wiarygodne, brak fałszywego ruchu, prawidłowe numery zamówień.

✅ **Reklamy Google Search działają świetnie:** Płatne wyszukiwanie Google generuje 9,27 PLN przychodu na każdą sesję — 3,1× więcej niż reklamy na Facebooku (2,71 PLN/sesja).

✅ **Program afiliacyjny Wedare ma 24% współczynnik konwersji:** To wyjątkowo wysoki wynik. Klientki przychodzące przez partnerów Wedare kupują bardzo chętnie. Potencjał do skalowania tego kanału.

✅ **Wysoki poziom zaangażowania:** Klientki są aktywne — engagement rate powyżej 85% we wszystkich głównych kanałach.

---

## Plan działania

### 🔴 Natychmiast (ten tydzień)

| Działanie | Efekt |
|-----------|-------|
| **Sprawdź w panelu Shopera**: ile zamówień złożono w marcu–kwietniu — porównaj z 31 090 w GA4 | Ustal czy mamy problem z niezliczaniem zamówień |
| **Wyłącz duplikację tagów**: poproś agencję o wyłączenie tagów zakupowych w jednym z dwóch aktywnych systemów zarządzania tagami | Koniec fałszywych danych w reklamach Meta i Google |
| **Włącz automatyczne oznaczenia UTM w Meta Ads Manager** | Reklamy na Facebooku będą prawidłowo widoczne w GA4 zamiast jako "polecenia" |

### 🟡 W ciągu miesiąca

| Działanie | Efekt |
|-----------|-------|
| **Uruchom automatyczne emaile do porzuconych koszyków w SALESmanago** (3 wiadomości: 1h / 24h / 72h) | Szacunkowo **+2 408 000 PLN/msc** |
| **Nagrania sesji mobilnych**: wdrożyć narzędzie nagrające jak klientki poruszają się po stronie na telefonie — zidentyfikować gdzie rezygnują | Podstawa do naprawy mobile CR |
| **Naprawienie danych produktowych**: poproś agencję o naprawienie systemu tak, żeby każde zamówienie miało przypisane kupione produkty | Odblokuje optymalizację reklam i personalizację emaili |
| **Podłącz Google BigQuery** (bezpłatna baza danych Google) | Zaawansowane analizy, customer lifetime value, segmentacja RFM |

### 🟢 W ciągu 2-3 miesięcy

| Działanie | Efekt |
|-----------|-------|
| **Optymalizacja UX mobile** na podstawie nagrań sesji | Szacunkowo **+1 749 000 PLN/msc** przy poprawie CR o 0,5pp |
| **Przesunięcie budżetu Google Ads** z kampanii wyświetleniowych do Paid Search (9,27 vs 2,22 PLN/sesja) | Lepszy zwrot z tego samego budżetu |
| **Skalowanie programu afiliacjnego Wedare** (24% CR) | Wzrost z kanału o najwyższej konwersji |
| **Weryfikacja RODO / Consent Mode** z dostępem do GTM | Zgodność prawna, ochrona przed karami |

---

## Potencjał finansowy po naprawach

| Działanie | Szacunek PLN/msc | PLN/rok |
|-----------|-----------------|---------|
| Odratowanie porzuconych koszyków (email) | +2 408 000 PLN | +28 896 000 PLN |
| Poprawa CR mobile o 0,5pp | +1 749 000 PLN | +20 988 000 PLN |
| Poprawa checkout drop-off o 10pp | +1 796 000 PLN | +21 552 000 PLN |
| **ŁĄCZNIE (realistyczny)** | **+5 953 000 PLN** | **+71 436 000 PLN** |

> Powyższe szacunki są konserwatywne i zakładają częściową realizację potencjału. Warunkiem koniecznym jest najpierw naprawienie problemów technicznych z tagami (Problemy 1-3).

---

*Audyt przeprowadzony przez: Adrian Andrzejczyk | 07.04.2026*
*Pełna dokumentacja techniczna: `20260407_modnakiecka_audyt.md`*
