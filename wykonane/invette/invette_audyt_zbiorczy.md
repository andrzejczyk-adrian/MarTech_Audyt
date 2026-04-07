# AUDYT GOOGLE ADS — INVETTE MCC
## Raport Zbiorczy | Marzec–Kwiecień 2026

**MCC:** 934-203-1404 | **Agencja:** Invette.pl
**Źródło 1:** BDOS AI v1.0.9 — dane za marzec 2026 (01–31.03.2026)
**Źródło 2:** BDOS AI v1.0 — dane za ostatnie 30 dni (raport z 02.04.2026)
**Cel raportu:** Kompleksowa ocena jakości zarządzanych kont Google Ads z perspektywy agencji SEM

> **Uwaga dot. GA4:** Brak dostępu do Google Analytics API (`bdos auth --add analytics` niezrealizowane).
> Analiza GA4 pominięta dla wszystkich kont. Do uzupełnienia po autoryzacji na invette.sem@gmail.com.

---

## CZĘŚĆ 0 — PORTFEL: DANE OGÓLNE

### 0.1 Liczba kont

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Kont łącznie w MCC | 150 | 150 |
| Kont z wydatkami | 90 | 94 |
| Kont nieaktywnych | 60 | 56 |

### 0.2 Łączne wyniki portfela — konta z danymi produktowymi (marzec 2026)

| Metryka | Wartość |
|---------|---------|
| Kont z danymi produktowymi | 45 |
| Łączne wydatki (45 kont) | 282 382 PLN |
| Łączna wartość konwersji | 1 618 388 PLN |
| ROAS portfela | **5.7x** |
| Produktów unikalnych (item_id) | 57 222 |
| Produktów aktywnych (min. 10 kliknięć) | 3 842 |

### 0.3 Segmentacja kont wg statusu (marzec 2026)

| Status | Liczba kont | Łączne wydatki | Opis |
|--------|-------------|----------------|------|
| ✅ OK | 22 konta | ~180 000 PLN | Brak krytycznych problemów, ROAS akceptowalny |
| ⚠️ Uwaga | 16 kont | ~95 000 PLN | Kampanie bez konwersji lub ROAS do poprawy |
| 🔴 Problem | 22 konta | ~107 000 PLN | Niski ROAS e-commerce lub brak konwersji |
| ℹ️ Lead gen | 20 kont | ~45 000 PLN | Brak wartości konwersji — wymaga weryfikacji |
| 💤 Nieaktywne | 60 kont | 0 PLN | Brak wydatków w marcu |

---

## CZĘŚĆ 1 — TABELA PRZESTAWNA WSZYSTKICH KONT AKTYWNYCH

### 1.1 Przegląd błędów i problemów per konto

| # | Konto | Wydatki 30d | ROAS | Konwersje | Kamp. bez konw. | Niski ROAS | Wysoki CPA | Niski QS | Status |
|---|-------|------------|------|-----------|-----------------|------------|------------|---------|--------|
| 1 | TABLE4U | 66 325 PLN | 9x | 178 | ✅ | 🔴 | ⚠️ | 🔴 QS 3.3 | ⚠️ |
| 2 | Synthagen Labs | 61 993 PLN | 2x | 282 | ✅ | 🔴 | ⚠️ | ✅ QS 8.2 | 🔴 |
| 3 | IdeaShirt | 58 367 PLN | 6x | 1 353 | ✅ | 🔴 | ✅ | ✅ QS 8.0 | ⚠️ |
| 4 | Optimum BHP | 42 748 PLN | 4x | 344 | ✅ | 🔴 | ✅ | ✅ QS 9.7 | ⚠️ |
| 5 | MegaKoszulki.pl | 23 316 PLN | 5x | 846 | ✅ | 🔴 | ✅ | ✅ QS 7.4 | ⚠️ |
| 6 | PaDrew | 18 792 PLN | 12x | 134 | ✅ | 🔴 | ✅ | 🔴 QS 3.4 | ⚠️ |
| 7 | Pastform | 18 763 PLN | 11x | 34 | ⚠️ 1 kamp. | 🔴 | 🔴 CPA 552 | ✅ QS 9.0 | ⚠️ |
| 8 | Janda | 16 813 PLN | 8x | 1 057 | ✅ | 🔴 | ✅ | 🔴 QS 2.8 | ⚠️ |
| 9 | Wedel Pijalnie | 16 547 PLN | 5x | 8 676 | ✅ | 🔴 | ✅ | ⚠️ QS 5.3 | ⚠️ |
| 10 | Expertia Naturals | 15 058 PLN | 17x | 1 175 | ✅ | 🔴 | ✅ | ✅ QS 9.7 | ⚠️ |
| 11 | PLC Nowe Google Ads | 14 651 PLN | 3x | 144 | ✅ | 🔴 | ✅ | — | ⚠️ |
| 12 | sklep.delia.pl | 13 451 PLN | 1x | 299 | ⚠️ 2 kamp. | 🔴 | ✅ | ✅ QS 8.6 | 🔴 |
| 13 | forcopy.com.pl | 12 444 PLN | 0x | 667 | ✅ | — | ✅ | ⚠️ QS 5.5 | 🔴 |
| 14 | PMEBLE G. Jakubek | 12 070 PLN | 17x | 158 | ✅ | 🔴 | ✅ | ✅ QS 9.6 | ⚠️ |
| 15 | Asepta | 10 591 PLN | 5x | 198 | ✅ | 🔴 | ✅ | ✅ QS 8.1 | ⚠️ |
| 16 | centus_zielonka | 8 979 PLN | 9x | 225 | ⚠️ 1 kamp. | 🔴 | ✅ | ⚠️ QS 5.1 | ⚠️ |
| 17 | EcoBeds | 8 926 PLN | 7x | 149 | ⚠️ 1 kamp. | 🔴 | ✅ | ✅ QS 10.0 | ⚠️ |
| 18 | LVNSYSTEM | 8 006 PLN | 1x | 74 | ⚠️ 3 kamp. | 🔴 | ✅ | — | 🔴 |
| 19 | KuraSport | 7 895 PLN | 4x | 261 | ✅ | 🔴 | ✅ | ✅ QS 10.0 | ⚠️ |
| 20 | TOMA | 7 837 PLN | 0.5x | 7 | ✅ | 🔴 | 🔴 CPA 1120 | — | 🔴 |
| 21 | RCL SYSTEM | 7 731 PLN | 1x | 15 | ✅ | 🔴 | 🔴 CPA 515 | ✅ QS 7.6 | 🔴 |
| 22 | stercontrol | 7 032 PLN | 9x | 19 081 | ⚠️ 3 kamp. | 🔴 | ✅ | ✅ QS 7.0 | ⚠️ |
| 23 | ASKO sp. z o.o. | 6 954 PLN | 53x | 53 | ⚠️ 4 kamp. | 🔴 | ✅ | ✅ QS 7.9 | ⚠️ |
| 24 | DD Projekt | 6 623 PLN | 1x | 23 | ⚠️ 1 kamp. | 🔴 | ⚠️ CPA 288 | ✅ QS 6.5 | 🔴 |
| 25 | Meblast | 6 588 PLN | 6x | 8 | ✅ | 🔴 | 🔴 CPA 824 | ✅ QS 8.6 | ⚠️ |
| 26 | Hempets | 6 486 PLN | 1x | 17 | ⚠️ 1 kamp. | 🔴 | ⚠️ CPA 382 | ✅ QS 8.8 | 🔴 |
| 27 | IN - SKYCAMP | 6 297 PLN | **105x** | 558 | ⚠️ 1 kamp. | ⚠️ | ✅ | ✅ QS 6.8 | ✅ |
| 28 | goralskiciuszek.pl | 6 120 PLN | 3x | 106 | ⚠️ 2 kamp. | 🔴 | ✅ | ✅ QS 8.0 | ⚠️ |
| 29 | POLSPORT ORBEA | 5 725 PLN | 2x | 1 623 | ✅ | 🔴 | ✅ | ⚠️ QS 5.8 | ⚠️ |
| 30 | Mr Łoś Sp. z o.o. | 5 691 PLN | 0.3x | 157 | ✅ | 🔴 | ✅ | ✅ QS 10.0 | 🔴 |
| 31 | Adrian Romkowski | 5 591 PLN | 0x lead | 63 | ✅ | — | ✅ | ⚠️ QS 4.4 | ℹ️ |
| 32 | Wywozimy | 5 461 PLN | 0.4x | 164 | ✅ | 🔴 | ✅ | 🔴 QS 2.4 | 🔴 |
| 33 | balneokosmetyki.pl | 5 284 PLN | 8x | 290 | ⚠️ 1 kamp. | 🔴 | ✅ | 🔴 QS 3.8 | ⚠️ |
| 34 | Profito | 5 004 PLN | 0.6x | 323 | ✅ | 🔴 | ✅ | 🔴 QS 2.8 | 🔴 |
| 35 | magdalena24.pl | 4 753 PLN | 13x | 337 | ⚠️ 1 kamp. | 🔴 | ✅ | ✅ QS 9.2 | ⚠️ |
| 36 | Kraksky | 4 314 PLN | 4x | 20 | ⚠️ 2 kamp. | 🔴 | ⚠️ CPA 216 | ✅ QS 6.8 | ⚠️ |
| 37 | Maxdent | 4 027 PLN | 0.05x | 208 | ✅ | 🔴 | ✅ | ⚠️ QS 4.3 | 🔴 |
| 38 | Marcoplast | 3 908 PLN | 0.2x | 13 | ✅ | 🔴 | ⚠️ CPA 303 | ✅ QS 6.0 | 🔴 |
| 39 | Phinance | 3 770 PLN | 0x lead | 12 | ✅ | — | ⚠️ CPA 314 | ⚠️ QS 5.9 | ℹ️ |
| 40 | Singularis | 3 742 PLN | 3x | 70 | ✅ | 🔴 | ✅ | ✅ QS 10.0 | ✅ |
| 41 | deltahr | 3 516 PLN | 19x | 109 | ⚠️ 1 kamp. | 🔴 | ✅ | ✅ QS 7.7 | ✅ |
| 42 | MODENA G. Wróblewski | 3 507 PLN | 12x | 198 | ✅ | 🔴 | ✅ | — | ✅ |
| 43 | GT - serwiskawowy | 3 488 PLN | 0.1x | 2 | ⚠️ 1 kamp. | 🔴 | 🔴 CPA 1584 | ✅ QS 6.1 | 🔴 |
| 44 | SEZARO Sp. z o.o. | 3 369 PLN | 0x lead | 13 | ✅ | — | ⚠️ CPA 259 | ⚠️ QS 5.8 | ℹ️ |
| 45 | OKULUS PLUS | 3 299 PLN | 0x lead | 23 | ✅ | — | ✅ | ✅ QS 8.6 | ℹ️ |
| 46 | Instytut Lingwistyki | 3 230 PLN | 3x | 13 | ✅ | 🔴 | ⚠️ CPA 248 | ✅ QS 8.0 | ⚠️ |
| 47 | KANTÓWKA Sp. z o.o. | 3 027 PLN | 0x lead | 36 | ✅ | — | ✅ | ✅ QS 6.7 | ℹ️ |
| 48 | odpady-kontenery | 3 004 PLN | 0.1x | 38 | ✅ | 🔴 | ✅ | 🔴 QS 3.3 | 🔴 |
| 49 | drukujdobrze.pl | 2 987 PLN | 11x | 143 | ✅ | 🔴 | ✅ | ⚠️ QS 5.5 | ✅ |
| 50 | Oknobank | 2 947 PLN | 0x lead | 103 | ✅ | — | ✅ | ⚠️ QS 4.4 | ℹ️ |

