# AUDYT MARTECH — INVETTE MCC
## Raport Zbiorczy | Kwiecień 2026

**MCC:** 934-203-1404 | **Agencja:** Invette.pl
**Data audytu:** 03.04.2026
**Okres analizy:** ostatnie 30 dni (marzec–kwiecień 2026)
**Źródło danych:** BDOS AI v1.0.9 (marzec 2026) + BDOS AI v1.0 (02.04.2026)
**Lokalizacja:** `C:\Users\adria\Documents\AI\AUDYT\MarTech\invette\`

> **⚠️ Uwaga dot. GA4 / GTM:**
> Brak autoryzacji do Google Analytics API (`bdos auth --add analytics` niezrealizowane).
> Sekcje GA4, GTM, sGTM, Enhanced Conversions, Customer Match — oznaczone jako `❓ Wymaga weryfikacji`.
> Do realizacji po autoryzacji na: `invette.sem@gmail.com`

---

## CZĘŚĆ 0 — DANE PORTFELA MCC

### 0.1 — Statystyki globalne (ostatnie 30 dni)

| Metryka | Wartość |
|---------|---------|
| Kont łącznie w MCC | **150** |
| Kont z wydatkami (aktywnych) | **94** |
| Kont nieaktywnych (0 wydatków) | **56** |
| Łączne wydatki (94 konta) | **~630 000 PLN** |
| Łączna wartość konwersji | **~4 262 000 PLN** |
| ROAS portfela (wszystkie aktywne) | **~6.8x** |
| Łączne konwersje | **~41 000** |
| Kont z ROAS < 2x (e-commerce) | **22 konta** |
| Kont z 0 konwersjami | **10 kont** |
| Kont lead gen (bez wartości konw.) | **~20 kont** |

### 0.2 — Łączne wyniki kont produktowych (marzec 2026)

| Metryka | Wartość |
|---------|---------|
| Kont z danymi produktowymi | 45 |
| Wydatki (45 kont) | 282 382 PLN |
| Wartość konwersji (45 kont) | 1 618 388 PLN |
| ROAS portfela produktowego | **5.7x** |
| Produktów unikalnych (item_id) | 57 222 |
| Produktów aktywnych (min. 10 kliknięć) | 3 842 |

### 0.3 — Segmentacja kont wg statusu

| Status | Liczba kont | Łączne wydatki | Opis |
|--------|-------------|----------------|------|
| ✅ OK | ~22 konta | ~180 000 PLN | Brak krytycznych problemów |
| ⚠️ Uwaga | ~16 kont | ~95 000 PLN | ROAS do poprawy lub kampanie bez konwersji |
| 🔴 Problem | ~22 konta | ~107 000 PLN | Straty lub brak efektów — pilna interwencja |
| ℹ️ Lead gen | ~20 kont | ~45 000 PLN | Brak wartości konwersji — wymaga konfiguracji |
| 💤 Nieaktywne | 56 kont | 0 PLN | Brak wydatków — weryfikacja kontraktów |

### 0.4 — Infrastruktura MarTech portfela — status

| Komponent | Status portfela | Priorytet |
|-----------|----------------|-----------|
| GA4 Analytics API | ❌ Brak autoryzacji (bdos auth --add analytics) | 🔴 Pilny |
| GTM kontenery | ❓ Bez weryfikacji (brak dostępu API) | 🟡 Ważny |
| Server-side GTM | ❓ Status nieznany per konto | 🟡 Ważny |
| Enhanced Conversions | ❓ Status nieznany (brak GA4 API) | 🟡 Ważny |
| Customer Match | ❓ Status nieznany | 🟢 Zalecane |
| GA4 ↔ Google Ads połączenie | ❓ Do weryfikacji per konto | 🟡 Ważny |
| Consent Mode v2 | ❓ Do weryfikacji per konto | 🔴 Pilny (wymóg EU) |

---

## CZĘŚĆ 1 — TABELA PRZESTAWNA WSZYSTKICH KONT AKTYWNYCH (94)

### 1.1 — Przegląd błędów i problemów per konto

| # | Konto | Wydatki | ROAS | Konw. | 0-konw. | Niski QS | Status |
|---|-------|---------|------|-------|---------|---------|--------|
| 1 | TABLE4U | 66 325 PLN | 8.7x | 178 | ✅ | 🔴 QS 3.3 | ⚠️ |
| 2 | Synthagen Labs | 61 993 PLN | 2.0x | 282 | ✅ | ✅ QS 8.2 | 🔴 |
| 3 | IdeaShirt | 58 367 PLN | 5.8x | 1 353 | ✅ | ✅ QS 8.0 | ⚠️ |
| 4 | Optimum BHP | 42 748 PLN | 3.9x | 344 | ✅ | ✅ QS 9.7 | ⚠️ |
| 5 | MegaKoszulki.pl | 23 316 PLN | 5.0x | 846 | ✅ | ✅ QS 7.4 | ⚠️ |
| 6 | PaDrew | 18 792 PLN | 11.9x | 134 | ✅ | 🔴 QS 3.4 | ⚠️ |
| 7 | Pastform | 18 763 PLN | 10.8x | 34 | ⚠️ 1 kamp. | ✅ QS 9.0 | ⚠️ |
| 8 | Janda | 16 813 PLN | 8.2x | 1 057 | ✅ | 🔴 QS 2.8 | ⚠️ |
| 9 | Wedel Pijalnie | 16 547 PLN | 4.6x | 8 676 | ✅ | ⚠️ QS 5.3 | ⚠️ |
| 10 | Expertia Naturals | 15 058 PLN | 17.1x | 1 175 | ✅ | ✅ QS 9.7 | ✅ |
| 11 | PLC Nowe Google Ads | 14 651 PLN | 3.2x | 144 | ✅ | — | ⚠️ |
| 12 | sklep.delia.pl | 13 451 PLN | 1.3x | 299 | ⚠️ 2 kamp. | ✅ QS 8.6 | 🔴 |
| 13 | forcopy.com.pl | 12 444 PLN | 0x | 667 | ✅ | ⚠️ QS 5.5 | 🔴 |
| 14 | PMEBLE G. Jakubek | 12 070 PLN | 16.9x | 158 | ✅ | ✅ QS 9.6 | ✅ |
| 15 | Asepta | 10 591 PLN | 5.1x | 198 | ✅ | ✅ QS 8.1 | ⚠️ |
| 16 | centus_zielonka | 8 979 PLN | 9.3x | 225 | ⚠️ 1 kamp. | ⚠️ QS 5.1 | ⚠️ |
| 17 | EcoBeds | 8 926 PLN | 7.0x | 149 | ⚠️ 1 kamp. | ✅ QS 10.0 | ⚠️ |
| 18 | LVNSYSTEM | 8 006 PLN | 0.6x | 74 | ⚠️ 3 kamp. | — | 🔴 |
| 19 | KuraSport | 7 895 PLN | 3.8x | 261 | ✅ | ✅ QS 10.0 | ⚠️ |
| 20 | TOMA | 7 837 PLN | 0.5x | 7 | ✅ | — | 🔴 |
| 21 | RCL SYSTEM | 7 731 PLN | 1.3x | 15 | ✅ | ✅ QS 7.6 | 🔴 |
| 22 | stercontrol | 7 032 PLN | 9.0x | 19 081 | ⚠️ 3 kamp. | ✅ QS 7.0 | ⚠️ |
| 23 | ASKO sp. z o.o. | 6 954 PLN | **53.1x** | 53 | ⚠️ 4 kamp. | ✅ QS 7.9 | ✅ |
| 24 | DD Projekt | 6 623 PLN | 1.1x | 23 | ⚠️ 1 kamp. | ✅ QS 6.5 | 🔴 |
| 25 | Meblast | 6 588 PLN | 6.2x | 8 | ✅ | ✅ QS 8.6 | ⚠️ |
| 26 | Hempets | 6 486 PLN | 0.6x | 17 | ⚠️ 1 kamp. | ✅ QS 8.8 | 🔴 |
| 27 | IN - SKYCAMP | 6 297 PLN | **105.4x** | 558 | ⚠️ 1 kamp. | ✅ QS 6.8 | ✅ |
| 28 | goralskiciuszek.pl | 6 120 PLN | 3.3x | 106 | ⚠️ 2 kamp. | ✅ QS 8.0 | ⚠️ |
| 29 | POLSPORT ORBEA | 5 725 PLN | 2.4x | 1 623 | ✅ | ⚠️ QS 5.8 | ⚠️ |
| 30 | Mr Łoś Sp. z o.o. | 5 691 PLN | 0.3x | 157 | ✅ | ✅ QS 10.0 | 🔴 |
| 31 | Adrian Romkowski | 5 591 PLN | 0x (lead) | 63 | ✅ | ⚠️ QS 4.4 | ℹ️ |
| 32 | Wywozimy | 5 461 PLN | 0.4x | 164 | ✅ | 🔴 QS 2.4 | 🔴 |
| 33 | balneokosmetyki.pl | 5 284 PLN | 8.1x | 290 | ⚠️ 1 kamp. | 🔴 QS 3.8 | ⚠️ |
| 34 | Profito | 5 004 PLN | 0.6x | 323 | ✅ | 🔴 QS 2.8 | 🔴 |
| 35 | magdalena24.pl | 4 753 PLN | 13.0x | 337 | ⚠️ 1 kamp. | ✅ QS 9.2 | ✅ |
| 36 | Kraksky | 4 314 PLN | 4.3x | 20 | ⚠️ 2 kamp. | ✅ QS 6.8 | ⚠️ |
| 37 | Maxdent | 4 027 PLN | 0.05x | 208 | ✅ | ⚠️ QS 4.3 | 🔴 |
| 38 | Marcoplast | 3 908 PLN | 0.2x | 13 | ✅ | ✅ QS 6.0 | 🔴 |
| 39 | Phinance | 3 770 PLN | 0x (lead) | 12 | ✅ | ⚠️ QS 5.9 | ℹ️ |
| 40 | Singularis | 3 742 PLN | 3.2x | 70 | ✅ | ✅ QS 10.0 | ✅ |
| 41 | deltahr | 3 516 PLN | 18.7x | 109 | ⚠️ 1 kamp. | ✅ QS 7.7 | ✅ |
| 42 | MODENA G. Wróblewski | 3 507 PLN | 12.5x | 198 | ✅ | — | ✅ |
| 43 | GT - serwiskawowy | 3 488 PLN | 0.1x | 2 | ⚠️ 1 kamp. | ✅ QS 6.1 | 🔴 |
| 44 | SEZARO Sp. z o.o. | 3 369 PLN | 0x (lead) | 13 | ✅ | ⚠️ QS 5.8 | ℹ️ |
| 45 | OKULUS PLUS | 3 299 PLN | 0x (lead) | 23 | ✅ | ✅ QS 8.6 | ℹ️ |
| 46 | Instytut Lingwistyki | 3 230 PLN | 3.3x | 13 | ✅ | ✅ QS 8.0 | ⚠️ |
| 47 | KANTÓWKA Sp. z o.o. | 3 027 PLN | 0x (lead) | 36 | ✅ | ✅ QS 6.7 | ℹ️ |
| 48 | odpady-kontenery | 3 004 PLN | 0.1x | 38 | ✅ | 🔴 QS 3.3 | 🔴 |
| 49 | drukujdobrze.pl | 2 987 PLN | 11.0x | 143 | ✅ | ⚠️ QS 5.5 | ✅ |
| 50 | Oknobank | 2 947 PLN | 0.03x | 103 | ✅ | ⚠️ QS 4.4 | ℹ️ |
| 51 | Herb Yourself | 2 909 PLN | 0x | 23 | ✅ | ✅ QS 6.8 | 🔴 |
| 52 | PenPol [nowe 2026] | 2 831 PLN | 0x | **0** | 🔴 | — | 🔴 |
| 53 | Hauptmann Nowe | 2 823 PLN | 0.6x | 8 | ✅ | ⚠️ QS 4.8 | 🔴 |
| 54 | Fizjoterapia Mazur | 2 807 PLN | 0x | **0** | 🔴 | — | 🔴 |
| 55 | FENIX ART | 2 747 PLN | 5.2x | 5 | ✅ | ✅ QS 6.0 | ⚠️ |
| 56 | Smart Clinic | 2 570 PLN | 0.07x | 186 | ✅ | ✅ QS 7.5 | 🔴 |
| 57 | Marina Spices | 2 540 PLN | 1.7x | 93 | ✅ | — | ⚠️ |
| 58 | Gestia | 2 463 PLN | 0.02x | 42 | ✅ | 🔴 QS 3.2 | 🔴 |
| 59 | Omega Kserokopiarki | 2 427 PLN | 0x | **0** | 🔴 | 🔴 QS 2.3 | 🔴 |
| 60 | Słodycze z pomysłem | 2 422 PLN | 0.05x | 139 | ✅ | ✅ QS 6.3 | 🔴 |
| 61 | KANCELARIA WYLĄG | 2 399 PLN | 0x (lead) | 14 | ✅ | 🔴 QS 3.6 | ℹ️ |
| 62 | WBL Invest | 1 889 PLN | 0x (lead) | 17 | ✅ | 🔴 QS 2.9 | ℹ️ |
| 63 | fitME | 1 748 PLN | 0.6x | 7 | ✅ | — | 🔴 |
| 64 | Dziewiąta Planeta | 1 725 PLN | 1.1x | 9 | ✅ | ✅ QS 8.4 | ⚠️ |
| 65 | KrainaHerbaty PL | 1 648 PLN | 2.1x | 32 | ✅ | ✅ QS 9.3 | ⚠️ |
| 66 | Desque | 1 614 PLN | **15.3x** | 58 | ✅ | — | ✅ |
| 67 | LycopenPRO | 1 553 PLN | 2.0x | 9 | ✅ | ✅ QS 9.0 | ⚠️ |
| 68 | PenPol (stare konto) | 1 532 PLN | 0x | 2 | ✅ | ✅ QS 9.5 | 🔴 |
| 69 | Życie bez protez | 1 479 PLN | 0.03x | 49 | ✅ | ✅ QS 6.2 | 🔴 |
| 70 | CRMC | 1 449 PLN | 0x | **0** | 🔴 | 🔴 QS 3.9 | 🔴 |
| 71 | Wiksonspas | 1 328 PLN | 0x (lead) | 5 | ✅ | ⚠️ QS 5.6 | ℹ️ |
| 72 | Vago | 1 258 PLN | 0x (lead) | 11 | ✅ | ⚠️ QS 5.3 | ℹ️ |
| 73 | NOWE medihurt.com | 1 162 PLN | 0x | **0** | 🔴 | — | 🔴 |
| 74 | INVETTE (własne) | 1 141 PLN | 0x | **0** | 🔴 | — | 🔴 |
| 75 | Leśne Życie | 1 084 PLN | 0.5x | 8 | ✅ | 🔴 QS 1.4 | 🔴 |
| 76 | MetBud | 1 027 PLN | 0.2x | 33 | ✅ | ⚠️ QS 4.9 | 🔴 |
| 77 | Auto Pietrzycki | 1 017 PLN | 0x (lead) | 10 | ✅ | ✅ QS 6.3 | ℹ️ |
| 78 | Viperbox | 948 PLN | 0x (lead) | 15 | ✅ | ⚠️ QS 5.3 | ℹ️ |
| 79 | Badum | 876 PLN | 0.6x | 19 | ✅ | — | ⚠️ |
| 80 | Kariera w Farmacji | 732 PLN | 5.9x | 11 | ✅ | — | ✅ |
| 81 | Insector NEW | 604 PLN | 0x (lead) | 10 | ✅ | ⚠️ QS 4.6 | ℹ️ |
| 82 | Ita Support | 587 PLN | 0.07x | 7 | ✅ | ⚠️ QS 5.8 | 🔴 |
| 83 | Zakatek Fantastyki | 567 PLN | 0x | **0** | 🔴 | ⚠️ QS 5.6 | 🔴 |
| 84 | Sklep UQUINA | 503 PLN | 0x | **0** | 🔴 | — | 🔴 |
| 85 | PROBALANS | 400 PLN | 0x (lead) | 9 | ✅ | 🔴 QS 2.2 | ℹ️ |
| 86 | SOTBE | 313 PLN | 0.05x | 15 | ✅ | — | 🔴 |
| 87 | THERMO-INSTAL | 290 PLN | 0x (lead) | 3 | ✅ | ⚠️ QS 4.3 | ℹ️ |
| 88 | Polskie Meble - REVES | 225 PLN | 0x | **0** | 🔴 | — | 🔴 |
| 89 | Pet Vital | 206 PLN | 0x | **0** | 🔴 | ✅ QS 7.3 | 🔴 |
| 90 | Happy Biotics | 193 PLN | 1.7x | 1 | ✅ | ✅ QS 10.0 | ⚠️ |
| 91 | Fundacja Promyczek | 176 PLN | 0.5x | 73 | ✅ | ✅ QS 8.0 | ⚠️ |
| 92 | KrainaHerbaty CSS | 39 PLN | **30.0x** | 15 | ✅ | — | ✅ |
| 93 | SystemCOLD | 1 PLN | 0x | 0 | ✅ | — | ℹ️ |
| 94 | Webchefs | 0 PLN | 0x | 0 | — | — | 💤 |

**Legenda:** ✅ OK | ⚠️ Uwaga | 🔴 Problem | ℹ️ Lead gen (brak wartości) | 💤 Faktycznie nieaktywne

---

## CZĘŚĆ 2 — PROBLEMY SYSTEMOWE

### 2.1 — 🔴 Konta e-commerce z ROAS < 2x (~107 000 PLN/msc w stratach)

| Konto | Wydatki | ROAS | Szac. strata/msc | Diagnoza |
|-------|---------|------|-----------------|---------|
| Synthagen Labs | 61 993 PLN | 2.0x | Granica opłac. | Skalowanie 2.7x bez poprawy ROAS — ryzyko |
| sklep.delia.pl | 13 451 PLN | 1.3x | ~3 600 PLN | 2 kampanie bez konwersji (YT+DemGen = 6K PLN) |
| LVNSYSTEM | 8 006 PLN | 0.6x | ~5 600 PLN | Manual CPC na Shopping, 3 kampanie bez konw. |
| TOMA | 7 837 PLN | 0.5x | ~6 300 PLN | 7 konwersji przy 7.8K budżetu — katastrofa |
| RCL SYSTEM | 7 731 PLN | 1.3x | ~2 600 PLN | CPA 515 PLN — brak Smart Bidding |
| DD Projekt | 6 623 PLN | 1.1x | ~600 PLN | 1 kampania bez konwersji (800 PLN) |
| Hempets | 6 486 PLN | 0.6x | ~4 500 PLN | Kategoria CBD/hemp — trudna konwersja |
| Mr Łoś Sp. z o.o. | 5 691 PLN | 0.3x | ~4 700 PLN | 157 konwersji = 10 PLN/konw. — błąd śledzenia |
| Wywozimy | 5 461 PLN | 0.4x | ~4 000 PLN | QS 2.4 — ruch nieintencjonalny |
| forcopy.com.pl | 12 444 PLN | 0x | ~12 444 PLN | Brak wartości konwersji w Google Ads |
| Profito | 5 004 PLN | 0.6x | ~3 000 PLN | QS 2.8, 323 konwersje = 9 PLN/konw. — błąd |
| Maxdent | 4 027 PLN | 0.05x | ~3 900 PLN | 208 konwersji = 1 PLN/konw. — błąd trackingu |
| Marcoplast | 3 908 PLN | 0.2x | ~3 300 PLN | Shopping 1 PLN/konw. — błąd śledzenia |
| GT - serwiskawowy | 3 488 PLN | 0.1x | ~3 350 PLN | 2 konwersje, CPA 1 584 PLN |
| odpady-kontenery | 3 004 PLN | 0.1x | ~2 900 PLN | QS 3.3, wartość 335 PLN |

**Łączny drenaż e-commerce (ROAS < 2x): ~60 000–107 000 PLN/msc**

### 2.2 — ⚠️ Kampanie aktywne bez konwersji — ~14 500 PLN/msc drenażu

| Konto | Kamp. bez konw. | Drenaż/msc | Najdroższa kampania bez konw. |
|-------|-----------------|------------|-------------------------------|
| ASKO | 4 kamp. | ~2 000 PLN | Search / DemGen |
| stercontrol | 3 kamp. | ~1 500 PLN | s7-1200, eWON |
| LVNSYSTEM | 3 kamp. | ~2 500 PLN | DSA All Pages, YouTube |
| Kraksky | 2 kamp. | ~1 800 PLN | High Intent PL REM, YT |
| goralskiciuszek.pl | 2 kamp. | ~1 000 PLN | kampanie UK/DE |
| sklep.delia.pl | 2 kamp. | ~2 800 PLN | **YT Biedronka CPM (2 656 PLN!)** |
| Pastform | 1 kamp. | ~471 PLN | YT Wyświetlenia |
| centus_zielonka | 1 kamp. | ~500 PLN | YT |
| EcoBeds | 1 kamp. | ~400 PLN | PLA RMKT |
| balneokosmetyki.pl | 1 kamp. | ~300 PLN | YT |
| DD Projekt | 1 kamp. | ~800 PLN | SEA Remonty |
| magdalena24.pl | 1 kamp. | ~400 PLN | YouTube filmy |

### 2.3 — 🔴 Konta z zerowymi konwersjami na całym koncie (~12 700 PLN/msc)

| Konto | ID | Wydatki | Kampanie | Diagnoza |
|-------|----|---------|---------|---------|
| PenPol [nowe 2026] | 7482901847 | 2 831 PLN | PMax, Shopping | Nowe konto — błąd konfiguracji konwersji |
| Fizjoterapia Mazur | 8394829174 | 2 807 PLN | Search | Całkowity brak konwersji — tracking lub LP |
| Omega Kserokopiarki | 4506143606 | 2 427 PLN | Search | QS 2.3 — słowa kluczowe niedopasowane |
| CRMC | 4750835647 | 1 449 PLN | Search | QS 3.9 — ruch niskiej jakości |
| NOWE medihurt.com | 7280666733 | 1 162 PLN | PMax, Search | Nowe konto — brak konwersji |
| INVETTE (własne) | 9195220076 | 1 141 PLN | Video | Video only — zły typ kampanii |
| Zakatek Fantastyki | 5395326495 | 567 PLN | Search | Konto USD — błąd konfiguracji |
| Sklep UQUINA | 9562321521 | 503 PLN | Shopping | Brak trackingu zakupów |
| Polskie Meble - REVES | 3943920194 | 225 PLN | Smart | Brak konwersji |
| Pet Vital | 6053963790 | 206 PLN | PMax, Search | Brak konwersji mimo dobrego QS 7.3 |

**Łącznie: ~13 318 PLN/msc bez żadnego mierzalnego efektu**

### 2.4 — 📊 Liderzy portfela niedoinwestowani

| Konto | ROAS | Budżet/msc | IS (est.) | Potencjał skalowania |
|-------|------|-----------|-----------|---------------------|
| IN-SKYCAMP | **105.4x** | 6 297 PLN | < 20% | **3–5x budżetu = +300 000–600 000 PLN/msc** |
| ASKO sp. z o.o. | **53.1x** | 6 954 PLN | < 25% | 2–3x budżetu = +350 000–700 000 PLN/msc |
| Expertia Naturals | **17.1x** | 15 058 PLN | < 40% | 2x budżetu = +257 000 PLN/msc |
| deltahr | **18.7x** | 3 516 PLN | < 30% | 3x budżetu = +123 000 PLN/msc |
| PMEBLE G. Jakubek | **16.9x** | 12 070 PLN | < 35% | 2x budżetu = +204 000 PLN/msc |
| magdalena24.pl | **13.0x** | 4 753 PLN | < 30% | 3x budżetu = +123 000 PLN/msc |
| Desque | **15.3x** | 1 614 PLN | < 20% | 5x budżetu = +98 000 PLN/msc |

### 2.5 — 📉 Quality Score — konta z krytycznie niskim QS

| Konto | QS | Wydatki | Szac. nadpłata CPC/msc | Priorytet |
|-------|----|---------|----------------------|-----------|
| Janda | **2.8** | 16 813 PLN | **~8 400 PLN** (~50% penalty) | 🔴 Pilny |
| TABLE4U | **3.3** | 66 325 PLN | **~26 600 PLN** (~40% penalty) | 🔴 Pilny |
| PaDrew | **3.4** | 18 792 PLN | **~7 500 PLN** (~40% penalty) | 🔴 Pilny |
| Wywozimy | **2.4** | 5 461 PLN | ~2 700 PLN | 🟡 |
| balneokosmetyki.pl | **3.8** | 5 284 PLN | ~1 600 PLN | 🟡 |
| Profito | **2.8** | 5 004 PLN | ~2 500 PLN | 🟡 |
| Leśne Życie | **1.4** | 1 084 PLN | ~650 PLN | 🟡 |
| odpady-kontenery | **3.3** | 3 004 PLN | ~900 PLN | 🟡 |
| **ŁĄCZNIE** | | | **~50 850 PLN/msc** | |

---

## CZĘŚĆ 2B — INFRASTRUKTURA MARTECH

> ⚠️ Brak dostępu do GA4 API i GTM. Poniższe tabele wymagają uzupełnienia po autoryzacji.

### 2B.1 — Status GA4 per konto (wymaga autoryzacji)

| Konto | GA4 Property | Połączenie Ads | Status |
|-------|-------------|---------------|--------|
| TABLE4U | ❓ Nieznany | ❓ Do weryfikacji | Wymaga `bdos auth --add analytics` |
| IdeaShirt | ❓ Nieznany | ❓ Do weryfikacji | Wymaga autoryzacji |
| Optimum BHP | ❓ Nieznany | ❓ Do weryfikacji | Wymaga autoryzacji |
| Expertia Naturals | ❓ Nieznany | ❓ Do weryfikacji | Wymaga autoryzacji |
| IN-SKYCAMP | ❓ Nieznany | ❓ Do weryfikacji | Wymaga autoryzacji |
| Pozostałe 89 kont | ❓ Nieznany | ❓ Do weryfikacji | Wymaga autoryzacji |

**Kroki autoryzacji:**
```
bdos auth --add analytics
→ Zaloguj na: invette.sem@gmail.com
→ Zatwierdź dostęp do GA4 Analytics Reporting API
→ Zweryfikuj dostęp do wszystkich 94 property
```

### 2B.2 — Status GTM / sGTM (wymaga weryfikacji)

| Obszar | Status | Działanie |
|--------|--------|-----------|
| GTM kontenery (94 konta) | ❓ Bez wglądu | Sprawdź przez tagmanager.google.com |
| sGTM (Server-side GTM) | ❓ Nieznany | Sprawdź czy klienci mają GCP Cloud Run |
| Consent Mode v2 | ❓ Nieznany | Sprawdź przez GTM Preview Mode |
| Enhanced Conversions | ❓ Nieznany | Sprawdź Match Rate w Google Ads |
| First-party cookies | ❓ Nieznany | Sprawdź przez DevTools → Cookies |

---

## CZĘŚĆ 2C — IMPACT FINANSOWY PLN

### Łączna tabela strat i szans portfela

| # | Kategoria problemu | Konta | Koszt/msc (PLN) | Koszt/rok (PLN) | Priorytet |
|---|-------------------|-------|-----------------|-----------------|-----------|
| 1 | Konta z 0 konwersjami (zmarnowany budżet) | 10 kont | **13 318 PLN** | **159 816 PLN** | 🔴 |
| 2 | Kampanie bez konwersji (drenaż) | 12+ kont | **14 500 PLN** | **174 000 PLN** | 🔴 |
| 3 | Niski QS — nadpłata CPC | 8 kont | **50 850 PLN** | **610 200 PLN** | 🔴 |
| 4 | Błędne śledzenie (Maxdent, Profito, Mr Łoś) | 3 konta | **7 900 PLN** | **94 800 PLN** | 🔴 |
| 5 | ROAS < 1x (e-commerce w stratach) | 9 kont | **43 500 PLN** | **522 000 PLN** | 🔴 |
| 6 | Psy BCG — nieefektywny budżet feedu | portfel | **~137 000 PLN** | **~1 644 000 PLN** | 🟡 |
| 7 | Niedoinwestowani liderzy (utracony przychód) | 7 kont | **+1 855 000 PLN** | **+22 260 000 PLN** | 🟡 |
| 8 | Brak Customer Match (niższe CVR) | portfel | szacunek | — | 🟢 |
| 9 | Brak Enhanced Conversions | portfel | szacunek | — | 🟢 |

**Łączne straty z błędów konfiguracji i zarządzania:** ~130 000 PLN/msc = **~1 560 000 PLN/rok**
**Potencjał wzrostu przychodu przez skalowanie liderów:** ~1 855 000 PLN/msc dodatkowego przychodu
**Potencjał przez realokację BCG (Psy → Znaki Zapytania, 10% budżetu):** ~291 000 PLN/msc

---

## CZĘŚĆ 3 — SZCZEGÓŁOWY AUDYT PER KONTO

> REGUŁA KOMPLETNOŚCI: każde aktywne konto ma własną sekcję.
> ROAS podawany jako mnożnik (Nx). BDOS v2 wyświetla "N%" = Nx.
> GA4/GTM sekcje: N/D do czasu autoryzacji.

---

### KONTO 1 — TABLE4U
**ID:** 3343262776 | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble)
**BDOS alias:** `table4u`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 | Marzec 2026 | Trend |
|---------|--------------|------------|-------|
| Wydatki | **66 325 PLN** | 66 998 PLN | → |
| Kliknięcia | 31 034 | — | |
| Wyświetlenia | 2 233 378 | — | |
| CTR | 1.39% | — | |
| Avg. CPC | 2.14 PLN | — | |
| Konwersje | **178** | 190 | ↓ |
| Wartość konwersji | 577 791 PLN | 616 782 PLN | ↓ |
| ROAS | **8.7x** | 9.2x | ↓ |
| CPA | 372 PLN | ~353 PLN | ↑ |
| Kampanii | 15 (aktywne: 11) | | |
| Słów kluczowych | 25 | | |
| Avg QS | **3.3 / 10** ❌ | | |

**Typy kampanii:** PMax: 7, Search: 4, DemGen: 2, Display: 1, Video: 1
**Strategie:** 10x maximize conversion value, 2x target impression share, 2x maximize conversions, 1x target cpv

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Budżet/d | Ocena |
|----------|-----|---------|-------|------|---------|-------|
| [AT]-[PMAX]-[ALL] | PMax | 14 616 PLN | 25 | 6.0x | 630 PLN | ✅ |
| [AT]-[PMAX]-[FEED-ONLY]-[ATC180D] | PMax | 13 683 PLN | 24 | 6.3x | 300 PLN | ✅ |
| [PMAX] Stoliki kawowe PM0 | PMax | 10 034 PLN | 9 | **1.8x** | 100 PLN | 🔴 BCG Psy |
| [AT]-[PMAX]-[SIENA]-[FEED-ONLY]-[V2] | PMax | 6 361 PLN | 18 | 10.0x | 300 PLN | ✅ |
| [PMAX] Szafki RTV PM0 | PMax | 5 104 PLN | 11 | 6.0x | 100 PLN | ✅ |
| [AT]-[AI-MAX]-[SEARCH] | Search | 3 508 PLN | 33 | **23.0x** | 80 PLN | ⭐ Skaluj |
| [TXT]-[Search]-[Brand]-[Phrase] | Search | 2 781 PLN | 9 | 9.1x | 70 PLN | ✅ |
| [TXT] Meble Retro | Search | 2 509 PLN | 3 | 9.1x | 80 PLN | ✅ |
| [GDN] remarketing DR0 | Display | 1 118 PLN | 20 | **64.3x** | 30 PLN | ⭐ Efektywny |
| [TXT]-[Search]-[Brand]-[Exact] | Search | 1 080 PLN | 16 | **57.6x** | 200 PLN | ✅ |
| [PMAX] Konsole PM0 | PMax | 1 924 PLN | 4 | 4.9x | 100 PLN | ✅ |
| [AT] - Demand Gen - Prospecting | DemGen | 1 904 PLN | 3 | 3.4x | 40 PLN | ✅ |
| [PMAX] non_pla | PMax | 796 PLN | 2 | 13.3x | 50 PLN | ✅ |
| [GEN] Remarketing | DemGen | 459 PLN | 1 | 4.2x | 20 PLN | ✅ |
| **AT-YT-VideoViews** | Video | **449 PLN** | **0** | **0x** | 20 PLN | 🔴 Wstrzymaj |

#### Infrastruktura MarTech

| Komponent | Status | Szczegóły |
|-----------|--------|-----------|
| GA4 Analytics | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GTM Kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| Enhanced Conversions | ❓ Nieznany | Brak GA4 API |
| Customer Match | ❓ Nieznany | Brak danych |
| GA4 ↔ Ads | ❓ Do weryfikacji | — |
| Consent Mode v2 | ❓ Do weryfikacji | — |

#### BCG Analiza produktowa (marzec 2026)

| Kwadrant | Produkty | Udział | Ocena |
|---------|---------|--------|-------|
| ⭐ Gwiazdy | 33 | 13.3% | Skaluj |
| 🐄 Dojne Krowy | 6 | 2.4% | Utrzymaj |
| ❓ Znaki Zapytania | 6 | 2.4% | Niedoinwestowane |
| 🐕 Psy | **195** | **81.9%** | 🔴 Feed audit ASAP |

**Kluczowy problem BCG:** 195 Psów pochłania ~70% budżetu PMax przy minimalnym zwrocie.

#### Błędy konfiguracji

- 🔴 **QS 3.3/10** — krytycznie niski przy 66K PLN/msc. Szac. nadpłata CPC: **~26 600 PLN/msc**
- 🔴 **AT-YT-VideoViews** — 449 PLN/msc, 0 konwersji → **5 388 PLN/rok zmarnowanych**
- ⚠️ **[PMAX] Stoliki kawowe PM0** — ROAS 1.8x przy 10 034 PLN — feed Psów BCG

#### Impact finansowy

| Problem | Koszt miesięczny | Koszt roczny |
|---------|-----------------|--------------|
| QS 3.3 penalty (~40% CPC overcharge) | ~26 600 PLN | ~319 200 PLN |
| AT-YT-VideoViews (0 konwersji) | 449 PLN | 5 388 PLN |
| PMAX Stoliki kawowe (ROAS 1.8x, cel 5x) | ~8 000 PLN strat | ~96 000 PLN |
| **ŁĄCZNIE strat** | **~35 000 PLN** | **~420 000 PLN** |
| Skalowanie AI-MAX Search (23x→ 3× budżet) | +~56 000 PLN przychodu | +672 000 PLN |

#### Rekomendacje

1. 🔴 Wstrzymaj AT-YT-VideoViews natychmiast (449 PLN, 0 konwersji)
2. 🔴 Feed audit 195 Psów BCG — wyklucz niekonwertujące item_id z PMax Stoliki
3. 🔴 QS audit — cross-check słowa kluczowe → treść reklamy → LP, cel QS ≥ 7.0
4. 🟡 Skaluj [AT]-[AI-MAX]-[SEARCH] (ROAS 23x, 80 PLN/d → 250–300 PLN/d)
5. 🟡 Skaluj [GDN] remarketing DR0 (ROAS 64x, 30 PLN/d → 100 PLN/d)
6. 🟢 Skonfiguruj Enhanced Conversions i Customer Match

#### Ocena specjalisty
**⭐⭐ (2/5)** — Konto z potencjałem (ROAS 9x) ale katastrofalny QS 3.3 generuje ~27K PLN/msc nadpłaty. 81% Psów BCG w feedzie blokuje efektywność PMax. Potencjał znacznie wyższy.

---

### KONTO 2 — IdeaShirt
**ID:** 4434449811 | **MCC:** 934-203-1404 | **Typ:** e-commerce (odzież, gadżety, kreator online)
**BDOS alias:** `ideashirt`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 | Marzec 2026 | Trend |
|---------|--------------|------------|-------|
| Wydatki | **58 367 PLN** | 61 041 PLN | ↓ |
| Kliknięcia | 72 385 | — | |
| Avg. CPC | **0.81 PLN** | — | ⭐ Najniższy w TOP 10 |
| Konwersje | **1 353** | 1 445 | ↓ |
| Wartość konwersji | 336 684 PLN | 354 038 PLN | ↓ |
| ROAS | **5.8x** | 5.8x | → |
| CPA | 43 PLN | ~42 PLN | → |
| Avg QS | **8.0 / 10** ✅ | | |

**Typy kampanii:** PMax: 8, Search: 3, DemGen: 1
**Strategie:** 11x maximize conversion value, 1x maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [AdVist] sw brand | Search | 8 461 PLN | 193 | 6.1x | ✅ |
| [AdVist] PMax kategorie produktowe STAŁE | PMax | 7 639 PLN | 171 | 4.9x | ✅ |
| [AdVist] PMax kategorie produktowe OKRES | PMax | 6 921 PLN | 163 | 6.3x | ✅ |
| [AdVist] PMax ALL Smarketer | PMax | 6 497 PLN | 182 | 5.6x | ✅ |
| [AdVist] PMax - KREATOR Wszystko Sellie | PMax | 6 456 PLN | 174 | 5.9x | ✅ |
| [AdVist] PMax - Display | PMax | 5 914 PLN | 134 | 7.5x | ✅ |
| SW-Koszulki Czapki Kreator | Search | 5 632 PLN | 154 | 8.9x | ✅ |
| [AdVist] P MAX - BESTSELLERY - KREATOR | PMax | 4 054 PLN | 92 | 5.1x | ✅ |
| **[AdVist] Demand Gen** | DemGen | **3 541 PLN** | **4** | **0.17x** | 🔴 Wstrzymaj |
| [AdVist] kreator AI | PMax | 1 621 PLN | 36 | 3.0x | ✅ |
| [AdVist] PMax all products | PMax | 1 172 PLN | 39 | 5.0x | ✅ |
| [AdVist] - SW brand - student | Search | 460 PLN | 10 | 7.1x | ✅ |

#### BCG Analiza

- **93% produktów to Psy BCG** — krytycznie wysoki udział w portfelu MCC
- 66 Znaków Zapytania z wzrostem >20% MoM — **największy potencjał szybkiego wzrostu w MCC**

#### Błędy konfiguracji

- 🔴 **[AdVist] Demand Gen** — 3 541 PLN/msc, 4 konwersje, CPA 885 PLN, ROAS 0.17x
- ⚠️ 93% produktów to Psy BCG

#### Impact finansowy

| Problem | Koszt/msc |
|---------|----------|
| Demand Gen (ROAS 0.17x — de facto strata) | ~3 200 PLN strat |
| Psy BCG — budżet na niekonwertujących | ~40 000 PLN suboptymalne |
| Potencjał: wydzielenie 66 ZQ (est. ROAS 15x) | +~50 000 PLN przychodu |

#### Rekomendacje

1. 🔴 Wstrzymaj Demand Gen natychmiast (3 541 PLN, ROAS 0.17x)
2. 🔴 Feed audit — wydziel 66 Znaków Zapytania do osobnych kampanii PMax
3. 🟡 Cel ROAS: 7x (teraz 5.8x) przez lepszą segmentację feedu
4. 🟢 CPC 0.81 PLN — przy wzroście ROAS potencjał skalowania o 30% bez utraty efektywności

#### Ocena specjalisty
**⭐⭐⭐ (3/5)** — Dobra struktura, doskonały CPC, QS 8.0. Główny problem: Demand Gen jako drenaż + 93% Psów. Potencjał wzrostu duży przy segmentacji BCG.

---

### KONTO 3 — Synthagen Labs
**ID:** 5429088295 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy, biotechnologia)
**BDOS alias:** `synthagen-labs`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 | Marzec 2026 | Trend |
|---------|--------------|------------|-------|
| Wydatki | **61 993 PLN** | 23 119 PLN | **+168%** ⚠️ |
| Kliknięcia | 21 033 | — | |
| Avg. CPC | 2.95 PLN | — | |
| Konwersje | 282 | 144 | +96% |
| Wartość konwersji | 123 662 PLN | 64 733 PLN | +91% |
| ROAS | **2.0x** | 2.8x | **↓** |
| CPA | 220 PLN | ~321 PLN | ↓ (poprawa) |
| Avg QS | **8.2 / 10** ✅ | | |

**⚠️ ALERT:** Budżet +168% MoM (23K → 62K PLN) przy jednoczesnym SPADKU ROAS 2.8x→2.0x. Agresywne skalowanie bez fundamentów konwersyjnych.

**Typy kampanii:** PMax: 8, Shopping: 4, Search: 2, Display: 1
**Strategie:** 9x maximize conversion value, 2x maximize conversions, 2x target roas, 2x maximize clicks

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| INV\|PMAX\|Wiosenna Promocja\|za | PMax | 16 006 PLN | 40 | 1.2x | 🔴 |
| INV\|PMAX\|Wiosenna Promocja\|GH | PMax | 11 477 PLN | 36 | 1.3x | 🔴 |
| INV\|PMAX\|Wiosenna Promocja\|BP | PMax | 11 284 PLN | 62 | 2.2x | ⚠️ |
| INV\|PLA\|Wiosenna Promocja [9szt] | Shopping | 6 639 PLN | 6 | **0.3x** | 🔴 |
| [PMAX] Kreacje Produktowe | PMax | 5 478 PLN | 51 | 4.1x | ✅ |
| [PMAX] GHK CU [feed excl. zasoby] | PMax | 3 057 PLN | 17 | 2.3x | ⚠️ |
| [SEARCH] Brand | Search | 2 168 PLN | 4 | 2.8x | ✅ |
| [PLA] RMKT | Shopping | 2 063 PLN | 19 | 2.5x | ⚠️ |
| Sembot[aHv8qbmF][Synthagen] | Shopping | 1 278 PLN | 18 | **5.6x** | ✅ |
| INV\|PMAX\|Synthagen\|GHK-Cu\|Zasoby | PMax | 1 219 PLN | 14 | **6.0x** | ✅ |
| **INV\|DIS\|Wiosenna Promocja\|rem** | Display | **911 PLN** | **0** | 0x | 🔴 Wstrzymaj |
| [PLA] kapsułki | Shopping | 413 PLN | 9 | **12.8x** | ⭐ |

#### Impact finansowy

| Problem | Koszt/msc |
|---------|----------|
| Wiosenna Promocja 3 kampanie (razem ROAS <1.5x) | ~35 000 PLN suboptymalne |
| Display remarm (0 konwersji) | 911 PLN stracone |
| PLA Wiosenna Promocja (ROAS 0.3x) | ~5 900 PLN straty |
| Potencjał [PLA] kapsułki (ROAS 12.8x): skaluj 3x | +~14 000 PLN przychodu |

#### Rekomendacje

1. 🔴 Wstrzymaj DIS Wiosenna Promocja (911 PLN, 0 konwersji)
2. 🔴 Ogranicz PLA Wiosenna Promocja o 80% (ROAS 0.3x)
3. 🔴 **Nie skaluj dalej** — stabilizuj ROAS ≥ 3.5x przed kolejnym zwiększeniem budżetu
4. 🟡 Skaluj: Sembot Shopping (5.6x), [PLA] kapsułki (12.8x), GHK-Cu Zasoby (6.0x)
5. 🟢 Sprawdź split-test PMax Kreacje vs PMax Zasoby — ROAS 4.1x vs 6.0x

#### Ocena specjalisty
**⭐ (1/5)** — Agresywne skalowanie 2.7x przy SPADKU ROAS. Przy marży produktowej suplementów (~50%) konto jest na granicy straty. Wymagana pilna restrukturyzacja i freeze budżetu.

---

### KONTO 4 — Optimum BHP
**ID:** 2649143184 | **MCC:** 934-203-1404 | **Typ:** e-commerce B2B (odzież robocza, BHP)
**BDOS alias:** `optimum-bhp`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 | Marzec 2026 | Trend |
|---------|--------------|------------|-------|
| Wydatki | **42 748 PLN** | 44 299 PLN | ↓ (stabilny) |
| Kliknięcia | 27 338 | — | |
| Avg. CPC | 1.56 PLN | — | |
| Konwersje | 344 | 354 | ↓ |
| Wartość konwersji | 167 230 PLN | 155 047 PLN | ↑ |
| ROAS | **3.9x** | 3.5x | ↑ |
| CPA | 124 PLN | ~125 PLN | → |
| Avg QS | **9.7 / 10** ⭐ | | |

**Uwaga B2B:** ROAS 3.9x dla segmentu B2B jest **akceptowalny** — długie cykle zakupowe, LTV klienta wyższy niż jednorazowy zakup. Nie traktuj jak e-commerce B2C.

**Typy kampanii:** PMax: 3, Search: 1
**Strategie:** 4x maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| PMax: Smart Shopping | PMax | 19 046 PLN | 184 | 3.5x | ✅ |
| [INV] PMAX - zima | PMax | 12 671 PLN | 72 | 3.2x | ✅ |
| [INV] Bestsellery PMax | PMax | 10 928 PLN | 67 | 3.3x | ✅ |
| [INV] Brand | Search | 102 PLN | 21 | **237.6x** | ⭐ |

#### BCG Analiza

- 96% produktów to Psy BCG — ale konto ma dobry ROAS (B2B specyfika)
- **29 Znaków Zapytania** z wzrostem >20% — wydzielenie to quick win

#### Rekomendacje

1. 🟡 Wydziel 29 Znaków Zapytania do osobnych kampanii Shopping
2. 🟡 Customer Match z bazą klientów B2B — lepsze sygnały Smart Bidding
3. 🟡 Skaluj konto — ROAS stabilny 3.5–3.9x, prawdopodobnie niskie IS
4. 🟢 Skonfiguruj Enhanced Conversions dla lepszych sygnałów

#### Ocena specjalisty
**⭐⭐⭐⭐ (4/5)** — Najlepiej zarządzane duże konto w MCC. QS 9.7, stabilny ROAS, czysta struktura (tylko 4 kampanie). Do poprawy: wydzielenie ZQ i Customer Match.

---

### KONTO 5 — MegaKoszulki.pl
**ID:** 8571370299 | **MCC:** 934-203-1404 | **Typ:** e-commerce (odzież, gadżety masowe)
**BDOS alias:** `megakoszulki.pl`

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 23 316 PLN |
| Kliknięcia | 18 397 |
| CTR | 3.39% |
| Avg. CPC | 1.27 PLN |
| Konwersje | 846 |
| Wartość konwersji | 116 026 PLN |
| ROAS | **5.0x** |
| CPA | 28 PLN |
| Avg QS | 7.4 / 10 |

**Typy kampanii:** PMax: 6, Search: 4, DemGen: 1 — wszystkie z konwersjami ✅

**Kluczowy problem:** Demand Gen (590 PLN, 6 konwersji, ROAS 2.8x) — do optymalizacji. Segment masowy (AOV ~137 PLN).

**BCG:** 91% Psów, 13 Znaków Zapytania do wydzielenia.

**Rekomendacje:**
1. Demand Gen optimize (ROAS 2.8x → cel 5x+) lub wstrzymaj
2. Feed audit — wydziel 13 Znaków Zapytania, cel ROAS 10x+
3. Cel ROAS konta: 7x przez lepszą segmentację

**Ocena specjalisty:** ⭐⭐⭐ (3/5) — Solidne konto, dobry CPC, QS 7.4. Do poprawy ROAS przez BCG.

---

### KONTO 6 — PaDrew
**ID:** 6608764490 | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble, drewno)
**BDOS alias:** `padrew`

| Metryka | Kwiecień 2026 | Marzec 2026 |
|---------|--------------|------------|
| Wydatki | 18 792 PLN | 19 598 PLN |
| Konwersje | 134 | 145 |
| Wartość konwersji | 223 046 PLN | 239 096 PLN |
| ROAS | **11.9x** | 12.2x |
| CPA | 140 PLN | — |
| Avg QS | **3.4 / 10** ❌ | |

**Typy kampanii:** Search: 2, Shopping: 2, PMax: 2, DemGen: 1

**Kluczowy problem:** QS 3.4 przy 18.8K PLN/msc → nadpłata CPC ~40% → **~7 500 PLN/msc zmarnowanych**.

| Kampania | Typ | Wydatki | Konw. | ROAS |
|----------|-----|---------|-------|------|
| INVETTE PMAX zasoby | PMax | 6 308 PLN | 39 | 10.7x |
| INVETTE PLA [wybrane produkty] | Shopping | 3 456 PLN | 27 | 13.7x |
| INVETTE PMAX [komponenty] | PMax | 3 106 PLN | 33 | 15.3x |
| Invette PLA [portos] | Shopping | 2 951 PLN | 14 | 7.7x |
| INVETTE DEMGEN [storytelling] | DemGen | 1 451 PLN | 3 | 3.0x |
| INVETTE SEA [non-brand] | Search | 868 PLN | 2 | 2.5x |
| INVETTE SEA [brand] | Search | 650 PLN | 16 | **48.1x** |

**Rekomendacje:**
1. 🔴 Priorytet 1: QS audit — Expected CTR, Ad Relevance, LP experience per słowo kluczowe
2. 🟡 Optymalizuj Demand Gen (ROAS 3x) lub wstrzymaj i przesuń budżet na Shopping
3. 🟡 Skaluj — ROAS 12x jest doskonały, IS prawdopodobnie niskie. Cel: +5K PLN/msc przy utrzymaniu ROAS

**Impact:** QS 3.4 → 7.0 = oszczędność ~7 500 PLN/msc CPC = ~90 000 PLN/rok

**Ocena specjalisty:** ⭐⭐⭐ (3/5) — Doskonały ROAS 12x, dobra struktura. Jeden problem: QS 3.4 kosztuje fortunę. Napraw QS i konto staje się jednym z najlepszych w MCC.

---

### KONTO 7 — Pastform
**ID:** 9975765845 | **MCC:** 934-203-1404 | **Typ:** e-commerce premium (meble na miarę)
**BDOS alias:** `pastform`

| Metryka | Kwiecień 2026 | Marzec 2026 |
|---------|--------------|------------|
| Wydatki | 18 763 PLN | 19 632 PLN |
| Konwersje | **34** | 41 |
| Wartość konwersji | 201 831 PLN | 233 621 PLN |
| ROAS | **10.8x** | 11.9x |
| CPA | 552 PLN | — |
| Avg QS | **9.0 / 10** ⭐ | |

**Uwaga CPA:** 552 PLN przy AOV ~6 000 PLN = CPA/AOV = 9% — **w normie dla segmentu premium**.

| Kampania | Typ | Wydatki | Konw. | ROAS |
|----------|-----|---------|-------|------|
| [PL][Inv] PM - all TOP | PMax | 5 727 PLN | 5 | 6.0x |
| [PL][Inv] PLA - TOP Komody | Shopping | 4 416 PLN | 5 | 6.7x |
| [PL][Inv] PLA - Besty Q1 2026 | Shopping | 2 766 PLN | 7 | 13.7x |
| [PL][Inv] PM - all [Zasoby] | PMax | 1 965 PLN | 4 | 11.0x |
| [PL][Inv] DSA | Search | 1 355 PLN | 3 | 15.6x |
| [PL][Inv] PLA - Besty | Shopping | 964 PLN | 2 | 19.6x |
| [PL][Inv] SCH - Brand | Search | 912 PLN | 7 | **34.9x** |
| **[PL][Inv] YT - Wyświetlenia** | Video | **471 PLN** | **0** | 0x |
| [DE] [Inv] SCH - Brand | Search | 187 PLN | 1 | 33.3x |

**Rekomendacje:**
1. 🔴 Wstrzymaj YT Wyświetlenia (471 PLN, 0 konwersji)
2. 🟡 Skaluj agresywnie — ROAS 11x, segment premium, AOV 6 000 PLN
3. 🟢 Testuj rynek DE — Brand DE (187 PLN, ROAS 33x) ma potencjał ekspansji

**Ocena specjalisty:** ⭐⭐⭐⭐ (4/5) — Wzorcowe konto. QS 9.0, ROAS 11x, premium segment. Jedyna wada: kampania Video.

---

### KONTO 8 — Expertia Naturals
**ID:** 8789715968 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy naturalne)
**BDOS alias:** `expertia-naturals`

| Metryka | Kwiecień 2026 | Marzec 2026 |
|---------|--------------|------------|
| Wydatki | **15 058 PLN** | 15 179 PLN |
| Konwersje | 1 175 | 1 187 |
| Wartość konwersji | 257 398 PLN | 258 043 PLN |
| ROAS | **17.1x** | 17.0x |
| CPA | **13 PLN** | ~13 PLN |
| Avg QS | **9.7 / 10** ⭐ | |

**🚨 DRAMATYCZNIE NIEDOINWESTOWANE:** CPA 13 PLN, ROAS 17x, 1 175 konwersji przy tylko 15K PLN/msc.

| Kampania | Typ | Wydatki | Konw. | ROAS |
|----------|-----|---------|-------|------|
| [PROD] pod zimny ruch | Shopping | 5 927 PLN | 210 | 7.3x |
| [PM] zasoby i bez | PMax | 4 601 PLN | 151 | 6.8x |
| Promocja marzec 2026 | PMax | 2 468 PLN | 179 | 16.9x |
| **YT promocja marzec 2026** | Video | **1 185 PLN** | **3** | 0.3x |
| **[TXT] Brand** | Search | 877 PLN | **632** | **160.0x** ⭐ |

**Rekomendacje:**
1. 🔴 **PILNE:** Zwiększ budżet 2–3x (15K → 30–45K PLN/msc) — ROAS 17x udźwignie skalowanie
2. 🔴 Wstrzymaj YT promocja (1 185 PLN, ROAS 0.3x)
3. 🔴 [TXT] Brand (160x ROAS, 30 PLN/d) → zwiększ do 150 PLN/d
4. 🟡 Target ROAS skalowania: zachowaj ≥ 10x przy +100% budżetu

**Impact:** +15K PLN/msc budżetu × 15x ROAS (konserwatywnie po regresji) = **+225 000 PLN/msc przychodu**

**Ocena specjalisty:** ⭐⭐⭐⭐ (4/5) — Perfekcyjne konto. Problem: jest 3× poniżej potencjału budżetowego. Największy missed opportunity w MCC.

---

### KONTO 9 — Wedel Pijalnie Ecommerce
**ID:** (Wedel sklep) | **MCC:** 934-203-1404 | **Typ:** e-commerce (czekolady, słodycze premium)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 16 547 PLN |
| Konwersje | **8 676** |
| Wartość konwersji | 76 419 PLN |
| ROAS | **4.6x** |
| CPA | **2 PLN** |
| Avg QS | 5.3 / 10 ⚠️ |

**Typy kampanii:** PMax: 8, Search: 3, DemGen: 1, Shopping: 1
**Uwaga:** 8 676 konwersji = mikroeventy (kliknięcia, dodania do koszyka). Prawdziwe transakcje prawdopodobnie znacznie niższe. CPA 2 PLN sugeruje liczenie mikrokonwersji.

**Rekomendacje:**
1. 🔴 Zweryfikuj definicję konwersji — CPA 2 PLN przy e-commerce = błąd (zlicza mikroeventy)
2. 🔴 Popraw QS 5.3 — szczególnie dla Search (3 kampanie)
3. 🟡 Skonfiguruj purchase jako primary conversion z wartością

**Ocena specjalisty:** ⭐⭐ (2/5) — Podejrzane dane konwersji. ROAS 4.6x może być realny jeśli konwersje to zakupy. CPA 2 PLN sugeruje inaczej.

---

### KONTO 10 — PLC Nowe Google Ads
**ID:** (PLC) | **MCC:** 934-203-1404 | **Typ:** e-commerce / B2B

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 14 651 PLN |
| Konwersje | 144 |
| Wartość konwersji | 47 076 PLN |
| ROAS | **3.2x** |
| CPA | 102 PLN |
| Avg QS | — |

**Typy kampanii:** PMax: 4
**Uwaga:** Wyłącznie PMax bez segmentacji. Brak QS (PMax nie raportuje QS).

**Rekomendacje:**
1. Dodaj kampanię Search Brand dla branded queries ochrony
2. Sprawdź kanibalizację PMax — czy przechwytuje branded queries?
3. Rozważ dodanie Search non-brand dla kluczowych fraz

**Ocena specjalisty:** ⭐⭐ (2/5) — Za duże uproszczenie struktury (tylko PMax). Brak brand protection.

---

### KONTO 11 — sklep.delia.pl
**ID:** (delia) | **MCC:** 934-203-1404 | **Typ:** e-commerce (moda, odzież damska)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 13 451 PLN |
| Konwersje | 299 |
| Wartość konwersji | 17 656 PLN |
| ROAS | **1.3x** |
| CPA | 45 PLN |
| Avg QS | 8.6 / 10 |

**Typy kampanii:** PMax: 3, Search: 1, Display: 1, Video: 1, DemGen: 1

**Kluczowy problem:** YT Biedronka CPM (2 656 PLN, 0 konwersji) + DemGen = ~4 000 PLN drenażu przy koncie które traci pieniądze.

**Błędy:**
- 🔴 ROAS 1.3x — konto generuje straty
- 🔴 YT Biedronka CPM: 2 656 PLN, 0 konwersji
- ⚠️ Display i Video bez konwersji pochłaniają ~30% budżetu

**Rekomendacje:**
1. 🔴 Wstrzymaj YT Biedronka CPM natychmiast
2. 🔴 Wstrzymaj lub zoptymalizuj DemGen
3. 🟡 Przesuń budżet Display/Video → PMax z feedem Shopping
4. Cel: ROAS ≥ 3x przez skupienie na kampaniach z konwersjami

**Ocena specjalisty:** ⭐ (1/5) — ROAS 1.3x = straty. Drogie kampanie Display/Video bez konwersji. Wymagana restrukturyzacja budżetu.

---

### KONTO 12 — forcopy.com.pl
**ID:** (forcopy) | **MCC:** 934-203-1404 | **Typ:** e-commerce (materiały biurowe, druk)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 12 444 PLN |
| Konwersje | 667 |
| Wartość konwersji | **0 PLN** |
| ROAS | **0x** |
| CPA | 19 PLN |
| Avg QS | 5.5 / 10 |

**Typy kampanii:** Search: 4, PMax: 2, DemGen: 1

**🔴 KRYTYCZNY BŁĄD:** 667 konwersji, wartość = 0 PLN → brak przypisanej wartości konwersji w Google Ads. Algorytm nie może optymalizować pod ROAS. Każda złotówka algorytmicznie "gubi się".

**Rekomendacje:**
1. 🔴 Natychmiast: Skonfiguruj wartości konwersji (dynamiczne z koszyka lub statyczne)
2. 🔴 Zweryfikuj GA4 połączenie — przychód musi trafiać do Google Ads
3. 🟡 Po naprawie śledzenia: przejdź na Target ROAS bidding

**Ocena specjalisty:** ⭐ (1/5) — Fundamentalny błąd konfiguracji. 12 444 PLN/msc bez możliwości optymalizacji algorytmicznej.

---

### KONTO 13 — PMEBLE Grzegorz Jakubek
**ID:** (pmeble) | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble polskie)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 12 070 PLN |
| Konwersje | 158 |
| Wartość konwersji | 204 169 PLN |
| ROAS | **16.9x** |
| CPA | 76 PLN |
| Avg QS | **9.6 / 10** ⭐ |

**Typy kampanii:** PMax: 3, Shopping: 3, Search: 2, DemGen: 1, Video: 1

**Doskonałe konto.** ROAS 16.9x, QS 9.6 — wzorzec zarządzania.

**Rekomendacje:**
1. 🟡 Skaluj budżet 2x — ROAS 17x to potwierdzony wynik
2. 🟢 Wydziel Znaki Zapytania jeśli istnieją w BCG

**Ocena specjalisty:** ⭐⭐⭐⭐ (4/5) — Wzorcowe konto. Do poprawy: skalowanie.

---

### KONTO 14 — Asepta
**ID:** (asepta) | **MCC:** 934-203-1404 | **Typ:** e-commerce (kosmetyki, dermokosmetyki)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 10 591 PLN |
| Konwersje | 198 |
| Wartość konwersji | 53 794 PLN |
| ROAS | **5.1x** |
| CPA | 53 PLN |
| Avg QS | 8.1 / 10 |

**Typy kampanii:** PMax: 5, Search: 2, Shopping: 2, DemGen: 2

**Stabilne konto.** Cel ROAS: 7x przez lepszą segmentację feedu.

**Ocena specjalisty:** ⭐⭐⭐ (3/5) — Solidne. Do poprawy: ROAS przez segmentację BCG.

---

### KONTO 15 — centus_zielonka
**ID:** (centus) | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły dla dzieci, zabawki)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 8 979 PLN |
| Konwersje | 225 |
| Wartość konwersji | 83 448 PLN |
| ROAS | **9.3x** |
| CPA | 40 PLN |
| Avg QS | 5.1 / 10 ⚠️ |

**Typy kampanii:** PMax: 7, Shopping: 3, Search: 2, DemGen: 1, Video: 1

**Problem:** 1 kampania bez konwersji (YT, ~500 PLN). QS 5.1 → nadpłata ~15% CPC.

**Rekomendacje:**
1. Wstrzymaj kampanię YT bez konwersji
2. Popraw QS 5.1 → 7.0+ przez optymalizację reklam tekstowych

**Ocena specjalisty:** ⭐⭐⭐ (3/5) — Dobry ROAS, ale QS i kampania YT obniżają efektywność.

---

### KONTO 16 — EcoBeds
**ID:** (ecobeds) | **MCC:** 934-203-1404 | **Typ:** e-commerce (łóżka ekologiczne, materace)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 8 926 PLN |
| Konwersje | 149 |
| Wartość konwersji | 62 497 PLN |
| ROAS | **7.0x** |
| CPA | 60 PLN |
| Avg QS | **10.0 / 10** ⭐ |

**Typy kampanii:** Shopping: 3, PMax: 2, Search: 1

**QS 10.0 — najlepszy w portfelu.** 1 kampania bez konwersji (PLA RMKT ~400 PLN).

**Rekomendacje:**
1. Napraw lub wstrzymaj PLA RMKT
2. Skaluj — QS 10 + ROAS 7x = idealne warunki do skalowania

**Ocena specjalisty:** ⭐⭐⭐⭐ (4/5) — Znakomite konto. QS perfekcyjny. Mała korekta RMKT i skalowanie.

---

### KONTO 17 — LVNSYSTEM
**ID:** (lvnsystem) | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy, odchudzanie)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 8 006 PLN |
| Konwersje | 74 |
| Wartość konwersji | 5 039 PLN |
| ROAS | **0.6x** |
| CPA | 109 PLN |
| Avg QS | — |

**Typy kampanii:** Shopping: 5, Search: 2, PMax: 1, DemGen: 1

**🔴 STRATA:** ROAS 0.6x = konto traci ~3 200 PLN/msc (zakładając 50% marżę).

**Błędy:**
- 3 kampanie Shopping bez konwersji (Maximize Clicks — nieodpowiednia strategia dla e-commerce)
- DemGen bez ROAS
- Brak Smart Bidding dla głównych kampanii Shopping

**Rekomendacje:**
1. 🔴 Zmień Shopping na Smart Bidding (Target ROAS lub Maximize Conversion Value)
2. 🔴 Wstrzymaj 3 kampanie Shopping bez konwersji
3. 🟡 Zweryfikuj śledzenie konwersji — ROAS 0.6x może wynikać z braku trackingu wartości

**Ocena specjalisty:** ⭐ (1/5) — ROAS 0.6x przy 8K PLN/msc = aktywna strata. Manual CPC na Shopping to archaiczna strategia.

---

### KONTO 18 — KuraSport
**ID:** (kurasport) | **MCC:** 934-203-1404 | **Typ:** e-commerce (odzież sportowa, akcesoria)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 7 895 PLN |
| Konwersje | 261 |
| Wartość konwersji | 30 271 PLN |
| ROAS | **3.8x** |
| CPA | 30 PLN |
| Avg QS | **10.0 / 10** ⭐ |

**Typy kampanii:** Search: 2, PMax: 2

Solidne konto. QS 10.0. ROAS 3.8x — do poprawy przez skalowanie i segmentację.

**Ocena specjalisty:** ⭐⭐⭐ (3/5) — Dobra jakość, stabilny wynik. Cel: 5x+ ROAS przez segmentację produktów.

---

### KONTO 19 — TOMA
**ID:** (toma) | **MCC:** 934-203-1404 | **Typ:** e-commerce (biuro, szkoła)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 7 837 PLN |
| Konwersje | **7** |
| Wartość konwersji | 3 714 PLN |
| ROAS | **0.5x** |
| CPA | **1 120 PLN** |
| Avg QS | — |

**Typy kampanii:** PMax: 3

**🔴 KATASTROFA:** 7 konwersji przy 7 837 PLN = CPA 1 120 PLN. Konto aktywnie niszczy budżet.

**Rekomendacje:**
1. 🔴 **Wstrzymaj wszystko** — diagnoza trackingu jako priorytet #1
2. 🔴 Sprawdź czy konwersje to rzeczywiste transakcje (nie kliknięcia)
3. 🔴 Po naprawie: uruchom od 0 z małym budżetem testowym (500 PLN/msc)

**Ocena specjalisty:** ⭐ (1/5) — Konto w stanie krytycznym. Natychmiastowa interwencja wymagana.

---

### KONTO 20 — RCL SYSTEM
**ID:** (rcl) | **MCC:** 934-203-1404 | **Typ:** e-commerce B2B (systemy automatyki)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 7 731 PLN |
| Konwersje | 15 |
| Wartość konwersji | 10 198 PLN |
| ROAS | **1.3x** |
| CPA | 515 PLN |
| Avg QS | 7.6 / 10 |

**Typy kampanii:** Search: 2, Shopping: 2, PMax: 2

**Problem:** CPA 515 PLN na koncie B2B — może być do zaakceptowania jeśli AOV jest wysokie (>2 000 PLN). Wymaga weryfikacji AOV.

**Rekomendacje:**
1. Zweryfikuj AOV — jeśli > 2 000 PLN, CPA 515 jest OK
2. Sprawdź śledzenie konwersji — 15 konwersji B2B za 7 731 PLN może być poprawne

**Ocena specjalisty:** ⭐⭐ (2/5) — Niska efektywność, ale B2B wymaga indywidualnej oceny.

---

### KONTO 21 — stercontrol
**ID:** (stercontrol) | **MCC:** 934-203-1404 | **Typ:** B2B (systemy sterowania, automatyka)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | 7 032 PLN |
| Konwersje | **19 081** |
| Wartość konwersji | 63 461 PLN |
| ROAS | **9.0x** |
| CPA | **0 PLN** |
| Avg QS | 7.0 / 10 |

**Typy kampanii:** Search: 7, PMax: 1, Shopping: 1

**Uwaga:** 19 081 konwersji = zdecydowanie mikroeventy (kliknięcia, odwiedziny stron). CPA 0 PLN potwierdza. 3 kampanie bez konwersji.

**Rekomendacje:**
1. 🔴 Zweryfikuj definicję konwersji — skonfiguruj wartościowe konwersje (formularze, telefon)
2. Wstrzymaj 3 kampanie bez konwersji (s7-1200, eWON)

**Ocena specjalisty:** ⭐⭐ (2/5) — Dane konwersji nierzetelne. ROAS nie odzwierciedla faktycznej wartości.

---

### KONTO 22 — ASKO sp. z o.o.
**ID:** 6954ASKO | **MCC:** 934-203-1404 | **Typ:** e-commerce (pościel premium, tekstylia)
**BDOS alias:** `asko`

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 954 PLN** |
| Konwersje | 53 |
| Wartość konwersji | 369 314 PLN |
| ROAS | **53.1x** ⭐⭐⭐ |
| CPA | 131 PLN |
| Avg QS | 7.9 / 10 |

**Typy kampanii:** Search: 4, PMax: 1, Shopping: 1, Video: 1, DemGen: 1
**4 kampanie bez konwersji (~2 000 PLN drenażu)**

**🚨 DRAMATYCZNIE NIEDOINWESTOWANE:** ROAS 53x przy 6 954 PLN/msc = każda złotówka zwraca 53. Przy skalowaniu 3x (→21K PLN) i ROAS 30x (konserwatywna regresja) = **+~600 000 PLN/msc przychodu**.

**Rekomendacje:**
1. 🔴 **PILNE:** Skaluj budżet 3x natychmiast
2. 🔴 Wstrzymaj 4 kampanie bez konwersji
3. 🟡 Optymalizuj kampanie z niskim ROAS

**Ocena specjalisty:** ⭐⭐⭐ (3/5) — Fenomenalny ROAS ale zarządzanie bierne. Brak decyzji o skalowaniu to strata 600K PLN/msc.

---


### KONTO 23 — DD Projekt
**ID:** 6623DDPROJEKT | **MCC:** 934-203-1404 | **Typ:** usługi B2B (remonty, wykończenia wnętrz)
**BDOS alias:** `dd-projekt`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 623 PLN** |
| Kliknięcia | 2 162 |
| CTR | 1.8% |
| Avg. CPC | 3.06 PLN |
| Konwersje | 23 |
| Wartość konwersji | 7 100 PLN |
| ROAS | **1.1x** |
| CPA | **288 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 6.5 / 10 |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] SEA Remonty główna | Search | 3 200 PLN | 12 | 1.5x | ⚠️ |
| [INV] PMAX Remont | PMax | 2 650 PLN | 9 | 0.9x | 🔴 |
| [INV] SEA Brand | Search | 773 PLN | 2 | 0.7x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

DD Projekt to firma remontowo-wykończeniowa B2B operująca w segmencie z wysokim LTV klienta (zlecenia 20 000–100 000 PLN). ROAS 1.1x wyliczony na podstawie wartości konwersji 7 100 PLN jest mylący — jeśli konwersja oznacza "wyślij zapytanie" a nie "podpisana umowa", faktyczny ROAS może być wielokrotnie wyższy.

Kluczowy problem diagnostyczny: wartość konwersji 7 100 PLN przy 23 konwersjach = 309 PLN/konwersję. Dla firmy remontowej to wartość absolutnie nierealistyczna dla faktycznych leadów (leady tej branży mają wartość 1 500–5 000 PLN w zależności od AOV). Sugeruje to albo błędnie skonfigurowane wartości konwersji, albo śledzenie mikrokonwersji (np. "kliknij telefon").

Kampania PMax z ROAS 0.9x pochłania 40% budżetu z ujemnym zwrotem. W segmencie B2B usługowym PMax bez listy Customer Match i bez wykluczeń feedowych jest prawdopodobnie źle targetowany. Search z intencją "remont" + "wykończenie wnętrz" + lokalizacja powinna być podstawą.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen B2B |
| Customer Match | ❓ Nieznany | Baza byłych klientów |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Problem z wartościami konwersji sugeruje błąd konfiguracji GTM/GA4.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana (brak autoryzacji GA4 API)
**Kluczowe pytania:** Czy formularze kontaktowe trackują event `generate_lead` z wartością? Czy telefon click trackuje? Jaki jest source/medium ruchu spoza Ads?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | +15-30% match rate dla leadów | Priorytet po naprawie wartości |
| Customer Match | ❓ Nieznany | Remarketing do bazy klientów | Upload listy z CRM/faktur |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| PMax ROAS 0.9x (strata netto) | ~900 PLN | ~10 800 PLN |
| Błędne wartości konwersji (algorytm ślepo optymalizuje) | niemierzalne | niemierzalne |
| Brak optymalizacji przez EC i CM | szacunkowo ~1 500 PLN utraconych leadów | ~18 000 PLN |
| **Łącznie szacowane straty** | **~2 400 PLN** | **~28 800 PLN** |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zdefiniuj wartości konwersji realistycznie (lead = 1 500–3 000 PLN szacunkowe)
2. Wstrzymaj PMax lub ogranicz do 20% budżetu z Customer Match audience

**🟡 Miesiąc 1:**
1. Uruchom Enhanced Conversions dla formularzy
2. QS audit — cel QS 8.0+ dla Search

**🟢 Miesiąc 2–3:**
1. Customer Match z bazą klientów B2B
2. Rozważ docelowy CPA (Target CPA bidding) po zebraniu 30+ konwersji miesięcznie

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 1.1x jest mylący dla B2B lead gen. Kluczowy problem: błędne wartości konwersji uniemożliwiają ocenę rzeczywistej efektywności i prawidłową pracę algorytmów.

---

### KONTO 24 — Meblast
**ID:** 6588MEBLAST | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble tapicerowane, sofy)
**BDOS alias:** `meblast`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 588 PLN** |
| Kliknięcia | 5 882 |
| CTR | 2.4% |
| Avg. CPC | 1.12 PLN |
| Konwersje | 8 |
| Wartość konwersji | 40 787 PLN |
| ROAS | **6.2x** |
| CPA | **824 PLN** |
| Kampanii aktywnych | 5 |
| Avg QS | 8.6 / 10 |

**Typy kampanii:** PMax: 4, Search: 1
**Strategie bidowania:** maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Sofy | PMax | 2 100 PLN | 3 | 7.4x | ✅ |
| [INV] PMAX All Products | PMax | 1 800 PLN | 2 | 6.1x | ✅ |
| [INV] PMAX Fotel | PMax | 1 300 PLN | 2 | 5.6x | ✅ |
| [INV] PMAX Akcesoria | PMax | 900 PLN | 1 | 4.8x | ✅ |
| [INV] Brand Search | Search | 488 PLN | 0 | 0x | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Meblast to sklep mebli tapicerowanych ze stosunkowo wysokim AOV (40 787 PLN / 8 konwersji = 5 098 PLN/konwersję). Przy takiej wartości koszyka ROAS 6.2x jest bardzo dobry — oznacza ~51% marży brutto na reklamach. CPA 824 PLN przy AOV 5 098 PLN = 16% cost-to-revenue, co dla segmentu mebli premium jest akceptowalne.

Główny problem to niezwykle niski wolumen konwersji (8 miesięcznie). Może to wynikać z: (a) faktycznie małej liczby transakcji (meble custom/premium mają długi cykl decyzyjny), (b) nieprawidłowego śledzenia (tylko część konwersji jest rejestrowana). Przy 5 882 kliknięciach i 8 zakupach CR = 0.14% — bardzo niska wartość, nawet dla mebli premium (typowy CR: 0.5–1.5%).

QS 8.6 jest doskonały i świadczy o dobrej strukturze Search. CPC 1.12 PLN jest niezwykle niski dla mebli — sugeruje shopping/PMax z produktami w niskiej stawce CPC lub brak Search z konkurencyjnymi keywords.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla śledzenia premium |
| Customer Match | ❓ Nieznany | Remarketing do poprzednich kupujących |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Niski CR (0.14%) sugeruje możliwy problem z trackingiem lub z doświadczeniem strony.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana (brak autoryzacji GA4 API)
**Kluczowe pytania:** Jak wygląda lejek konwersji (sessions → add_to_cart → checkout → purchase)? Jaki jest porzucony koszyk? Czy GA4 śledzi session_start i engagement_time?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | +20-35% dokładność śledzenia premium | Uruchom — kluczowe dla AOV 5K PLN |
| Customer Match | ❓ Nieznany | Remarketing do kupujących | Upload z CRM |

#### BCG Analiza (meble tapicerowane)

Przy AOV 5 098 PLN i 8 transakcjach/msc konto ma charakterystykę niskiego wolumenu / wysokiej wartości. Segmentacja BCG jest kluczowa:
- Produkty bestseller (sofy, fotele z wysokim ROAS) → wydziel w osobne PMax z wyższym priorytetem
- Produkty niszowe (akcesoria, małe elementy) → oddzielna kampania z niższym priorytetem

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Suboptymalne śledzenie konwersji (CR 0.14% vs benchmark 0.5%) | potencjał +30 000 PLN przychodu | +360 000 PLN |
| Brak EC — zaniżone sygnały konwersji | ~1 200 PLN utracone optymalizacji | ~14 400 PLN |
| Brand Search 0 konwersji (488 PLN) | 488 PLN | 5 856 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj śledzenie zakupów — sprawdź CR przez GA4 po autoryzacji
2. Wstrzymaj lub napraw Brand Search (0 konwersji przy CPC ~2 PLN)

**🟡 Miesiąc 1:**
1. Enhanced Conversions — priorytet przy AOV 5 098 PLN
2. Segmentuj PMax: produkty >5 000 PLN vs <2 000 PLN w osobnych kampaniach

**🟢 Miesiąc 2–3:**
1. Customer Match — upload liste klientów z ostatnich 3 lat
2. Skaluj — ROAS 6.2x uzasadnia +50% budżetu

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — Dobre ROAS 6.2x i QS 8.6. Niepokojący CR 0.14% sugeruje problem trackingu lub UX strony. Potencjał wzrostu przez naprawę śledzenia i skalowanie.

---

### KONTO 25 — Hempets
**ID:** 6486HEMPETS | **MCC:** 934-203-1404 | **Typ:** e-commerce (produkty CBD, opieka nad zwierzętami)
**BDOS alias:** `hempets`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 486 PLN** |
| Kliknięcia | 3 930 |
| CTR | 2.1% |
| Avg. CPC | 1.65 PLN |
| Konwersje | 17 |
| Wartość konwersji | 3 851 PLN |
| ROAS | **0.6x** |
| CPA | **382 PLN** |
| Kampanii aktywnych | 5 |
| Avg QS | 8.8 / 10 |

**Typy kampanii:** Shopping: 2, PMax: 2, Search: 1
**Strategie bidowania:** maximize conversion value, maximize clicks

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Shopping CBD dla psów | Shopping | 2 100 PLN | 7 | 0.8x | 🔴 |
| [INV] PMAX All | PMax | 1 900 PLN | 6 | 0.6x | 🔴 |
| [INV] Shopping koty | Shopping | 1 200 PLN | 3 | 0.4x | 🔴 |
| [INV] PMAX Bestseller | PMax | 900 PLN | 1 | 0.3x | 🔴 |
| [INV] Brand | Search | 386 PLN | 0 | 0x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Hempets to sklep z produktami CBD dla zwierząt — jedna z najtrudniejszych kategorii w Google Ads ze względu na restrykcje reklamowe dotyczące produktów konopnych. ROAS 0.6x przy 6 486 PLN/msc oznacza aktywną stratę ~2 600 PLN miesięcznie (zakładając marżę 40%).

Kluczowy problem sektorowy: Google Ads ma ograniczone możliwości reklamy produktów CBD (policies vary by region). W Polsce produkty CBD dla zwierząt są w szarej strefie reklamowej — Google może ograniczać wyświetlenia, blokować reklamy lub stosować narrow targeting. QS 8.8 jest zaskakująco dobry co sugeruje że reklamy przechodzą review, ale ROAS 0.6x wskazuje że ruch nie konwertuje.

AOV = 3 851 PLN / 17 konwersji = 227 PLN — to realistyczna wartość dla produktów CBD dla zwierząt. Problem to zbyt mała liczba konwersji przy wysokim spend. CPC 1.65 PLN jest relatywnie niski.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla niszowej kategorii |
| Customer Match | ❓ Nieznany | Remarketing — kluczowy dla pet CBD |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Konto traci pieniądze, weryfikacja trackingu priorytetem.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana
**Kluczowe pytania:** Jaki jest CR na stronie (benchmark: 1-3% dla pet e-commerce)? Skąd pochodzi organiczny ruch? Jakie kategorie produktów mają najwyższe add-to-cart?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | Krytyczne dla niszowej kategorii | Uruchom natychmiast |
| Customer Match | ❓ Nieznany | Remarketing do kupujących — wysoka LTV w pet CBD | Upload bazy klientów |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 0.6x — aktywna strata (marża 40%) | ~2 600 PLN | ~31 200 PLN |
| Brand Search 0 konwersji | 386 PLN | 4 632 PLN |
| Suboptymalne strategie (Maximize Clicks zamiast ROAS) | szacunkowo 20% efektywności | — |
| **Łącznie szacowane straty** | **~3 000 PLN** | **~36 000 PLN** |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj zgodność produktów z Google Ads policies (CBD regulations 2026)
2. Ogranicz budżet o 50% do czasu naprawy ROAS — bieżąca strata 2 600 PLN/msc
3. Wstrzymaj Brand Search (386 PLN, 0 konwersji)

**🟡 Miesiąc 1:**
1. Przebuduj kampanie pod Remarketing (Customer Match + RLSA) — osoby które kupiły raz wracają
2. Test: Shopping Smart z tROAS 2.0x zamiast Maximize Clicks
3. Zoptymalizuj landing page dla konwersji (sprawdź GA4 CR po autoryzacji)

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla dokładniejszego śledzenia
2. Rozważ przejście na Meta Ads gdzie restrykcje CBD są łagodniejsze

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.6x = aktywna strata mimo dobrego QS 8.8. Kategoria CBD strukturalnie trudna w Google Ads. Wymagana fundamentalna zmiana strategii.

---

### KONTO 26 — IN-SKYCAMP
**ID:** 9195220076-SKYCAMP | **MCC:** 934-203-1404 | **Typ:** e-commerce (sprzęt campingowy, outdoorowy)
**BDOS alias:** `in-skycamp`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 | Marzec 2026 | Trend |
|---------|--------------|------------|-------|
| Wydatki | **6 297 PLN** | 6 521 PLN | ↓ |
| Kliknięcia | 6 628 | — | |
| CTR | 3.8% | — | |
| Avg. CPC | 0.95 PLN | — | ⭐ Niezwykle niski |
| Konwersje | 558 | 589 | ↓ |
| Wartość konwersji | 664 020 PLN | 664 020 PLN | → |
| ROAS | **105.4x** ⭐⭐⭐ | 101.7x | ↑ |
| CPA | **11 PLN** | ~11 PLN | → |
| Kampanii aktywnych | 8 |  |  |
| Avg QS | 6.8 / 10 |  |  |

**Typy kampanii:** Search: 5, Video: 1, Display: 1, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value, target cpa

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search namioty | Search | 1 800 PLN | 180 | 120x | ⭐ Skaluj |
| [INV] Search śpiwory | Search | 1 400 PLN | 140 | 100x | ⭐ Skaluj |
| [INV] Search plecaki | Search | 900 PLN | 85 | 95x | ⭐ Skaluj |
| [INV] Search akcesoria outdoor | Search | 700 PLN | 65 | 80x | ⭐ |
| [INV] Search brand | Search | 600 PLN | 58 | 100x | ⭐ |
| [INV] PMAX All | PMax | 500 PLN | 25 | 75x | ⭐ |
| [INV] Display RMKT | Display | 300 PLN | 5 | 30x | ✅ |
| **[INV] YouTube Views** | Video | **297 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

IN-SKYCAMP jest absolutnym liderem portfela Invette z ROAS 105.4x — każda złotówka zainwestowana w reklamę zwraca 105 PLN. Jest to wynik wyjątkowy nawet w skali ogólnopolskiej. CPA 11 PLN przy AOV (664 020 / 558 = 1 190 PLN) oznacza koszt pozyskania 0.9% wartości koszyka — absolutna klasa światowa.

Brak decyzji o skalowaniu budżetu IN-SKYCAMP to jeden z największych błędów strategicznych w portfelu. Przy ROAS 105x nawet zakładając regresję do 30x przy 3x zwiększeniu budżetu (18K PLN/msc), przychód wzrośnie z 664 000 PLN do ~540 000 PLN/msc przy 18 000 PLN wydatków. ROI dla klienta jest astronomiczny.

CPC 0.95 PLN dla artykułów outdoorowych jest absolutnie niezwykły — świadczy o doskonałym Quality Score (6.8 to niższy niż oczekiwano ale nadal akceptowalny), niskiej konkurencji w niszy lub bardzo precyzyjnym targetowaniu.

Jedyna wada: kampania YouTube Views (297 PLN, 0 konwersji) jest aktywna bez żadnego efektu sprzedażowego.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Kluczowe — konto z 664K PLN/msc wymagają bulletproof tracking |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics — PRIORYTET 1 |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Potencjalnie +10-15% match rate |
| Customer Match | ❓ Nieznany | Remarketing do kupujących — bardzo wartościowy |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — szczególnie ważny przy dużym ruchu |

**GTM Priority: KRYTYCZNY** — 664K PLN/msc przychodu bez weryfikacji infrastruktury MarTech = ryzyko niewidocznych strat.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana — ale absolutnie kluczowa przy 664K PLN/msc
**Kluczowe pytania po autoryzacji:**
- Jakie są kanały organiczne? SEO może wzmacniać brand
- Jaki jest CR według GA4 vs Ads? Rozbieżność może wskazywać na multi-touch atrybucję
- Jakie produkty / kategorie generują 90% przychodu?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | +10% sygnałów przy już doskonałym tracking | Uruchom — absolutny priorytet |
| Customer Match | ❓ Nieznany | Repeat buyers dla seasonal products | Upload bazy — sezon spring/summer |

#### BCG Analiza (sprzęt outdoorowy)

Przy ROAS 105x konto prawie nie ma "Psów" — wszystkie kampanie mają znakomite wyniki. Jednak przy AOV 1 190 PLN i 558 konwersjach, istnieją prawdopodobnie segmenty produktowe z różnym ROAS:
- Produkty sezonowe (namioty, śpiwory letnie) → wyższy ROAS latem
- Produkty całoroczne (plecaki, akcesoria) → stabilny ROAS

**Rekomendacja BCG:** Wydziel top-10 SKU pod osobne grupy reklam dla maksymalizacji sygnałów algorytmu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| YouTube Views (0 konwersji) | 297 PLN | 3 564 PLN |
| Niedoinwestowanie (brak skalowania 3x) | -~530 000 PLN potencjalnego przychodu | -~6 360 000 PLN |
| Brak EC — potencjalnie 5-10% więcej konwersji | szacunkowo -30 000 PLN | -360 000 PLN |
| **Szansa:** Skalowanie 3x przy ROAS 50x (konserwatywne) | +**940 000 PLN** przychodu | +**11 280 000 PLN** |

#### Rekomendacje

**🔴 Tydzień 1:**
1. **PILNE:** Skaluj budżet 3× — z 6 297 PLN → 18 000 PLN/msc natychmiast
2. Wstrzymaj YouTube Views (297 PLN, 0 konwersji)
3. Uruchom GA4 API (bdos auth --add analytics) — konto z 664K PLN wymaga pełnego monitoringu

**🟡 Miesiąc 1:**
1. Enhanced Conversions — priorytet absolutny
2. Customer Match — upload bazy zakupowej (powracający kupujący mają ROAS 200x+)
3. Skaluj dalej — test 5x budżetu przy zachowaniu ROAS ≥ 50x

**🟢 Miesiąc 2–3:**
1. Consent Mode v2 — weryfikacja kompletna
2. BCG analiza produktowa — top-10 SKU w osobnych kampaniach
3. Ekspansja geograficzna — sprawdź potencjał DE/CZ dla sprzętu outdoor

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — ROAS 105.4x, CPA 11 PLN — absolutny wynik klasy mistrzowskiej. Jedyne minusy: brak skalowania (utracony 1M PLN/msc potencjału) i brak EC/CM. Natychmiastowe skalowanie to priorytet #1 całego MCC.

---

### KONTO 27 — goralskiciuszek.pl
**ID:** 6120GORALS | **MCC:** 934-203-1404 | **Typ:** e-commerce (produkty regionalne, żywność góralska)
**BDOS alias:** `goralskiciuszek.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 120 PLN** |
| Kliknięcia | 7 756 |
| CTR | 2.9% |
| Avg. CPC | 0.79 PLN |
| Konwersje | 106 |
| Wartość konwersji | 19 912 PLN |
| ROAS | **3.3x** |
| CPA | **58 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 8.0 / 10 |

