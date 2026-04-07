# Sekcja 8 — Spójność GA4 ↔ Google Ads

## Meta
sekcja_id: 8
sekcja_nazwa: Spójność GA4 ↔ Google Ads + Enhanced Conversions
dotyczy_domyslnie: ads
agent_etap: 3
zrodla_danych: GA4 Admin (Połączone usługi), Google Ads Panel (Konwersje), 01_raw-data.md
ostatnia_aktualizacja: 2026-04
wersja: 2.0
warunek_wejscia: klient z kontem Google Ads

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 8.1 | Połączenie GA4↔Ads aktywne | Wysoki | ads | GA4 → Admin → Połączone usługi → Google Ads → status | Status: Połączono | Brak połączenia lub błąd | 3 | |
| 8.2 | Reklamy spersonalizowane włączone | Wysoki | ads | GA4 → Połączone usługi → reklamy spersonalizowane | Włączone | Wyłączone = brak remarketingu w Ads | 3 | |
| 8.3 | Konwersje GA4 widoczne w Google Ads | Wysoki | ads | Google Ads → Narzędzia → Konwersje → filtruj GA4 | Min. 1 konwersja zaimportowana z GA4 | Brak importu konwersji z GA4 | 3 | |
| 8.4 | Delta przychodów GA4 vs Ads ≤30% | Wysoki | ads+ecommerce | Oblicz: (ads_revenue - ga4_cpc_revenue) / ads_revenue × 100 | Delta ≤15% | Delta >30% = błąd konfiguracji | 3 | ✅ ≤15% / ⚠️ 15-30% / ❌ >30% |
| 8.5 | Konwersja Primary ustawiona | Wysoki | ads | Google Ads → Konwersje → Primary/Secondary | purchase jako Primary (e-comm) | Brak Primary lub mikrokonwersja jako Primary | 3 | |
| 8.6 | Wartości konwersji dynamiczne | Wysoki | ads+ecommerce | Google Ads → Konwersje → Wartość | Dynamiczna wartość z DataLayer | Stała wartość 1 PLN | 3 | |
| 8.7 | Brak duplikacji śledzenia | Wysoki | ads | Sprawdź czy nie ma tagu Ads + importu GA4 dla tej samej akcji | Max 1 źródło per konwersja | Dwie konwersje purchase z różnych źródeł | 3 | |
| 8.8 | Enhanced Conversions włączone | Średni | ads | Google Ads → Narzędzia → Konwersje → EC | Aktywne, match rate >40% | Wyłączone lub match rate <20% | 2 | |
| 8.9 | Listy odbiorców eksportowane | Średni | ads | Sprawdź listy: Wszyscy użytkownicy, Porzucający koszyk, Kupujący | Min. 3 listy aktywne z odpowiednim rozmiarem | Brak list lub listy za małe (Remarketing <100 userów) | 2 | |
| 8.10 | Customer Match | Średni | ads | Google Ads → Odbiorcy → Customer Match | Lista aktywna, match rate >30%, >1000 dopasowanych | Match rate <20% lub <1000 dopasowanych | 2 | ➖ jeśli brak bazy CRM |

---

## Notatki rozszerzone (tylko dla agenta)

### 8.4 — Obliczanie delty
```
GA4 CPC revenue = suma purchaseRevenue z raw-data gdzie sessionMedium = cpc
Ads conv_value = suma z BDOS perf.data (conv_value)
delta_pct = |GA4_revenue - Ads_conv_value| / Ads_conv_value × 100
```

Typowe przyczyny dużej delty:
- GA4 Cross-network nie jest w filtrze CPC
- Różne okna atrybucji (Google Ads 30d klik vs GA4 7d)
- Brak `items[]` array w zdarzeniu purchase

### 8.9 — Minimalne rozmiary list
- Remarketing Display: min. 100 userów
- RLSA (Search): min. 1 000 userów
- Customer Match: min. 1 000 dopasowanych, match rate >30%

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| ads (zawsze jeśli Google Ads) | 8.1–8.10 | 27 pkt |
| **ŁĄCZNIE** | | **27 pkt** |