**Legenda:** ✅ OK | ⚠️ Uwaga | 🔴 Problem | ℹ️ Lead gen (brak wartości konwersji)

### 1.2 Wyniki kampanii — ROAS, CPA, Quality Score

| # | Konto | Wydatki | Kliknięcia | Konwersje | Wart. konw. | ROAS | CPA | Avg QS | Typy kampanii |
|---|-------|---------|-----------|----------|------------|------|-----|--------|--------------|
| 1 | TABLE4U | 66 325 PLN | 31 034 | 178 | 577 791 PLN | 9x | 372 PLN | 3.3 | PMax: 7, Search: 4, DemGen: 2, Disp: 1, Video: 1 |
| 2 | Synthagen Labs | 61 993 PLN | 21 033 | 282 | 123 662 PLN | 2x | 220 PLN | 8.2 | PMax: 8, Shopping: 4, Search: 2, Display: 1 |
| 3 | IdeaShirt | 58 367 PLN | 72 385 | 1 353 | 336 684 PLN | 6x | 43 PLN | 8.0 | PMax: 8, Search: 3, DemGen: 1 |
| 4 | Optimum BHP | 42 748 PLN | 27 338 | 344 | 167 230 PLN | 4x | 124 PLN | 9.7 | PMax: 3, Search: 1 |
| 5 | MegaKoszulki.pl | 23 316 PLN | 18 397 | 846 | 116 026 PLN | 5x | 28 PLN | 7.4 | PMax: 6, Search: 4, DemGen: 1 |
| 6 | PaDrew | 18 792 PLN | 7 804 | 134 | 223 046 PLN | 12x | 140 PLN | 3.4 | Search: 2, Shopping: 2, PMax: 2, DemGen: 1 |
| 7 | Pastform | 18 763 PLN | 14 412 | 34 | 201 831 PLN | 11x | 552 PLN | 9.0 | Search: 3, Shopping: 3, PMax: 2, Video: 1 |
| 8 | Janda | 16 813 PLN | 16 929 | 1 057 | 137 669 PLN | 8x | 16 PLN | 2.8 | PMax: 5, Search: 2, Shopping: 2 |
| 9 | Wedel Pijalnie | 16 547 PLN | 17 572 | 8 676 | 76 419 PLN | 5x | 2 PLN | 5.3 | PMax: 8, Search: 3, DemGen: 1, Shopping: 1 |
| 10 | Expertia Naturals | 15 058 PLN | 11 858 | 1 175 | 257 398 PLN | 17x | 13 PLN | 9.7 | PMax: 2, Search: 1, Shopping: 1, Video: 1 |
| 11 | PLC Nowe Google Ads | 14 651 PLN | 18 827 | 144 | 47 076 PLN | 3x | 102 PLN | — | PMax: 4 |
| 12 | sklep.delia.pl | 13 451 PLN | 20 167 | 299 | 17 656 PLN | 1x | 45 PLN | 8.6 | PMax: 3, Search: 1, Display: 1, Video: 1, DemGen: 1 |
| 13 | forcopy.com.pl | 12 444 PLN | 5 996 | 667 | 0 PLN | 0x | 19 PLN | 5.5 | Search: 4, PMax: 2, DemGen: 1 |
| 14 | PMEBLE G. Jakubek | 12 070 PLN | 12 305 | 158 | 204 169 PLN | 17x | 76 PLN | 9.6 | PMax: 3, Shopping: 3, Search: 2, DemGen: 1, Video: 1 |
| 15 | Asepta | 10 591 PLN | 10 328 | 198 | 53 794 PLN | 5x | 53 PLN | 8.1 | PMax: 5, Search: 2, Shopping: 2, DemGen: 2 |
| 16 | centus_zielonka | 8 979 PLN | 13 011 | 225 | 83 448 PLN | 9x | 40 PLN | 5.1 | PMax: 7, Shopping: 3, Search: 2, DemGen: 1, Video: 1 |
| 17 | EcoBeds | 8 926 PLN | 8 372 | 149 | 62 497 PLN | 7x | 60 PLN | 10.0 | Shopping: 3, PMax: 2, Search: 1 |
| 18 | LVNSYSTEM | 8 006 PLN | 4 067 | 74 | 5 039 PLN | 1x | 109 PLN | — | Shopping: 5, Search: 2, PMax: 1, DemGen: 1 |
| 19 | KuraSport | 7 895 PLN | 6 724 | 261 | 30 271 PLN | 4x | 30 PLN | 10.0 | Search: 2, PMax: 2 |
| 20 | TOMA | 7 837 PLN | 10 523 | 7 | 3 714 PLN | 0.5x | 1 120 PLN | — | PMax: 3 |
| 21 | RCL SYSTEM | 7 731 PLN | 4 265 | 15 | 10 198 PLN | 1x | 515 PLN | 7.6 | Search: 2, Shopping: 2, PMax: 2 |
| 22 | stercontrol | 7 032 PLN | 22 026 | 19 081 | 63 461 PLN | 9x | 0 PLN | 7.0 | Search: 7, PMax: 1, Shopping: 1 |
| 23 | ASKO sp. z o.o. | 6 954 PLN | 14 394 | 53 | 369 314 PLN | 53x | 131 PLN | 7.9 | Search: 4, PMax: 1, Shopping: 1, Video: 1, DemGen: 1 |
| 24 | DD Projekt | 6 623 PLN | 2 162 | 23 | 7 100 PLN | 1x | 288 PLN | 6.5 | Search: 2, PMax: 1 |
| 25 | Meblast | 6 588 PLN | 5 882 | 8 | 40 787 PLN | 6x | 824 PLN | 8.6 | PMax: 4, Search: 1 |
| 26 | Hempets | 6 486 PLN | 3 930 | 17 | 3 851 PLN | 1x | 382 PLN | 8.8 | Shopping: 2, PMax: 2, Search: 1 |
| 27 | IN - SKYCAMP | 6 297 PLN | 6 628 | 558 | 664 020 PLN | **105x** | 11 PLN | 6.8 | Search: 5, Video: 1, Display: 1, PMax: 1 |
| 28 | goralskiciuszek.pl | 6 120 PLN | 7 756 | 106 | 19 912 PLN | 3x | 58 PLN | 8.0 | PMax: 5, Search: 1 |
| 29 | POLSPORT ORBEA | 5 725 PLN | 10 501 | 1 623 | 13 837 PLN | 2x | 4 PLN | 5.8 | Search: 7, DemGen: 2, PMax: 2, Shopping: 2 |
| 30 | Mr Łoś Sp. z o.o. | 5 691 PLN | 10 038 | 157 | 1 570 PLN | 0.3x | 36 PLN | 10.0 | Search: 1, PMax: 1 |
| 31 | Wywozimy | 5 461 PLN | 1 739 | 164 | 2 180 PLN | 0.4x | 33 PLN | 2.4 | Search: 2, PMax: 1 |
| 32 | balneokosmetyki.pl | 5 284 PLN | 4 741 | 290 | 42 523 PLN | 8x | 18 PLN | 3.8 | Search: 2, PMax: 2, DemGen: 1, Video: 1 |
| 33 | Profito | 5 004 PLN | 1 566 | 323 | 3 041 PLN | 0.6x | 15 PLN | 2.8 | Search: 2 |
| 34 | magdalena24.pl | 4 753 PLN | 27 089 | 337 | 61 679 PLN | 13x | 14 PLN | 9.2 | PMax: 4, Search: 1, Video: 1 |
| 35 | Kraksky | 4 314 PLN | 1 628 | 20 | 18 717 PLN | 4x | 216 PLN | 6.8 | Search: 4, Video: 1, PMax: 1 |
| 36 | Maxdent | 4 027 PLN | 2 153 | 208 | 208 PLN | 0.05x | 19 PLN | 4.3 | Search: 2, PMax: 1 |
| 37 | Marcoplast | 3 908 PLN | 2 515 | 13 | 800 PLN | 0.2x | 303 PLN | 6.0 | Shopping: 1, Search: 1 |
| 38 | Singularis | 3 742 PLN | 2 695 | 70 | 12 049 PLN | 3x | 53 PLN | 10.0 | Shopping: 1, Search: 1, PMax: 1, Smart: 1 |
| 39 | deltahr | 3 516 PLN | 4 537 | 109 | 65 854 PLN | 19x | 32 PLN | 7.7 | Search: 2, PMax: 1, DemGen: 1 |
| 40 | MODENA G. Wróblewski | 3 507 PLN | 3 484 | 198 | 43 718 PLN | 12x | 18 PLN | — | PMax: 1 |
| 41 | GT - serwiskawowy | 3 488 PLN | 1 896 | 2 | 454 PLN | 0.1x | 1 584 PLN | 6.1 | PMax: 2, Search: 1 |
| 42 | Instytut Lingwistyki | 3 230 PLN | 3 969 | 13 | 10 561 PLN | 3x | 248 PLN | 8.0 | DemGen: 1, Search: 1 |
| 43 | Marcoplast | 3 908 PLN | 2 515 | 13 | 800 PLN | 0.2x | 303 PLN | 6.0 | Shopping: 1, Search: 1 |
| 44 | odpady-kontenery | 3 004 PLN | 956 | 38 | 335 PLN | 0.1x | 79 PLN | 3.3 | Search: 1, PMax: 1 |
| 45 | drukujdobrze.pl | 2 987 PLN | 2 158 | 143 | 32 957 PLN | 11x | 21 PLN | 5.5 | Search: 3, PMax: 1 |

---

## CZĘŚĆ 2 — ANALIZA PROBLEMÓW SYSTEMOWYCH

### 2.1 🔴 Konta e-commerce z ROAS < 2x — koszt strat ~107 000 PLN/msc

