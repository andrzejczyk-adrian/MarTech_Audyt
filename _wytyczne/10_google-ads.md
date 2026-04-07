# Sekcja 10 — Audyt Google Ads

## Meta
sekcja_id: 10
sekcja_nazwa: Audyt Google Ads
dotyczy_domyslnie: ads
agent_etap: 3
zrodla_danych: 01_raw-data.md (sekcja Google Ads), BDOS, Google Ads Panel
ostatnia_aktualizacja: 2026-04
wersja: 2.0
warunek_wejscia: klient z kontem Google Ads + dostep przez BDOS lub API

---

## Kryteria — 10A: Struktura konta

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10A.1 | Brak kampanii z 0 konwersji >30d przy wydatkach >500 PLN | Wysoki | ads | raw-data → kampanie bez konwersji → wydatki | 0 takich kampanii | Każda kampania >300 PLN bez konwersji = drenaż | 3 | Wycen drenaż PLN/msc |
| 10A.2 | Brand i non-brand wydzielone | Wysoki | ads | Sprawdź czy jest osobna kampania brandowa | Osobna kampania brand z własnym budżetem | Brak kampanii brand lub brand z generic | 3 | |
| 10A.3 | Auto-apply recommendations wyłączone | Wysoki | ads | Google Ads → Rekomendacje → Auto-apply | Wyłączone | Włączone = Google sam zmienia kampanie | 3 | |
| 10A.4 | Naming convention spójna | Niski | ads | Sprawdź wzorzec nazw kampanii | Spójny format | Losowe nazwy | 1 | |

---

## Kryteria — 10B: Konwersje i śledzenie

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10B.1 | Konwersja Primary ustawiona | Wysoki | ads | Google Ads → Konwersje → Primary/Secondary | purchase jako Primary (e-comm) lub lead (lead gen) | Brak Primary lub mikrokonwersja jako Primary | 3 | |
| 10B.2 | Wartości konwersji dynamiczne | Wysoki | ads+ecommerce | Google Ads → Konwersje → Wartość | Dynamiczna wartość z DataLayer | Stała 1 PLN lub 0 PLN | 3 | |
| 10B.3 | Brak duplikacji śledzenia | Wysoki | ads | Tag Ads + import GA4 tej samej akcji = duplikacja | Max 1 źródło per konwersja | Dwie konwersje purchase z tagu i GA4 jednocześnie | 3 | |
| 10B.4 | Enhanced Conversions aktywne | Średni | ads | Google Ads → EC → status + match rate | Aktywne, match rate >40% | Wyłączone lub match rate <20% | 2 | |
| 10B.5 | Conversion window 30d klik / 1d view | Średni | ads | Google Ads → Konwersje → okno | 30d klik, 1d view | 7d klik bez uzasadnienia | 2 | |

---

## Kryteria — 10C: Strategie bidowania

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10C.1 | Target ROAS / CPA ustawiony | Wysoki | ads | Nie Maximize bez celu | Cel ROAS lub CPA zdefiniowany | Maximize bez limitu = brak kontroli kosztów | 3 | |
| 10C.2 | Target ROAS ≤1.5× osiągalnego ROAS | Wysoki | ads+ecommerce | raw-data → porównaj target vs osiągany ROAS | Target ≤1.5× osiągalny | Target 2× wyższy niż osiągany = kampania zablokowana | 3 | |
| 10C.3 | Brak kampanii w Learning >14 dni | Średni | ads | Status kampanii w BDOS lub panelu | <5 kampanii w Learning | >10 kampanii w Learning jednocześnie | 2 | |
| 10C.4 | Brak zmian budżetu >30% jednorazowo | Wysoki | ads | Historia zmian budżetu | Zmiany ≤20%/tydzień | Skok budżetu 2× jednorazowo | 3 | |

---

## Kryteria — 10D: Performance Max

> Pomiń jeśli brak kampanii PMax w raw-data.

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10D.1 | Asset groups segmentowane | Wysoki | ads | Lista asset groups per kampania | Min. 2-3 asset groups per kampania | Jedna flat asset group dla wszystkich produktów | 3 | |
| 10D.2 | Gwiazdy BCG w osobnych asset groups | Wysoki | ads+ecommerce | Sprawdź czy top produkty wydzielone | Gwiazdy z dedykowaną AG i wyższym target ROAS | Gwiazdy i Psy w tej samej AG | 3 | |
| 10D.3 | Psy BCG wykluczone | Wysoki | ads+ecommerce | Sprawdź wykluczenia listing group | Psy wykluczone lub <5% budżetu | Psy w głównej kampanii bez ograniczenia | 3 | |
| 10D.4 | Negative keywords na PMax | Wysoki | ads | PMax → negative keywords | Brand terms i irrelewantne frazy wykluczone | Brak negatywów = PMax kanibaluje Search brand | 3 | |
| 10D.5 | Brand exclusion skonfigurowany | Wysoki | ads | PMax → ustawienia → brand terms | Brand terms na liście wykluczeń | Brak = PMax przejmuje branded traffic | 3 | |
| 10D.6 | URL expansion wyłączone lub zawężone | Średni | ads | PMax → URL expansion | Wyłączone lub z wykluczeniami URL | Włączone bez wykluczeń | 2 | |

