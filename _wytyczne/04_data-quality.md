# Sekcja 4 — Data Quality

## Meta
sekcja_id: 4
sekcja_nazwa: Data Quality
dotyczy_domyslnie: all
agent_etap: 3
zrodla_danych: 01_raw-data.md (sekcje: źródła ruchu, transakcje, zdarzenia, lejek)
ostatnia_aktualizacja: 2026-04
wersja: 2.0

---

## Kryteria — 4A: Jakość źródeł ruchu

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 4A.1 | Udział sesji (not set) <5% | Wysoki | all | raw-data → źródła ruchu → oblicz % (not set)/wszystkie sesje | <5% | >15% | 3 | |
| 4A.2 | Udział pierwszego źródła (not set) <5% | Wysoki | all | raw-data → pierwsze źródło użytkownika → % (not set) | <5% | >15% | 3 | |
| 4A.3 | Pierwsze źródło użytkownika wygląda naturalnie | Wysoki | all | raw-data → sprawdź dystrybucję first user source | Naturalna dystrybucja kanałów | Dominacja direct/none >50% bez uzasadnienia | 3 | |
| 4A.4 | Pozostały ruch wygląda naturalnie | Wysoki | all | raw-data → sprawdź metryki per kanał | Brak anomalii w sesjach, CR, czasie | Jeden kanał >70% bez uzasadnienia lub nierealne metryki | 3 | |
| 4A.5 | Cross-domain — brak własnych domen w referral | Średni | all | raw-data → sprawdź czy własne domeny w referral | Brak własnych domen jako referral | Własna domena z >100 sesjami jako referral | 2 | |
| 4A.6 | Brak ruchu spamowego | Średni | all | raw-data → sprawdź podejrzane domeny referral | Ruch spamowy <1% | >5% podejrzanego ruchu | 2 | |
| 4A.7 | Bramki płatności poza ścieżką | Wysoki | ecommerce | raw-data → sprawdź czy PayU, Przelewy24, PayPal w referral | Bramki nieobecne w referral | Bramki w referral z transakcjami | 3 | |
| 4A.8 | Bramki pocztowe poza ścieżką | Wysoki | all | raw-data → sprawdź czy webmaile (wp.pl, onet.pl) w referral | Webmaile nieobecne lub <10 sesji | Setki sesji z webmaili | 3 | |
| 4A.9 | Facebook/Meta — dane unifikowane | Średni | all | raw-data → policz warianty source dla Meta | Max 2 warianty | 5+ wariantów (facebook, fb, facebook.com, m.facebook.com...) | 2 | |
| 4A.10 | Ruch międzynarodowy | Średni | all | raw-data → geografia → sprawdź kraje | Ruch z krajów dostawy/targetowania | Duży % z krajów poza targetem (bot?) | 2 | |

---

## Kryteria — 4B: Jakość strony

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 4B.1 | Czas trwania sesji naturalny | Średni | all | raw-data → avg session duration | Powyżej 1 minuty dla typowego ruchu | <20s średnio = ruch botów lub błąd śledzenia | 2 | |
| 4B.2 | Engagement rate naturalny | Średni | all | raw-data → engagement rate | >40% | <20% = niemal cały ruch niezaangażowany | 2 | |
| 4B.3 | CR naturalny | Średni | ecommerce | raw-data → CR = transactions/sessions | 0.5–3% | <0.1% lub >10% | 2 | |

---

## Kryteria — 4C: Sesje (not set) — szczegóły

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 4C.1 | source/medium not set <5% | Wysoki | all | raw-data → source/medium → % (not set) | <5% | >15% | 3 | |
| 4C.2 | direct/none <30% | Wysoki | all | raw-data → source/medium → % direct/none | <30% | >50% | 3 | |
| 4C.3 | Łączny not set + direct <40% | Wysoki | all | Suma obu powyższych | <40% | >60% | 3 | |
| 4C.4 | Transakcje (not set) <10% | Wysoki | ecommerce | raw-data → transakcje → % bez źródła | <10% | >20% | 3 | |

