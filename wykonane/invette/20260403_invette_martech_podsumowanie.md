# INVETTE — PODSUMOWANIE AUDYTU MARTECH
## MCC 934-203-1404 | Kwiecień 2026

---

## KLUCZOWE LICZBY

| Metryka | Wartość |
|---------|---------|
| Kont zarządzanych łącznie | 150 |
| Kont aktywnych z wydatkami | **94** |
| Kont nieaktywnych | 56 |
| Łączne wydatki portfela (30d) | **~630 000 PLN** |
| Łączna wartość konwersji (30d) | **~4 262 000 PLN** |
| ROAS portfela (wszystkie aktywne) | **~6.8x** |
| ROAS portfela produktowego (45 kont) | **5.7x** |
| Kont z ROAS < 2x (e-commerce) | **22 konta** / ~107 000 PLN/msc |
| Kont z 0 konwersjami | **10 kont** / ~13 318 PLN/msc |
| Kont lead gen (brak wartości konw.) | ~20 kont / ~45 000 PLN/msc |
| Status GA4 API | ❌ Brak autoryzacji |

---

## SEGMENTACJA PORTFELA

```
✅ OK         (~22 konta)  Brak krytycznych problemów, ROAS akceptowalny
⚠️ Uwaga      (~16 kont)   ROAS do poprawy, kampanie bez konwersji
🔴 Problem    (~22 konta)  Straty lub brak efektów — pilna interwencja
ℹ️ Lead gen   (~20 kont)   Brak wartości konwersji — wymaga konfiguracji
💤 Nieaktywne (56 kont)    Zero wydatków — weryfikacja kontraktów
```

---

## TOP 5 PROBLEMÓW SYSTEMOWYCH

### 1. 🔴 22 konta e-commerce z ROAS < 2x (~107 000 PLN/msc w stratach)

Konta sprzedażowe z ROAS poniżej progu opłacalności. Najgorzej:
- **Maxdent** (ROAS 0.05x, 4 027 PLN) — 208 konwersji = 1 PLN/konw. = **błąd śledzenia**
- **TOMA** (ROAS 0.5x, 7 837 PLN) — 7 konwersji przy CPA 1 120 PLN
- **GT-serwiskawowy** (ROAS 0.1x, 3 488 PLN) — 2 konwersje, CPA 1 584 PLN
- **Synthagen Labs** (ROAS 2.0x, 61 993 PLN) — agresywne skalowanie 2.7x przy SPADKU ROAS

Łączne szacowane straty klientów (przy marży 30%): **~32 000 PLN/msc**

### 2. 🔴 10 kont z zerowymi konwersjami (~13 318 PLN/msc bez efektu)

| Konto | Wydatki | Diagnoza |
|-------|---------|---------|
| PenPol [nowe 2026] | 2 831 PLN | Błąd konfiguracji trackingu |
| Fizjoterapia Mazur | 2 807 PLN | Brak trackingu lub LP |
| Omega Kserokopiarki | 2 427 PLN | QS 2.3 — błędne słowa kluczowe |
| CRMC | 1 449 PLN | QS 3.9 — ruch niskiej jakości |
| NOWE medihurt.com | 1 162 PLN | Nowe konto bez konwersji |
| INVETTE (własne) | 1 141 PLN | Video-only — zły typ kampanii |
| Zakatek Fantastyki | 567 PLN | Błąd konfiguracji |
| Sklep UQUINA | 503 PLN | Shopping bez trackingu |
| Polskie Meble - REVES | 225 PLN | Smart bez konwersji |
| Pet Vital | 206 PLN | Tracking pomimo QS 7.3 |

### 3. 📉 Quality Score — ~50 850 PLN/msc nadpłaty CPC

Konta z krytycznie niskim QS przepłacają za każde kliknięcie o 30–50%:
- **TABLE4U** (QS 3.3, 66K PLN/msc) → **~26 600 PLN/msc nadpłaty** ← największy priorytet
- **Janda** (QS 2.8, 16.8K PLN/msc) → ~8 400 PLN/msc nadpłaty
- **PaDrew** (QS 3.4, 18.8K PLN/msc) → ~7 500 PLN/msc nadpłaty
- **Wywozimy** (QS 2.4), **Profito** (QS 2.8), **odpady-kontenery** (QS 3.3)