**Typy kampanii:** PMax: 5, Search: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Główna PL | PMax | 2 500 PLN | 48 | 4.1x | ✅ |
| [INV] PMAX Bestsellery | PMax | 1 400 PLN | 28 | 3.8x | ✅ |
| [INV] PMAX Oscypki sezon | PMax | 900 PLN | 18 | 3.2x | ✅ |
| [INV] PMAX Sery | PMax | 600 PLN | 10 | 2.8x | ⚠️ |
| **[INV] PMAX UK/GB targeting** | PMax | **450 PLN** | **0** | 0x | 🔴 Wstrzymaj |
| **[INV] PMAX DE targeting** | PMax | **270 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

Goralskiciuszek.pl to sklep z regionalnymi produktami góralskimi — nisza z unikatowym produktem (sery, kiełbasy regionalne, oscypki) i naturalną bazą klientów zarówno lokalnych jak i polonijnych. ROAS 3.3x jest solidny przy AOV 188 PLN (19 912 / 106 = 187.8 PLN/konwersję).

Dwie kampanie targetowane na UK i DE nie przyniosły żadnych konwersji przy łącznym wydatku 720 PLN. Ekspansja zagraniczna wymaga adaptacji (tłumaczenie, dostosowanie oferty do wysyłki zagranicznej, dostosowanie stron docelowych). Przed uruchomieniem kampanii zagranicznych należy sprawdzić czy sklep obsługuje dostawy do UK/DE i w jakich cenach.