---

## Kryteria — 4D: Jakość transakcji (e-commerce)

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 4D.1 | Ratio ecommercePurchases:transactions ≤1.1 | Wysoki | ecommerce | raw-data → ecommercePurchases / transactions | ≤1.1 (GA4 deduplicuje) | >1.5 = duplikacja zdarzeń purchase | 3 | |
| 4D.2 | % transakcji bez transactionId <2% | Wysoki | ecommerce | raw-data → % wierszy z transactionId=null | <2% | >5% | 3 | |
| 4D.3 | Brak malformed transaction_id | Wysoki | ecommerce | raw-data → sprawdź czy ID zawiera & = spacje | 0 malformed ID | Jakikolwiek ID z parametrami URL w środku | 3 | |
| 4D.4 | value >0 przy purchase | Wysoki | ecommerce | raw-data → % purchase z value=0 | <1% | >5% | 3 | |
| 4D.5 | currency ustawione | Wysoki | ecommerce | raw-data → currency per transaction | 100% z walutą | Pusta waluta lub mieszane waluty | 3 | |

---

## Kryteria — 4E: Zdarzenia e-commerce (kompletność)

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 4E.1 | view_item wdrożone | Wysoki | ecommerce | raw-data → zdarzenia → view_item obecny | Tak | Brak view_item | 3 | |
| 4E.2 | add_to_cart wdrożone | Wysoki | ecommerce | raw-data → zdarzenia → add_to_cart obecny | Tak | Brak add_to_cart | 3 | |
| 4E.3 | begin_checkout wdrożone | Wysoki | ecommerce | raw-data → zdarzenia → begin_checkout obecny | Tak | Brak begin_checkout | 3 | |
| 4E.4 | purchase wdrożone | Wysoki | ecommerce | raw-data → zdarzenia → purchase obecny | Tak | Brak purchase = brak śledzenia sprzedaży | 3 | |
| 4E.5 | Lejek wygląda naturalnie | Wysoki | ecommerce | raw-data → lejek: purchase < begin_checkout < add_to_cart < view_item | Każdy krok mniej niż poprzedni | purchase > begin_checkout = duplikacja | 3 | |
| 4E.6 | AOV naturalny i spójny | Średni | ecommerce | raw-data → purchaseRevenue / transactions = AOV | AOV >0, spójny per kanał | AOV (not set) >>2× średniej = problem atrybucji | 2 | |

---

## Notatki rozszerzone (tylko dla agenta)

### 4D.1 — Jak obliczyć ratio
Z `01_raw-data.md` sekcja "Transakcje":
- `ecommercePurchases` = RAW liczba zdarzeń purchase
- `transactions` = metryka GA4 po deduplicacji
- Ratio = ecommercePurchases / transactions
- Jeśli GA4 deduplicuje: każdy wiersz transactionId ma transactions=1 → ratio ≈ 1.0

### 4A.9 — Fragmentacja Meta — jak wycenić
```
Warianty Meta w raw-data → zsumuj sesje:
  facebook / cpc: 184 372
  facebook.com / referral: 38 291
  m.facebook.com / referral: 19 440
  l.facebook.com / referral: 8 218
→ Razem 250 321 sesji rozbitych na 4 wiersze → GA4 liczy je jako 4 różne źródła
```

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| all (zawsze) | 4A.1–4A.6 + 4A.8–4A.10 + 4B.1–4B.2 + 4C.1–4C.3 | ~40 pkt |
| ecommerce | 4A.3, 4A.7, 4B.3, 4C.4, 4D.1–4D.5, 4E.1–4E.6 | +35 pkt |
| **MINIMUM (all)** | | **~40 pkt** |
| **E-COMMERCE** | | **~75 pkt** |
