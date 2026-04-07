# Audyt MarTech — Podsumowanie dla właściciela

**Klient:** Patrizia Aryton (patrizia.aryton.pl)
**Data:** 07.04.2026 | **Okres analizy:** 08.03 – 07.04.2026 (30 dni)
**Audytor:** Adrian Andrzejczyk
**Typ biznesu:** E-commerce premium (odzież damska) | Platforma: PrestaShop

---

## Wyniki ogólne

| Obszar | Wynik | Ocena |
|--------|-------|-------|
| 1. Infrastruktura śledzenia | 41% | ❌ Krytyczny |
| 2. Zgodność z prawem (cookies) | 40% | ❌ Krytyczny |
| 3. Konfiguracja systemu analitycznego | 31% | ❌ Krytyczny |
| 4. Jakość danych | 53% | ⚠️ Wymaga poprawy |
| 5. Oznaczenia ruchu (UTM) | 72% | ⚠️ Wymaga poprawy |
| 7. Lejki zakupowe | 38% | ❌ Krytyczny |
| **ŁĄCZNIE** | **45%** | **❌ Krytyczny** |

**Ocena ogólna:** System analityczny sklepu dostarcza fałszywe dane sprzedażowe i naraża firmę na naruszenie RODO — decyzje marketingowe oparte na obecnych raportach GA4 są oparte na błędnych liczbach.

---

## Najważniejsze problemy (z wyceną)

### 🔴 Problem 1 — Dane sprzedażowe zawyżone prawie 4-krotnie

System analityczny rejestruje każdy zakup średnio **3,83 razy** zamiast raz. Dzieje się tak dlatego, że sklep ma jednocześnie zainstalowane dwa "liczniki" Google Analytics — jeden wbudowany w kod strony, drugi przez Google Tag Manager. Oba liczą tę samą sprzedaż.

W efekcie raporty pokazują 1 582 zakupów zamiast rzeczywistych ~413. Wszelkie wskaźniki oparte na liczbie transakcji (np. ROAS kampanii, współczynnik konwersji) są błędne. Ten problem wykryliśmy już 4 dni temu (audyt 03.04.2026) — ratio wzrosło z 3.53 do 3.83 co świadczy o pogłębieniu błędu.

**Szacowany koszt:** Błędne decyzje budżetowe w kampaniach (niepoliczalne) | **Priorytet:** Natychmiastowy

---

### 🔴 Problem 2 — 72% zamówień bez możliwości analizy

Spośród 1 503 unikalnych numerów zamówień z ostatnich 30 dni, aż **1 088 (72,4%) zawiera błędny format** — zamiast czystego numeru zamówienia (np. "210032"), do systemu trafia cały adres URL strony potwierdzenia (np. "210032&key=1abe2783..."). To błąd w konfiguracji sklepu PrestaShop.

Konsekwencja: nie można przyporządkować konkretnego zamówienia do klienta, kanału marketingowego ani produktu. Przychód z 72% transakcji jest niemożliwy do zweryfikowania w GA4.

**Szacowany koszt:** Brak wglądu w ~373 000 PLN/msc przychodu | **Priorytet:** Natychmiastowy

---

### 🔴 Problem 3 — Dane produktowe całkowicie zepsute

Przez ostatnie 30 dni system analityczny **nie zarejestrował ani jednego zakupionego produktu**. Dosłownie: `zakupionych produktów = 0` dla wszystkich 2 691 pozycji w katalogu. Oznacza to że niemożliwe jest sprawdzenie:
- Które produkty się sprzedają najlepiej
- Które kategorie generują największy przychód
- Jaką marżowość mają bestsellery
- Które produkty powinny być priorytetem w kampaniach reklamowych Google Shopping i Meta

Bez tych danych kampanie produktowe są "ślepe" — system reklamowy nie wie które produkty warto promować.

**Szacowany koszt:** Nieoptymalny dobór produktów do kampanii = przepalony budżet reklamowy | **Priorytet:** Natychmiastowy

---

### 🔴 Problem 4 — Brak wymaganego bannera zgody (ryzyko RODO)

Sklep ma technicznie poprawnie skonfigurowany system zgód (Consent Mode), ale **baner cookie nie wyświetla się użytkownikom**. Oznacza to że odwiedzający stronę nie mają możliwości ani wyrażenia, ani odmówienia zgody na przetwarzanie danych.

Jest to niezgodne z RODO i polską ustawą o ochronie danych osobowych. Inspekcja UODO może nałożyć karę do **20 mln EUR lub 4% rocznego obrotu** (cokolwiek jest wyższe). Moduł GDPR jest zainstalowany w sklepie — wymaga technicznej naprawy konfiguracji.

**Szacowany koszt:** Ryzyko kary do 20 mln EUR | **Priorytet:** Natychmiastowy

---

### 🟡 Problem 5 — Tylko 1 na 3 klientów finalizuje zakup

