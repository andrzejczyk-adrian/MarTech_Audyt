# Audyt MarTech — Podsumowanie

**Klient:** Patrizia by Aryton
**Data:** 2026-04-07 | **Okres analizy:** 8 marca – 7 kwietnia 2026
**Audytor:** Adrian Andrzejczyk
**Konto GA4:** G-93NK3C48R3 | **Google Ads:** 196-867-6668
**Typ biznesu:** e-commerce (odzież premium)

---

## Wyniki ogólne

| Obszar | Wynik | Ocena |
|--------|-------|-------|
| 1. Infrastruktura śledzenia | 14% | ❌ Krytyczny |
| 2. Zgodność z prawem (cookies) | 0% | ❌ Krytyczny |
| 3. Konfiguracja systemu analitycznego | 22% | ❌ Krytyczny |
| 4. Jakość danych | 53% | ⚠️ Wymaga poprawy |
| 5. Oznaczenia ruchu (UTM) | 50% | ⚠️ Wymaga poprawy |
| 6–7. Analiza produktów i lejki zakupowe | 7% | ❌ Krytyczny |
| 8. Połączenie GA4 ↔ Google Ads | 22% | ❌ Krytyczny |
| 9. Analiza wyników | 25% | ❌ Krytyczny |
| 10. Google Ads | brak dostępu | 🔒 |
| **ŁĄCZNIE** | **26%** | **❌ Krytyczny** |

**Ocena ogólna:** System śledzenia patrizia.aryton.pl jest technicznie uszkodzony — sklep generuje realny przychód (515 556 PLN/miesiąc), ale dane analityczne są w znacznej mierze błędne i uniemożliwiają prawidłową ocenę efektywności kampanii reklamowych.

---

## Najważniejsze problemy (z wyceną)

---

**🔴 Problem 1 — Licznik zakupów nalicza każdą transakcję 3.83 razy**

W ciągu ostatnich 30 dni sklep odnotował 413 faktycznych zamówień. Tymczasem system analityczny "widzi" aż 1 582 zakupów — ponieważ jeden zakup jest rejestrowany 3.83 razy. Przyczyną jest podwójna instalacja: firma Google i platforma Shoper mają jednocześnie włączone śledzenie, które liczy te same transakcje wielokrotnie. Google Ads, widząc 3.83× więcej konwersji niż ma miejsce, błędnie ocenia skuteczność kampanii i może podejmować złe decyzje o budżecie. Ten problem wykryto już 4 kwietnia 2026 — do dziś nie został naprawiony.

**Szacowany koszt:** Niezmierzalne przepalenie budżetu reklamowego | **Priorytet:** Natychmiastowy | **Czas naprawy:** 2 godziny

---

**🔴 Problem 2 — Sklep "nie wie" co sprzedaje — brak danych o produktach**

Mimo że sklep sprzedał w ciągu 30 dni produkty za 515 556 PLN, w systemie analitycznym przy każdym produkcie widnieje: 0 zakupów, 0 PLN przychodu. Rejestrujemy fakt zakupu, ale nie przesyłamy informacji *co* zostało kupione i za ile. Konsekwencja: nie można sprawdzić które sukienki, buty ani płaszcze przynoszą zysk, nie można zoptymalizować reklam produktowych pod bestsellery, a kampanie Google Shopping działają "w ciemno".

**Szacowany koszt:** Niemierzalne — blokuje całą optymalizację produktową | **Priorytet:** Natychmiastowy | **Czas naprawy:** 4–8 godzin (deweloper)

---

**🔴 Problem 3 — Użytkownicy na telefonach kupują 2.6× rzadziej niż na komputerach**

78% odwiedzających patrizia.aryton.pl używa telefonu. Jednak z komputerów kupuje co 100-ty odwiedzający (CR: ~0.26%), a z telefonów tylko co 270-ty (~0.10%). Ta różnica oznacza, że sklep "traci" od 100 000 do 500 000 PLN miesięcznie, bo strona nie jest wystarczająco wygodna na małym ekranie. Dotyczy to procesu zakupu: skomplikowany formularz, małe przyciski, wolne ładowanie na 4G.