**Poprawa QS 3→7 dla TABLE4U = ~90 000 PLN/rok oszczędności na CPC**

### 4. ⭐ Liderzy portfela dramatycznie niedoinwestowani

| Konto | ROAS | Budżet | Potencjał skalowania |
|-------|------|--------|---------------------|
| **IN-SKYCAMP** | **105.4x** | 6 297 PLN | +**300 000–650 000 PLN/msc** przy 3–5x |
| **ASKO sp. z o.o.** | **53.1x** | 6 954 PLN | +**350 000–700 000 PLN/msc** przy 3x |
| **Expertia Naturals** | **17.1x** | 15 058 PLN | +**257 000 PLN/msc** przy 2x |
| **deltahr** | **18.7x** | 3 516 PLN | +**123 000 PLN/msc** przy 3x |

Brak decyzji o skalowaniu IN-SKYCAMP i ASKO to **strata ~1 000 000 PLN/msc** dla klientów.

### 5. 🐕 Psy BCG pochłaniają 48.6% budżetu produktowego

Z 282 382 PLN wydatków na kontach e-commerce, **137 195 PLN trafia na produkty bez konwersji**.

| Kwadrant | Produkty | Wydatki | ROAS | Działanie |
|---------|---------|---------|------|-----------|
| ⭐ Gwiazdy | 632 | 21.5% | 14.7x | Skaluj |
| 🐄 Dojne Krowy | 354 | 28.0% | 6.2x | Utrzymaj |
| ❓ Znaki Zapytania | 416 | 1.9% | 21.3x | **Niedoinwestowane — priorytet** |
| 🐕 Psy | 14 527 | **48.6%** | 0.8x | Ogranicz / feed audit |

**Realokacja 10% budżetu z Psów na Znaki Zapytania = +291 000 PLN/msc przychodu**

---

## MARTECH INFRASTRUCTURE — STATUS

| Komponent | Status | Priorytet |
|-----------|--------|-----------|
| GA4 Analytics API | ❌ **Brak autoryzacji** — wymaga `bdos auth --add analytics` | 🔴 PILNY |
| GTM kontenery (94 konta) | ❓ Bez weryfikacji | 🟡 |
| Server-side GTM | ❓ Status nieznany | 🟡 |
| Enhanced Conversions | ❓ Nieznany | 🟡 |
| Customer Match | ❓ Nieznany | 🟢 |
| Consent Mode v2 | ❓ Nieznany | 🔴 (wymóg EU) |

**Krok 1 do pełnego audytu MarTech:**
```bash
bdos auth --add analytics
# Zaloguj: invette.sem@gmail.com
# Zatwierdź: Google Analytics Reporting API
```

Po autoryzacji dostępne: analiza GA4 per konto, GTM health score, EC match rate, audience listy, atrybucja.

---

## IMPACT FINANSOWY — PODSUMOWANIE

| Kategoria | Koszt/msc | Koszt/rok |
|-----------|----------|----------|
| Konta z 0 konwersjami (strata) | 13 318 PLN | **159 816 PLN** |
| Kampanie bez konwersji (drenaż) | 14 500 PLN | **174 000 PLN** |
| Nadpłata CPC (niski QS) | 50 850 PLN | **610 200 PLN** |
| Konta ROAS < 1x (straty netto) | ~43 500 PLN | **522 000 PLN** |
| Błędne śledzenie (fałszywy ROAS) | ~7 900 PLN | **94 800 PLN** |
| **ŁĄCZNE STRATY** | **~130 068 PLN** | **~1 560 816 PLN** |
| | | |
| Potencjał: skalowanie liderów | +750 000 PLN | **+9 000 000 PLN** |
| Potencjał: realokacja BCG | +291 000 PLN | **+3 492 000 PLN** |

**Potencjał wzrostu przychodów portfela bez zwiększania łącznego budżetu: 20–35%**

---

## ACTION PLAN

### 🔴 Tydzień 1 — Zatamowanie strat

