# INVETTE — PODSUMOWANIE AUDYTU GOOGLE ADS
## MCC 934-203-1404 | Marzec–Kwiecień 2026

---

## KLUCZOWE LICZBY

| Metryka | Wartość |
|---------|---------|
| Kont zarządzanych łącznie | 150 |
| Kont aktywnych z wydatkami | 90–94 |
| ROAS portfela (konta produktowe) | **5.7x** |
| Wydatki portfela (marzec) | ~450 000 PLN |
| Wart. konwersji (portfel produktowy, marzec) | 1 618 388 PLN |
| Kont z ROAS <2x (e-commerce) | **22 konta** / ~107 000 PLN/msc |
| Kont z 0 konwersjami | **10 kont** / ~12 700 PLN/msc |
| Produktów w bazie BCG | 57 222 |

---

## SEGMENTACJA PORTFELA

```
✅ OK         (~22 konta)  Brak krytycznych problemów, ROAS akceptowalny
⚠️ Uwaga      (~16 kont)   Kampanie bez konwersji lub ROAS do poprawy
🔴 Problem    (~22 konta)  Aktywne straty lub brak efektów — pilna interwencja
ℹ️ Lead gen   (~20 kont)   Brak wartości konwersji — wymaga konfiguracji
💤 Nieaktywne (60 kont)    Zero wydatków — weryfikacja kontraktów
```

---

## TOP 5 PROBLEMÓW SYSTEMOWYCH

### 1. 🔴 22 konta e-commerce generują straty (~107 000 PLN/msc)
Konta sprzedażowe z ROAS <2x. Najgorzej: **TOMA** (ROAS 0.1x, 8 268 PLN), **Maxdent** (ROAS 0.1x, 4 113 PLN), **forcopy** (ROAS 0.7x, 12 747 PLN). Łączne straty licząc minimalną marżę 30%: szacunkowo **-30 000 PLN/msc** dla klientów.

### 2. 🐕 48.6% budżetu produktowego trafia w "Psy" BCG (ROAS 0.8x)
Z 282 382 PLN wydatków na kontach e-commerce, **137 195 PLN trafia na produkty bez konwersji**. Gwiazdy (16.4% produktów) generują 55.2% przychodu przy 21.5% wydatków — algorytm jest niedożywiony sygnałami. Znaki Zapytania mają ROAS 21.3x ale pochłaniają tylko 1.9% budżetu — kluczowy quick win.

### 3. 🔴 10 kont z zerowymi konwersjami (12 700 PLN/msc bez efektu)
Konta aktywne z wydatkami ale zero konwersji: Fizjoterapia Mazur, Omega Kserokopiarki, PenPol, CRMC, NOWE medihurt, INVETTE własne, Zakatek Fantastyki, Sklep UQUINA, Polskie Meble REVES, Pet Vital. Wymaga natychmiastowej diagnostyki śledzenia lub wstrzymania kampanii.

### 4. ⚠️ Quality Score krytycznie niski na dużych kontach
**Janda** (QS 2.8, 14 160 PLN), **TABLE4U** (QS 3.3, 66 998 PLN), **PaDrew** (QS 3.4, 19 598 PLN). Niski QS = wyższy CPC, gorsze pozycje, zmarnowany budżet. Przy TABLE4U (66K PLN/msc) nawet +1 punkt QS może obniżyć CPC o 10–15%.

### 5. 📊 Liderzy portfela są niedoinwestowani
**IN-SKYCAMP** (ROAS 101.7x, budżet tylko 6 521 PLN/msc), **ASKO** (ROAS 58.2x, 7 721 PLN/msc), **Expertia Naturals** (ROAS 17.0x, 15 179 PLN/msc). Przy takim ROAS każda złotówka dodanego budżetu generuje natychmiastowy zwrot. Brak proaktywnej rekomendacji skalowania to koszt utraconych przychodów dla klientów.

---

## ANALIZA BCG — WNIOSKI PORTFELOWE

| Kwadrant | Produkty | Udział w wydatkach | ROAS | Ocena |
|----------|----------|--------------------|------|-------|
| ⭐ Gwiazdy | 632 | 21.5% | **14.7x** | Skaluj |
| 🐄 Dojne Krowy | 354 | 28.0% | 6.2x | Utrzymaj |
| ❓ Znaki Zapytania | 416 | **1.9%** | **21.3x** | Niedoinwestowane — priorytet |
| 🐕 Psy | 14 527 | **48.6%** | 0.8x | Ogranicz lub zoptymalizuj feed |

**Kluczowy wniosek:** Realokacja choćby 10% budżetu z Psów (–13 700 PLN) na Znaki Zapytania (+13 700 PLN) przy zachowaniu proporcji ROAS 21.3x oznacza potencjalnie +291 000 PLN dodatkowych przychodów miesięcznie.

---

## ACTION PLAN — PRIORYTETY

### Tydzień 1 — Zatamowanie strat
- [ ] Wstrzymaj kampanie z >300 PLN / 0 konwersji: **ASKO** (4), **stercontrol** (3), **TOMA** (wszystko)
- [ ] Zdiagnozuj śledzenie konwersji: **forcopy**, **Maxdent**, **GT-serwiskawowy**, **Smart Clinic**
- [ ] Zweryfikuj konta 0 konwersji: **PenPol**, **Fizjoterapia Mazur**, **CRMC**

### Miesiąc 1 — Optymalizacja
- [ ] Poprawa QS: **Janda** (2.8), **TABLE4U** (3.3), **PaDrew** (3.4) — cross-check słów kluczowych/LP
- [ ] Feed audit BCG: **TABLE4U** (195 Psów), **IdeaShirt** (93%), **Optimum BHP** (96%)
- [ ] Wydziel Znaki Zapytania do osobnych kampanii: **IdeaShirt** (66 ZQ), **Optimum BHP** (29 ZQ)

### Miesiąc 2–3 — Skalowanie i konfiguracja
- [ ] Skaluj liderów: **IN-SKYCAMP** (3–5x budżet), **ASKO** (2–3x), **Expertia** (2x)
- [ ] Enhanced Conversions: wszystkie konta e-commerce
- [ ] Customer Match: **TABLE4U**, **PaDrew**, **Pastform**, **Janda**
- [ ] GA4 autoryzacja: `bdos auth --add analytics` → pełny cross-platform audit
- [ ] Wartości konwersji dla lead gen: ustalenie z klientami i konfiguracja

---

## OCENA AGENCJI

| Obszar | Ocena |
|--------|-------|
| ROAS portfela | ⚠️ Dobry (5.7x) ale nierówny |
| Reagowanie na problemy | 🔴 Reaktywne (nie proaktywne) |
| Konfiguracja śledzenia | 🔴 Liczne błędy i luki |
| Feed management (BCG) | 🔴 48.6% budżetu na Psach |
| Quality Score | ⚠️ 25% kont QS<5 |
| Skalowanie liderów | 🔴 Niedoinwestowani |

**Ocena ogólna: ⭐⭐ / 5**

Portfel Invette ma silnych liderów, ale dolna ćwiartka kont generuje straty bez interwencji. Główne problemy: brak proaktywnego monitoringu, błędne konfiguracje konwersji i brak BCG-driven zarządzania feedem. Potencjał wzrostu przychodów portfela o 20–35% bez zwiększania łącznego budżetu — przez realokację z Psów na Znaki Zapytania i skalowanie liderów.

---

*Dane: BDOS AI v1.0.9 | MCC 934-203-1404 | Invette.pl | Marzec–Kwiecień 2026*