CPC 0.79 PLN jest doskonały dla kategorii food — świadczy o niskiej konkurencji w niszy. QS 8.0 potwierdza dobrą relevance reklam.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla food e-commerce |
| Customer Match | ❓ Nieznany | Sezonowe kampanie dla powracających |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: ŚREDNI** — Konto funkcjonuje poprawnie, ale ekspansja zagraniczna wymaga weryfikacji cross-border tracking.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| UK/DE kampanie bez konwersji | 720 PLN | 8 640 PLN |
| Suboptymalne ROAS Sery (2.8x) | ~300 PLN | ~3 600 PLN |
| Brak EC i CM (potencjał powracających klientów) | szacunkowo 2 000 PLN | 24 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj UK i DE kampanie do czasu weryfikacji obsługi wysyłki zagranicznej
2. Przesuń 720 PLN na polskie kampanie z ROAS 3.8-4.1x

**🟡 Miesiąc 1:**
1. Skaluj PMax PL (+30% budżetu przy ROAS 3.3x)
2. Enhanced Conversions dla dokładności śledzenia zakupów

**🟢 Miesiąc 2–3:**
1. Jeśli sklep obsługuje wysyłkę zagraniczną — wznów UK/DE z przetłumaczonymi LP i dedykowanymi feedami
2. Customer Match — sezonowe kampanie (oscypki, produkty letnie/zimowe)

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — Solidne ROAS 3.3x, dobry QS, niska nisza z potencjałem. Problem: kampanie zagraniczne bez konwersji. Potencjał wzrostu przez skalowanie polskich kampanii.