| Konto | Wydatki | ROAS | Kluczowy problem |
|-------|---------|------|-----------------|
| TOMA | 7 837 PLN | 0.5x | 7 konwersji przy 7,8K budżetu — katastrofalna konfiguracja |
| Maxdent | 4 027 PLN | 0.05x | 208 konwersji = 1 PLN/konwersja — błąd śledzenia |
| GT - serwiskawowy | 3 488 PLN | 0.1x | 2 konwersje, CPA 1 584 PLN |
| Marcoplast | 3 908 PLN | 0.2x | 13 konwersji, wartość 800 PLN |
| odpady-kontenery | 3 004 PLN | 0.1x | 38 konwersji, wartość 335 PLN |
| Mr Łoś Sp. z o.o. | 5 691 PLN | 0.3x | 157 konwersji = 10 PLN/konwersja |
| Wywozimy | 5 461 PLN | 0.4x | QS 2.4 — ruch nieintencjonalny |
| Profito | 5 004 PLN | 0.6x | 323 konwersje = 9 PLN/konwersja, QS 2.8 |
| Hempets | 6 486 PLN | 1x | CBD/hemp — trudna kategoria |
| LVNSYSTEM | 8 006 PLN | 1x | Manual CPC na 3 kampaniach Shopping |
| DD Projekt | 6 623 PLN | 1x | 1 kampania bez konwersji |
| RCL SYSTEM | 7 731 PLN | 1x | CPA 515 PLN — brak optymalizacji bidowania |
| sklep.delia.pl | 13 451 PLN | 1x | 2 kampanie bez konwersji (Display+Video=6,2K PLN) |
| forcopy.com.pl | 12 444 PLN | 0x | Brak wartości konwersji w Google Ads |
| Synthagen Labs | 61 993 PLN | 2x | Granica opłacalności — skalowanie z 23K do 62K PLN przy spadku ROAS |

**Łącznie: ~107 000 PLN/msc przy śladowym lub ujemnym zwrocie**

**Główne przyczyny niskiego ROAS:**
1. Błędne śledzenie konwersji — liczą mikroeventy (Maxdent: 1 PLN/konw., Profito: 9 PLN/konw.)
2. Brak wykluczeń — ruch nieintencjonalny (Wywozimy QS 2.4, Profito QS 2.8)
3. Zła alokacja budżetu — kampanie Display/Video bez ROAS pochłaniają budżet (sklep.delia.pl)
4. Nieoptymalne strategie — Manual CPC, Maximize Clicks na e-commerce (LVNSYSTEM)
5. Trudne kategorie — CBD/hemp, usługi bez wartości konwersji

### 2.2 ⚠️ Kampanie aktywne bez konwersji — drenaż budżetu

| Konto | Kamp. bez konw. | Szac. drenaż/msc | Najdroższa pusta kampania |
|-------|-----------------|-----------------|--------------------------|
| ASKO sp. z o.o. | 4 kamp. | ~2 000 PLN | Kampania Search/DemGen |
| stercontrol | 3 kamp. | ~1 500 PLN | s7-1200, eWON |
| LVNSYSTEM | 3 kamp. | ~2 500 PLN | DSA All Pages, YouTube |
| Kraksky | 2 kamp. | ~1 800 PLN | High Intent PL REM, YT |
| goralskiciuszek.pl | 2 kamp. | ~1 000 PLN | Kampanie UK/DE |
| sklep.delia.pl | 2 kamp. | ~2 800 PLN | [YT] Biedronka CPM (2 656 PLN!), DemGen |
| Pastform | 1 kamp. | ~471 PLN | [PL][Invette] YT - Wyświetlenia |
| centus_zielonka | 1 kamp. | ~500 PLN | [YT] |
| EcoBeds | 1 kamp. | ~400 PLN | INV\|PLA\|RMKT |
| balneokosmetyki.pl | 1 kamp. | ~300 PLN | YT |
| DD Projekt | 1 kamp. | ~800 PLN | [WWW] SEA Remonty |
| magdalena24.pl | 1 kamp. | ~400 PLN | YouTube filmy |

**Łączny szacowany drenaż: ~14 500 PLN/msc** na kampaniach bez konwersji

### 2.3 🔴 Konta z zerowymi konwersjami na całym koncie

| Konto | Wydatki | Kampanie aktywne | Diagnoza |
|-------|---------|-----------------|---------|
| Fizjoterapia Mazur | 2 883 PLN | 2 | Całkowity brak konwersji — błąd trackingu lub zły produkt |
| Omega Kserokopiarki | 2 380 PLN | 1 | QS 2.3 — słowa kluczowe zupełnie niedopasowane |
| PenPol [nowe 2026] | 2 326 PLN | 4 | Nowe konto — błąd konfiguracji konwersji |
| CRMC | 1 503 PLN | 1 | QS 3.9 |
| NOWE medihurt.com | 1 167 PLN | 2 | Nowe konto — brak konwersji |
| INVETTE (własne) | 1 112 PLN | 1 | Video only — zły typ kampanii |
| Zakatek Fantastyki | 634 USD | 2 | Konto USD — błąd konfiguracji |
| Sklep UQUINA | 507 PLN | 1 | Brak konwersji |
| Polskie Meble - REVES | 217 PLN | 1 | Brak konwersji |

**Łącznie: ~12 700 PLN/msc bez żadnego mierzalnego efektu**

### 2.4 ℹ️ Konta lead gen bez wartości konwersji (~20 kont)

Konta z konwersjami ale bez przypisanej wartości pieniężnej. Może być celowe (usługi) lub wymagać konfiguracji:

Adrian Romkowski Kancelaria, Phinance, SEZARO, OKULUS PLUS, KANTÓWKA, Oknobank, Hauptmann Nowe, FENIX ART, Gestia, KANCELARIA WYLĄG, WBL Invest, Życie bez protez, Wiksonspas, Vago, Auto Pietrzycki, Insector NEW, Viperbox, PROBALANS, THERMO-INSTAL, Fundacja Promyczek

**Rekomendacja:** Dla każdego konta — ustal z klientem: wartość leada (jeśli sprzedaż na kontakt) lub Target CPA zamiast Target ROAS.

---

## CZĘŚĆ 3 — SZCZEGÓŁOWY AUDYT PER KONTO

> Dane źródłowe: BDOS AI v1.0.9 (marzec 2026) + BDOS AI v1.0 (kwiecień 2026).
> ROAS z BDOS v1 = standardowy mnożnik (9.2x = 920%). ROAS z BDOS v2 wyrażony jako mnożnik (9x).
> GA4: brak dostępu — wymaga autoryzacji.

---

### KONTO 1 — TABLE4U
**ID:** 3343262776 | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble)
**BDOS alias:** `table4u`

#### Wyniki kampanii Google Ads

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki łączne | 66 998 PLN | 66 325 PLN |
| Kliknięcia | — | 31 034 |
| Wyświetlenia | — | 2 233 378 |
| CTR | — | 1.39% |
| Avg. CPC | — | 2.14 PLN |
| Konwersje | 190 | 178 |
| Wartość konwersji | 616 782 PLN | 577 791 PLN |
| ROAS | 9.2x | 8.7x |
| CPA | ~353 PLN | 372 PLN |
| Avg Quality Score | — | **3.3 / 10** ❌ |

**Typy kampanii:** PMax: 7, Search: 4, DemGen: 2, Display: 1, Video: 1
**Strategie bidowania:** 10x maximize conversion value, 2x target impression share, 2x maximize conversions, 1x target cpv

#### Kampanie (ostatnie 30 dni)

| Kampania | Typ | Wydatki | Konw. | ROAS | Budżet/d | Strategia | Ocena |
|----------|-----|---------|-------|------|---------|-----------|-------|
| [AT]-[PMAX]-[ALL] | PMax | 14 616 PLN | 25 | 6x | 630 PLN | max conv. value | ✅ |
| [AT]-[PMAX]-[FEED-ONLY]-[ATC180D] | PMax | 13 683 PLN | 24 | 6.3x | 300 PLN | max conv. value | ✅ |
| [PMAX] Stoliki kawowe PM0 | PMax | 10 034 PLN | 9 | **1.8x** | 100 PLN | max conv. value | 🔴 Drenaż |
| [AT]-[PMAX]-[SIENA]-[FEED-ONLY]-[V2] | PMax | 6 361 PLN | 18 | 10x | 300 PLN | max conv. value | ✅ |
| [PMAX] Szafki RTV PM0 | PMax | 5 104 PLN | 11 | 6x | 100 PLN | max conv. value | ✅ |
| [AT]-[AI-MAX]-[SEARCH] | Search | 3 508 PLN | 33 | **23x** | 80 PLN | max conv. value | ⭐ Najlepszy |
| [TXT]-[Search]-[Brand]-[Phrase] | Search | 2 781 PLN | 9 | 9x | 70 PLN | target imp. share | ✅ |
| [TXT] Meble Retro | Search | 2 509 PLN | 3 | 9.1x | 80 PLN | max conv. value | ✅ |
| [GDN] remarketing DR0 | Display | 1 118 PLN | 20 | **64x** | 30 PLN | max conv. value | ⭐ Efektywny |
| [TXT]-[Search]-[Brand]-[Exact] | Search | 1 080 PLN | 16 | 57.6x | 200 PLN | target imp. share | ✅ |
| [PMAX] Konsole PM0 | PMax | 1 924 PLN | 4 | 4.9x | 100 PLN | max conv. value | ✅ |
| [AT] - Demand Gen - Prospecting | DemGen | 1 904 PLN | 3 | 3.4x | 40 PLN | max conversions | ✅ |
| [PMAX] non_pla | PMax | 796 PLN | 2 | 13.3x | 50 PLN | max conv. value | ✅ |
| [GEN] Remarketing | DemGen | 459 PLN | 1 | 4.2x | 20 PLN | max conversions | ✅ |
| **AT-YT-VideoViews** | Video | **449 PLN** | **0** | **0x** | 20 PLN | target cpv | **🔴 Wstrzymaj** |

**Kampanie bez konwersji (drenaż):**
- AT-YT-VideoViews: 449 PLN / 30d → 5 388 PLN/rok zmarnowanych

#### BCG — analiza produktowa (marzec 2026)
- Produktów aktywnych: 184 / 248
- ⭐ Gwiazdy: 33 produkty (meble Siena, retro premium)
- 🐄 Dojne Krowy: 6 produktów
- ❓ Znaki Zapytania: 6 produktów
- 🐕 Psy: **195 produktów (81%)** — krytycznie wysoki udział

**Problem strukturalny:** Kampania „Stoliki kawowe PM0" (10 034 PLN, ROAS 1.8x) — segment z dominacją Psów BCG. Wymaga feed auditu i wykluczenia niekonwertujących item_id.