**Szacowany potencjał:** 100 000 – 500 000 PLN/msc | **Priorytet:** Natychmiastowy | **Czas wdrożenia:** 3–6 tygodni

---

**⚠️ Problem 4 — 2 na 3 osoby gotowe kupić — rezygnują na etapie płatności**

Ze 1 296 osób, które zaczęły proces zakupu (wypełnienie adresu, wybór dostawy), zaledwie 413 finalizuje zamówienie. 68% rezygnuje. W dobrze działającym sklepie odzieżowym ten wskaźnik powinien wynosić maksymalnie 40–50%. Każda osoba, która dotarła do etapu "płacę" to ktoś zdecydowany — rezygnacja to sygnał problemów technicznych lub UX (za dużo kroków, nieczytelny formularz, brak preferowanej metody płatności, zaskakujące koszty dostawy).

**Szacowany potencjał:** 100 000 – 200 000 PLN/msc | **Priorytet:** Miesiąc 1 | **Czas wdrożenia:** 2–4 tygodnie

---

**ℹ️ Problem 5 — Ponad 32 000 koszyków porzuconych bez żadnego przypomnienia**

W ciągu miesiąca 32 653 razy ktoś dodał produkt do koszyka — ale nie kupił. Z 413 faktycznych zakupów wynika, że 98.7% koszyków jest porzucanych. Część z tych osób to "okienni" kupujący, ale znaczna część to osoby, które potrzebują tylko lekkiego impulsu: przypomnienia emailem, małego rabatu, lub informacji o dostępności. Platforma edrone (email marketing), z której korzysta Aryton, posiada gotową funkcję wysyłania takich przypomnień — wymaga tylko aktywacji.

**Szacowany potencjał:** 80 000 – 120 000 PLN/msc (przy 3% odzysku) | **Priorytet:** Miesiąc 1 | **Czas wdrożenia:** 1–2 tygodnie

---

**Łączny szacowany koszt problemów 1–2:** Niemierzalne przepalenie budżetu reklamowego
**Łączny potencjał napraw 3–5:** **280 000 – 820 000 PLN/miesiąc** (3,4 – 9,8 MLN PLN/rok)

---

## Plan działania

### 🔴 Natychmiast (0–7 dni) — zatamowanie strat

| # | Działanie | Efekt | Kto |
|---|-----------|-------|-----|
| 1 | Wyłączyć wbudowane śledzenie Google w panelu Shoper (Ustawienia → Integracje → Google Analytics → wyłączyć) | Naprawia podwójne liczenie zakupów — dane stają się wiarygodne | Klient / Admin Shoper |
| 2 | Deweloper: naprawić system przekazywania danych produktowych na stronie "Dziękujemy za zakup" — uzupełnić dane o produktach (nazwa, cena, ilość) | Odblokowuje analizę sprzedaży per produkt, optymalizację reklam Shopping | Deweloper (4–8h) |
| 3 | Ustawić przekazywanie źródła kampanii przy odmowie cookies (tzw. url_passthrough w systemie analitycznym) | Odzysk ~29 transakcji/msc bez atrybuacji = ~36 000 PLN/msc | Admin GTM (30 min) |
| 4 | Wykluczyć płatności Klarna i webmaile (onet.pl, wp.pl, interia.pl, o2.pl) ze źródeł ruchu — prawidłowe przypisanie kampanii | Prawidłowa atrybuacja ~470 sesji/msc, 719 PLN/msc odzyskane | Admin GA4 (30 min) |

---

### 🟡 Miesiąc 1 — optymalizacja i naprawa

