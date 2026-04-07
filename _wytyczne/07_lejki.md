# Sekcja 7 — Lejki zachowań per kampania

## Meta
sekcja_id: 7
sekcja_nazwa: Lejki zachowań użytkowników per typ kampanii
dotyczy_domyslnie: ecommerce
agent_etap: 3
zrodla_danych: 01_raw-data.md (sekcja lejek zakupowy)
ostatnia_aktualizacja: 2026-04
wersja: 2.0
warunek_wejscia: ecommerce z 4 zdarzeniami GA4: view_item add_to_cart begin_checkout purchase

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|---|---|---|---|---|---|---|---|---|
| 7.1 | Wszystkie 4 zdarzenia e-commerce wdrożone | Wysoki | ecommerce | raw-data → zdarzenia → view_item add_to_cart begin_checkout purchase obecne | Wszystkie 4 zdarzenia aktywne z sensownymi liczbami | Brak któregokolwiek z 4 zdarzeń | 2 |  |
| 7.2 | CR paid ≥50% CR organic | Wysoki | ecommerce+ads | raw-data → CR(CPC) / CR(organic) | CR paid / CR organic ≥0.5 | CR paid <30% CR organic = słaba jakość ruchu płatnego | 2 |  |
| 7.3 | Brak kanału z CR <0.1% przy wydatkach >1000 PLN | Wysoki | ecommerce+ads | raw-data → CR per kanał + wydatki z BDOS | Żaden kanał płatny z CR <0.1% | Kanał płatny z setkami PLN i CR bliskim 0 | 2 |  |
| 7.4 | Checkout drop-off ≤40% | Wysoki | ecommerce | raw-data → begin_checkout → purchase: oblicz % przejścia | begin_checkout → purchase ≥60% | Przejście <40% = problem z bramką lub UX kasy | 2 |  |

---

## Notatki rozszerzone (tylko dla agenta)

### Obliczenia przejść lejka (z raw-data)

| Przejście | Wzór | Benchmark PL |
|-----------|------|-------------|
| view→cart | add_to_cart / view_item × 100% | 5–20% |
| cart→checkout | begin_checkout / add_to_cart × 100% | 30–60% |
| checkout→purchase | purchase / begin_checkout × 100% | 50–80% |
| CR całkowity | purchase / view_item × 100% | 0.3–2% |

### Interpretacja anomalii

| Problem | Możliwa przyczyna |
|---------|-----------------|
| Niski view→cart dla paid | Niedopasowany landing page lub złe targetowanie |
| Niski cart→checkout | Problem UX koszyka lub zbyt wiele kroków |
| Niski checkout→purchase | Problem z bramką płatności, brak metod, wysoki koszt dostawy |
| CR paid <50% organic | Ruch płatny słabej jakości |

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| ecommerce | 7.1–7.4 | 8 pkt |
| **ŁĄCZNIE** | | **8 pkt** |