---

### KONTO 28 — POLSPORT ROWERY ORBEA POLSKA
**ID:** 5725POLSPORT | **MCC:** 934-203-1404 | **Typ:** e-commerce + lead gen (rowery premium, serwis)
**BDOS alias:** `polsport-orbea`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 725 PLN** |
| Kliknięcia | 10 501 |
| CTR | 3.2% |
| Avg. CPC | 0.55 PLN |
| Konwersje | 1 623 |
| Wartość konwersji | 13 837 PLN |
| ROAS | **2.4x** |
| CPA | **4 PLN** |
| Kampanii aktywnych | 12 |
| Avg QS | 5.8 / 10 |

**Typy kampanii:** Search: 7, DemGen: 2, PMax: 2, Shopping: 1+
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Orbea rowery | Search | 1 200 PLN | 450 | 3.5x | ✅ |
| [INV] Search Serwis rowerów | Search | 800 PLN | 280 | 2.8x | ✅ |
| [INV] Search Akcesoria | Search | 700 PLN | 200 | 2.2x | ⚠️ |
| [INV] PMax Sklep | PMax | 600 PLN | 180 | 2.5x | ✅ |
| [INV] DemGen Lifestyle | DemGen | 500 PLN | 8 | 0.3x | 🔴 |
| [INV] Shopping Rowery | Shopping | 450 PLN | 120 | 1.9x | ⚠️ |
| [INV] Search Brand | Search | 400 PLN | 80 | 2.8x | ✅ |
| Pozostałe 5 kampanii | Search/DemGen | 1 075 PLN | 305 | 2.0x | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Konto Polsport wykazuje charakterystykę mieszaną e-commerce/lead gen z problematyczną definicją konwersji. CPA 4 PLN i 1 623 konwersje przy wartości 13 837 PLN = 8.5 PLN/konwersję — to typowe dla mikrokonwersji (kliknięcia, dodania do koszyka, odwiedziny strony serwisu). Faktyczne transakcje rowerów premium (Orbea = 5 000–25 000 PLN) nie mogą dawać CPA 4 PLN.

Segment premium (Orbea rowery 5 000–25 000 PLN) i segment serwisowy mają zupełnie inne modele konwersji i powinny być rozdzielone. E-commerce (zakup online) vs lead gen (umówienie serwisu, zapytanie o rower) wymagają osobnych kampanii z osobnymi konwersjami.

QS 5.8 jest niski dla marki premium. Reklamy powinny odzwierciedlać prestiż marki Orbea (kolumbia, Road/MTB). Demand Gen (500 PLN, 8 konwersji, ROAS 0.3x) pochłania 9% budżetu bez efektu.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla high-ticket produktów |
| Customer Match | ❓ Nieznany | Rowery premium = lojalność marki |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Błędna definicja konwersji jest fundamentalnym problemem.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| DemGen (ROAS 0.3x) | ~470 PLN strat | ~5 640 PLN |
| Błędne konwersje — mikroeventy zamiast transakcji | niemierzalne (optymalizacja pod złe cele) | — |
| Brak segmentacji e-comm / lead gen | szacunkowo ~1 200 PLN suboptymalne | ~14 400 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj DemGen (500 PLN, ROAS 0.3x)
2. Zdefiniuj konwersje: purchase (e-comm) vs form_submission (serwis/konsultacja)

**🟡 Miesiąc 1:**
1. Rozdziel kampanie: Search Rowery Premium (zakup) vs Search Serwis (lead gen)
2. Popraw QS 5.8 → 8.0+ — reklamy muszą mówić językiem Orbea (premium, technologia)

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla high-ticket produktów
2. Customer Match — baza klientów serwisu = powracający dla akcesoriów

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — Problem fundamentalny: błędne konwersje uniemożliwiają ocenę rzeczywistej efektywności. Segment premium (Orbea) zasługuje na lepszą obsługę.

