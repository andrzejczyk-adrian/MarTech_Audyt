# Sekcja 6 — Macierz BCG

## Meta
sekcja_id: 6
sekcja_nazwa: Macierz BCG — analiza produktów
dotyczy_domyslnie: ecommerce+ads
agent_etap: 3
zrodla_danych: 01_raw-data.md (Google Ads shopping, GA4 items)
ostatnia_aktualizacja: 2026-04
wersja: 2.0
warunek_wejscia: ecommerce z kampaniami Shopping lub PMax z feedem + dostep do GA4

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 6.1 | Gwiazdy w osobnych kampaniach lub asset groups | Wysoki | ecommerce+ads | Sprawdź czy top produkty BCG mają dedykowane grupy/kampanie z wyższym target ROAS | Gwiazdy wydzielone z własnym target ROAS | Gwiazdy i Psy w tej samej kampanii bez segmentacji | 3 | |
| 6.2 | Dojne Krowy z ograniczonym target ROAS | Średni | ecommerce+ads | Sprawdź czy high-revenue/low-ROAS produkty mają ograniczenia budżetu | Dojne Krowy z CPC cap lub ograniczonym target ROAS | Brak ograniczeń na Dojnych Krowach | 2 | |
| 6.3 | Psy wykluczone lub <5% budżetu | Średni | ecommerce+ads | % budżetu na Psy + czy wykluczone z głównych kampanii | Psy <5% budżetu lub wykluczone | Psy >20% budżetu bez uzasadnienia | 2 | |
| 6.4 | Znaki Zapytania w wydzielonym teście | Średni | ecommerce+ads | Osobna kampania lub asset group lub niższy budżet dla ZQ | ZQ z dedykowanym testem | ZQ bez wydzielenia — brak danych o potencjale | 2 | |
| 6.5 | Delta Ads vs GA4 ≤30% | Wysoki | ecommerce+ads | Oblicz delta_pct = (ads_revenue - ga4_cpc_revenue) / ads_revenue × 100 | Delta ≤15% | Delta >30% = błąd konfiguracji e-commerce tracking | 3 | ✅ ≤15% / ⚠️ 15-30% / ❌ >30% |

---

## Notatki rozszerzone (tylko dla agenta)

### Metodologia klasyfikacji BCG
1. Oblicz `revenue_share` = `conv_value_produktu / total_conv_value_konta × 100%`
2. Oblicz `roas` = `conv_value / cost`
3. Wyznacz mediany obu dla konta
4. Przypisz kwadrant:

| Kwadrant | Warunek |
|----------|---------|
| ⭐ Gwiazda | revenue_share ≥ mediana AND roas ≥ mediana |
| 🐄 Dojna Krowa | revenue_share ≥ mediana AND roas < mediana |
| ❓ Znak Zapytania | revenue_share < mediana AND roas ≥ mediana |
| 🐕 Pies | revenue_share < mediana AND roas < mediana |
| ⚫ Nieaktywny | 0 transakcji |

### Psy organiczne
Produkt = Pies w Google Ads (niski ROAS) + GA4 all-channels revenue > 50 PLN → sprzedaje się organicznie, Ads nie pomaga → możliwy błąd struktury lub produkt nie wymaga wsparcia płatnego.

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| ecommerce+ads | 6.1–6.5 | 12 pkt |
| **ŁĄCZNIE** | | **12 pkt** |