- [ ] Autoryzuj GA4 API: `bdos auth --add analytics` → invette.sem@gmail.com
- [ ] Wstrzymaj konta 0 konwersji: **PenPol nowe**, **Fizjoterapia Mazur**, **Omega Ksero**, **CRMC**, **medihurt**
- [ ] Napraw tracking: **forcopy** (0x ROAS), **Maxdent** (0.05x), **Profito** (0.6x), **Mr Łoś**
- [ ] Wstrzymaj kampanie: YT Biedronka w **sklep.delia.pl** (2 656 PLN, 0 konwersji), YT w **TABLE4U**, **Pastform**, **Expertia**
- [ ] **Skaluj IN-SKYCAMP** (ROAS 105x) — zwiększ budżet 3x natychmiast

### 🟡 Miesiąc 1 — Optymalizacja

- [ ] QS audit: **TABLE4U** (QS 3.3 → 7.0+), **Janda** (2.8), **PaDrew** (3.4)
- [ ] Feed audit BCG: **TABLE4U** (195 Psów), **IdeaShirt** (93%), **Optimum BHP** (96%)
- [ ] Wydziel Znaki Zapytania: **IdeaShirt** (66 ZQ), **Optimum BHP** (29 ZQ), **MegaKoszulki** (13 ZQ)
- [ ] **Skaluj ASKO** (ROAS 53x) 2–3x budżetu
- [ ] **Skaluj Expertia Naturals** (ROAS 17x) 2x budżetu
- [ ] Wstrzymaj Synthagen Wiosenna Promocja (ROAS 0.3–1.3x, ~38 000 PLN)

### 🟢 Miesiąc 2–3 — Konfiguracja MarTech

- [ ] GA4 full audit (po autoryzacji) — GTM, sGTM, EC, Consent Mode v2
- [ ] Enhanced Conversions: wszystkie konta e-commerce
- [ ] Customer Match: **TABLE4U**, **PaDrew**, **Pastform**, **Janda**, **ASKO**
- [ ] Wartości konwersji dla lead gen: **Adrian Romkowski**, **Phinance**, **OKULUS**, **SEZARO**, **KANTÓWKA**
- [ ] Weryfikacja 56 kont nieaktywnych — kontrakty, sezonowość, archiwizacja

---

## OCENA AGENCJI

| Obszar | Ocena | Szczegóły |
|--------|-------|-----------|
| ROAS portfela | ⚠️ Nierówny (6.8x) | Kilka outlierów, dolna ćwiartka w stratach |
| Reagowanie na problemy | 🔴 Reaktywne | Konta z 0 konw. aktywne tygodniami |
| Konfiguracja konwersji | 🔴 Liczne błędy | Mikroeventy, brak wartości, 0x ROAS |
| Feed management (BCG) | 🔴 48.6% budżetu na Psach | Brak segmentacji produktowej |
| Quality Score | ⚠️ 25% kont QS < 5 | 50 000 PLN/msc nadpłaty |
| Skalowanie liderów | 🔴 Niedoinwestowanie | IN-SKYCAMP, ASKO — missed 1M PLN/msc |
| MarTech (GA4/GTM) | ❌ Bez weryfikacji | Brak autoryzacji GA4 API |

**Ocena ogólna: ⭐⭐ / 5**

Portfel Invette ma silnych liderów (IN-SKYCAMP 105x, ASKO 53x, Expertia 17x) ale dolna ćwiartka kont generuje straty bez interwencji. Główne problemy: brak proaktywnego monitoringu, błędne konfiguracje konwersji, brak BCG-driven zarządzania feedem i nieautoryzowany GA4 uniemożliwiający pełen audyt MarTech.

**Potencjał wzrostu przychodów portfela o 20–35% bez zwiększania łącznego budżetu** — przez naprawę błędów, realokację z Psów na Znaki Zapytania i skalowanie liderów.

---

*Dane: BDOS AI v1.0.9 + v1.0 | MCC 934-203-1404 | Invette.pl | Kwiecień 2026*
*MarTech Audit Framework v1.0 | `C:\Users\adria\Documents\AI\AUDYT\MarTech\invette\`*