| # | Działanie | Efekt szacowany | Kto |
|---|-----------|----------------|-----|
| 1 | Audyt UX na telefonie: szybkość strony, uproszczenie formularza zakupu, wdrożenie Google Pay / Apple Pay | +100 000 – 500 000 PLN/msc (poprawa CR mobile) | UX + Deweloper |
| 2 | Aktywować "ratowanie porzuconych koszyków" w edrone — sekwencja 3 emaili (1h, 24h, 72h po porzuceniu) | +80 000 – 120 000 PLN/msc | Marketing / edrone |
| 3 | Uprościć checkout — analiza gdzie użytkownicy rezygnują, redukcja kroków, lepsze CTA | Zmniejszenie drop-off z 68% do ~50% = +100 000 PLN/msc | UX + Deweloper |
| 4 | Dodać oznaczenia UTM do postów organicznych na Facebooku i Instagramie | Precyzyjny pomiar ROAS Meta, ~5 000 PLN/msc lepiej widoczne | Marketing |
| 5 | Weryfikacja i naprawa Consent Mode (system zarządzania zgodami cookies) przez specjalistę GTM | Zgodność z RODO, poprawa jakości danych analitycznych | Specjalista GTM |

---

### 🟢 Miesiąc 2–3 — skalowanie i strategia

| # | Działanie | Efekt szacowany | Kto |
|---|-----------|----------------|-----|
| 1 | Po naprawieniu danych produktowych — analiza sprzedaży BCG (które produkty przynoszą zysk, które go pochłaniają) + restrukturyzacja kampanii wg rentowności | Lepsza alokacja budżetu reklamowego, wyższy ROAS | Performance Marketing |
| 2 | Wdrożyć kampanie Microsoft (Bing) Ads — Bing jest najefektywniejszym kanałem (9.43 PLN przychodu na sesję!), kompletnie niedoinwestowanym | Przy 10× większym wolumenie: +260 000 PLN/msc | Performance Marketing |
| 3 | Wdrożyć GTM Server-Side (zaawansowana forma śledzenia przez własny serwer) — lepsza ochrona danych, wyższa jakość konwersji | Poprawa dokładności śledzenia o ~15–20%, lepsza zgodność z prawem | Specjalista GTM |
| 4 | Aktywować i naprawić kampanie SMS z właściwymi linkami do produktów + UTM | +5 000 PLN/msc (1 735 sesji bez konwersji → odzysk) | Marketing |

---

## Kluczowe wskaźniki do monitorowania po wdrożeniach

| Wskaźnik | Teraz | Cel (Miesiąc 3) |
|----------|-------|-----------------|
| Ratio zakupów: eventy / transakcje | 3.83× | ≤1.1× |
| Przychód per produkt (itemRevenue) | 0 PLN (brak danych) | >0 PLN (dane widoczne) |
| Wskaźnik konwersji mobile | ~0.10% | >0.15% |
| Drop-off checkout | 68% | <50% |
| Wskaźnik odzysku koszyków | 0% | 2–3% |
| Sesje (not set) / wszystkie sesje | 2.52% | <1% |
| CR google/cpc vs google/organic | 30% | >50% |

---

## Podsumowanie

Patrizia by Aryton to marka premium z realną sprzedażą (~515 000 PLN/miesiąc) i dużym potencjałem wzrostu. Jednak obecna infrastruktura techniczna działa jak licznik ze skręconym kablem — mierzy coś, ale nie to co trzeba. Naprawy techniczne (pierwsze 4 kroki) można wykonać w tydzień i kosztują kilka godzin pracy. Rezultat: wiarygodne dane, prawidłowe decyzje reklamowe, odblokowanie możliwości analitycznych.

Optymalizacje UX i retencji (mobile, checkout, koszyk) to inwestycja 3–6 tygodni, która według konserwatywnych szacunków może zwiększyć przychód o **300 000 – 800 000 PLN miesięcznie**.

Najszybszy zwrot z inwestycji daje: naprawienie danych (darmowe, 1 dzień) + abandoned cart w edrone (tygodniowa konfiguracja) + uproszczenie procesu zakupu na telefonie.