---

## Kryteria — 10E: Kampanie Search

> Pomiń jeśli brak kampanii Search.

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10E.1 | Kampania brandowa wydzielona | Wysoki | ads | Osobna kampania brand z własnym budżetem | Tak | Brak kampanii brand | 3 | |
| 10E.2 | Impression Share brand ≥70% | Wysoki | ads | IS kampanii brandowej | ≥70% | <50% = konkurencja na własną markę | 3 | |
| 10E.3 | Negative keywords aktywne | Wysoki | ads | Shared negative lists + kampanie | Lista negatywów aktywna | Brak negatywów = przepalanie na irrelewantne frazy | 3 | |
| 10E.4 | Ad Strength RSA: Good/Excellent | Średni | ads | % reklam z oceną Good lub Excellent | ≥70% | <50% reklam z Poor | 2 | |

---

## Kryteria — 10F: Geo i feed

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10F.1 | Geo targeting PRESENCE (nie INTEREST) | Wysoki | ads | Location targeting → metoda | PRESENCE | PRESENCE_OR_INTEREST = nieprecyzyjne | 3 | |
| 10F.2 | Wykluczenia mobile app (Display/PMax) | Średni | ads | Placement exclusions | App categories wykluczone | Brak wykluczeń = budżet na gry mobilne | 2 | |
| 10F.3 | Eligible products >90% feedu | Wysoki | ads+ecommerce | Merchant Center → Diagnostyka | >90% active/eligible | <80% eligible | 3 | ➖ jeśli brak kampanii Shopping |
| 10F.4 | Tytuły produktów zoptymalizowane | Średni | ads+ecommerce | Sprawdź przykładowe tytuły | Marka + model + kolor/rozmiar | Tytuły systemowe bez optymalizacji | 2 | ➖ jeśli brak feedu |
| 10F.5 | Custom labels wypełnione | Średni | ads+ecommerce | MC → produkty → custom labels | Min. 1 label (sezon/marża/BCG) | Puste custom labels | 2 | ➖ jeśli brak feedu |

---

## Kryteria — 10G: Quality Score i diagnostyka

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 10G.1 | Avg QS ≥7 | Wysoki | ads | QS per kampania Search → oblicz średnią | ≥7.0 | <5.0 = przepłacanie CPC 20-80% | 3 | ✅ ≥7 / ⚠️ 5-7 / ❌ <5 |
| 10G.2 | Brak kampanii ROAS <1× | Wysoki | ads+ecommerce | raw-data → kampanie z ROAS <1x | 0 kampanii tracących pieniądze | Kampania kosztuje więcej niż zarabia | 3 | Wycen stratę PLN/msc |
| 10G.3 | IS kampanii niebrandowych ≥30% | Wysoki | ads | IS per kampania | ≥30% | <15% = zbyt mały budżet lub niski QS | 3 | |

---

## Notatki rozszerzone (tylko dla agenta)

### 10A.1 — Wycena drenażu
```
drenaż_miesięczny = suma wydatków (30d) dla kampanii z 0 konwersjami
Przykład: 3 kampanie: 1 240 + 830 + 450 = 2 520 PLN/msc drenażu
```

### 10G.1 — Nadkoszt CPC per zakres QS
| QS | Nadkoszt |
|-----|---------|
| 9-10 | oszczędność |
| 7-8 | bazowy |
| 5-6 | +20-40% |
| 3-4 | +50-80% |
| 1-2 | +100-200% |

### 10D — ROAS: notacja
ZAWSZE używaj mnożnika: `9x`, `12x` — NIGDY procent z BDOS.
`9%` w BDOS = ROAS 9x (weryfikuj: conv_value / cost).

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| ads (zawsze) | 10A.1–10A.4 + 10B.1–10B.5 + 10C.1–10C.4 + 10E.1–10E.4 + 10G.1–10G.3 | ~65 pkt |
| ads+ecommerce | 10B.2, 10C.2, 10D.2, 10D.3, 10F.3–10F.5, 10G.2 | +18 pkt |
| PMax (jeśli dotyczy) | 10D.1–10D.6 | +17 pkt |
| **MINIMUM (ads bez PMax/feed)** | | **~65 pkt** |
| **MAKSIMUM (ads+ecomm+PMax+feed)** | | **~100 pkt** |