#### Analiza GA4
> ⚠️ Brak dostępu — wymaga `bdos auth --add analytics`

#### Błędy w konfiguracji
- 🔴 **Niski Quality Score 3.3/10** — krytyczny przy 66K PLN/msc. Wskazuje na słabe dopasowanie reklam do zapytań lub LP. Przy poprawie QS do 7+ → obniżka CPC o szac. 15–20%
- 🔴 **AT-YT-VideoViews** — 449 PLN/msc, 0 konwersji, Target CPV zamiast conv.-oriented
- ⚠️ **[PMAX] Stoliki kawowe PM0** — ROAS 1.8x przy 10 034 PLN — najdroższy problem

#### Analiza trackingu
- ✅ Konwersje śledzone (178 konwersji, 577 791 PLN wartości)
- ✅ Wartości konwersji aktywne
- ❓ Enhanced Conversions — status nieznany (brak GA4 API)
- ❓ GA4 ↔ Ads połączenie — do weryfikacji

#### Rekomendacje
1. **Natychmiast:** Wstrzymaj AT-YT-VideoViews (449 PLN, 0 konwersji)
2. **Priorytet 1:** Feed audit dla 195 Psów BCG — tytuły, zdjęcia, ceny vs. konkurencja
3. **Priorytet 1:** Zrób analizę Search Term Report dla „Stoliki kawowe PM0" — zidentyfikuj frazy bez konwersji i dodaj negatywne słowa kluczowe
4. **Priorytet 2:** Skaluj [AT]-[AI-MAX]-[SEARCH] — ROAS 23x przy zaledwie 80 PLN/d → zwiększ do 200–300 PLN/d
5. **Priorytet 2:** Popraw QS — cross-check: słowa kluczowe → treść reklamy → LP. Cel: QS ≥ 7.0

#### Ocena specjalisty
⭐⭐ (2/5) — Konto ma dobry ROAS ogólny (9x) ale jest nieoptymalne: niski QS (3.3), drogie kampanie PMax bez segmentacji BCG, 80% produktów to Psy bez działania. Potencjał znacznie lepszy.

---

### KONTO 2 — IdeaShirt
**ID:** 4434449811 | **MCC:** 934-203-1404 | **Typ:** e-commerce (odzież, gadżety)
**BDOS alias:** `ideashirt`

#### Wyniki kampanii Google Ads

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 61 041 PLN | 58 367 PLN |
| Kliknięcia | — | 72 385 |
| CTR | — | 3.15% |
| Avg. CPC | — | **0.81 PLN** (najniższy w TOP10) |
| Konwersje | 1 445 | 1 353 |
| Wart. konwersji | 354 038 PLN | 336 684 PLN |
| ROAS | 5.8x | 5.8x |
| CPA | ~42 PLN | 43 PLN |
| Avg QS | — | 8.0 / 10 ✅ |

**Typy kampanii:** PMax: 8, Search: 3, DemGen: 1
**Strategie:** 11x maximize conversion value, 1x maximize conversions

#### Kampanie (ostatnie 30 dni)

| Kampania | Typ | Wydatki | Konw. | ROAS | Budżet/d | Ocena |
|----------|-----|---------|-------|------|---------|-------|
| [AdVist] sw brand | Search | 8 461 PLN | 193 | 6.1x | 150 PLN | ✅ |
| [AdVist] PMax kategorie produktowe STAŁE | PMax | 7 639 PLN | 171 | 4.9x | 250 PLN | ✅ |
| [AdVist] PMax kategorie produktowe OKRES | PMax | 6 921 PLN | 163 | 6.3x | 110 PLN | ✅ |
| [AdVist] PMax ALL Smarketer | PMax | 6 497 PLN | 182 | 5.6x | 100 PLN | ✅ |
| [AdVist] PMax - KREATOR Wszystko Sellie | PMax | 6 456 PLN | 174 | 5.9x | 250 PLN | ✅ |
| [AdVist] PMax - Display | PMax | 5 914 PLN | 134 | 7.5x | 220 PLN | ✅ |
| SW-Koszulki Czapki Kreator | Search | 5 632 PLN | 154 | 8.9x | 300 PLN | ✅ |
| [AdVist] P MAX - BESTSELLERY - KREATOR | PMax | 4 054 PLN | 92 | 5.1x | 150 PLN | ✅ |
| **[AdVist] Demand Gen** | DemGen | **3 541 PLN** | **4** | **0.17x** | 120 PLN | 🔴 Drenaż |
| [AdVist] kreator AI | PMax | 1 621 PLN | 36 | 3x | 120 PLN | ✅ |
| [AdVist] PMax all products | PMax | 1 172 PLN | 39 | 5x | 41 PLN | ✅ |
| [AdVist] - SW brand - student | Search | 460 PLN | 10 | 7.1x | 72 PLN | ✅ |

**Kluczowy problem:** [AdVist] Demand Gen — 3 541 PLN/msc, 4 konwersje = 885 PLN/konwersja, ROAS 0.17x. Drenaż prawie 3,5K PLN miesięcznie.

#### BCG — analiza produktowa
- **93% produktów to Psy** — bardzo wysoki udział
- 66 Znaków Zapytania z wzrostem >20% MoM — największy potencjał w MCC

#### Błędy w konfiguracji
- 🔴 **Demand Gen** — 3 541 PLN, ROAS 0.17x — natychmiast optymalizuj lub wstrzymaj
- ⚠️ 93% produktów to Psy BCG — feed audit urgentny

#### Rekomendacje
1. Wstrzymaj lub drastycznie zoptymalizuj Demand Gen (–3 541 PLN straty/msc)
2. Feed audit dla Psów BCG — cel: wydzielenie 66 Znaków Zapytania do osobnych kampanii
3. Cel ROAS: 7x (aktualnie 5.8x) przez lepszy feed i wykluczenia
4. CPC 0.81 PLN to bardzo niski koszt — potencjał skalowania przy zachowanym ROAS

#### Ocena specjalisty
⭐⭐⭐ (3/5) — Dobra struktura, wysokie wolumeny, dobry QS. Główny problem: Demand Gen jako drenaż i 93% produktów nieaktywnych. Potencjał wzrostu duży.

---

### KONTO 3 — Synthagen Labs
**ID:** 5429088295 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy, laboratoryjne)
**BDOS alias:** `synthagen-labs`

#### Wyniki kampanii Google Ads

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 23 119 PLN | **61 993 PLN** (+168% MoM) |
| Kliknięcia | — | 21 033 |
| CTR | — | 2.10% |
| Avg. CPC | — | 2.95 PLN |
| Konwersje | 144 | 282 |
| Wart. konwersji | 64 733 PLN | 123 662 PLN |
| ROAS | 2.8x | **2.0x** ↓ |
| CPA | ~321 PLN | 220 PLN |
| Avg QS | — | 8.2 / 10 ✅ |

**ALERT:** Budżet wzrósł 2.7x (23K → 62K PLN) przy jednoczesnym SPADKU ROAS (2.8x → 2.0x). To klasyczny błąd agresywnego skalowania bez solidnych sygnałów. Konto na granicy opłacalności.

#### Kampanie (ostatnie 30 dni)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| INV\|PMAX\|Wiosenna Promocja 2026\|za | PMax | 16 006 PLN | 40 | 1.2x | 🔴 |
| INV\|PMAX\|Wiosenna Promocja 2026\|GH | PMax | 11 477 PLN | 36 | 1.3x | 🔴 |
| INV\|PMAX\|Wiosenna Promocja 2026\|BP | PMax | 11 284 PLN | 62 | 2.2x | ⚠️ |
| INV\|PLA\|Wiosenna Promocja 2026 [9szt] | Shopping | 6 639 PLN | 6 | 0.3x | 🔴 |
| [PMAX] Kreacje Produktowe | PMax | 5 478 PLN | 51 | 4.1x | ✅ |
| [PMAX] GHK CU [feed excl. zasoby] | PMax | 3 057 PLN | 17 | 2.3x | ⚠️ |
| [SEARCH] Brand | Search | 2 168 PLN | 4 | 2.8x | ✅ |
| [PLA] RMKT | Shopping | 2 063 PLN | 19 | 2.5x | ⚠️ |
| Sembot[aHv8qbmF][Synthagen] | Shopping | 1 278 PLN | 18 | 5.6x | ✅ |
| INV\|PMAX\|Synthagen\|GHK-Cu\|Zasoby | PMax | 1 219 PLN | 14 | 6x | ✅ |
| **INV\|DIS\|Wiosenna Promocja 2026\|rem** | Display | **911 PLN** | **0** | 0x | **🔴 Wstrzymaj** |
| [PLA] kapsułki | Shopping | 413 PLN | 9 | 12.8x | ✅ |

**Kluczowy problem:** 3 kampanie Wiosenna Promocja (razem 38 806 PLN = 63% budżetu) przy ROAS 0.3–2.2x.

#### Rekomendacje
1. Zredukuj budżet Wiosennych Promocji o 50–60% lub wstrzymaj najgorsze (PLA Promocja 0.3x)
2. Wstrzymaj DIS Wiosenna Promocja (911 PLN, 0 konwersji)
3. Nie skaluj dalej przed osiągnięciem stabilnego ROAS ≥ 3.5x
4. Sprawdź Sembot Shopping (5.6x) i [PLA] kapsułki (12.8x) — te kanały działają, zwiększ ich budżet kosztem PMax promocyjnych

#### Ocena specjalisty
⭐ (1/5) — Agresywne skalowanie (2.7x w 1 miesiąc) bez poprawy efektywności spowodowało ROAS 2x przy 62K PLN wydatków. To 62K PLN na koncie które zarabia 123K PLN = strata przy marży <50%. Wymagana pilna restrukturyzacja.

---

### KONTO 4 — Optimum BHP
**ID:** 2649143184 | **MCC:** 934-203-1404 | **Typ:** e-commerce B2B (odzież robocza, BHP)
**BDOS alias:** `optimum-bhp`

#### Wyniki kampanii Google Ads

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 44 299 PLN | 42 748 PLN |
| Kliknięcia | — | 27 338 |
| CTR | — | 2.64% |
| Avg. CPC | — | 1.56 PLN |
| Konwersje | 354 | 344 |
| Wart. konwersji | 155 047 PLN | 167 230 PLN |
| ROAS | 3.5x | **3.9x** ↑ |
| CPA | ~125 PLN | 124 PLN |
| Avg QS | — | **9.7 / 10** ⭐ |