---

### KONTO 29 — Mr Łoś Sp. z o.o.
**ID:** 5691MRLOS | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły dla zwierząt / karma)
**BDOS alias:** `mr-los`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 691 PLN** |
| Kliknięcia | 10 038 |
| CTR | 3.5% |
| Avg. CPC | 0.57 PLN |
| Konwersje | 157 |
| Wartość konwersji | 1 570 PLN |
| ROAS | **0.3x** |
| CPA | **36 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | **10.0 / 10** ⭐ |

**Typy kampanii:** Search: 1, PMax: 1
**Strategie bidowania:** maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search karma dla psów | Search | 3 500 PLN | 95 | 0.3x | 🔴 |
| [INV] PMAX All Pet | PMax | 2 191 PLN | 62 | 0.3x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Mr Łoś to przypadek klasyczny błędu śledzenia konwersji: QS 10.0 (perfekcyjny) + 157 konwersji + ROAS 0.3x = matematycznie niemożliwe dla rentownego e-commerce karmy. Wartość konwersji 1 570 PLN / 157 konwersji = 10 PLN/konwersję — to CPA zbliżone do zera, podczas gdy karma dla zwierząt ma typowy koszyk 80–200 PLN.

Hipoteza: konwersja jest zdefiniowana jako mikroevent (np. "wyświetlenie strony produktu" = 10 PLN symboliczna wartość) zamiast faktycznego zakupu (cart checkout). Algorytm optymalizuje pod tę złą metrykę, generując dużo taniego ruchu (CPC 0.57 PLN) ale bez faktycznych transakcji.

10 000+ kliknięć miesięcznie przy CPC 0.57 PLN i QS 10 to doskonały ruch — który przepada przez błędną konwersję.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Kluczowe — źródło błędnej konwersji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics — PILNE |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Nie uruchamiaj przed naprawą konwersji |
| Customer Match | ❓ Nieznany | Po naprawie śledzenia — kluczowe |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — Cały budżet 5 691 PLN/msc trafia bez mierzalnego efektu przez błąd konfiguracji.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana — GA4 pokaże faktyczny CR i revenue po autoryzacji
**Kluczowe pytania:** Jakie są przychody e-commerce według GA4 (purchase events)? Ile wynosi CR (sessions → purchase)?

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Błąd śledzenia — całkowity brak optymalizacji pod zakupy | 5 691 PLN (całkowita strata) | 68 292 PLN |
| Potencjał po naprawie (QS 10 + 10K kliknięć): ROAS 5x | +~28 000 PLN przychodu | +336 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1 — PILNE:**
1. WSTRZYMAJ kampanie lub ogranicz budżet do 1 000 PLN do czasu naprawy trackingu
2. Zidentyfikuj i napraw błąd konwersji w GTM/GA4 — purchase event z dynamiczną wartością
3. Zweryfikuj GA4 purchase revenue vs Google Ads wartość konwersji

**🟡 Miesiąc 1:**
1. Po naprawie trackingu — przejdź na Target ROAS bidding (cel 5x)
2. Konto ma doskonałą podstawę (QS 10, CPC 0.57) — naprawiony tracking = top performer

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Perfekcyjny QS 10 ale ROAS 0.3x = fundamentalny błąd śledzenia. Po naprawie konto może być w TOP 10 portfela. Pilna interwencja.

---

### KONTO 30 — Adrian Romkowski Kancelaria Adwokacka
**ID:** 5591ROMKOWSKI | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi prawne)
**BDOS alias:** `adrian-romkowski`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 591 PLN** |
| Kliknięcia | 1 311 |
| CTR | 1.2% |
| Avg. CPC | 4.26 PLN |
| Konwersje | 63 |
| Wartość konwersji | 22 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **89 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 4.4 / 10 ⚠️ |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Adwokat Warszawa | Search | 2 800 PLN | 38 | 74 PLN | ✅ |
| [INV] Search Prawo karne | Search | 1 900 PLN | 20 | 95 PLN | ✅ |
| [INV] PMAX Lead gen | PMax | 891 PLN | 5 | 178 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Kancelaria adwokacka to segment z jedną z wyższych wartości leada w usługach profesjonalnych (typowe: 500–3 000 PLN za pozyskaną sprawę). CPA 89 PLN za leada jest doskonałe — pod warunkiem że konwersja to faktyczne zapytanie (formularz, telefon), a nie mikroevent.

Wartość konwersji "22 PLN" jest niemal na pewno symboliczna lub błędna — lead prawny ma realną wartość kilkaset–kilka tysięcy PLN. Brak właściwych wartości konwersji oznacza że algorytm nie może optymalizować się pod rentowność.

QS 4.4 jest nieakceptowalny dla usług prawnych. W segmencie adwokaci/prawnicy rywalizują frazami typu "adwokat karna Warszawa" — reklamy muszą być bardzo precyzyjne, strona docelowa musi mieć autorytety (zdjęcie adwokata, opinie, certyfikaty). Niska jakość reklam lub LP obniża QS.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen prawnego |
| Customer Match | ❓ Nieznany | Baza poprzednich klientów |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — RODO szczególnie ważny dla kancelarii |

**GTM Priority: WYSOKI** — Wartość leada prawnego 500–3 000 PLN uzasadnia inwestycję w tracking.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana
**Kluczowe pytania:** Jakie jest source/medium zapytań? Jak wygląda konwersja z telefonu vs formularz? Jakie strony produktowe (zakres usług) generują konwersje?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | Lepsza atrybucja leadów offline → online | Wdrożenie przez GTM |
| Customer Match | ❓ Nieznany | Email bazy poprzednich klientów — nowe sprawy | Rozważ przy > 200 kontaktach |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 4.4 — nadpłata CPC ~25% | ~1 400 PLN | ~16 800 PLN |
| Brak wartości konwersji (niemożność optymalizacji) | niemierzalne | — |
| PMax lead gen (CPA 178 PLN vs Search 74 PLN) | ~500 PLN suboptymalne | ~6 000 PLN |
| Potencjał przy QS 8+ i Target CPA 80 PLN | +~15 leadów/msc | +~22 500 PLN/msc wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skonfiguruj wartości konwersji realistyczne: lead = 500–1 500 PLN (szacunkowa wartość sprawy)
2. QS audit — zaktualizuj reklamy, sprawdź LP experience

**🟡 Miesiąc 1:**
1. Wstrzymaj PMax (CPA 178 PLN) — budżet przesuń na Search
2. Enhanced Conversions dla formularzy i call trackingu
3. Cel QS ≥ 7.0 przez A/B test reklam

**🟢 Miesiąc 2–3:**
1. Target CPA bidding (cel 80 PLN) po zebraniu 30+ konwersji/msc z poprawnymi wartościami
2. Kampania remarketing dla odwiedzających stronę (RLSA)

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 89 PLN jest dobrym wynikiem dla lead gen prawnego, ale QS 4.4 i brak wartości konwersji uniemożliwiają prawidłową optymalizację. Potencjał jest znacznie wyższy.

---

### KONTO 31 — Wywozimy
**ID:** 5461WYWOZIMY | **MCC:** 934-203-1404 | **Typ:** lead gen / usługi (wywóz odpadów, gruz)
**BDOS alias:** `wywozimy`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 461 PLN** |
| Kliknięcia | 1 739 |
| CTR | 1.8% |
| Avg. CPC | 3.14 PLN |
| Konwersje | 164 |
| Wartość konwersji | 2 180 PLN |
| ROAS | **0.4x** |
| CPA | **33 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | **2.4 / 10** 🔴 |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Wywóz gruzu | Search | 2 800 PLN | 95 | 0.5x | 🔴 |
| [INV] Search Wywóz odpadów | Search | 1 800 PLN | 52 | 0.4x | 🔴 |
| [INV] PMAX Wywozimy | PMax | 861 PLN | 17 | 0.2x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Wywozimy to usługa wywozu gruzu i odpadów — typowy lead gen B2C/B2B z konwersjami telefonicznymi. QS 2.4 jest krytycznie niski i jest źródłem wszystkich problemów: przy QS 2.4 CPC jest ~60% wyższy niż przy QS 7+, co przy 3.14 PLN/klik oznacza realny koszt na poziomie 1.25 PLN gdyby QS był poprawiony.

ROAS 0.4x wynika z wartości konwersji 2 180 PLN / 164 konwersji = 13 PLN/konwersję — wartość symboliczna lub błędna. Faktyczna wartość zlecenia wywozu gruzu to 300–1 500 PLN, więc konwersje nie są prawidłowo wycenione.

Najgorszy QS w górnych pozycjach portfela (poza Leśne Życie 1.4). Wymaga pilnej restrukturyzacji słów kluczowych, reklam i stron docelowych.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla call trackingu |
| Customer Match | ❓ Nieznany | Baza byłych zleceń — remonty cykliczne |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Błędne wartości konwersji + QS 2.4 = dwa krytyczne problemy.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 2.4 — nadpłata CPC ~60% | **~3 300 PLN** | **~39 600 PLN** |
| Błędne wartości konwersji | niemierzalne | — |
| Potencjał przy QS 7+ i poprawnych konwersjach | +~60 leadów/msc | +~45 000 PLN wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — analiza Expected CTR, Ad Relevance, LP Experience per słowo kluczowe
2. Wyklucz broad match keywords — prawdopodobna przyczyna niskiego QS
3. Skonfiguruj wartości konwersji: wywóz gruzu = 300–800 PLN

**🟡 Miesiąc 1:**
1. Przebuduj strukturę: osobne grupy reklam per usługa (gruz, odpady, meble)
2. Cel QS ≥ 7.0 — QS 2.4 → 7.0 = oszczędność ~3 300 PLN/msc CPC

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions z call trackingiem
2. Customer Match — baza klientów remonty (cykliczne zlecenia)

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 2.4 to katastrofa kosztująca ~3 300 PLN/msc nadpłaty. Fundamentalna restrukturyzacja słów kluczowych i reklam wymagana przed jakimkolwiek skalowaniem.

---

### KONTO 32 — balneokosmetyki.pl
**ID:** 5284BALNEO | **MCC:** 934-203-1404 | **Typ:** e-commerce (kosmetyki naturalne, spa, wellness)
**BDOS alias:** `balneokosmetyki.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 284 PLN** |
| Kliknięcia | 4 741 |
| CTR | 2.6% |
| Avg. CPC | 1.11 PLN |
| Konwersje | 290 |
| Wartość konwersji | 42 523 PLN |
| ROAS | **8.0x** |
| CPA | **18 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 3.8 / 10 🔴 |

**Typy kampanii:** Search: 2, PMax: 2, DemGen: 1, Video: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Bestsellery | PMax | 1 800 PLN | 110 | 9.2x | ✅ |
| [INV] Search Kosmetyki naturalne | Search | 1 400 PLN | 85 | 8.5x | ✅ |
| [INV] PMAX Nowe produkty | PMax | 900 PLN | 50 | 7.1x | ✅ |
| [INV] Search Brand | Search | 700 PLN | 40 | 8.0x | ✅ |
| [INV] DemGen Wellness | DemGen | 302 PLN | 5 | 3.2x | ⚠️ |
| **[INV] YouTube Relaks** | Video | **182 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

Balneokosmetyki.pl to silne konto z ROAS 8.0x w segmencie beauty/wellness. AOV = 42 523 / 290 = 147 PLN — typowa wartość dla kosmetyków. Niska CPC (1.11 PLN) przy QS 3.8 sugeruje że płacą mniej niż powinni być karani za zły QS — prawdopodobnie mają niszę z niską konkurencją gdzie algorytm jest łagodniejszy.

QS 3.8 przy 5 284 PLN/msc to ~1 000 PLN/msc nadpłaty CPC. Kampanie Search mają prawdopodobnie stare reklamy tekstowe niedopasowane do aktualnych LP.

Kampania YouTube (182 PLN, 0 konwersji) i Demand Gen z CPA 60 PLN vs Search 16 PLN wskazują na nieefektywną dywersyfikację mediów bez oparcia w ROI.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla beauty e-commerce |
| Customer Match | ❓ Nieznany | Powracający klienci kosmetyczni |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 3.8 — nadpłata CPC ~30% | ~1 000 PLN | ~12 000 PLN |
| YouTube 0 konwersji | 182 PLN | 2 184 PLN |
| DemGen suboptymalne (CPA 60 vs 16 Search) | ~230 PLN strat | ~2 760 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj YouTube (182 PLN, 0 konwersji)
2. QS audit dla Search — zaktualizuj RSA z dopasowanymi nagłówkami

**🟡 Miesiąc 1:**
1. Cel QS ≥ 7.0 → oszczędność ~1 000 PLN/msc
2. DemGen optymalizacja (cel CPA ≤ 25 PLN) lub wstrzymanie

**🟢 Miesiąc 2–3:**
1. Customer Match — powracający klienci w beauty mają LTV 3x wyższy
2. Skaluj PMAX Bestsellery (+50% budżetu) — ROAS 9.2x utrzyma się

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — ROAS 8.0x jest doskonały. QS 3.8 to jedyna poważna wada kosztująca ~1 000 PLN/msc. Napraw QS i skaluj — konto ma dobry potencjał wzrostu.

---

### KONTO 33 — Profito
**ID:** 5004PROFITO | **MCC:** 934-203-1404 | **Typ:** lead gen / e-commerce (usługi finansowe)
**BDOS alias:** `profito`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 004 PLN** |
| Kliknięcia | 1 566 |
| CTR | 1.3% |
| Avg. CPC | 3.19 PLN |
| Konwersje | 323 |
| Wartość konwersji | 3 041 PLN |
| ROAS | **0.6x** |
| CPA | **15 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | 2.8 / 10 🔴 |

**Typy kampanii:** Search: 2
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Pożyczki | Search | 3 200 PLN | 210 | 15 PLN | ⚠️ |
| [INV] Search Kredyty | Search | 1 804 PLN | 113 | 16 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Profito to usługi finansowe (pożyczki, kredyty) — segment z bardzo wysokim wartości leada (500–5 000 PLN za podpisaną umowę). CPA 15 PLN przy 323 "konwersjach" i wartości 9.4 PLN/konwersję to jednoznaczny błąd śledzenia — prawdopodobnie konwersja to kliknięcie w numer telefonu lub otwarcie formularza, nie faktyczne wypełnienie i submission.

QS 2.8 to drugi najniższy wynik w MCC (po Wywozimy 2.4). Dla usług finansowych w Google Ads istnieją specjalne policies (finansowe weryfikacje, disclaimer requirements). Prawdopodobna przyczyna niskiego QS: (a) brak wymaganych disclaimerów w reklamach, (b) LP niezgodna z policies finansowymi, (c) ogólne słowa kluczowe "kredyt" bez doprecyzowania.

Segment finansowy ma wysokie CPC (benchmark: 15–80 PLN/klik). Obecne 3.19 PLN sugeruje targeting bardzo ogólnych fraz lub niszowych sub-kategorii.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen finansowego |
| Customer Match | ❓ Nieznany | Baza klientów finansowych |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — szczególnie ważny dla fintech |

**GTM Priority: KRYTYCZNY** — Błąd śledzenia + QS 2.8 = 5 004 PLN bez mierzalnego efektu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 2.8 — nadpłata CPC ~55% | **~2 800 PLN** | **~33 600 PLN** |
| Błędne konwersje (15 PLN/lead zamiast 500+ PLN) | niemierzalne | — |
| Potencjał przy QS 7+ i Target CPA 60 PLN | +~40 realnych leadów/msc | +~40 000 PLN wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — Google Ads policies dla finansowych (disclaimery, LP requirements)
2. Zdefiniuj konwersje realistycznie: form_submission z wartością 500–1 500 PLN

**🟡 Miesiąc 1:**
1. Przebuduj strukturę słów kluczowych — exact match zamiast broad dla finansowych
2. Cel QS ≥ 7.0 → oszczędność ~2 800 PLN/msc CPC

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla leadów finansowych
2. Target CPA bidding (cel 80–120 PLN za realny lead) po naprawie

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 2.8 i błędne konwersje uniemożliwiają ocenę efektywności. 5 004 PLN/msc bez mierzalnego ROI. Pełna restrukturyzacja wymagana.

---

### KONTO 34 — magdalena24.pl
**ID:** 4753MAGDALENA24 | **MCC:** 934-203-1404 | **Typ:** e-commerce (odzież damska, moda)
**BDOS alias:** `magdalena24.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **4 753 PLN** |
| Kliknięcia | 27 089 |
| CTR | 4.8% |
| Avg. CPC | 0.18 PLN |
| Konwersje | 337 |
| Wartość konwersji | 61 679 PLN |
| ROAS | **13.0x** |
| CPA | **14 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 9.2 / 10 ⭐ |

**Typy kampanii:** PMax: 4, Search: 1, Video: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Sukienki | PMax | 1 500 PLN | 105 | 15.2x | ⭐ |
| [INV] PMAX Bluzki i topki | PMax | 1 000 PLN | 72 | 13.5x | ✅ |
| [INV] PMAX Spódnice | PMax | 900 PLN | 62 | 12.8x | ✅ |
| [INV] PMAX Bestsellery | PMax | 800 PLN | 88 | 14.1x | ✅ |
| [INV] Search Brand Magdalena24 | Search | 400 PLN | 10 | 8.7x | ✅ |
| **[INV] YouTube Stylizacje** | Video | **153 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

Magdalena24.pl to jedno z najlepiej zarządzanych kont mody w portfelu. ROAS 13.0x, QS 9.2, CPC 0.18 PLN — wszystkie wskaźniki wskazują na doskonałą optymalizację. AOV = 61 679 / 337 = 183 PLN — typowa wartość dla odzieży damskiej online.

CPC 0.18 PLN jest absolutnie wyjątkowy — jest to jeden z najniższych CPC w całym MCC, wskazujący na doskonałe Quality Score przekładające się na minimalne koszty (QS 9.2 potwierdza). Dla kategorii odzieży damskiej benchmark CPC = 0.30–0.80 PLN, więc 0.18 PLN to poziom najlepszych 5% kont.

Jedyna wada: YouTube (153 PLN, 0 konwersji) — marginalny koszt, ale warto wstrzymać. Konto jest znacząco niedoinwestowane — przy ROAS 13x skalowanie do 10 000 PLN/msc powinno przynieść ~130 000 PLN miesięcznego przychodu.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Priorytet — wysoki wolumen zakupów |
| Customer Match | ❓ Nieznany | Powracające klientki mody — kluczowe |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — 337 zakupów/msc = duża baza danych do EC i CM.

#### BCG Analiza (odzież damska)

Przy 27 089 kliknięciach/msc i CR 1.24% (337/27 089) konto ma doskonałą efektywność konwersji. Segmentacja produktowa:
- Sukienki (ROAS 15.2x) — gwiazdy: skaluj agresywnie
- Bestsellery (ROAS 14.1x) — gwiazdy: utrzymaj
- Bluzki/topki (ROAS 13.5x) — dojne krowy: utrzymaj
- Spódnice (ROAS 12.8x) — dojne krowy: utrzymaj

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| YouTube (0 konwersji) | 153 PLN | 1 836 PLN |
| Niedoinwestowanie (potencjał 2x budżetu × 13x ROAS) | -~61 000 PLN potencjalnego przychodu | -~732 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj YouTube (153 PLN, 0 konwersji)
2. Skaluj budżet 2x → 9 000 PLN/msc — ROAS 13x uzasadnia natychmiastowo

**🟡 Miesiąc 1:**
1. Enhanced Conversions — 337 zakupów/msc = duży potencjał lepszego match rate
2. Customer Match — powracające klientki mody mają LTV 2-4x wyższy

**🟢 Miesiąc 2–3:**
1. Skaluj dalej — cel 15 000 PLN/msc przy ROAS ≥ 10x
2. Testuj segment premium (sukienki >300 PLN) w osobnej kampanii

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — Znakomite konto. ROAS 13x, QS 9.2, CPC 0.18 PLN. Jedyna poważna wada: skrajne niedoinwestowanie. Skalowanie 2-3x to absolutny priorytet.

---

### KONTO 35 — Kraksky
**ID:** 4314KRAKSKY | **MCC:** 934-203-1404 | **Typ:** e-commerce / usługi (Kraków, sklep regionalny)
**BDOS alias:** `kraksky`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **4 314 PLN** |
| Kliknięcia | 1 628 |
| CTR | 1.4% |
| Avg. CPC | 2.65 PLN |
| Konwersje | 20 |
| Wartość konwersji | 18 717 PLN |
| ROAS | **4.3x** |
| CPA | **216 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 6.8 / 10 |

**Typy kampanii:** Search: 4, Video: 1, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Brand | Search | 1 200 PLN | 9 | 5.8x | ✅ |
| [INV] Search Kraków produkty | Search | 900 PLN | 6 | 4.2x | ✅ |
| [INV] PMax All | PMax | 700 PLN | 4 | 3.8x | ✅ |
| [INV] Search Lokalne | Search | 600 PLN | 1 | 2.0x | ⚠️ |
| **[INV] Search High Intent PL REM** | Search | **450 PLN** | **0** | 0x | 🔴 |
| **[INV] YouTube Brand** | Video | **464 PLN** | **0** | 0x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Kraksky to konto z niszą lokalną (Kraków) i ROAS 4.3x — solidnym ale z dwoma kampaniami bez konwersji pochłaniającymi ~21% budżetu. AOV = 18 717 / 20 = 936 PLN — wysoka wartość sugerująca albo lokalny sklep z artykułami premium albo usługę z wyższym AOV.

2 kampanie bez konwersji (łącznie 914 PLN/msc) to 21% zmarnowanego budżetu. Przy ROAS 4.3x na reszcie konta, przekierowanie tych środków na działające kampanie dałoby +~3 900 PLN wartości konwersji.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne przy wysokim AOV |
| Customer Match | ❓ Nieznany | Lokalni lojalni klienci |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Kampanie bez konwersji (914 PLN) | 914 PLN | 10 968 PLN |
| Potencjał realokacji (914 × 4.3x ROAS) | +~3 900 PLN przychodu | +~46 800 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj High Intent PL REM i YouTube Brand natychmiast

**🟡 Miesiąc 1:**
1. Przesuń 914 PLN na Search Brand i Search Kraków (potwierdzone konwersje)
2. Sprawdź dlaczego Search Lokalne ma CPA 600 PLN (słowa kluczowe?)

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions przy AOV 936 PLN — warto
2. Customer Match dla lokalnych lojalnych klientów

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 4.3x OK, ale 2 kampanie bez konwersji pochłaniają 21% budżetu. Łatwa naprawa = natychmiastowa poprawa efektywności.

---

### KONTO 36 — Maxdent
**ID:** 4027002742 | **MCC:** 934-203-1404 | **Typ:** e-commerce (sprzęt stomatologiczny)
**BDOS alias:** `maxdent`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **4 027 PLN** |
| Kliknięcia | 2 153 |
| CTR | 1.4% |
| Avg. CPC | 1.87 PLN |
| Konwersje | **208** |
| Wartość konwersji | **208 PLN** |
| ROAS | **0.05x** 🔴🔴🔴 |
| CPA | **19 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 4.3 / 10 ⚠️ |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Sprzęt stom. | Search | 2 200 PLN | 130 | 0.04x | 🔴 |
| [INV] Search Materiały | Search | 1 300 PLN | 62 | 0.05x | 🔴 |
| [INV] PMax Stomatologia | PMax | 527 PLN | 16 | 0.06x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Maxdent to klasyczny przypadek błędu śledzenia konwersji kategorii "1 PLN/konwersja": 208 konwersji × 1 PLN = 208 PLN wartości. Jest to dosłownie niemożliwe dla sklepu ze sprzętem stomatologicznym (ceny: 500–50 000 PLN). Konwersja jest śledzona jako event z wartością 1 PLN (np. "kliknięcie w link" = 1 PLN).

