# Audyt MarTech v2 — Podsumowanie

**Klient:** Patrizia by Aryton (patrizia.aryton.pl)
**Data:** 2026-04-09 | **Okres analizy:** marzec–kwiecień 2026 vs marzec–kwiecień 2025
**Audytor:** Adrian Andrzejczyk
**Platforma:** PrestaShop | **GA4:** G-93NK3C48R3 | **Google Ads:** 196-867-6668

---

## Wyniki ogólne

| Obszar | Wynik | Ocena |
|--------|-------|-------|
| 1. Infrastruktura śledzenia | 28% | ❌ Krytyczny |
| 2. Zgodność z prawem (cookies) | 2% | ❌ Krytyczny |
| 3. Konfiguracja systemu analitycznego | 16% | ❌ Krytyczny |
| 4. Jakość danych | 40% | ❌ Krytyczny |
| 5. Oznaczenia ruchu (UTM) | 50% | ⚠️ Wymaga poprawy |
| 6–7. Produkty i lejki zakupowe | 25% | ❌ Krytyczny |
| 8. Połączenie GA4 ↔ Google Ads | 11% | ❌ Krytyczny |
| 9. Analiza wyników | 17% | ❌ Krytyczny |
| **ŁĄCZNIE** | **22%** | **❌ Krytyczny** |

**Ocena ogólna:** Sklep patrizia.aryton.pl stracił 71% sprzedaży rok do roku (z 1 856 701 PLN do 529 914 PLN miesięcznie) — nie z powodu złych produktów czy złych cen, ale z powodu zepsutych kampanii reklamowych, błędów technicznych w śledzeniu i degradacji doświadczenia na telefonach.

---

## Najważniejsze problemy (z wyceną)

---

**🔴 Problem 1 — Sklep stracił 71% sprzedaży rok do roku**

Rok temu (marzec-kwiecień 2025) sklep notował 1 495 zamówień miesięcznie za 1 857 tys. PLN. Dziś — 427 zamówień za 530 tys. PLN. Wartość średniego koszyka jest identyczna (1 241 PLN). Problem NIE leży w produktach ani cenach — leży w tym, że mniej osób trafia na stronę i mniejszy procent z nich kupuje.

**Strata: -1 326 787 PLN/miesiąc vs rok temu**

---

**🔴 Problem 2 — System nalicza błędnie zakupy — kampanie są "oślepione"**

Przy każdym zakupie system analityczny tworzy dwa zdarzenia zamiast jednego: jedno prawidłowe i jedno z błędnym numerem zamówienia (np. `210034` poprawnie ORAZ `210034&key=1abe2783...` błędnie). W ciągu miesiąca naliczono 1 105 takich błędnych zdarzeń. Oprócz tego, jeden ze skryptów śledzących uruchamia się bez danych o zakupie — generując 89 pustych zdarzeń.

Efekt: algorytm Google Ads "widzi" 1 610 zakupów zamiast 427 i na tej podstawie kieruje budżet. Optymalizuje kampanie na iluzoryczny sukces, tracąc realny budżet.

**Ten problem nie istniał w 2025** — pojawił się w 2026, prawdopodobnie przy aktualizacji strony.

**Czas naprawy: 2–4 godziny specjalisty GTM**

---

**🔴 Problem 3 — Reklamy Google Search praktycznie wyłączone (-92% ruchu)**

Rok temu kampanie Google Search przynosiły 58 884 wizyt miesięcznie. Dziś — 4 600. Skuteczność tych kampanii (procent osób, które po kliknięciu kupowały) pozostała identyczna. Problem jest wyłącznie w skali — dramatyczne zmniejszenie budżetu lub wyłączenie kampanii.

**Szacunkowa strata: ~201 000 PLN/miesiąc** (przy zachowaniu dotychczasowej skuteczności)

---

**⚠️ Problem 4 — Konwersja na telefonach spadła 3-krotnie**

Telefony stanowią 78% ruchu na stronie (260 tys. wizyt miesięcznie). Rok temu na 1 000 odwiedzających telefonem kupowało ~3 osoby. Dziś — niecała 1. Desktop też stracił, ale mniej (2.9 osoby na 1000 → 2.8). Tak duży spadek tylko na telefonach wskazuje, że coś konkretnie zmieniło się w wyglądzie lub działaniu strony na małych ekranach.

**Szacunkowy potencjał naprawy: 100 000–350 000 PLN/miesiąc**

---

**⚠️ Problem 5 — Kampanie PMax przynoszą więcej ruchu ale mniej sprzedaży**

Kampanie PMax (Performance Max) Google generują dziś 63% więcej wizyt niż rok temu (137 tys. vs 84 tys. miesięcznie), ale przynoszą 62% mniej zamówień (70 vs 186). To bezpośrednia konsekwencja problemu nr 2 — algorytm myśli, że działa bardzo dobrze i skupia się na ilości kliknięć zamiast na jakości.

**Szacunkowy potencjał po naprawie: ~90 000–144 000 PLN/miesiąc**