**Uwaga:** ROAS 3.5–3.9x dla segmentu B2B jest **akceptowalny** — długie cykle zakupowe, wielosesyjne ścieżki konwersji, wartość klienta (LTV) wyższa niż jednorazowy zakup. Nie traktuj jak e-commerce B2C.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| PMax: Smart Shopping | PMax | 19 046 PLN | 184 | 3.5x | ✅ |
| [INV] PMAX - zima | PMax | 12 671 PLN | 72 | 3.2x | ✅ |
| [INV] Bestsellery PMax | PMax | 10 928 PLN | 67 | 3.3x | ✅ |
| [INV] Brand | Search | 102 PLN | 21 | 237.6x | ⭐ |

**Uwaga:** 96% produktów to Psy BCG, ale konto ma dobry ROAS — to B2B specyfika. Klienci kupują przez wiele sesji, algorytm musi zbierać sygnały. 29 Znaków Zapytania z wzrostem >20%.

#### Rekomendacje
1. Wydziel 29 Znaków Zapytania do osobnych kampanii Shopping — cel: ROAS 10x+ dla tego segmentu
2. Customer Match z bazą klientów B2B — lepsze sygnały dla Smart Bidding
3. Skaluj konto — ROAS 3.9x jest stabilny, IS prawdopodobnie niskie

#### Ocena specjalisty
⭐⭐⭐⭐ (4/5) — Najlepiej zarządzane duże konto w MCC. QS 9.7, stabilny ROAS, czysta struktura. Do poprawy: wydzielenie ZQ i Customer Match.

---

### KONTO 5 — MegaKoszulki.pl
**ID:** 8571370299 | **Typ:** e-commerce (odzież, gadżety masowe)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 23 316 PLN |
| Kliknięcia | 18 397 |
| CTR | 3.39% |
| Avg. CPC | 1.27 PLN |
| Konwersje | 846 |
| Wart. konwersji | 116 026 PLN |
| ROAS | 5x |
| CPA | 28 PLN |
| Avg QS | 7.4 |

**Kampanie:** PMax: 6, Search: 4, DemGen: 1 — wszystkie z konwersjami, brak kampanii bez konwersji ✅

Kampanie Demand Gen (590 PLN, 6 konwersji, ROAS 2.8x) — do optymalizacji. Segment masowy (koszyk ~137 PLN) — priorytet to upsell i personalizacja produktów.

#### Ocena specjalisty
⭐⭐⭐ (3/5) — Solidne konto, dobre CPC, dobry QS 7.4. Do poprawy: ROAS (cel 7x) przez feed audit (91% Psów) i wydzielenie 13 Znaków Zapytania.

---

### KONTO 6 — PaDrew
**ID:** 6608764490 | **Typ:** e-commerce (meble, drewno)

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 19 598 PLN | 18 792 PLN |
| Konwersje | 145 | 134 |
| Wart. konwersji | 239 096 PLN | 223 046 PLN |
| ROAS | 12.2x | 11.9x |
| CPA | ~1 649 PLN | 140 PLN |
| Avg QS | — | **3.4 / 10** ❌ |

**Najważniejszy problem:** QS 3.4 przy 18.8K PLN/msc to kosztowny błąd. Przy poprawie QS 3.4 → 7.0: szac. obniżka CPC o ~40%, co przy 7 804 kliknięciach daje ok. 3 000 PLN/msc oszczędności.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| INVETTE PMAX zasoby | PMax | 6 308 PLN | 39 | 10.7x | ✅ |
| INVETTE PLA [wybrane produkty] | Shopping | 3 456 PLN | 27 | 13.7x | ✅ |
| INVETTE PMAX [komponenty - bolek] | PMax | 3 106 PLN | 33 | 15.3x | ✅ |
| Invette PLA [portos] | Shopping | 2 951 PLN | 14 | 7.7x | ✅ |
| INVETTE DEMGEN [storytelling] | DemGen | 1 451 PLN | 3 | 3x | ⚠️ |
| INVETTE SEA [non-brand] | Search | 868 PLN | 2 | 2.5x | ⚠️ |
| INVETTE SEA [brand] | Search | 650 PLN | 16 | **48x** | ⭐ |

**Obserwacja:** Wszystkie kampanie mają konwersje. Problem leży wyłącznie w Quality Score — niskie dopasowanie słów kluczowych/reklam/LP.

#### Rekomendacje
1. **Priorytet 1:** Audyt QS — sprawdź Expected CTR, Ad Relevance, Landing Page Experience dla każdego słowa kluczowego
2. Optymalizuj Demand Gen (3x ROAS) lub wstrzymaj
3. Skaluj — ROAS 12x jest doskonały, IS prawdopodobnie niskie

#### Ocena specjalisty
⭐⭐⭐ (3/5) — Doskonały ROAS, dobra struktura kampanii. Krytyczny problem: QS 3.4 generuje nadmiarowe koszty CPC. Jeden techniczny błąd blokuje dalszy wzrost.

---

### KONTO 7 — Pastform
**ID:** 9975765845 | **Typ:** e-commerce premium (meble, wyposażenie na miarę)

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 19 632 PLN | 18 763 PLN |
| Konwersje | 41 | 34 |
| Wart. konwersji | 233 621 PLN | 201 831 PLN |
| ROAS | 11.9x | 10.8x |
| CPA | ~5 698 PLN | 552 PLN ❌ |
| Avg QS | — | **9.0 / 10** ⭐ |

**Uwaga: CPA 552 PLN** — przy produktach o wartości ~6 000 PLN/transakcja jest to **w normie** (CPA/AOV = 9%). Nie traktuj jako problemu.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [PL][Invette] PM - all [Zasoby] - TOP m | PMax | 5 727 PLN | 5 | 6x | ✅ |
| [PL][Invette] PLA - TOP Komody | Shopping | 4 416 PLN | 5 | 6.7x | ✅ |
| [PL][Invette] PLA - Besty Q1 2026 | Shopping | 2 766 PLN | 7 | 13.7x | ✅ |
| [PL][Invette] PM - all [Zasoby] | PMax | 1 965 PLN | 4 | 11x | ✅ |
| [PL][Invette] DSA | Search | 1 355 PLN | 3 | 15.6x | ✅ |
| [PL][Invette] PLA - Besty | Shopping | 964 PLN | 2 | 19.6x | ✅ |
| [PL][Invette] SCH - Brand | Search | 912 PLN | 7 | 34.9x | ⭐ |
| **[PL][Invette] YT - Wyświetlenia** | Video | **471 PLN** | **0** | 0x | **🔴 Wstrzymaj** |
| [DE] [Invette] SCH - Brand | Search | 187 PLN | 1 | 33.3x | ✅ |

#### Rekomendacje
1. Wstrzymaj YT - Wyświetlenia (471 PLN, 0 konwersji, target CPV)
2. Skaluj agresywnie — ROAS 11x jest doskonały, produkt premium
3. Testuj rynek DE (brand 187 PLN, ROAS 33x) — potencjał ekspansji zagranicznej

#### Ocena specjalisty
⭐⭐⭐⭐ (4/5) — Wzorcowe konto. QS 9.0, doskonały ROAS 11x, segment premium z wysokim AOV. Jedyna wada: nieoptymalna kampania Video. Priorytet agencji: skalowanie.

---

### KONTO 8 — Expertia Naturals
**ID:** 8789715968 | **Typ:** e-commerce (suplementy naturalne, kosmetyki)

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 15 179 PLN | 15 058 PLN |
| Konwersje | 1 187 | 1 175 |
| Wart. konwersji | 258 043 PLN | 257 398 PLN |
| ROAS | 17x | 17.1x |
| CPA | ~13 PLN | 13 PLN |
| Avg QS | — | **9.7 / 10** ⭐ |

**Jeden z 3 najlepszych kont w MCC.** CPA 13 PLN, ROAS 17x, 1 175 konwersji w 30 dni — przy 15K PLN budżetu. Konto **dramatycznie niedoinwestowane** — IS prawidłowo poniżej 50%.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [PROD] pod zimny ruch | Shopping | 5 927 PLN | 210 | 7.3x | ✅ |
| [PM] zasoby i bez | PMax | 4 601 PLN | 151 | 6.8x | ✅ |
| Promocja marzec 2026 | PMax | 2 468 PLN | 179 | 16.9x | ⭐ |
| **YT promocja marzec 2026** | Video | **1 185 PLN** | **3** | 0.3x | 🔴 |
| [TXT] Brand | Search | 877 PLN | 632 | 160x | ⭐ Absolutny lider |

#### Rekomendacje
1. **PILNE:** Skaluj budżet 2–3x (z 15K do 30–45K PLN/msc) — ROAS 17x udźwignie skalowanie
2. Wstrzymaj YT promocja (1 185 PLN, 3 konwersje, ROAS 0.3x)
3. [TXT] Brand (160x ROAS) jest mocno ograniczony budżetem (30 PLN/d) — zwiększ do 100 PLN/d
4. **ALERT dla zarządzającego:** To najlepiej zarządzane konto w MCC. Zadbaj by specjalista pozostał na tym koncie.

#### Ocena specjalisty
⭐⭐⭐⭐⭐ (5/5) — Wzorcowe zarządzanie. ROAS 17x, QS 9.7, niskie CPA, czysta struktura. Jedyna pilna sprawa: skalowanie i wstrzymanie YT.

---

### KONTO 9 — Janda
**ID:** 2019227467 | **Typ:** e-commerce (odzież, akcesoria)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 16 813 PLN |
| Kliknięcia | 16 929 |
| CTR | 3.08% |
| Avg. CPC | 0.99 PLN |
| Konwersje | 1 057 |
| Wart. konwersji | 137 669 PLN |
| ROAS | 8x |
| CPA | 16 PLN |
| Avg QS | **2.8 / 10** ❌ |

**Krytyczny problem:** QS 2.8 to najgorszy wynik wśród kont z dużymi wydatkami. Przy 16 813 PLN/msc i CPC 0.99 PLN — poprawa QS do 7.0 dałaby szac. -35% CPC = ~5 900 PLN oszczędności/msc.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PLA cały asortyment | Shopping | 3 463 PLN | 133 | 5x | ✅ |
| [INV] SEARCH - Brand | Search | 3 213 PLN | 503 | 20.5x | ⭐ |
| [INV] PMAX -40% na wszystko | PMax | 2 949 PLN | 112 | 5x | ✅ |
| [INV] PLA [wybrane serie] | Shopping | 2 734 PLN | 89 | 4.9x | ✅ |
| [INV] PMAX Promocja dzień kobiet | PMax | 2 345 PLN | 136 | 6.8x | ✅ |
| [INV] PMAX do -60% [zasoby] | PMax | 1 338 PLN | 51 | 4.8x | ✅ |
| **[INV] SEA kategorie wiekowe** | Search | **772 PLN** | **4** | 0.7x | 🔴 |