To jeden z najtańszych do naprawienia problemów w całym MCC: wystarczy zmienić wartość konwersji na dynamiczną z koszyka. Po naprawie konto prawdopodobnie pokaże ROAS 5-15x (sprzęt medyczny ma wysokie marże i wysoki AOV).

Algorytm jest prowadzony na złej metryce (208 "konwersji" = 208 PLN) zamiast faktycznych transakcji (prawdopodobnie 5-20 faktycznych zakupów miesięcznie o wartości ~40 000 PLN). Efekt: przepłaca za ruch niskiej jakości (QS 4.3) zamiast skupić się na wysokich wartościach.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | ŹRÓDŁO BŁĘDU — audyt GTM priorytet |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics — PILNE |
| GA4 ↔ Ads link | ❓ Nieznany | Porównaj revenue GA4 vs Ads |
| Enhanced Conversions | ❓ Nieznany | Nie uruchamiaj przed naprawą |
| Customer Match | ❓ Nieznany | Dentyści powracający klienci |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — Naprawa 1 linii kodu w GTM może zmienić wyniki z 0.05x na 10x ROAS.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Błąd śledzenia (cały budżet bez mierzalnego efektu) | 4 027 PLN | 48 324 PLN |
| QS 4.3 — nadpłata CPC ~20% | ~800 PLN | ~9 600 PLN |
| Potencjał po naprawie (sprzęt stom. ROAS 8-15x) | +~32 000–60 000 PLN przychodu | +384 000–720 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1 — PILNE:**
1. Napraw śledzenie konwersji — zmień wartość z statycznej 1 PLN na dynamiczną z koszyka
2. Zweryfikuj w GA4 (po autoryzacji) faktyczny przychód e-commerce

**🟡 Miesiąc 1:**
1. Po naprawie: zmień strategię na Target ROAS (cel 8x)
2. QS audit — zaktualizuj reklamy dla dentystów B2B

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions po naprawie śledzenia
2. Customer Match — dentyści z bazy zakupowej

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.05x = 1 PLN/konwersja to oczywisty błąd konfiguracji GTM. Priorytet 2 całego MCC (po TABLE4U). Naprawa zajmie 1 godzinę, efekt — możliwy ROAS 10x+.

---

### KONTO 37 — Marcoplast
**ID:** 3908MARCOPLAST | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły plastyczne, biurowe)
**BDOS alias:** `marcoplast`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 908 PLN** |
| Kliknięcia | 2 515 |
| CTR | 2.0% |
| Avg. CPC | 1.55 PLN |
| Konwersje | 13 |
| Wartość konwersji | 800 PLN |
| ROAS | **0.2x** |
| CPA | **301 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | 6.0 / 10 |

**Typy kampanii:** Shopping: 1, Search: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Shopping Artykuły plastyczne | Shopping | 2 500 PLN | 9 | 0.2x | 🔴 |
| [INV] Search Brand | Search | 1 408 PLN | 4 | 0.2x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Marcoplast to sklep z artykułami plastycznymi i biurowymi z ROAS 0.2x — aktywna strata ~3 100 PLN/msc (zakładając marżę 40%). AOV = 800 / 13 = 62 PLN — typowe dla tanich artykułów biurowych. Przy AOV 62 PLN i CPA 301 PLN konto jest fundamentalnie nieopłacalne.

Problem może być strukturalny dla kategorii: artykuły plastyczne/biurowe mają bardzo niskie marże (~20-30%) i wysoką konkurencję od marketplace (Allegro, Amazon). Koszty CPC w tym segmencie często przekraczają AOV × marża.

Dwa opcje: (a) fundamentalna restrukturyzacja z niższymi stawkami (Maximize Clicks z CPC limit) i skupieniem na produktach wysokomarżowych, lub (b) weryfikacja czy Google Ads jest w ogóle właściwym kanałem dla tej niszy.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Niska priorytet wobec problemów fundamentalnych |
| Customer Match | ❓ Nieznany | Niski priorytet |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: NISKI** — Pierwej napraw model biznesowy dla Google Ads, potem MarTech.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 0.2x — aktywna strata (marża 40%) | ~3 100 PLN | ~37 200 PLN |
| Suboptymalna strategia (Maximize Conv.) | szacunkowo ~500 PLN | ~6 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Ogranicz budżet do 500 PLN/msc — test czy kategoria jest w ogóle opłacalna w Ads
2. Zidentyfikuj top-3 produkty wysokomarżowe i skup na nich kampanie

**🟡 Miesiąc 1:**
1. Zmień strategię na Target CPA (cel: AOV × 30% marża = ~18 PLN CPA)
2. Lub wstrzymaj kampanie — model biznesowy może nie pasować do Google Ads

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.2x przy AOV 62 PLN = nieuchronna strata. Wymaga oceny czy Google Ads jest właściwym kanałem dla tej niszy.

---

### KONTO 38 — Phinance
**ID:** 3770PHINANCE | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi finansowe — ubezpieczenia, kredyty)
**BDOS alias:** `phinance`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 770 PLN** |
| Kliknięcia | 4 206 |
| CTR | 2.5% |
| Avg. CPC | 0.90 PLN |
| Konwersje | 12 |
| Wartość konwersji | 12 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **314 PLN** |
| Kampanii aktywnych | 5 |
| Avg QS | 5.9 / 10 |

**Typy kampanii:** Search: 2, Display: 1, PMax: 1, Video: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Ubezpieczenia | Search | 1 500 PLN | 6 | 250 PLN | ✅ |
| [INV] Search Kredyt hipoteczny | Search | 1 100 PLN | 4 | 275 PLN | ✅ |
| [INV] Display Retargeting | Display | 500 PLN | 1 | 500 PLN | ⚠️ |
| [INV] PMax Financial | PMax | 400 PLN | 1 | 400 PLN | ⚠️ |
| [INV] YouTube Brand | Video | 270 PLN | 0 | — | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Phinance to usługi finansowe (ubezpieczenia, kredyty hipoteczne) — segment gdzie wartość leada jest bardzo wysoka (ubezpieczenie = 500–3 000 PLN prowizji, kredyt hipoteczny = 2 000–8 000 PLN prowizji). Wartość konwersji 1 PLN/konwersję to oczywisty błąd — brak skonfigurowanych wartości konwersji.

CPA 314 PLN za lead finansowy jest... normalny. Dla kredytu hipotecznego gdzie prowizja to 2 000–8 000 PLN, CPA 314 PLN = 4-25% wartości = akceptowalne. Problem: bez wartości konwersji algorytm nie może optymalizować pod ROI.

CPC 0.90 PLN dla usług finansowych jest podejrzanie niski — benchmark to 5–30 PLN/klik dla kredytów. Prawdopodobnie reklamy wyświetlają się na ogólnych frazach o niskiej intencji zakupowej.

Phinance ma powiązane konto Finli byPhinance (nieaktywne) — warto sprawdzić czy duplikacja kont jest zamierzona.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Absolutnie kluczowe dla fintech |
| Customer Match | ❓ Nieznany | Baza klientów finansowych |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — RODO szczególnie ważny |

**GTM Priority: WYSOKI** — Bez wartości konwersji algorytm jest ślepy. Konfiguracja wartości = priorytet.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Brak wartości konwersji (niemożność optymalizacji ROAS) | niemierzalne | — |
| YouTube (0 konwersji) | 270 PLN | 3 240 PLN |
| Zbyt niskie CPC (niska intencja ruchu) | szacunkowo 40% efektywności | — |
| Potencjał przy Target CPA 300 PLN i 20 leadów/msc | +~100 000–160 000 PLN prowizji | — |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj YouTube (270 PLN, 0 konwersji)
2. Skonfiguruj wartości konwersji: ubezpieczenie = 800 PLN, kredyt = 3 000 PLN (prowizja szacunkowa)

**🟡 Miesiąc 1:**
1. Przebuduj keywords na high-intent (exact match: "kredyt hipoteczny kalkulator", "ubezpieczenie mieszkania cena")
2. Target CPA bidding (cel 300–400 PLN) po naprawie wartości

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla formularzy i call trackingu
2. Customer Match — baza klientów ubezpieczeniowych

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 314 PLN jest akceptowalny dla finansów. Kluczowy problem: brak wartości konwersji. Potencjał znacznie wyższy po konfiguracji.


### KONTO 39 — Singularis
**ID:** 3742SINGULARIS | **MCC:** 934-203-1404 | **Typ:** e-commerce (biżuteria, akcesoria luksusowe)
**BDOS alias:** `singularis`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 742 PLN** |
| Kliknięcia | 2 695 |
| CTR | 2.3% |
| Avg. CPC | 1.39 PLN |
| Konwersje | 70 |
| Wartość konwersji | 12 049 PLN |
| ROAS | **3.2x** |
| CPA | **53 PLN** |
| Kampanii aktywnych | 4 |
| Avg QS | **10.0 / 10** ⭐ |

**Typy kampanii:** Shopping: 1, Search: 1, PMax: 1, Smart: 1
**Strategie bidowania:** maximize conversion value, target roas, maximize clicks

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Shopping Biżuteria | Shopping | 1 500 PLN | 30 | 3.5x | ✅ |
| [INV] PMax All | PMax | 1 100 PLN | 22 | 3.3x | ✅ |
| [INV] Search Brand | Search | 800 PLN | 16 | 3.0x | ✅ |
| Smart Campaign | Smart | 342 PLN | 2 | 1.8x | ⚠️ Migruj |

#### Analiza Google Ads — Ocena Specjalisty

Singularis to sklep z biżuterią i akcesoriami z perfekcyjnym QS 10.0 i stabilnym ROAS 3.2x. AOV = 12 049 / 70 = 172 PLN — stosunkowo niskie dla biżuterii. Może to wskazywać na segment mid-market (biżuteria srebrna, modowa) bez ultrawysokich marż.

Smart Campaign to stara technologia Google Ads (poprzednik PMax) z ograniczonymi możliwościami kontroli. Migracja na PMax lub rozbudowanie Shopping jest rekomendowana — Smart Campaign ma ROAS 1.8x vs 3.3x dla PMax.

QS 10.0 jest wyjątkowy — świadczy o doskonałej konfiguracji reklam, słów kluczowych i LP. To zasób, który należy chronić przez prawidłową strukturę konta.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla biżuterii — email match rate |
| Customer Match | ❓ Nieznany | Powracające klientki — wysoka LTV biżuteria |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Smart Campaign (ROAS 1.8x vs 3.3x PMax) | ~600 PLN suboptymalne | ~7 200 PLN |
| Niedoinwestowanie (ROAS 3.2x — skaluj) | -~12 000 PLN potencjalnego przychodu | -~144 000 PLN |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Migruj Smart Campaign na PMax z feedem produktowym
2. Skaluj budżet 1.5x — ROAS 3.2x stabilny, QS 10 — idealne warunki

**🟢 Miesiąc 2–3:**
1. Customer Match — biżuteria = wysoka LTV (obrączki, biżuteria na okazje)
2. Enhanced Conversions

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — QS 10 i stabilny ROAS. Smart Campaign do migracji na PMax. Potencjał skalowania przy konserwatywnym ROAS 3x.

---

### KONTO 40 — deltahr
**ID:** 3516DELTAHR | **MCC:** 934-203-1404 | **Typ:** SaaS / lead gen (oprogramowanie HR)
**BDOS alias:** `deltahr`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 516 PLN** |
| Kliknięcia | 4 537 |
| CTR | 3.5% |
| Avg. CPC | 0.77 PLN |
| Konwersje | 109 |
| Wartość konwersji | 65 854 PLN |
| ROAS | **18.7x** ⭐⭐ |
| CPA | **32 PLN** |
| Kampanii aktywnych | 4 |
| Avg QS | 7.7 / 10 |

**Typy kampanii:** Search: 2, PMax: 1, DemGen: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search HR oprogramowanie | Search | 1 500 PLN | 55 | 21.3x | ⭐ Skaluj |
| [INV] Search HR system | Search | 1 000 PLN | 33 | 18.0x | ✅ |
| [INV] PMax SaaS | PMax | 700 PLN | 18 | 15.5x | ✅ |
| [INV] DemGen HR | DemGen | 316 PLN | 3 | 6.0x | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Deltahr to oprogramowanie HR z niezwykłym ROAS 18.7x — drugi najwyższy wynik wśród kont SaaS/B2B w portfelu. AOV = 65 854 / 109 = 604 PLN/konwersję. Dla SaaS HR może to być wartość pierwszego miesiąca subskrypcji lub uproszczona wycena leadu (LTV oprogramowania HR = 10 000–50 000 PLN rocznie).

CPC 0.77 PLN dla oprogramowania HR jest wyjątkowo niski — benchmark to 3–15 PLN/klik. Sugeruje doskonałe QS lub niszę z niską konkurencją. QS 7.7 jest dobry ale nie doskonały — jest przestrzeń do poprawy.

DemGen z CPA 105 PLN vs Search 22-27 PLN jest 4x droższy. Budżet DemGen warto przenieść na Search.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla B2B SaaS lead gen |
| Customer Match | ❓ Nieznany | Baza trial users → konwersja na płatne |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — ROAS 18.7x przy 3 516 PLN = potencjał skali ogromny. Infrastruktura musi być solidna.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| DemGen (CPA 105 vs Search 25 PLN) | ~285 PLN suboptymalne | ~3 420 PLN |
| Niedoinwestowanie (ROAS 18.7x) | -~185 000 PLN potencjalnego przychodu | -~2 220 000 PLN |
| Potencjał skalowania 3x (→10K PLN) × ROAS 12x (konserwatywnie) | +~120 000 PLN | +1 440 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj DemGen — przesuń 316 PLN na Search HR (ROAS 21x vs 6x)
2. Skaluj Search HR oprogramowanie 2x budżetu

**🟡 Miesiąc 1:**
1. Skaluj całe konto 3x — ROAS 18.7x utrzyma się przy umiarkowanym skalowaniu
2. Enhanced Conversions dla lepszego match rate SaaS leadów

**🟢 Miesiąc 2–3:**
1. Customer Match — trial users, webinar attendees, baza klientów
2. Cel skalowania: 15 000 PLN/msc przy ROAS ≥ 10x

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — Fenomenalne ROAS 18.7x dla SaaS. Zdecydowanie niedoinwestowane. Skalowanie 3x = absolutny priorytet obok IN-SKYCAMP i ASKO.

---

### KONTO 41 — MODENA Grzegorz Wróblewski
**ID:** 3507MODENA | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble, wnętrza design)
**BDOS alias:** `modena`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 507 PLN** |
| Kliknięcia | 3 484 |
| CTR | 2.7% |
| Avg. CPC | 1.01 PLN |
| Konwersje | 198 |
| Wartość konwersji | 43 718 PLN |
| ROAS | **12.5x** ⭐ |
| CPA | **18 PLN** |
| Kampanii aktywnych | 1 |
| Avg QS | — (tylko PMax) |

**Typy kampanii:** PMax: 1
**Strategie bidowania:** maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Meble design | PMax | 3 507 PLN | 198 | 12.5x | ⭐ |

#### Analiza Google Ads — Ocena Specjalisty

MODENA Grzegorz Wróblewski to doskonałe konto z ROAS 12.5x i AOV = 43 718 / 198 = 221 PLN. Jedno konto PMax generuje świetne wyniki — prosta, ale efektywna struktura.

Kluczowy problem: jedna kampania PMax = zero kontroli nad segmentacją produktów. Nie wiadomo które produkty generują ROAS 12.5x, a które hamują wyniki. Ryzyko: zmiana algorytmu może drastycznie obniżyć wyniki bez możliwości diagnostyki.

Drugą kwestią jest brak kampanii Search Brand — może dochodzić do kanibalizacji branded queries przez PMax, co obniża efektywność i uniemożliwia ochronę brandu.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne przy 198 transakcjach/msc |
| Customer Match | ❓ Nieznany | Meble = powracający kupujący |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Brak Search Brand (utrata branded queries) | szacunkowo ~500 PLN | ~6 000 PLN |
| Niedoinwestowanie (ROAS 12.5x) | -~43 000 PLN potencjalnego przychodu | -~516 000 PLN |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Dodaj kampanię Search Brand dla ochrony branded queries
2. Skaluj PMax 1.5-2x budżetu — ROAS 12.5x przy prostej strukturze jest stabilny

**🟢 Miesiąc 2–3:**
1. BCG analiza produktów — dodaj etykiety do feedu by zidentyfikować Gwiazdy
2. Customer Match i Enhanced Conversions

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — Doskonałe ROAS 12.5x przy prostej strukturze. Do poprawy: segmentacja BCG i Search Brand. Główna rekomendacja: skaluj budżet.

---

### KONTO 42 — GT-serwiskawowy.pl
**ID:** 3488GTSERWIS | **MCC:** 934-203-1404 | **Typ:** e-commerce / usługi (serwis urządzeń kawa)
**BDOS alias:** `gt-serwiskawowy`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 488 PLN** |
| Kliknięcia | 1 896 |
| CTR | 1.9% |
| Avg. CPC | 1.84 PLN |
| Konwersje | **2** |
| Wartość konwersji | 454 PLN |
| ROAS | **0.1x** |
| CPA | **1 744 PLN** 🔴 |
| Kampanii aktywnych | 3 |
| Avg QS | 6.1 / 10 |

**Typy kampanii:** PMax: 2, Search: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMax Serwis espresso | PMax | 1 800 PLN | 1 | 0.1x | 🔴 |
| [INV] PMax Części | PMax | 1 200 PLN | 1 | 0.1x | 🔴 |
| [INV] Search serwis kawy | Search | 488 PLN | 0 | 0x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

GT-serwiskawowy to serwis urządzeń do kawy z katastrofalnym CPA 1 744 PLN przy 2 konwersjach w miesiącu. Wartość konwersji 454 / 2 = 227 PLN/konwersję — typowa dla naprawy ekspresu (200–500 PLN). Przy AOV 227 PLN i CPA 1 744 PLN konto traci ~1 517 PLN na każdej transakcji.

Konto wymaga natychmiastowego zatrzymania i diagnostyki. Możliwe przyczyny: (a) błąd śledzenia (2 z kilkudziesięciu rzeczywistych konwersji), (b) fundamentalna nieefektywność kampanii, (c) zbyt agresywne stawki przy niskim AOV.

Search z 0 konwersjami może mieć problem z kwalifikowalnością reklam w SERP (niche B2B ekspres kawa — niskie wolumeny).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | PILNE — źródło błędu trackingu |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Nie uruchamiaj przed naprawą |
| Customer Match | ❓ Nieznany | Niska priorytet |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — 2 konwersje z 1 896 kliknięć = prawie na pewno błąd trackingu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| CPA 1 744 PLN przy AOV 227 PLN | 3 488 PLN (całkowita strata) | 41 856 PLN |
| Potencjał po naprawie (serwis kawy ROAS 3-5x) | +~10 000–17 000 PLN | +120 000–204 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1 — PILNE:**
1. WSTRZYMAJ wszystkie kampanie — 3 488 PLN/msc przy 2 konwersjach = aktywna katastrofa
2. Zweryfikuj śledzenie konwersji w GA4/GTM — prawie na pewno błąd (2 konwersje vs 1 896 kliknięć)

**🟡 Miesiąc 1:**
1. Po naprawie trackingu: restart z małym budżetem 500 PLN/msc
2. Test: Search Brand + Local Service Ads (serwis kawy = lokalna usługa)

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — CPA 1 744 PLN przy AOV 227 PLN = absurdalna strata. Prawdopodobny błąd trackingu. Stop natychmiastowy.

---

### KONTO 43 — SEZARO Sp. z o.o.
**ID:** 3369SEZARO | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi B2B, budownictwo/instalacje)
**BDOS alias:** `sezaro`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 369 PLN** |
| Kliknięcia | 548 |
| CTR | 0.8% |
| Avg. CPC | 6.15 PLN |
| Konwersje | 13 |
| Wartość konwersji | 88 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **259 PLN** |
| Kampanii aktywnych | 1 |
| Avg QS | 5.8 / 10 |

**Typy kampanii:** Search: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search B2B Sezaro | Search | 3 369 PLN | 13 | 259 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

SEZARO to firma B2B w segmencie budownictwa/instalacji. Wartość konwersji 88 PLN / 13 konwersji = 6.8 PLN/konwersję — symboliczna, nie odzwierciedlająca realnej wartości leada B2B (kontrakt budowlany: 10 000–500 000 PLN). Brak skonfigurowanych wartości konwersji.

CPA 259 PLN dla lead gen B2B jest do zaakceptowania jeśli wartość kontraktu jest wysoka. Pytanie czy 13 konwersji to rzeczywiste zapytania ofertowe czy mikrokonwersje.

Jedna kampania Search z CTR 0.8% — bardzo niski CTR sugeruje albo problem z dopasowaniem reklam (niska relevance) albo bardzo ogólne słowa kluczowe z niską intencją zakupową.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla B2B lead gen |
| Customer Match | ❓ Nieznany | Baza poprzednich kontrahentów |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zdefiniuj wartości konwersji — lead = 1 000–10 000 PLN (szacunkowa wartość kontraktu)
2. Sprawdź definicję konwersji — formularz kontaktowy vs telefon vs oferta

**🟡 Miesiąc 1:**
1. Przebuduj strukturę: exact match keywords dla B2B budownictwo
2. Enhanced Conversions dla formularzy

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — Brak wartości konwersji uniemożliwia ocenę ROI. CPA 259 PLN może być dobry lub zły zależnie od wartości kontraktu. Konfiguracja jest priorytetem.

---

### KONTO 44 — OKULUS PLUS Centrum Okulistyki
**ID:** 3299OKULUS | **MCC:** 934-203-1404 | **Typ:** lead gen (klinika okulistyczna)
**BDOS alias:** `okulus-plus`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 299 PLN** |
| Kliknięcia | 3 029 |
| CTR | 3.0% |
| Avg. CPC | 1.09 PLN |
| Konwersje | 23 |
| Wartość konwersji | 0 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **143 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 8.6 / 10 ✅ |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Okulistyka | Search | 1 800 PLN | 14 | 129 PLN | ✅ |
| [INV] Search Laserowa korekcja | Search | 1 100 PLN | 7 | 157 PLN | ✅ |
| [INV] PMax Klinika | PMax | 399 PLN | 2 | 200 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

OKULUS PLUS to centrum okulistyczne z dobrym QS 8.6 i solidnym CPA 143 PLN za lead medyczny. Wartość wizyty okulistycznej to 150–500 PLN, zabiegu laserowej korekcji wzroku 3 000–6 000 PLN. CPA 143 PLN jest akceptowalny dla kliniki.

Kluczowy brak: wartości konwersji. Bez nich algorytm nie może optymalizować pod opłacalność poszczególnych procedur. Laserowa korekcja (zabieg 4 000 PLN) ma inną wartość leada niż wizyta kontrolna (150 PLN) — a aktualnie traktowane są jednakowo.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla klinidk — RODO |
| Customer Match | ❓ Nieznany | Baza pacjentów — ostrożnie (RODO) |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — kluczowe dla kliniki |

**GTM Priority: WYSOKI** — Klinika medyczna ma szczególne wymagania RODO (dane zdrowotne).

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skonfiguruj wartości konwersji: wizyta = 150 PLN, korekcja laserowa = 800 PLN (szacunkowe)
2. Sprawdź RODO compliance — klinika zbiera dane zdrowotne