---

**Łączna strata vs rok temu: -1 326 787 PLN/miesiąc**
**Łączny potencjał optymalizacji (niezależnie od YoY): +350 000–700 000 PLN/miesiąc**

---

## Plan działania

### 🔴 Natychmiast (0–7 dni) — naprawić śledzenie i odblokować reklamy

| # | Działanie | Efekt | Kto | Czas |
|---|-----------|-------|-----|------|
| 1 | Naprawić błędne odczytywanie numeru zamówienia w systemie śledzenia (GTM) — zmienna z URL → DataLayer | Algorytm Google Ads dostaje prawdziwe dane; kampanie PMax przestają "przepalać" budżet | Specjalista GTM | 2–4h |
| 2 | Wyłączyć wbudowany moduł Google Analytics w PrestaShop (pozostawić tylko GTM) | Eliminacja 89 pustych zdarzeń zakupu; czyste dane | Admin PrestaShop | 30 min |
| 3 | Sprawdzić w Google Ads dlaczego kampanie Search mają 92% mniej ruchu — przywrócić lub zwiększyć budżet | Odzysk ~200k PLN/msc potencjału | Specjalista Ads | 1 dzień |
| 4 | Dodać bramki płatności i skrzynki pocztowe do wykluczeń (Klarna, onet.pl, wp.pl, interia.pl, o2.pl) | Prawidłowe przypisanie ~420 wizyt/msc do właściwych kanałów | Admin GA4 | 30 min |

---

### 🟡 Miesiąc 1 — poprawa konwersji i śledzenia

| # | Działanie | Efekt szacowany | Kto |
|---|-----------|----------------|-----|
| 1 | Audyt doświadczenia na telefonach: nagrania sesji (Clarity/Hotjar), prędkość ładowania (PageSpeed), uproszczenie procesu zakupu | +100 000–350 000 PLN/msc | UX + Deweloper |
| 2 | Aktywować "ratowanie porzuconych koszyków" w edrone — 32 640 osób/msc porzuca koszyk bez zakupu | +650–980 transakcji/rok = ~800 000–1 200 000 PLN/rok | Marketing / edrone |
| 3 | Poprawić lejek checkout (analiza gdzie jest 67% drop-off) — uprościć kroki, dodać Google Pay/Apple Pay | +80 000–120 000 PLN/msc | UX + Deweloper |
| 4 | Wyłączyć ruch z serwerów testowych/deweloperskich z analityki (dev18.arytondev.pl, aryton81.local) | Czyste dane, 1 fałszywa transakcja mniej | Admin GA4 | 15 min |
| 5 | Naprawić SMS — sprawdzić linki i landing pages | Odzysk 0 → 8 trans/msc (jak w 2025) = ~10 000 PLN/msc | Marketing |

---

### 🟢 Miesiąc 2–3 — skalowanie

| # | Działanie | Efekt szacowany | Kto |
|---|-----------|----------------|-----|
| 1 | Uruchomić reklamy Microsoft Bing Ads — Bing daje najwyższy zwrot z sesji na całym koncie (10.51 PLN/sesja!) | +~293 000 PLN/msc przy 10× skalowaniu | Specjalista Ads |
| 2 | Przebudować kampanie PMax po naprawie śledzenia — segmentacja produktów na podstawie rzeczywistej rentowności | Wyższy ROAS z PMax | Performance Marketing |
| 3 | Zbadać i wzmocnić lojalność klientów — ruch bezpośredni (stali klienci) spadł -46%, CR bezpośredni -83% | Odzysk powracających klientów, program lojalnościowy | Marketing |

---

## Najważniejsze wskaźniki do monitorowania

| Wskaźnik | Teraz | Cel (3 miesiące) |
|----------|-------|-----------------|
| Transakcje/miesiąc | 427 | >700 |
| Przychód/miesiąc | 530 000 PLN | >900 000 PLN |
| Ratio ecommercePurchases:transactions | 3.77× | <1.2× |
| CR mobile | 0.095% | >0.15% |
| CR desktop | 0.276% | >0.35% |
| Paid Search sesje/msc | 4 600 | >20 000 |
| Checkout drop-off | 67% | <50% |

---

## Podsumowanie

Sklep Patrizia by Aryton ma wszystko co potrzeba do sukcesu: silną markę, wysoką wartość zamówień (1 241 PLN AOV), dobrze działające śledzenie GA4 dla prawdziwych transakcji, dane produktowe. Problem jest **techniczny i strategiczny** — nie produktowy.

Trzy najpilniejsze działania:
1. **Naprawić błędne śledzenie** (2–4h pracy) → kampanie Google przestają działać "w ciemno"
2. **Reaktywować kampanie Search** → bezpośredni odzysk ~200 000 PLN/msc
3. **Naprawić UX mobile** → odzysk 100 000–350 000 PLN/msc

Te trzy działania mogą zostać wdrożone w ciągu 2 tygodni i powinny przynieść widoczne rezultaty już w ciągu 30 dni.
