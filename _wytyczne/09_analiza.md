# Sekcja 9 — Analiza danych

## Meta
sekcja_id: 9
sekcja_nazwa: Analiza danych — efektywność kanałów, urządzenia, retencja
dotyczy_domyslnie: all
agent_etap: 3
zrodla_danych: 01_raw-data.md (wszystkie sekcje GA4), GA4 API
ostatnia_aktualizacja: 2026-04
wersja: 2.0

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 9.1 | CVR paid ≥50% CVR organic | Wysoki | ecommerce | raw-data → CR(CPC) / CR(organic) | ≥50% | <30% = ruch płatny słabej jakości | 3 | |
| 9.2 | Najlepszy kanał wg Rev/sesja zidentyfikowany | Średni | all | raw-data → revenue/sessions per kanał | Raport z konkretną kwotą PLN per kanał | Brak analizy per kanał | 2 | Informacyjne — bez punktów zero/jeden |
| 9.3 | Mobile/Desktop CVR ratio | Wysoki | ecommerce | raw-data → CVR mobile / CVR desktop | Mobile CVR ≥50% desktop CVR | Mobile CVR <30% desktop = problem UX mobile | 3 | |
| 9.4 | Engagement rate naturalny | Średni | all | raw-data → engagement rate | >40% | <20% = niska jakość ruchu lub błąd śledzenia | 2 | |
| 9.5 | Porzucenie koszyka <80% | Wysoki | ecommerce | raw-data → 1 - (purchase/add_to_cart) | Porzucenie <80% | >90% porzucenia koszyka | 3 | |
| 9.6 | Anomalie ruchu zidentyfikowane | Średni | all | raw-data → trend ruchu → szczyty i spadki | Anomalie zidentyfikowane z możliwą przyczyną | Niewyjaśnione skoki/spadki >30% | 2 | Informacyjne |
| 9.7 | Ruch wewnętrzny nie zaburza danych | Wysoki | all | raw-data → geografia → miasto siedziby firmy | Brak anomalii z miasta firmy | Miasto firmy z wysokim ruchem i niskim CR = niezfiltrowany ruch wewnętrzny | 3 | |
| 9.8 | Referral z wysokim CVR zidentyfikowany | Niski | all | raw-data → referral → CVR per domena | Lista referrali z CVR >2% | ➖ Informacyjne | 1 | Quick win |
| 9.9 | Bramki płatności/webmaile w referral | Wysoki | all | raw-data → referral → sprawdź PayU onet wp | Brak bramek i webmaili w referral | Bramki lub webmaile jako referral z sesjami | 3 | |
| 9.10 | Retencja — % powracających kupujących | Średni | ecommerce | raw-data → new vs returning purchasers | % powracających >20% | <10% = brak programu retencji | 2 | |

---

## Notatki rozszerzone (tylko dla agenta)

### 9.3 — Wycena potencjału mobile
```
Potencjał = (CVR_desktop - CVR_mobile) × mobile_sessions × AOV
Przykład: (2.1% - 0.8%) × 45 000 sesji × 280 PLN = 16 380 PLN/msc
```

### 9.7 — Jak wykryć niezfiltrowany ruch wewnętrzny
Z raw-data sekcja "Top 20 miast" — sprawdź:
- Miasto siedziby firmy lub agencji z >500 sesjami
- CR z tego miasta znacznie niższy niż średnia konta
- Jeśli tak → ruch pracowników nie jest filtrowany → punkt 3C.8 (Filtrowanie) = ❌

### Kanały do analizy quick wins (9.8)
Kanały z CVR > 2% i niskim budżetem = niedoinwestowane → rekomendacja skalowania.

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| all (zawsze) | 9.4, 9.6, 9.7, 9.8, 9.9 | 11 pkt |
| ecommerce | 9.1, 9.2, 9.3, 9.5, 9.10 | +13 pkt |
| **MINIMUM (all)** | | **11 pkt** |
| **E-COMMERCE** | | **24 pkt** |