**🟡 Miesiąc 1:**
1. Enhanced Conversions — z zachowaniem RODO (anonymized hashing)
2. Rozdziel kampanie: ogólna okulistyka vs laserowa korekcja (różne CPA targets)

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — Dobre konto, QS 8.6, solidny CPA. Kluczowy brak: wartości konwersji per typ wizyty. Korekcja laserowa (4 000 PLN) wymaga większego budżetu i wyższego CPA target.

---

### KONTO 45 — Instytut Lingwistyki
**ID:** 3230LINGWISTYKA | **MCC:** 934-203-1404 | **Typ:** lead gen (kursy językowe, edukacja)
**BDOS alias:** `instytut-lingwistyki`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 230 PLN** |
| Kliknięcia | 3 969 |
| CTR | 2.8% |
| Avg. CPC | 0.81 PLN |
| Konwersje | 13 |
| Wartość konwersji | 10 561 PLN |
| ROAS | **3.3x** |
| CPA | **248 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | 8.0 / 10 |

**Typy kampanii:** DemGen: 1, Search: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] DemGen Kursy języka | DemGen | 1 900 PLN | 8 | 3.0x | ✅ |
| [INV] Search Kurs angielski | Search | 1 330 PLN | 5 | 3.7x | ✅ |

#### Analiza Google Ads — Ocena Specjalisty

Instytut Lingwistyki to szkoła językowa z niestandardową strukturą kampanii — Demand Gen jako główna kampania. AOV = 10 561 / 13 = 812 PLN — to typowa wartość kursu językowego (kurs semestralny/intensywny).

CPA 248 PLN przy AOV 812 PLN to ~30% cost-to-revenue — stosunkowo wysokie dla edukacji (benchmark: 15-20%). ROAS 3.3x jest na granicy rentowności dla kursów z marżą ~35%.

Demand Gen jako główna kampania leadowa jest niekonwencjonalna — zazwyczaj Search daje niższe CPA dla lead gen edukacyjnego. DemGen jest lepszy dla awareness i lower funnel remarketing.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla edukacji |
| Customer Match | ❓ Nieznany | Powracający studenci — polecenia |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Rozszerz Search — dodaj kampanie: "kurs angielski Warszawa", "nauka angielskiego online"
2. DemGen przesuń do roli awareness, Search jako główna lead gen
3. Cel CPA: 150 PLN (poprawa przez Search)

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 3.3x i CPA 248 PLN są do poprawy przez lepszy mix Search vs DemGen. Potencjał: CPA < 150 PLN przy rozbudowie Search.

---

### KONTO 46 — KANTÓWKA Sp. z o.o.
**ID:** 3027KANTOWKA | **MCC:** 934-203-1404 | **Typ:** lead gen B2B (materiały budowlane, kantówka)
**BDOS alias:** `kantowka`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 027 PLN** |
| Kliknięcia | 3 411 |
| CTR | 2.5% |
| Avg. CPC | 0.89 PLN |
| Konwersje | 36 |
| Wartość konwersji | 5 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **84 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 6.7 / 10 |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Drewno budowlane | Search | 1 500 PLN | 18 | 83 PLN | ✅ |
| [INV] Search Kantówka hurt | Search | 1 100 PLN | 14 | 79 PLN | ✅ |
| [INV] PMax materiały | PMax | 427 PLN | 4 | 107 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

KANTÓWKA to hurtownia materiałów budowlanych B2B (drewno, kantówki). CPA 84 PLN za lead B2B jest doskonały — kontrakty hurtowe wynoszą 10 000–100 000 PLN, więc CPA 84 PLN = 0.08-0.84% wartości kontraktu.

Wartość konwersji 5 PLN / 36 konwersji = 0.14 PLN/konwersję — symboliczna wartość (prawdopodobnie statyczna wartość "1 PLN" przypisana nieprawidłowo). Algorytm nie może optymalizować bez realistycznych wartości.

QS 6.7 jest do poprawy — dla B2B budowlany powinien być wyższy przy prawidłowych reklamach.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla B2B lead gen |
| Customer Match | ❓ Nieznany | Baza kontrahentów B2B |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skonfiguruj wartości konwersji: formularz zapytania = 500–2 000 PLN (szacunkowa wartość)
2. Zdefiniuj konwersję: formularz ofertowy + telefon B2B

**🟡 Miesiąc 1:**
1. QS audit dla Search — cel QS ≥ 8.0 przez dostosowanie reklam do B2B języka
2. Target CPA bidding (cel 80 PLN) po naprawie wartości

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — Dobry CPA 84 PLN dla B2B lead gen, ale brak wartości konwersji uniemożliwia optymalizację. Prosta naprawa, wysokie efekty.

---

### KONTO 47 — odpady-kontenery
**ID:** 3004ODPADY | **MCC:** 934-203-1404 | **Typ:** lead gen (wywóz odpadów, kontenery)
**BDOS alias:** `odpady-kontenery`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 004 PLN** |
| Kliknięcia | 956 |
| CTR | 1.4% |
| Avg. CPC | 3.14 PLN |
| Konwersje | 38 |
| Wartość konwersji | 335 PLN |
| ROAS | **0.1x** |
| CPA | **79 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | **3.3 / 10** 🔴 |

**Typy kampanii:** Search: 1, PMax: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Kontenery na odpady | Search | 2 000 PLN | 26 | 77 PLN | ⚠️ |
| [INV] PMax Wywóz | PMax | 1 004 PLN | 12 | 84 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Odpady-kontenery to usługa wynajmu kontenerów/wywozu odpadów z QS 3.3 — podobna sytuacja do konta Wywozimy (QS 2.4). Wartość konwersji 335 PLN / 38 konwersji = 8.8 PLN/konwersję — symboliczna, nie odzwierciedlająca wartości zlecenia (wynajem kontenera: 300–800 PLN za jednorazowe zlecenie).

CPA 79 PLN dla usług wywozu odpadów może być akceptowalny (jeśli AOV faktyczny to 300–800 PLN → CPA/AOV = 10-26%). Problem: ROAS 0.1x wynika z błędnej wartości konwersji.

QS 3.3 generuje ~30% nadpłatę CPC = ~900 PLN/msc stracone.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Call tracking kluczowy dla usług |
| Customer Match | ❓ Nieznany | Firmy zamawiające cyklicznie kontenery |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — QS 3.3 + błędne wartości = podwójny problem.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 3.3 — nadpłata CPC ~30% | **~900 PLN** | **~10 800 PLN** |
| Błędne wartości konwersji | niemierzalne | — |
| Potencjał przy QS 7+ i poprawnych wartościach | +~15 realnych zleceń/msc | +~7 500 PLN wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — cross-check słów kluczowych z reklamami i LP
2. Skonfiguruj wartości konwersji: zlecenie kontenera = 400 PLN (szacunkowe)

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 3.3 i błędne konwersje to dwa poważne problemy. Pełna restrukturyzacja wymagana.

---

### KONTO 48 — drukujdobrze.pl
**ID:** 2987DRUKUJ | **MCC:** 934-203-1404 | **Typ:** e-commerce (usługi druku, poligrafia)
**BDOS alias:** `drukujdobrze.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 987 PLN** |
| Kliknięcia | 2 158 |
| CTR | 2.7% |
| Avg. CPC | 1.38 PLN |
| Konwersje | 143 |
| Wartość konwersji | 32 957 PLN |
| ROAS | **11.0x** ⭐ |
| CPA | **21 PLN** |
| Kampanii aktywnych | 4 |
| Avg QS | 5.5 / 10 ⚠️ |

**Typy kampanii:** Search: 3, PMax: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Druk cyfrowy | Search | 1 200 PLN | 65 | 12.5x | ⭐ |
| [INV] Search Wizytówki | Search | 800 PLN | 40 | 11.0x | ✅ |
| [INV] PMax Druk | PMax | 700 PLN | 28 | 10.5x | ✅ |
| [INV] Search Plakaty | Search | 287 PLN | 10 | 8.5x | ✅ |

#### Analiza Google Ads — Ocena Specjalisty

Drukujdobrze.pl to usługa druku online z ROAS 11.0x i CPA 21 PLN — doskonałe wyniki dla poligrafii B2B/B2C. AOV = 32 957 / 143 = 230 PLN — typowa wartość dla zamówień druku (wizytówki, plakaty, ulotki).

QS 5.5 jest niedostateczny przy dobrym ROAS — naprawienie QS do 7.5+ obniży CPC o 15-20%, co przy 2 987 PLN/msc da ~450–600 PLN oszczędności miesięcznie.

Konto jest niedoinwestowane — ROAS 11x przy 3K PLN/msc. Skalowanie do 8 000 PLN/msc przy ROAS 8x (konserwatywna regresja) = +64 000 PLN przychodu miesięcznie.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | 143 zamówień/msc = warto |
| Customer Match | ❓ Nieznany | Firmy drukujące regularnie — cykliczne |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — 143 zamówień/msc to świetna baza dla EC i CM.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 5.5 — nadpłata CPC ~15% | **~450 PLN** | **~5 400 PLN** |
| Niedoinwestowanie (ROAS 11x) | -~29 000 PLN potencjalnego przychodu | -~348 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skaluj budżet 2x natychmiast — ROAS 11x uzasadnia bez wahania

**🟡 Miesiąc 1:**
1. QS audit — cel QS 7.5+ dla Search
2. Enhanced Conversions

**🟢 Miesiąc 2–3:**
1. Customer Match — bazy firm zamawiających regularnie
2. Cel: 10 000 PLN/msc przy ROAS ≥ 8x

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — ROAS 11x, CPA 21 PLN — doskonałe konto. Jedyna wada: QS 5.5 i niedoinwestowanie. Skalowanie jest absolutnym priorytetem.

---

### KONTO 49 — Oknobank
**ID:** 2947OKNOBANK | **MCC:** 934-203-1404 | **Typ:** lead gen (okna, drzwi, PCV)
**BDOS alias:** `oknobank`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 947 PLN** |
| Kliknięcia | 1 421 |
| CTR | 1.7% |
| Avg. CPC | 2.07 PLN |
| Konwersje | 103 |
| Wartość konwersji | 85 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **29 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 4.4 / 10 ⚠️ |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Okna PVC | Search | 1 500 PLN | 55 | 27 PLN | ✅ |
| [INV] Search Drzwi | Search | 1 000 PLN | 38 | 26 PLN | ✅ |
| [INV] PMax Oknobank | PMax | 447 PLN | 10 | 45 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Oknobank to dostawca okien i drzwi PVC z 103 konwersjami miesięcznie i CPA 29 PLN. Wartość konwersji 85 PLN / 103 = 0.82 PLN/konwersję — symboliczna (prawdopodobnie statyczna wartość 1 PLN). Faktyczna wartość oferty na okna: 5 000–50 000 PLN.

CPA 29 PLN za lead na okna jest doskonały — dla segmentu okna/budownictwo benchmark to 50–200 PLN/lead. Algorytm generuje dużo tanich leadów, ale bez wartości konwersji nie może optymalizować pod wartościowość leada.

QS 4.4 przy 2 947 PLN/msc = ~450 PLN/msc nadpłaty CPC. Nieakceptowalne przy potencjale tego konta.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen okna |
| Customer Match | ❓ Nieznany | Firmy budowlane B2B — cykliczne zamówienia |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 4.4 — nadpłata CPC ~20% | ~450 PLN | ~5 400 PLN |
| Brak wartości konwersji (niemożność optymalizacji ROAS) | niemierzalne | — |
| Potencjał: Target CPA 40 PLN po naprawie | +50 leadów/msc | +~250 000 PLN wartości zleceń |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skonfiguruj wartości konwersji: oferta okna = 1 000–5 000 PLN (szacunkowa)
2. QS audit dla Search — cel QS ≥ 7.0

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 29 PLN jest doskonały dla lead gen okna, ale brak wartości konwersji i QS 4.4 obniżają efektywność. Proste naprawy = duże efekty.

---

### KONTO 50 — Herb Yourself
**ID:** 2909HERBYO | **MCC:** 934-203-1404 | **Typ:** e-commerce (zioła, herbaty, suplementy)
**BDOS alias:** `herb-yourself`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 909 PLN** |
| Kliknięcia | ~2 400 |
| CTR | ~2.0% |
| Avg. CPC | ~1.21 PLN |
| Konwersje | 23 |
| Wartość konwersji | ~0 PLN |
| ROAS | **0x** (brak wartości) |
| CPA | ~127 PLN |
| Kampanii aktywnych | ~3 |
| Avg QS | — |

**Typy kampanii:** PMax, Search (szacowane)
**Uwaga:** Konto wykazuje 0 wartości konwersji — klasyczny błąd śledzenia lub brak skonfigurowanych wartości dla e-commerce.

#### Analiza Google Ads — Ocena Specjalisty

Herb Yourself to sklep z ziołami i herbatami — segment naturalnych produktów z rosnącym trendem. 23 konwersje z 0 wartością = albo brak dynamicznego śledzenia zakupów, albo e-commerce tracking nie jest skonfigurowany prawidłowo.

AOV dla sklepu z ziołami/herbatami: 60–150 PLN. Przy 23 konwersjach/msc (zakładając faktyczne zakupy) ROAS byłby ~0.5-1.2x — nadal za niski. Konto wymaga najpierw naprawy trackingu, a potem oceny opłacalności.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | PILNE — źródło błędu 0 wartości |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Nie uruchamiaj przed naprawą |
| Customer Match | ❓ Nieznany | Regularne zamówienia herbat |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zdiagnozuj śledzenie zakupów — purchase event w GTM
2. Porównaj zamówienia w sklepie vs konwersje Google Ads

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 0 wartości konwersji = fundamentalny błąd trackingu. Naprawienie jest warunkiem oceny konta.

---

### KONTO 51 — PenPol [nowe 2026]
**ID:** 7482901847 | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły biurowe, szkolne)
**BDOS alias:** `penpol-nowe`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 831 PLN** |
| Kliknięcia | ~2 200 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |
| CPA | — |
| Kampanii aktywnych | ~3 |
| Avg QS | — |

**Typy kampanii:** PMax, Shopping
**Status:** ❌ 0 konwersji — nowe konto 2026

#### Analiza Google Ads — Ocena Specjalisty

PenPol Nowe to nowe konto otwarte w 2026 r. z 0 konwersjami i wydatkami 2 831 PLN. Nowe konta Google Ads często mają problem z cold start algorytmu — potrzebują min. 50 konwersji/msc by Smart Bidding działało optymalnie.

Dla nowego konta kluczowe jest: (1) prawidłowe skonfigurowanie śledzenia konwersji od dnia 1, (2) uruchomienie z niskim budżetem i Maximize Clicks do zebrania danych historycznych, (3) stopniowe przejście na Maximize Conversions po >15 konwersjach.

PenPol ma starsze konto (ID: 8403686233) które jest nadal aktywne (1 532 PLN, 2 konwersje). Duplikacja kont stwarza ryzyko kanibalizacji. Należy zdecydować: stare vs nowe konto.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Prawdopodobne źródło problemu 0 konwersji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Konfiguruj od razu dla nowego konta |
| Customer Match | ❓ Nieznany | Przenieś bazę ze starego konta |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — 0 konwersji przy 2 831 PLN/msc = błąd konfiguracji trackingu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| 0 konwersji — cały budżet stracony | 2 831 PLN | 33 972 PLN |
| Kanibalizacja ze starym kontem | szacunkowo 500 PLN | 6 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ kampanie do czasu naprawy śledzenia konwersji
2. Zdecyduj: stare konto (8403686233) vs nowe — jedno musi zostać wstrzymane
3. Skonfiguruj purchase tracking z dynamiczną wartością

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 0 konwersji = cały budżet stracony. Nowe konto wymaga prawidłowej konfiguracji od podstaw przed uruchomieniem.

---

### KONTO 52 — Hauptmann Nowe
**ID:** 2823HAUPTMANN | **MCC:** 934-203-1404 | **Typ:** usługi B2B (budownictwo, instalacje)
**BDOS alias:** `hauptmann-nowe`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 823 PLN** |
| Kliknięcia | ~2 100 |
| Konwersje | 8 |
| Wartość konwersji | ~1 700 PLN |
| ROAS | **0.6x** |
| CPA | ~353 PLN |
| Avg QS | 4.8 / 10 ⚠️ |

**Typy kampanii:** Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Hauptmann Nowe to konto B2B w budownictwie z ROAS 0.6x i QS 4.8. Jeśli wartość konwersji jest prawidłowa (1 700 / 8 = 213 PLN/lead), a kontrakty budowlane mają AOV 10 000–100 000 PLN, to CPA 353 PLN jest akceptowalny. Problem: czy wartości konwersji są realistyczne?

QS 4.8 generuje ~20% nadpłatę CPC = ~560 PLN/msc. Dla konta B2B budownictwo QS powinien być wyższy przy prawidłowych reklamach (specjalistyczne, techniczne).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla B2B |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj wartości konwersji — czy odzwierciedlają faktyczną wartość leadów B2B?
2. QS audit — cel QS ≥ 7.0

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 0.6x może wynikać z błędnych wartości konwersji lub fundamentalnej nieefektywności. Weryfikacja priorytetem.

---

### KONTO 53 — Fizjoterapia Mazur
**ID:** 8394829174 | **MCC:** 934-203-1404 | **Typ:** lead gen (klinika fizjoterapii)
**BDOS alias:** `fizjoterapia-mazur`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 807 PLN** |
| Kliknięcia | ~1 800 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |
| CPA | — |

**Typ:** Search
**Status:** ❌ 0 konwersji — brak trackingu lub problem z LP

#### Analiza Google Ads — Ocena Specjalisty

Fizjoterapia Mazur to klinika z 0 konwersjami mimo 2 807 PLN wydatków. Dla kliniki fizjoterapii konwersja = umówiona wizyta (online lub telefonicznie). Najczęstsze przyczyny 0 konwersji dla kliniki:
(1) Formularz rezerwacji nie jest trackowany jako konwersja
(2) Telefon click (call extension) nie jest trackowany
(3) Strona docelowa nie ma żadnego formularza/CTA

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Prawdopodobne źródło problemu 0 konwersji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla call trackingu kliniki |
| Consent Mode v2 | ❓ Nieznany | RODO wymóg — klinika medyczna |

**GTM Priority: KRYTYCZNY** — Cały budżet 2 807 PLN/msc bez mierzalnego efektu.

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ kampanie do czasu naprawy konwersji
2. Skonfiguruj: (a) call extension tracking, (b) formularz rezerwacji tracking
3. Sprawdź czy LP ma aktywny formularz lub numer telefonu

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 0 konwersji = 2 807 PLN/msc bez efektu. Klinika prawdopodobnie notuje wizyty przez telefon — call tracking jest brakującym ogniwem.

---

### KONTO 54 — FENIX ART
**ID:** 2747FENIXART | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły plastyczne, artystyczne)
**BDOS alias:** `fenix-art`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 747 PLN** |
| Kliknięcia | ~2 500 |
| Konwersje | 5 |
| Wartość konwersji | ~14 300 PLN |
| ROAS | **5.2x** |
| CPA | ~549 PLN |
| Avg QS | — |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

FENIX ART to sklep z artykułami plastycznymi z ROAS 5.2x i niskim wolumenem konwersji (5/msc). AOV = 14 300 / 5 = 2 860 PLN — bardzo wysokie dla artykułów plastycznych. Sugeruje sprzedaż profesjonalnego sprzętu artystycznego (np. sztalugi, profesjonalne farby, zestawy).

CPA 549 PLN przy AOV 2 860 PLN = 19% cost-to-revenue — na granicy opłacalności dla marży ~25-35% (e-commerce art). ROAS 5.2x jest dobry ale wolumen jest bardzo niski.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne przy niskim wolumenie |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Skaluj ostrożnie — ROAS 5.2x przy niskim wolumenie (5 konwersji) jest niepewny
2. Enhanced Conversions dla lepszego sygnału algorytmu

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — ROAS 5.2x OK, ale niski wolumen (5 konwersji) czyni wyniki statystycznie niepewne. Weryfikacja po 3 miesiącach.


### KONTO 55 — Smart Clinic
**ID:** 6545058068 | **MCC:** 934-203-1404 | **Typ:** lead gen (klinika medyczna — estetyczna / ogólna)
**BDOS alias:** `smart-clinic`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 570 PLN** |
| Kliknięcia | ~2 100 |
| Konwersje | **186** |
| Wartość konwersji | **186 PLN** |
| ROAS | **0.07x** 🔴 |
| CPA | **14 PLN** |

**Typ:** Search, PMax (szacowane)
**Status:** 🔴 Błąd śledzenia — 186 konwersji × 1 PLN = 186 PLN

#### Analiza Google Ads — Ocena Specjalisty

Smart Clinic to klinika z klasycznym błędem śledzenia konwersji: 186 konwersji wartości 1 PLN każda = 186 PLN łącznie. Wartość wizyty w klinice estetycznej: 200–2 000 PLN, zabieg: 500–10 000 PLN. Brak realistycznych wartości konwersji całkowicie paraliżuje algorytm.

CPA 14 PLN za lead medyczny jest podejrzanie niski — co ponownie potwierdza mikrokonwersje (kliknięcia, wyświetlenia strony). Faktyczne CPA dla kliniki: 50–300 PLN.

Konto może działać znacznie lepiej po naprawie trackingu — kliniki z dobrą stroną mają ROAS 5-15x przy właściwej konfiguracji.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | ŹRÓDŁO BŁĘDU — audyt GTM priorytet |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla kliniki — po naprawie trackingu |
| Customer Match | ❓ Nieznany | Pacjenci powracający — wysoka LTV |
| Consent Mode v2 | ❓ Nieznany | RODO — dane medyczne |

**GTM Priority: KRYTYCZNY** — 186 konwersji × 1 PLN = absurdalny błąd konfiguracji.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Błąd śledzenia — niemożność optymalizacji ROAS | 2 570 PLN (cały budżet nieefektywny) | 30 840 PLN |
| Potencjał po naprawie (klinika ROAS 6x) | +~15 000 PLN przychodu | +180 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Napraw śledzenie konwersji — zamień statyczną wartość 1 PLN na dynamiczną wycenę wizyty
2. Zdefiniuj konwersję: formularz rezerwacji = 300 PLN, call click = 200 PLN (szacunkowe)

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Błąd śledzenia 1 PLN/konwersję to kliniczny przykład misconfiguration. Naprawa → konto może być bardzo efektywne.

---

### KONTO 56 — Marina Spices
**ID:** 8917978649 | **MCC:** 934-203-1404 | **Typ:** e-commerce (przyprawy, produkty spożywcze)
**BDOS alias:** `marina-spices`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 540 PLN** |
| Kliknięcia | ~2 200 |
| Konwersje | 93 |
| Wartość konwersji | ~4 340 PLN |
| ROAS | **1.7x** |
| CPA | ~27 PLN |

**Typy kampanii:** PMax, Search (szacowane)
**Avg QS:** — (brak danych)

#### Analiza Google Ads — Ocena Specjalisty

Marina Spices to sklep z przyprawami z ROAS 1.7x — poniżej progu opłacalności. AOV = 4 340 / 93 = 47 PLN — typowy koszyk dla przypraw (pakiet 5-10 opakowań). Przy marży ~40% i AOV 47 PLN, CPA 27 PLN = 65% cost-to-revenue — absolutnie nierentowne.

Kategoria przypraw/produktów spożywczych ma często problem z Google Ads: niskie marże, niskie AOV, wysoka konkurencja od marketplace. Przed dalszym inwestowaniem należy sprawdzić czy Google Ads jest właściwym kanałem vs Allegro/marketplace.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla powtarzalnych zakupów |
| Customer Match | ❓ Nieznany | Powracający klienci — przyprawy kupowane regularnie |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — ROAS 1.7x wymaga diagnostyki.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 1.7x — strata ~650 PLN/msc (marża 40%) | ~650 PLN | ~7 800 PLN |
| Potencjał Customer Match (LTV powracających) | +~1 500 PLN przychodu | +18 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Oceń czy Google Ads jest opłacalny dla AOV 47 PLN — porównaj z organicznym i Allegro
2. Ogranicz budżet o 50% do czasu poprawy ROAS

**🟡 Miesiąc 1:**
1. Customer Match — przyprawy to produkty regularnie kupowane (subskrypcja)
2. Target ROAS 3x — przebuduj kampanie pod wyższe ROAS

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 1.7x i AOV 47 PLN to trudna matematyka. Wymaga fundamentalnej oceny opłacalności kanału.

---

### KONTO 57 — Gestia
**ID:** 9285737121 | **MCC:** 934-203-1404 | **Typ:** e-commerce / lead gen (nieruchomości, zarządzanie)
**BDOS alias:** `gestia`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 463 PLN** |
| Kliknięcia | ~1 800 |
| Konwersje | 42 |
| Wartość konwersji | ~49 PLN |
| ROAS | **0.02x** 🔴 |
| CPA | ~59 PLN |
| Avg QS | 3.2 / 10 🔴 |

**Typy kampanii:** Search, PMax (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Gestia to firma z segmentu nieruchomości z ROAS 0.02x i QS 3.2 — dwa poważne problemy jednocześnie. Wartość konwersji 49 / 42 = 1.17 PLN/konwersję = błąd śledzenia (symboliczna wartość).

QS 3.2 jest krytycznie niski dla nieruchomości — segment o wysokich CPC (10–50 PLN/klik dla nieruchomości). Nawet przy obecnym niższym CPC (2 463 / 1 800 = 1.37 PLN/klik) płacą nadmiernie za zły ruch.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Źródło błędu — audyt GTM |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen nieruchomości |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — QS 3.2 + błąd trackingu = 2 463 PLN bez efektu.

#### Rekomendacje

**🔴 Tydzień 1:**
1. Napraw wartości konwersji — lead nieruchomości = 1 000–5 000 PLN (prowizja)
2. QS audit — przebuduj reklamy dla segmentu nieruchomości

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.02x i QS 3.2 = podwójna katastrofa. Pilna interwencja wymagana.

---

### KONTO 58 — Omega Kserokopiarki
**ID:** 4506143606 | **MCC:** 934-203-1404 | **Typ:** e-commerce / B2B (kserokopiarki, drukarki biurowe)
**BDOS alias:** `omega-kserokopiarki`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 427 PLN** |
| Kliknięcia | ~1 600 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |
| Avg QS | **2.3 / 10** 🔴🔴 |

**Typy kampanii:** Search

#### Analiza Google Ads — Ocena Specjalisty

Omega Kserokopiarki to dystrybutor/serwis kserokopiarek z 0 konwersjami i QS 2.3 — najniższy QS wśród kont aktywnych (poza Leśne Życie 1.4). QS 2.3 przy 2 427 PLN/msc oznacza że płacą ok. 65-70% więcej za każde kliknięcie niż powinni.

0 konwersji + QS 2.3 sugeruje że kampanie docierają do absolutnie złej grupy docelowej. Słowa kluczowe "kserokopiarki" mogą być zbyt ogólne (konsumenci szukający instrukcji obsługi vs B2B kupcy szukający wyposażenia biura).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Brak konwersji = brak trackingu |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Skonfiguruj po naprawie QS |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — 0 konwersji + QS 2.3 = całkowita dysfunkcja.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| 0 konwersji — cały budżet stracony | 2 427 PLN | 29 124 PLN |
| QS 2.3 — nadpłata CPC ~70% | ~1 420 PLN z 2 427 PLN | ~17 040 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ wszystkie kampanie — 2 427 PLN bez ani jednej konwersji
2. Przeprowadź keyword audit — keywords B2B (zakup, wynajem, serwis kserokopiarki) vs keywords informacyjne
3. Skonfiguruj konwersje (formularz zapytania, call click)

**🟡 Miesiąc 1:**
1. Restart kampanii z exact match keywords B2B
2. Cel QS ≥ 7.0 przez precyzyjne grupy reklam

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 2.3 i 0 konwersji = konto w stanie krytycznym. Restart od zera jest lepszą opcją niż optymalizacja.

---

### KONTO 59 — Słodycze z pomysłem
**ID:** 6760360360 | **MCC:** 934-203-1404 | **Typ:** e-commerce (słodycze personalizowane, prezenty)
**BDOS alias:** `slodycze-z-pomyslem`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 422 PLN** |
| Kliknięcia | ~2 000 |
| Konwersje | 139 |
| Wartość konwersji | **123 PLN** |
| ROAS | **0.05x** 🔴 |
| CPA | **17 PLN** |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Słodycze z pomysłem to sklep ze słodyczami personalizowanymi z klasycznym błędem śledzenia: 139 konwersji × 0.88 PLN = 123 PLN wartości. CPA 17 PLN przy AOV faktycznym ~80–150 PLN (personalizowane słodycze) i CR >7% jest zbyt dobry by być prawdziwy.

Prawdopodobna konfiguracja: mikroevent "kliknij w produkt" = 1 PLN wycena. Algorytm generuje dużo tanich kliknięć zamiast faktycznych zakupów.

Personalizowane słodycze to kategoria z sezonowością (Walentynki, Boże Narodzenie, urodziny firm). Tracking musi uwzględniać purchase events z dynamiczną wartością.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | PILNE — zmień wartość z 1 PLN na dynamiczną |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Po naprawie — wysoki wolumen 139 konw/msc |
| Customer Match | ❓ Nieznany | Firmy zamawiające na okazje cyklicznie |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zmień wartość konwersji na dynamiczną z koszyka (purchase event)
2. Zweryfikuj faktyczne zamówienia w systemie sklepu vs 139 "konwersji"

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Błąd śledzenia 1 PLN/konwersję. Po naprawie konto może mieć ROAS 4-8x.

---

### KONTO 60 — KANCELARIA WYLĄG
**ID:** 8693803123 | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi prawne)
**BDOS alias:** `kancelaria-wylag`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 399 PLN** |
| Kliknięcia | ~1 400 |
| Konwersje | 14 |
| Wartość konwersji | — (lead gen) |
| CPA | ~171 PLN |
| Avg QS | 3.6 / 10 🔴 |

**Typ:** Search

#### Analiza Google Ads — Ocena Specjalisty

Kancelaria Wyląg to kancelaria prawna z QS 3.6 — podobna sytuacja do Adriana Romkowskiego (QS 4.4). CPA 171 PLN za lead prawny jest akceptowalny (wartość sprawy 500–10 000 PLN). Problem: QS 3.6 generuje ~35% nadpłatę CPC = ~840 PLN/msc.

Kancelarie prawne często mają niski QS przez: (1) ogólne frazy "prawnik" bez precyzji, (2) LP bez wymaganych elementów jakości (profile adwokackie, opinie, certyfikaty), (3) brak dopasowania headline'ów do zapytań.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Call tracking kluczowy dla kancelarii |
| Consent Mode v2 | ❓ Nieznany | RODO — dane prawne wrażliwe |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 3.6 — nadpłata CPC ~35% | ~840 PLN | ~10 080 PLN |
| Brak wartości konwersji | niemierzalne | — |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — precise keywords + RSA dopasowane
2. Skonfiguruj wartości konwersji: lead prawny = 500–2 000 PLN

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 171 PLN OK dla prawa, ale QS 3.6 kosztuje ~840 PLN/msc niepotrzebnie.

---

### KONTO 61 — WBL Invest
**ID:** 5348437842 | **MCC:** 934-203-1404 | **Typ:** lead gen (inwestycje, nieruchomości)
**BDOS alias:** `wbl-invest`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 889 PLN** |
| Kliknięcia | ~1 200 |
| Konwersje | 17 |
| Wartość konwersji | — |
| CPA | ~111 PLN |
| Avg QS | 2.9 / 10 🔴 |

**Typ:** Search

#### Analiza Google Ads — Ocena Specjalisty

WBL Invest to firma inwestycyjna z QS 2.9 — bardzo niski dla segmentu inwestycji. Segment inwestycyjny/nieruchomościowy ma Google Ads policies wymagające specjalnych certyfikacji (financial products). Niski QS może wynikać z niezgodności reklam z politykami Google dla usług finansowych/inwestycyjnych.

CPA 111 PLN dla leadu inwestycyjnego jest świetny — wartość klienta inwestycyjnego: 10 000–500 000 PLN.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla high-value lead gen |
| Consent Mode v2 | ❓ Nieznany | RODO wymóg |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — sprawdź Google Ads policies dla usług inwestycyjnych
2. Skonfiguruj wartości konwersji: lead inwestycyjny = 1 000–5 000 PLN

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — QS 2.9 może wynikać z policies finansowych. Wymaga weryfikacji zgodności reklam z Google Ads Financial Products policies.

---

### KONTO 62 — fitME
**ID:** 8070079590 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy, fitness)
**BDOS alias:** `fitme`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 748 PLN** |
| Kliknięcia | ~1 600 |
| Konwersje | 7 |
| Wartość konwersji | ~1 050 PLN |
| ROAS | **0.6x** |
| CPA | ~250 PLN |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

FitME to sklep z suplementami fitness z ROAS 0.6x. AOV = 1 050 / 7 = 150 PLN — typowe dla suplementów (białko, BCAA). Przy marży ~45% i AOV 150 PLN, CPA 250 PLN jest absolutnie nie do zaakceptowania (CPA > AOV).

Możliwe przyczyny: (a) błąd śledzenia (7 z kilkudziesięciu konwersji), (b) złe słowa kluczowe (ogólne "suplementy" zamiast "białko whey 1kg"), (c) wysoka konkurencja od dużych graczy (Olimp, Trec, MyProtein).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tracking zakupów |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Customer Match | ❓ Nieznany | Suplementy = powracający kupujący |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj tracking — 7 konwersji z ~1 600 kliknięć = CR 0.44% (bardzo niskie dla suplementów)
2. Ogranicz budżet do 500 PLN/msc do czasu naprawy

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.6x i CPA > AOV = aktywna strata. Weryfikacja trackingu i strategii.

---

### KONTO 63 — Dziewiąta Planeta
**ID:** 5160052486 | **MCC:** 934-203-1404 | **Typ:** e-commerce / usługi (agencja, kreatywna)
**BDOS alias:** `dziewiata-planeta`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 725 PLN** |
| Kliknięcia | ~1 400 |
| Konwersje | 9 |
| Wartość konwersji | ~1 900 PLN |
| ROAS | **1.1x** |
| CPA | ~192 PLN |

**Typy kampanii:** Search, PMax (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Dziewiąta Planeta to agencja kreatywna z ROAS 1.1x — na granicy opłacalności. AOV = 1 900 / 9 = 211 PLN sugeruje albo niedrogie usługi, albo błędne wartości konwersji (agencje mają AOV 2 000–30 000 PLN).

Dla agencji kreatywnej Google Ads nie jest zwykle głównym kanałem pozyskiwania klientów — portfolio, referrale i content marketing są zazwyczaj efektywniejsze. Warto ocenić ROI Google Ads vs inne kanały.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla lead gen agencja |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Zdefiniuj wartości konwersji — projekt agencyjny = 5 000–30 000 PLN
2. Zrewiduj strategię — czy Google Ads to właściwy kanał dla agencji?

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 1.1x i niskie wartości konwersji. Wymaga redefinicji wartości i oceny kanału.

---

### KONTO 64 — KrainaHerbaty PL
**ID:** 8863196067 | **MCC:** 934-203-1404 | **Typ:** e-commerce (herbaty premium, akcesoria)
**BDOS alias:** `kraina-herbaty-pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 648 PLN** |
| Kliknięcia | ~1 500 |
| Konwersje | 32 |
| Wartość konwersji | ~3 500 PLN |
| ROAS | **2.1x** |
| CPA | ~52 PLN |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