#### Rekomendacje
1. **PRIORYTET 1:** Audyt QS (2.8/10) — analiza Expected CTR + Ad Relevance + Landing Page Experience
2. Wstrzymaj lub zoptymalizuj [INV] SEA kategorie wiekowe (ROAS 0.7x, 772 PLN)
3. Skaluj [INV] SEARCH - Brand (20.5x ROAS, tylko 3 213 PLN/msc)

#### Ocena specjalisty
⭐⭐ (2/5) — Dobre ROAS ogólne ale QS 2.8 to katastrofa. Konto traci ~6K PLN/msc na nadmiarowych CPCach.

---

### KONTO 10 — sklep.delia.pl
**ID:** 4982871984 | **Typ:** e-commerce (kosmetyki, lakiery)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 13 451 PLN |
| Kliknięcia | 20 167 |
| CTR | 1.40% |
| Avg. CPC | 0.67 PLN |
| Konwersje | 299 |
| Wart. konwersji | 17 656 PLN |
| ROAS | **1.3x** 🔴 |
| CPA | 45 PLN |
| Avg QS | 8.6 |

**KRYTYCZNY.** Konto wydaje 13 451 PLN i zarabia 17 656 PLN — przy marży ~30% = strata operacyjna.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| **[GDN] Kampania teaserowa Biedronka** | Display | **3 511 PLN** | 3 | 0.01x | **🔴 STOP** |
| **[YT] Kampania lakiery Biedronka CPM** | Video | **2 656 PLN** | **0** | 0x | **🔴 STOP** |
| PMax: IPLA - Standard - Cameleo | PMax | 2 636 PLN | 83 | 1.6x | ⚠️ |
| PMax: IPLA - Standard - Delia | PMax | 2 482 PLN | 82 | 1.6x | ⚠️ |
| 2dm - SERP - Brand | Search | 1 472 PLN | 101 | 4.8x | ✅ |
| [Pmax] Delia\|Henna Pudrowa | PMax | 538 PLN | 30 | 4.4x | ✅ |
| **[DemGen] Kampania Biedronka** | DemGen | **154 PLN** | **0** | 0x | **🔴 STOP** |

**Diagnoza:** 6 321 PLN (47% budżetu) na kampaniach Display/Video/DemGen bez konwersji. To kampanie brand awareness finansowane z budżetu performanceowego — błąd strategiczny.

#### Rekomendacje
1. **NATYCHMIAST:** Wstrzymaj GDN Teaserowa (3 511 PLN, ROAS 0.01x), YT Lakiery (2 656 PLN, 0 konwersji), DemGen Biedronka (154 PLN, 0 konwersji) → oszczędność 6 321 PLN/msc
2. Z zaoszczędzonego budżetu zwiększ PMax performance (Brand 4.8x, Henna 4.4x)
3. Brand/awareness kampanie powinny mieć osobny, dedykowany budżet
4. Migracja Manual CPC (1 kampania) → Target ROAS

#### Ocena specjalisty
⭐ (1/5) — Fundamentalny błąd budżetowania: kampanie świadomościowe (GDN, YT CPM, DemGen) prowadzone z performance budżetu. Konto generuje straty operacyjne. Wymaga natychmiastowej restrukturyzacji.

---

### KONTO 11 — forcopy.com.pl
**ID:** 2118534299 | **Typ:** e-commerce / lead gen (kserokopiarki, materiały biurowe)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 12 444 PLN |
| Konwersje | 667 |
| Wart. konwersji | **0 PLN** |
| ROAS | 0x |
| CPA | 19 PLN |
| Avg QS | 5.5 |

**KRYTYCZNY.** 667 konwersji przy wartości 0 PLN — brak wartości pieniężnej przypisanej do konwersji. Wszystkie 667 konwersji to prawdopodobnie mikroeventy lub konfiguracja bez wartości.

**Typy kampanii:** Search: 4, PMax: 2, DemGen: 1
**Strategie:** 5x maximize conversions (optymalizuje pod wolumen, nie wartość — błąd)

#### Rekomendacje
1. **PILNE:** Przypisz wartości pieniężne do konwersji lub zmień typ konwersji na zakupy z wartością
2. Zmień strategię z Maximize Conversions na Maximize Conversion Value
3. Sprawdź czy któreś z 667 konwersji to faktyczne zakupy (sprawdź w panelu GA4 po autoryzacji)

#### Ocena specjalisty
⭐ (1/5) — Brak wartości konwersji przy 12 444 PLN wydatków uniemożliwia jakąkolwiek ocenę efektywności. Podstawowy błąd konfiguracji.

---

### KONTO 12 — TOMA
**ID:** 1065983176 | **Typ:** e-commerce (materiały budowlane, parapety)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 7 837 PLN |
| Kliknięcia | 10 523 |
| CTR | 2.57% |
| Avg. CPC | 0.74 PLN |
| Konwersje | **7** |
| Wart. konwersji | 3 714 PLN |
| ROAS | **0.5x** |
| CPA | **1 120 PLN** |

**KATASTROFALNY.** 7 konwersji przy 7 837 PLN wydatków. CPA 1 120 PLN dla produktów materialnych — nie ma biznesowego sensu. Tylko PMax (3 kampanie), strategie Maximize Conversions zamiast Conv. Value.

#### Diagnoza
- CTR 2.57% = kliknięcia są, ale konwersje jednostkowe → problem landing page lub ceny
- Strategia Maximize Conversions (bez wartości) → algorytm generuje kliknięcia, nie zakupy
- Brak Search, brak Shopping Standard — zero kontroli nad zapytaniami

#### Rekomendacje
1. **NATYCHMIAST:** Pauza konta lub całkowita restrukturyzacja
2. Zmień na Shopping Standard z Target ROAS aby odzyskać kontrolę nad zapytaniami
3. Sprawdź landing page — czy strona konwertuje? (GA4 po autoryzacji)
4. Oceń z klientem czy Google Ads ma sens dla tego produktu przy tej cenie

#### Ocena specjalisty
⭐ (1/5) — Konto w katastrofalnym stanie. Prawdopodobna przyczyna: produkt z niską marżą + nieoptymalna strona + brak kontroli nad typem konwersji.

---

### KONTO 13 — stercontrol
**ID:** 4986969025 | **Typ:** e-commerce / B2B (automatyka przemysłowa)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 7 032 PLN |
| Kliknięcia | 22 026 |
| CTR | 2.70% |
| Avg. CPC | 0.32 PLN |
| Konwersje | **19 081** ⚠️ |
| Wart. konwersji | 63 461 PLN |
| ROAS | 9x |
| CPA | ~0.37 PLN |
| Avg QS | 7.0 |

**ANOMALIA:** 19 081 konwersji w 30 dni przy 7 032 PLN = 0.37 PLN/konwersja. To **jednoznaczna mikrokonwersja** — liczą się np. odsłony strony produktu, kliknięcia w menu lub scroll jako konwersja. Faktyczny ROAS nieznany.

**Typy kampanii:** Search: 7, PMax: 1, Shopping: 1
**Problem:** 3 kampanie bez konwersji (s7-1200, eWON) + Manual CPC w 3 kampaniach (powinno być smart bidding)

#### Rekomendacje
1. **PILNE:** Audyt konfiguracji konwersji — zidentyfikuj co liczy się jako "konwersja" (czy to zakupy?)
2. Wstrzymaj 3 kampanie bez konwersji (szac. drenaż 1 500 PLN/msc)
3. Migruj 3 kampanie Manual CPC na Maximize Conversion Value
4. Po ustaleniu prawdziwych konwersji — ponownie oceń ROAS

#### Ocena specjalisty
⭐⭐ (2/5) — Konto wymaga pilnego audytu konwersji. Aktualny wynik 19K "konwersji" jest fałszywym obrazem — niemożliwe do zarządzania bez czystych danych.

---

### KONTO 14 — ASKO sp. z o.o.
**ID:** 4153217999 | **Typ:** e-commerce (meble premium, stolarka)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 6 954 PLN |
| Konwersje | 53 |
| Wart. konwersji | **369 314 PLN** |
| ROAS | **53x** |
| CPA | 131 PLN |
| Avg QS | 7.9 |

**Najlepszy ROAS wśród dużych kont.** 369 314 PLN przychodu przy 6 954 PLN budżetu = ROAS 53x. Produkt premium (~6 968 PLN/transakcja).

**Problem:** 4 kampanie bez konwersji mimo doskonałego konta globalnie. Oznacza to, że 4 kampanie "drenują" budżet który mógłby trafiać na kampanie z 53x ROAS.

#### Kampanie (kwiecień 2026)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| ARCHE Design Table [Search] | Search | 2 871 PLN | 23 | 71x | ⭐ |
| [ARCHE] PLA | Shopping | 1 436 PLN | 15 | 67x | ⭐ |
| [ARCHE] PMax | PMax | 1 024 PLN | 8 | 41x | ✅ |
| [ARCHE] Brand | Search | 687 PLN | 7 | 104x | ⭐ |
| 4 kampanie bez konwersji | mix | ~936 PLN | 0 | 0x | 🔴 |

#### Rekomendacje
1. **NATYCHMIAST:** Zidentyfikuj i wstrzymaj 4 kampanie bez konwersji
2. **PILNE:** Skaluj budżet 2–3x — konto z ROAS 53x jest drastycznie niedoinwestowane
3. Customer Match z bazą historycznych klientów premium

#### Ocena specjalisty
⭐⭐⭐⭐ (4/5) — Doskonały ROAS, premium segment. Jedyna wada: 4 kampanie bez konwersji bez interwencji. Po ich wstrzymaniu → 5/5.

---

### KONTO 15 — IN - SKYCAMP
**ID:** 2438489490 | **Typ:** e-commerce (sprzęt outdoorowy, kampingowy)

| Metryka | Marzec 2026 | Kwiecień 2026 |
|---------|------------|--------------|
| Wydatki | 6 521 PLN | 6 297 PLN |
| Konwersje | 557 | 558 |
| Wart. konwersji | 663 187 PLN | 664 020 PLN |
| ROAS | **101.7x** | **105x** |
| CPA | ~11.7 PLN | 11 PLN |
| Avg QS | — | 6.8 |

**Absolutny lider portfela.** ROAS 105x, CPA 11 PLN, 664 020 PLN przychodów przy 6 297 PLN budżetu. Konto jest **dramatycznie niedoinwestowane** — przy ROAS 105x każda złotówka dodatkowego budżetu generuje 105 złotych przychodu.

**Typy kampanii:** Search: 5, Video: 1, Display: 1, PMax: 1

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [Search kampanie — 5 szt.] | Search | ~5 300 PLN | 558 | ~107x | ⭐ |
| **IN \| YT [wyświetlenia filmu]** | Video | ~500 PLN | **0** | 0x | **🔴 Wstrzymaj** |
| [Display] | Display | ~300 PLN | 0 | 0x | ⚠️ |
| [PMax] | PMax | ~197 PLN | 0 | 0x | ⚠️ |