Z klientów którzy **zaczęli realizację zamówienia**, tylko **31,9% doprowadza ją do końca** (benchmark dla dobrych sklepów: 50-80%). Oznacza to że 68% klientów, którzy dotarli do kasy i zaczęli składać zamówienie, porzuca ten proces.

Przy obecnym poziomie sprzedaży (515 556 PLN/msc): poprawa finalizacji zamówień z 32% do 50% mogłaby przełożyć się na **+123 000 PLN/msc dodatkowego przychodu** bez zwiększania budżetu reklamowego.

Możliwe przyczyny: zbyt wiele kroków w procesie zamówienia, brak preferowanych metod płatności, wymaganie zakładania konta, koszty dostawy widoczne zbyt późno.

**Szacowany potencjał:** +123 000 PLN/msc | **Priorytet:** Miesiąc 1

---

**Łączny szacowany koszt problemów 1–4:** Niepoliczalny bezpośrednio (błędne dane uniemożliwiają wycenę) + ryzyko kary RODO do 20 mln EUR
**Łączny potencjał optymalizacji (problem 5):** +123 000 PLN/msc (+1,48 mln PLN/rok)

---

## Plan działania

### 🔴 Natychmiast (0–7 dni) — zatamowanie strat

| # | Działanie | Efekt | Kto |
|---|-----------|-------|-----|
| 1 | Usunąć jeden z dwóch "liczników" GA4 z kodu HTML sklepu (zostawić tylko ten przez Google Tag Manager) | Naprawia duplikację danych — ratio 3.83x → 1.0x | Deweloper PrestaShop |
| 2 | Naprawić sposób pobierania numeru zamówienia na stronie potwierdzenia (pobierać tylko cyfrę, nie cały URL) | 72% zamówień z poprawnym ID → pełna analiza transakcji | Deweloper PrestaShop |
| 3 | Dodać dane produktowe do systemu śledzenia na stronie potwierdzenia zamówienia | Odblokowanie analizy produktowej i optymalizacji kampanii Shopping | Deweloper PrestaShop |
| 4 | Naprawić lub wymienić moduł zgody cookie (psgdpr) tak aby baner wyświetlał się użytkownikom | Compliance RODO — eliminacja ryzyka kary | Deweloper / Agencja |

### 🟡 Miesiąc 1 — optymalizacja i naprawa

| # | Działanie | Efekt szacowany | Kto |
|---|-----------|----------------|-----|
| 5 | Wykluczyć Klarna i webmaile (wp.pl, onet.pl, interia.pl, o2.pl) ze źródeł "referral" w GA4 | Prawidłowa atrybucja zakupów do kanałów | Analityk / Agencja |
| 6 | Ujednolicić oznaczenia UTM w kampaniach Meta Ads (1 format zamiast 6 wariantów) | Spójne raporty Facebook Ads | Agencja Meta |
| 7 | Analiza i optymalizacja procesu realizacji zamówienia (UX kasy) | Potencjał +123 000 PLN/msc | UX / Deweloper |
| 8 | Dodanie "add_to_cart" i "begin_checkout" jako celów konwersji w GA4 | Lepsza optymalizacja kampanii reklamowych | Analityk |

### 🟢 Miesiąc 2–3 — skalowanie i strategia

| # | Działanie | Efekt szacowany | Kto |
|---|-----------|----------------|-----|
| 9 | Uruchomienie raportów produktowych po naprawie danych | Identyfikacja top produktów → skalowanie sprzedaży | Analityk |
| 10 | Przegląd i optymalizacja kampanii PMax (Cross-network = 39% ruchu, CR 0,20%) | Poprawa efektywności budżetu reklamowego | Agencja Google |
| 11 | Skalowanie email marketingu eDrone (CR 1,02% — najwyższy z kanałów) | Wzrost sprzedaży bez zwiększania budżetu reklamowego | Email marketing |

---

## Kluczowe wskaźniki do monitorowania (po naprawie)

| Wskaźnik | Obecny wynik | Cel (3 miesiące) |
|----------|-------------|-----------------|
| Ratio purchase:transakcja | 3,83x ❌ | ≤1,1x ✅ |
| % zamówień z poprawnym ID | 27,5% ❌ | >95% ✅ |
| itemsPurchased | 0 ❌ | >0 (rzeczywiste) ✅ |
| Finalizacja kasy (checkout → zakup) | 31,9% ❌ | ≥50% 🎯 |
| % (not set) w źródłach ruchu | 2,5% ✅ | <5% ✅ |
| Baner cookie wyświetlany | Nie ❌ | Tak ✅ |
| CR (współczynnik konwersji) | 0,13% ❌ | ≥0,40% 🎯 |
| AOV (średnia wartość zamówienia) | 1 249 PLN ✅ | ≥1 249 PLN |

---

*Pełna dokumentacja techniczna z uzasadnieniem każdego wniosku → raport szczegółowy: `20260407_cc_patricia_audyt.md`*