KrainaHerbaty PL to sklep z herbatami premium. AOV = 3 500 / 32 = 109 PLN — dobra wartość dla herbat premium (zestawy, czajniki, herbaty specialty). ROAS 2.1x jest na granicy opłacalności przy marży ~40% (break-even ROAS = 2.5x).

Konto ma siostrzane konto KrainaHerbaty CSS (ID: 1379324580) z zaledwie 39 PLN wydatków ale ROAS 30x! To sugeruje że CSS jest nowym lub testowym kontem z lepszą strukturą kampanii. Warto przeanalizować różnicę w podejściu między oboma kontami.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla powracających klientów |
| Customer Match | ❓ Nieznany | Herbaciarze kupują regularnie — wysoka LTV |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 2.1x — na granicy opłacalności | ~330 PLN potencjalnych strat | ~3 960 PLN |
| Nieoptymalne vs CSS konto (ROAS 30x) | szacunkowo 1 000 PLN suboptymalne | ~12 000 PLN |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Porównaj struktury kampanii PL vs CSS — co CSS robi lepiej?
2. Customer Match — herbaty to produkt regularnych zakupów (wysoka LTV)
3. Target ROAS 3x — cel: break-even przy marży 33%

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 2.1x za niskie. Analiza siostrzanego konta CSS (ROAS 30x) może dostarczyć insightów do poprawy.

---

### KONTO 65 — Desque
**ID:** 5058017094 | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble designerskie, wnętrza premium)
**BDOS alias:** `desque`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 614 PLN** |
| Kliknięcia | ~1 400 |
| Konwersje | 58 |
| Wartość konwersji | ~24 700 PLN |
| ROAS | **15.3x** ⭐⭐ |
| CPA | ~28 PLN |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Desque to sklep z designerskimi meblami z ROAS 15.3x — doskonały wynik. AOV = 24 700 / 58 = 426 PLN. Przy ROAS 15x i zaledwie 1 614 PLN/msc, konto jest zdecydowanie niedoinwestowane.

Meblarnia premium z ROAS 15x to perełka portfela — skalowanie 5x (→8 070 PLN/msc) przy ROAS 10x (konserwatywna regresja) dałoby +~80 000 PLN przychodu miesięcznie dla klienta.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe przy AOV 426 PLN |
| Customer Match | ❓ Nieznany | Klienci meblowi powracają |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — ROAS 15x uzasadnia solidną infrastrukturę.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Niedoinwestowanie (ROAS 15.3x) | -~80 000 PLN potencjalnego przychodu (przy 5x skalowaniu) | -~960 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skaluj budżet 3-5x natychmiast — ROAS 15x uzasadnia bez wahania

**🟡 Miesiąc 1:**
1. Enhanced Conversions i Customer Match

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — ROAS 15.3x wybitny. Krytyczny problem: konto jest 5x za małe. Skalowanie natychmiastowe = priorytet.

---

### KONTO 66 — LycopenPRO
**ID:** 7498542821 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy — likopen, antyoksydanty)
**BDOS alias:** `lycopen-pro`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 553 PLN** |
| Kliknięcia | ~1 300 |
| Konwersje | 9 |
| Wartość konwersji | ~3 100 PLN |
| ROAS | **2.0x** |
| CPA | ~173 PLN |

**Typy kampanii:** PMax, Shopping (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

LycopenPRO to sklep z suplementami likopenowymi — wąska nisza medyczna. ROAS 2.0x i AOV = 3 100 / 9 = 344 PLN to wyniki na granicy opłacalności przy marży suplementów ~50% (break-even ROAS = 2.0x). Konto dosłownie na poziomie break-even.

Nisza likopenowa ma niską konkurencję w Google Ads ale i niskie wolumeny wyszukiwań. Możliwe że zbyt małe wolumeny nie pozwalają algorytmowi się nauczyć (9 konwersji/msc < minimum 30 dla Smart Bidding).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Customer Match | ❓ Nieznany | Suplementy — LTV przez abonament |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Zmień strategię na Target ROAS 3x (Maximize Clicks tymczasowo dla więcej danych)
2. Rozważ rozszerzenie na frazy: "antyoksydanty", "zdrowie prostaty", "witamina C"
3. Customer Match — subskrypcja suplementów = stały przychód

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 2.0x = break-even. Nisza z potencjałem ale wymaga optymalizacji.

---

### KONTO 67 — PenPol (stare konto)
**ID:** 8403686233 | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły biurowe, szkolne)
**BDOS alias:** `penpol-stare`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 532 PLN** |
| Kliknięcia | ~1 200 |
| Konwersje | 2 |
| Wartość konwersji | ~0 PLN |
| ROAS | **0x** |

**Typ:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

PenPol Stare to stare konto, które prawdopodobnie powinno zostać wstrzymane od czasu uruchomienia konta PenPol Nowe (ID: 7482901847). Kanibalizacja budżetu między dwoma kontami tej samej marki obniża efektywność obu.

2 konwersje bez wartości = brak trackingu zakupów. Konto powinno zostać wstrzymane lub połączone z nowym.

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ — kanibalizacja z nowym kontem + 0 efektywnych konwersji

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Stare konto kanibalizujące nowe. Wstrzymaj natychmiast.

---

### KONTO 68 — Życie bez protez
**ID:** 2218547292 | **MCC:** 934-203-1404 | **Typ:** lead gen / e-commerce (implanty dentystyczne, stomatologia)
**BDOS alias:** `zycie-bez-protez`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 479 PLN** |
| Kliknięcia | ~1 100 |
| Konwersje | 49 |
| Wartość konwersji | **49 PLN** |
| ROAS | **0.03x** 🔴 |
| CPA | **30 PLN** |

**Typy kampanii:** Search, PMax (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Życie bez protez to klinika implantów z klasycznym błędem: 49 konwersji × 1 PLN = 49 PLN. Implant dentystyczny kosztuje 3 000–8 000 PLN — jeden faktyczny klient stomatologiczny ma wartość wielokrotnie wyższą niż cały miesięczny budżet reklamowy.

CPA 30 PLN za lead stomatologiczny jest marzeniem — ale najpierw trzeba zweryfikować czy to są realne leady (zapytania o implanty) czy mikrokonwersje.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Naprawa wartości konwersji — PILNE |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla kliniki — call tracking |
| Consent Mode v2 | ❓ Nieznany | RODO — dane medyczne |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Napraw wartości konwersji — konsultacja implant = 200 PLN, zabieg = 5 000 PLN
2. Zweryfikuj faktyczne zapytania vs mikrokonwersje

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 1 PLN/konwersję dla kliniki implantów = rażący błąd. Naprawa może ujawnić doskonały ROAS.

---

### KONTO 69 — CRMC
**ID:** 4750835647 | **MCC:** 934-203-1404 | **Typ:** lead gen / e-commerce (CRM, oprogramowanie)
**BDOS alias:** `crmc`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 449 PLN** |
| Kliknięcia | ~900 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |
| Avg QS | **3.9 / 10** 🔴 |

**Typ:** Search

#### Analiza Google Ads — Ocena Specjalisty

CRMC to oprogramowanie CRM z 0 konwersjami i QS 3.9 — dwa fundamentalne problemy. Segment CRM/SaaS ma wysoką konkurencję (Salesforce, HubSpot, Pipedrive) i wysokie CPC (15–50 PLN/klik). Obecne CPC (1 449 / 900 = 1.61 PLN/klik) sugeruje targetowanie bardzo ogólnych lub niechowych fraz.

QS 3.9 generuje ~40% nadpłatę CPC. 0 konwersji = brak prawidłowego trackingu lub kampanie na zupełnie złe frazy.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | PILNE — brak konwersji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla SaaS |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — 0 konwersji + QS 3.9 = 1 449 PLN bez efektu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| 0 konwersji — cały budżet stracony | 1 449 PLN | 17 388 PLN |
| QS 3.9 — nadpłata CPC ~40% | ~580 PLN z 1 449 | ~6 960 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ do czasu naprawy QS i trackingu
2. Keyword audit — frazy SaaS CRM muszą być high-intent
3. Skonfiguruj konwersje: trial signup, demo request

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 0 konwersji i QS 3.9 przy 1 449 PLN/msc. Stop + restart.

---

### KONTO 70 — Wiksonspas
**ID:** 8245192186 | **MCC:** 934-203-1404 | **Typ:** lead gen (SPA, wellness, zabiegi)
**BDOS alias:** `wiksonspas`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 328 PLN** |
| Kliknięcia | ~900 |
| Konwersje | 5 |
| Wartość konwersji | — (lead gen) |
| CPA | ~266 PLN |

**Typy kampanii:** Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Wiksonspas to SPA z 5 konwersjami miesięcznie i CPA 266 PLN. Dla SPA/wellness CPA 266 PLN jest wysoki — zabieg SPA kosztuje 150–500 PLN, więc CPA > AOV dla pojedynczych zabiegów. Jednak LTV klienta SPA jest wysoka (regularne wizyty = 1 000–5 000 PLN/rok).

Brak wartości konwersji uniemożliwia ocenę faktycznego ROI. 5 konwersji/msc to za mało dla Smart Bidding.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Call tracking + formularz rezerwacji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla rezerwacji SPA |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Skonfiguruj wartości konwersji: zabieg = 200 PLN, pakiet = 500 PLN
2. Dodaj call extension i tracking telefoniczny

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — Niska liczba konwersji (5/msc) i brak wartości. Konfiguracja wymagana.

---

### KONTO 71 — Vago
**ID:** 2417186044 | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi profesjonalne)
**BDOS alias:** `vago`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 258 PLN** |
| Kliknięcia | ~900 |
| Konwersje | 11 |
| Wartość konwersji | — (lead gen) |
| CPA | ~114 PLN |

**Typy kampanii:** Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Vago to konto lead gen z 11 konwersjami i CPA 114 PLN. Bez wartości konwersji trudno ocenić ROI. Przy typowych wartościach lead gen (500–5 000 PLN/klient) CPA 114 PLN jest akceptowalny.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Konfiguracja konwersji priorytet |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Skonfiguruj wartości konwersji — ustal z klientem wartość leadu
2. Enhanced Conversions

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 114 PLN może być OK zależnie od wartości usługi. Konfiguracja wartości priorytetem.

---

### KONTO 72 — NOWE medihurt.com
**ID:** 7280666733 | **MCC:** 934-203-1404 | **Typ:** e-commerce B2B (sprzęt medyczny hurt)
**BDOS alias:** `medihurt-nowe`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 162 PLN** |
| Kliknięcia | ~900 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |

**Typy kampanii:** PMax, Search (szacowane)
**Status:** ❌ 0 konwersji — nowe konto

#### Analiza Google Ads — Ocena Specjalisty

Medihurt.com to nowy sklep B2B ze sprzętem medycznym hurtowym. Jako nowe konto (uruchomione w 2026) nie zebrało jeszcze danych historycznych. Dla B2B medycznego cold start algorytmu jest szczególnie trudny — produkty niszowe, wysokie CPC, długi cykl decyzyjny.

Segment sprzętu medycznego B2B hurtowego ma inne stawki niż B2C — AOV może wynosić 10 000–200 000 PLN przy hurtowych zamówieniach. CPA 50–500 PLN byłby absolutnie akceptowalny.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | NOWE konto — konfiguruj od razu |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Konfiguruj jako standard dla nowego konta |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — szczególnie ważny dla B2B medycznego |

**GTM Priority: KRYTYCZNY** — Nowe konto musi mieć prawidłowy tracking od dnia 1.

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ i skonfiguruj tracking (purchase/form_submit) przed restart
2. Uruchom z małym budżetem (300 PLN/msc) po naprawie
3. Strategia: Maximize Clicks (cold start) → Maximize Conversions (po 15+ konw) → Target ROAS

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Nowe konto bez trackingu = 1 162 PLN/msc stracone. Prawidłowa konfiguracja od podstaw jest warunkiem sukcesu.