#### Rekomendacje
1. **NATYCHMIAST:** Wstrzymaj YT wyświetlenia (0 konwersji)
2. **PILNE:** Skaluj budżet 3–5x (z 6K do 18–30K PLN/msc) — przy ROAS 105x to priorytet #1 całego MCC
3. Sprawdź IS (Impression Share) — przy ROAS 105x prawdopodobnie <20% → ogromne straty przychodów z powodu niskiego budżetu
4. Popraw QS (6.8 → 8+) — dodatkowy potencjał

#### Ocena specjalisty
⭐⭐⭐⭐ (4/5) — Znakomite wyniki Search. Brakuje działań: (1) skalowania budżetu, (2) wstrzymania pustych kampanii Video/PMax/Display. Potencjał: największy w całym MCC.

---

### KONTO 16 — Wywozimy
**ID:** 8194750827 | **Typ:** usługi (wywóz odpadów)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 5 461 PLN |
| Konwersje | 164 |
| Wart. konwersji | 2 180 PLN |
| ROAS | 0.4x |
| CPA | 33 PLN |
| Avg QS | **2.4 / 10** ❌ (najgorszy w MCC) |

**QS 2.4 to najniższy wynik w całym MCC.** Przy 5 461 PLN/msc — konto płaci wielokrotnie zawyżone CPCy. Słowa kluczowe, reklamy i strona docelowa są zupełnie niedopasowane.

**Ocena specjalisty:** ⭐ (1/5) — Natychmiastowa przebudowa struktury lub wstrzymanie.

---

### KONTO 17 — Profito
**ID:** 3700097290 | **Typ:** e-commerce (prawdopodobnie finansowy/usługi)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 5 004 PLN |
| Kliknięcia | 1 566 |
| CTR | **12.39%** (anomalia) |
| Konwersje | 323 |
| Wart. konwersji | 3 041 PLN |
| ROAS | 0.6x |
| CPA | 15 PLN |
| Avg QS | **2.8 / 10** ❌ |

**Anomalia CTR 12.39%** przy QS 2.8 sugeruje: reklamy klikane ale landing page nie konwertuje (lub konwertuje mikroeventy). 323 konwersje = 9.4 PLN/konwersja — jednoznaczne mikrokonwersje.

**Ocena specjalisty:** ⭐ (1/5) — Błąd śledzenia konwersji + najgorszy QS wśród kont z wyższymi wydatkami.

---

### KONTA 18–50 — Skrócony przegląd

| Konto | Wydatki | ROAS | QS | Kluczowy problem | Ocena |
|-------|---------|------|-----|-----------------|-------|
| RCL SYSTEM | 7 731 PLN | 1x | 7.6 | CPA 515 PLN — brak optymalizacji | ⭐⭐ |
| LVNSYSTEM | 8 006 PLN | 1x | — | Manual CPC na 3 kamp. Shopping, 3 kamp. bez konw. | ⭐⭐ |
| KuraSport | 7 895 PLN | 4x | 10.0 | ROAS do poprawy, dobra struktura | ⭐⭐⭐ |
| centus_zielonka | 8 979 PLN | 9x | 5.1 | 1 kampania YT bez konwersji, QS do poprawy | ⭐⭐⭐ |
| EcoBeds | 8 926 PLN | 7x | 10.0 | 1 kampania RMKT bez konwersji | ⭐⭐⭐ |
| DD Projekt | 6 623 PLN | 1x | 6.5 | CPA 288 PLN, 1 kampania bez konw. | ⭐⭐ |
| Meblast | 6 588 PLN | 6x | 8.6 | CPA 824 PLN (premium produkt?), Manual CPC | ⭐⭐ |
| Hempets | 6 486 PLN | 1x | 8.8 | Kategoria CBD — trudna, RMKT bez konwersji | ⭐⭐ |
| goralskiciuszek.pl | 6 120 PLN | 3x | 8.0 | 2 kampanie geoexpansji bez konwersji (UK, DE) | ⭐⭐⭐ |
| POLSPORT ORBEA | 5 725 PLN | 2x | 5.8 | 1 623 konwersje = 8.5 PLN/konw. — mikrokonwersje | ⭐⭐ |
| Mr Łoś Sp. z o.o. | 5 691 PLN | 0.3x | 10.0 | 157 konw. = 10 PLN — mikrokonwersje | ⭐⭐ |
| balneokosmetyki.pl | 5 284 PLN | 8x | 3.8 | QS 3.8, YT bez konwersji | ⭐⭐ |
| magdalena24.pl | 4 753 PLN | 13x | 9.2 | YT bez konwersji, Manual CPC | ⭐⭐⭐⭐ |
| Kraksky | 4 314 PLN | 4x | 6.8 | 2 kamp. bez konwersji (Remarketing, YT) | ⭐⭐ |
| Maxdent | 4 027 PLN | 0.05x | 4.3 | 208 konw = 1 PLN — mikro-konw., katastrofa | ⭐ |
| Marcoplast | 3 908 PLN | 0.2x | 6.0 | Manual CPC, brak wartości | ⭐ |
| Singularis | 3 742 PLN | 3x | 10.0 | ROAS do poprawy, dobra struktura | ⭐⭐⭐ |
| deltahr | 3 516 PLN | 19x | 7.7 | 1 kamp. bez konwersji, ogólnie dobry | ⭐⭐⭐⭐ |
| MODENA G. Wróblewski | 3 507 PLN | 12x | — | Brak danych QS, 1 kampania PMax — dobry wynik | ⭐⭐⭐⭐ |
| GT - serwiskawowy | 3 488 PLN | 0.1x | 6.1 | CPA 1 584 PLN, 2 konwersje na 3.5K PLN | ⭐ |
| Instytut Lingwistyki | 3 230 PLN | 3x | 8.0 | CPA 248 PLN — za wysoki dla usług | ⭐⭐ |
| odpady-kontenery | 3 004 PLN | 0.1x | 3.3 | QS 3.3 + ROAS 0.1x — podwójny problem | ⭐ |
| drukujdobrze.pl | 2 987 PLN | 11x | 5.5 | ROAS dobry, QS 5.5 do poprawy | ⭐⭐⭐ |
| Asepta | 10 591 PLN | 5x | 8.1 | 11 kampanii PMax/Shopping/Search — do konsolidacji | ⭐⭐⭐ |
| PMEBLE G. Jakubek | 12 070 PLN | 17x | 9.6 | 1 kamp. YT bez konwersji | ⭐⭐⭐⭐ |
| PLC Nowe Google Ads | 14 651 PLN | 3x | — | Tylko PMax, CTR 16% (anomalia lub Display), brak brand | ⭐⭐ |
| Wedel Pijalnie | 16 547 PLN | 5x | 5.3 | 8 676 konwersji = 9 PLN — mikrokonwersje | ⭐⭐ |

---

## CZĘŚĆ 4 — ANALIZA BCG PORTFELA PRODUKTOWEGO

### 4.1 Rozkład BCG cross-account (marzec 2026)

Dane: 45 kont z aktywnymi danymi Shopping, 57 222 unikalnych produktów (item_id).

| Kwadrant | Produkty | % aktywnych | Wydatki 30d | Przychód 30d | ROAS | Śr. CTR | Śr. Conv. Rate |
|----------|----------|-------------|-------------|-------------|------|---------|----------------|
| ⭐ Gwiazdy | 632 | 16.4% | 60 653 PLN | 893 170 PLN | **14.7x** | 1.40% | 9.92% |
| 🐄 Dojne Krowy | 354 | 9.2% | 79 041 PLN | 487 840 PLN | 6.2x | 1.69% | 4.04% |
| ❓ Znaki Zapytania | 416 | 10.8% | **5 493 PLN** | 116 840 PLN | **21.3x** | 1.46% | 8.33% |
| 🐕 Psy | 14 527 | 378.1% | **137 195 PLN** | 109 721 PLN | **0.8x** | 1.79% | 0.00% |

### 4.2 Kluczowe insighty BCG

**Kryzys alokacji budżetu:**
- Psy (14 527 produktów, 48.6% wydatków) generują 6.8% przychodów
- Gwiazdy (632 produkty, 21.5% wydatków) generują **55.2% przychodów**
- Znaki Zapytania mają ROAS **21.3x** ale pochłaniają tylko **1.9% budżetu** — krytyczne niedoinwestowanie

**Zachowanie Smart Bidding wg kwadrantów:**
- Gwiazdy: algorytm aktywnie skaluje (CTR 1.40%, mediana wzrostu MoM +12%)
- Znaki Zapytania: ROAS 21.3x ale algorytm nie dostał sygnału → budżet zbyt niski
- Psy: CTR 1.79% (wyższy niż Gwiazdy!) ale CR = 0% → problem po stronie LP lub ceny, nie reklamy
- Dojne Krowy: stabilne, MoM +21% kliknięć → faza wzrostu

**Potencjał realokacji:**
Przesunięcie 10% budżetu z Psów (–13 720 PLN) na Znaki Zapytania (+13 720 PLN) przy ROAS 21.3x = +292 236 PLN dodatkowych przychodów/msc.

### 4.3 Konta z dominacją Psów i potencjałem ZQ

| Konto | % Psów | Psów (n) | ZQ z wzrostem >20% | Wydatki | ROAS | Priorytet feedaudit |
|-------|--------|----------|-------------------|---------|------|---------------------|
| Optimum BHP | 96% | ~320 | 29 | 18 392 PLN | 3.5x | Bardzo wysoki |
| Pastform | 91% | ~300 | — | 13 882 PLN | 7.8x | Wysoki |
| IdeaShirt | 93% | ~1000 | 66 | 15 254 PLN | 6.1x | Bardzo wysoki |
| MegaKoszulki.pl | 91% | ~800 | 13 | 7 634 PLN | 4.0x | Wysoki |
| EcoBeds | 87% | ~130 | 13 | 7 815 PLN | 7.4x | Wysoki |
| centus_zielonka | 86% | ~200 | 15 | 7 016 PLN | 8.9x | Wysoki |
| PaDrew | 76% | ~110 | — | 13 182 PLN | 11.1x | Średni |
| TABLE4U | 81% | 195 | 6 | 46 451 PLN | 5.2x | Bardzo wysoki |
| Synthagen Labs | 62% | ~250 | — | 38 984 PLN | 1.9x | Krytyczny |

---

## CZĘŚĆ 5 — ANALIZA QUALITY SCORE PORTFELA

### 5.1 Rozkład QS wśród kont aktywnych

| Zakres QS | Konta | Łączne wydatki | Ocena |
|-----------|-------|----------------|-------|
| 9.0–10.0 (wzorcowe) | Optimum BHP 9.7, Expertia 9.7, PMEBLE 9.6, Pastform 9.0, Hempets 8.8, Janda (nie!), magdalena24 9.2, Meblast 8.6, sklep.delia 8.6 | ~110 000 PLN | ⭐ |
| 7.0–8.9 (dobre) | IdeaShirt 8.0, Synthagen 8.2, Asepta 8.1, EcoBeds 10.0, KuraSport 10.0, Singularis 10.0, Mr Łoś 10.0, stercontrol 7.0, ASKO 7.9 | ~120 000 PLN | ✅ |
| 5.0–6.9 (wymaga pracy) | MegaKoszulki 7.4, IN-SKYCAMP 6.8, deltahr 7.7, Kraksky 6.8, forcopy 5.5, GT 6.1, Marcoplast 6.0, POLSPORT 5.8, DD Projekt 6.5 | ~65 000 PLN | ⚠️ |
| <5.0 (krytyczny) | **TABLE4U 3.3, PaDrew 3.4, Janda 2.8, Wywozimy 2.4, balneokosmetyki 3.8, Profito 2.8, odpady 3.3, Maxdent 4.3, Oknobank 4.4, Adrian Romkowski 4.4** | ~90 000 PLN | 🔴 |

**Konta z najniższym QS i najwyższymi wydatkami (pilna interwencja):**
1. TABLE4U — QS 3.3, 66 325 PLN/msc — szac. nadmiar CPC: **~10 000–15 000 PLN/msc**
2. Janda — QS 2.8, 16 813 PLN/msc — szac. nadmiar CPC: **~5 900 PLN/msc**
3. PaDrew — QS 3.4, 18 792 PLN/msc — szac. nadmiar CPC: **~3 000 PLN/msc**

---

## CZĘŚĆ 6 — ŚLEDZENIE I KONFIGURACJA KONWERSJI

### 6.1 Typologia problemów ze śledzeniem

| Typ problemu | Konta | Wpływ |
|-------------|-------|-------|
| **Mikrokonwersje zamiast zakupów** | stercontrol (19 081 konw/msc!), POLSPORT (1 623 konw = 8.5 PLN), Maxdent (208 konw = 1 PLN), Profito (323 konw = 9.4 PLN), Mr Łoś (157 konw = 10 PLN) | Fałszywe sygnały dla Smart Bidding → nieoptymalne alokacje |
| **Brak wartości konwersji** | forcopy (667 konw, wartość 0 PLN), ~20 kont lead gen | Brak możliwości Target ROAS, zła strategia bidowania |
| **Zero konwersji na koncie** | Fizjoterapia Mazur, Omega Kserokopiarki, PenPol, CRMC, NOWE medihurt, INVETTE, Zakatek, UQUINA, REVES, Pet Vital | 12 700 PLN/msc bez efektu |
| **GA4 brak dostępu** | 100% kont | Brak cross-platform weryfikacji, brak bounce rate, brak ścieżek |

### 6.2 Weryfikacja GA4 — blokada systemowa

> ⚠️ Wszystkie konta w MCC mają zablokowany dostęp do GA4 API.
> Token: `bdos auth --add analytics` → zaloguj na invette.sem@gmail.com
> Do weryfikacji po autoryzacji dla każdego konta:
> - Czy GA4 jest połączone z Google Ads?
> - Delta przychodów GA4 vs Ads (akceptowalna < 15%)
> - Bounce rate kampanii płatnych vs organic
> - Ścieżki konwersji wielodotykowe

---

## CZĘŚĆ 7 — REKOMENDACJE STRATEGICZNE

### 7.1 Akcje natychmiastowe (0–7 dni) — zatamowanie strat

| Priorytet | Działanie | Konto | Szac. efekt finansowy |
|-----------|-----------|-------|----------------------|
| P0 | Wstrzymaj kampanie Video/Display bez konwersji | sklep.delia.pl | +6 321 PLN odzysku/msc |
| P0 | Wstrzymaj YT VideoViews (0 konwersji) | TABLE4U | +449 PLN/msc |
| P0 | Wstrzymaj YT Wyświetlenia | Pastform | +471 PLN/msc |
| P0 | Wstrzymaj Display Remarketing | Synthagen | +911 PLN/msc |
| P0 | Wstrzymaj YT Promocja marzec | Expertia | +1 185 PLN/msc |
| P0 | Wstrzymaj 4 kampanie bez konwersji | ASKO | ~1 000 PLN/msc |
| P0 | Wstrzymaj Demand Gen (ROAS 0.17x) | IdeaShirt | +3 541 PLN/msc |
| P0 | Zdiagnozuj i wstrzymaj konta 0 konwersji | PenPol, Fizjoterapia, CRMC | +5 800 PLN/msc |
| P0 | Pauza lub przebudowa | TOMA | +7 837 PLN/msc zatamowania |

**Łączny szac. efekt natychmiastowych działań: +27 515 PLN/msc** (odzysk lub zatamowanie strat)

### 7.2 Optymalizacja (miesiąc 1)

| Działanie | Konta | Efekt |
|-----------|-------|-------|
| Poprawa Quality Score | TABLE4U (3.3), Janda (2.8), PaDrew (3.4), Wywozimy (2.4), Profito (2.8), odpady (3.3) | Obniżka CPC ~20–40% na tych kontach = szac. ~20 000 PLN/msc oszczędności |
| Feed audit — Psy BCG | TABLE4U (195 Psów), IdeaShirt (93%), Optimum BHP (96%), Synthagen (62%) | ROAS +20–40% na feedowych kampaniach |
| Wydziel Znaki Zapytania | IdeaShirt (66 ZQ), Optimum BHP (29 ZQ), centus_zielonka (15 ZQ) | ROAS 21.3x dostępny dla tych produktów |
| Audyt konwersji | stercontrol, POLSPORT, Maxdent, Profito, forcopy | Czyste dane → poprawne Smart Bidding |
| GA4 autoryzacja | Wszystkie konta | Cross-platform weryfikacja |

### 7.3 Skalowanie liderów (miesiąc 2–3)

Konta z wysokim ROAS i prawdopodobnie niskim IS — każda złotówka dodanego budżetu generuje proporcjonalny zwrot:

| Konto | ROAS | Obecny budżet/msc | Zalecany budżet | Szac. wzrost przychodów |
|-------|------|------------------|----------------|------------------------|
| IN - SKYCAMP | **105x** | 6 297 PLN | 20 000 PLN | +1 430 000 PLN/msc |
| ASKO sp. z o.o. | **53x** | 6 954 PLN | 15 000 PLN | +425 000 PLN/msc |
| Expertia Naturals | **17x** | 15 058 PLN | 35 000 PLN | +340 000 PLN/msc |
| deltahr | **19x** | 3 516 PLN | 8 000 PLN | +85 500 PLN/msc |
| PMEBLE G. Jakubek | **17x** | 12 070 PLN | 25 000 PLN | +220 000 PLN/msc |
| PaDrew | **12x** | 18 792 PLN | 35 000 PLN | +194 000 PLN/msc |
| Pastform | **12x** | 18 763 PLN | 35 000 PLN | +194 000 PLN/msc |
| MODENA | **12x** | 3 507 PLN | 8 000 PLN | +54 000 PLN/msc |

---

## CZĘŚĆ 8 — OCENA OGÓLNA AGENCJI INVETTE

### 8.1 Ocena per obszar

| Obszar | Ocena | Komentarz |
|--------|-------|-----------|
| ROAS portfela | ⚠️ 5.7x | Dobry wynik, ale silnie ciągną go liderzy — dolna ćwiartka generuje straty |
| Monitoring problematycznych kont | 🔴 Brak reakcji | 22 konta z ROAS <2x, brak interwencji; 10 kont 0 konwersji |
| Konfiguracja konwersji | 🔴 Wielokrotne błędy | Mikrokonwersje, brak wartości, brak GA4 dostępu |
| Feed / BCG management | 🔴 Brak | 48.6% budżetu na Psach (ROAS 0.8x), brak custom labels BCG |
| Quality Score | 🔴 Krytyczny | 4 największe konta z QS <4.0 — ~20 000 PLN/msc nadmiarowych CPC |
| Skalowanie liderów | 🔴 Brak | IN-SKYCAMP (105x) przy 6K PLN budżetu = ogromna strata szans |
| Struktura kampanii | ⚠️ Mixowana | Część kont dobrze zarządzana, część bez podstawowej optymalizacji |
| Enhanced Conversions | 🔴 Brak danych | GA4 brak dostępu — nie możemy zweryfikować |
| Customer Match | 🔴 Brak danych | Nie zweryfikowane — prawdopodobnie niewykorzystane |

### 8.2 Ocena zbiorcza

**Wynik portfela: ⭐⭐ (2/5)**

**Uzasadnienie:**
- Portfel ma silnych liderów (TABLE4U, IdeaShirt, Expertia, PaDrew, Pastform, IN-SKYCAMP, ASKO) które maskują skalę problemów
- Dolna ćwiartka kont (~30 kont z 90 aktywnych) generuje straty lub zerowe efekty bez żadnej interwencji
- Brak proaktywnego monitoringu — problemy jak TOMA (0.5x ROAS), sklep.delia (display bez konwersji), Janda (QS 2.8) istnieją miesiącami bez reakcji
- Największe single quick wins są dostępne natychmiastowo: wstrzymanie ~15 pustych kampanii Video/Display = ~14 500 PLN/msc
- Dramatyczne niedoinwestowanie liderów — IN-SKYCAMP (105x) przy 6 297 PLN to utrata ~660K PLN przychodów potencjalnych miesięcznie

**Mocne strony agencji:**
- Dobre konta mają bardzo dobrą strukturę (Pastform QS 9.0, Optimum BHP QS 9.7, Expertia QS 9.7)
- Naming convention kampanii czytelna (prefiks [INV], [AT], [AdVist])
- Dywersyfikacja typów kampanii (PMax, Search, Shopping, DemGen)
- Brand campaigns wdrożone na kluczowych kontach

**Słabe strony agencji:**
- Reaktywne zarządzanie — problemy narastają bez interwencji
- Brak BCG-driven feed management
- Brak GA4 integracji dla audytu (token niezaktualizowany)
- Quality Score kluczowych kont nie monitorowany
- Skalowanie bez sprawdzenia opłacalności (Synthagen: +168% budżetu przy spadku ROAS)

---

*Raport przygotowany na podstawie:*
*GAdsBDOS_audyt.md (BDOS AI v1.0.9 — marzec 2026) + Invette_audit_v2.md (BDOS AI v1.0 — kwiecień 2026)*
*MCC: 934-203-1404 | Agencja: Invette.pl | Data raportu: 03.04.2026*
