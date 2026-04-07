# Sekcja 3 — Konfiguracja

## Meta
sekcja_id: 3
sekcja_nazwa: Konfiguracja GTM i GA4
dotyczy_domyslnie: all
agent_etap: 3
zrodla_danych: GTM Panel (Web+Server), GA4 Admin, GCP Cloud Run, DevTools
ostatnia_aktualizacja: 2026-04
wersja: 2.0

---

## Kryteria — 3A: GTM Web

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|---|---|---|---|---|---|---|---|---|
| 3A.1 | Walidacja GTM | Wysoki | all | Źródło strony → szukaj GTM snippet → sprawdź pozycję w head i noscript po body | GTM jako pierwszy skrypt w head, noscript bezpośrednio po body | GTM na dole strony lub zakomentowany | 3 |  |
| 3A.2 | Brak błędów i powiadomień w GTM | Wysoki | all | GTM → Workspace → ikona dzwonka + zakładka Aktywność | 0 powiadomień krytycznych | Czerwone powiadomienia w panelu GTM | 3 |  |
| 3A.3 | Consent dla wszystkich tagów | Wysoki | all | GTM → każdy tag → Ustawienia zaawansowane → Wymagania zgody | Każdy tag ma min. 1 wymóg zgody | Tag analityczny lub reklamowy bez consent settings | 3 |  |
| 3A.4 | Tag łączący konwersje | Wysoki | ads | GTM → Tagi → szukaj Conversion Linker → reguła All Pages | Conversion Linker aktywny z All Pages | Brak Conversion Linker lub zła reguła | 3 |  |
| 3A.5 | Podsumowanie zasięgu tagu | Wysoki | all | GTM → Admin → Podsumowanie zasięgu tagu | Zasięg >95% | Zasięg <80% lub nieotagowane kluczowe podstrony | 3 |  |
| 3A.6 | Wersje kontenerów mają tytuły | Niski | all | GTM → Wersje → sprawdź nazwy | Wersje z datą i opisem zmian | Wszystkie wersje z domyślną nazwą Published | 1 |  |
| 3A.7 | Brak kodów UA w GTM | Wysoki | all | GTM → Tagi → filtruj Universal Analytics lub UA- | 0 aktywnych tagów UA | Jakikolwiek aktywny tag UA w GTM | 3 |  |
| 3A.8 | GA4 wdrożone przez GTM | Niski | all | GTM → Tagi → GA4 Configuration → sprawdź Measurement ID | GA4 wdrożone przez tag GTM | GA4 tylko hardcoded w HTML | 1 |  |
| 3A.9 | Liczba tagów <40 | Średni | all | GTM → Tagi → policz wszystkie | <30 tagów | >60 tagów | 2 | ✅ <30 / ⚠️ 30–60 / ❌ >60 |
| 3A.10 | Brak zduplikowanych tagów | Wysoki | all | Sprawdź czy ta sama akcja śledzona 2× | 0 duplikatów | Jakikolwiek duplikat śledzenia tej samej akcji | 3 |  |
| 3A.11 | Konwencja nazewnictwa tagów | Średni | all | Standard: [Narzędzie] - [Akcja] - [Trigger] | >80% tagów z konwencją | >20% tagów bez konwencji | 2 |  |
| 3A.12 | Brak martwych reguł i zmiennych | Średni | all | Reguły bez tagu, zmienne bez użycia w tagach | 0 martwych elementów | Martwe reguły i zmienne zaśmiecają kontener | 2 |  |
| 3B.1 | sGTM włączony i skonfigurowany | Wysoki | sgtm | GTM → kontenery → kontener Server | Kontener Server istnieje i aktywny | ➖ jeśli brak sGTM | 3 |  |
| 3B.2 | GCP skonfigurowane i płatność OK | Wysoki | sgtm | GCP Console → Cloud Run + Rozliczenia | Cloud Run aktywny, brak zaległości | Zaległości płatnicze lub nieaktywny serwis | 3 |  |
| 3B.3 | Custom domain 1st party dodana | Wysoki | sgtm | DNS → sprawdź CNAME dla analytics.{domena} | Własna domena skonfigurowana | Brak własnej domeny dla sGTM | 3 |  |
| 3B.4 | Transport URL ustawiony | Wysoki | sgtm | GTM Web → Tag GA4 Config → server_container_url | URL sGTM = własna domena (nie googletagmanager.com) | URL wskazuje na googletagmanager.com | 3 |  |
| 3B.5 | Walidacja klienta przeszła | Wysoki | sgtm | GTM Server → Klienci → status | Status: Zweryfikowany | Status: Niezweryfikowany lub błąd | 3 |  |
| 3B.6 | Preview Mode sGTM bez błędów | Wysoki | sgtm | GTM Server Preview → requesty docierają | Requesty widoczne w Preview | Brak requestów w Preview | 3 |  |
| 3C.1 | Alerty i powiadomienia GA4 | Wysoki | all | GA4 → Admin → ikona dzwonka | 0 powiadomień krytycznych | Nieprzeczytane alerty o problemach z danymi | 3 |  |
| 3C.2 | Uprawnienia do konta | Wysoki | all | GA4 → Admin → Zarządzanie dostępem | Tylko aktywni pracownicy/agencje z adekwatnymi rolami | Byli pracownicy lub nieznane konta z rolą Edytor/Admin | 3 |  |
| 3C.3 | Waluta | Średni | ecommerce | GA4 → Admin → Ustawienia usługi → Waluta | Waluta zgodna z rynkiem (PLN dla PL) | EUR lub USD dla sklepu PLN | 2 |  |
| 3C.4 | Google Signals | Wysoki | all | GA4 → Admin → Zbieranie danych → Google Signals | Status: Aktywne | Wyłączone | 3 |  |
| 3C.5 | User-ID | Średni | all | GA4 → Admin → Zbieranie danych → User-ID | Włączone jeśli klient ma rejestrację | Wyłączone przy sklepie z kontem klienta | 2 |  |
| 3C.6 | Import danych | Średni | all | GA4 → Admin → Import danych → daty odświeżenia | Importy aktualne | Import kosztów nieaktualizowany >30 dni | 2 |  |
| 3C.7 | Przechowywanie danych — 14 miesięcy | Niski | all | GA4 → Admin → Przechowywanie danych | 14 miesięcy | Domyślne 2 miesiące | 1 |  |
| 3C.8 | Filtrowanie ruchu wewnętrznego | Wysoki | all | GA4 → Admin → Filtry danych | Filtr Ruch wewnętrzny aktywny z listą IP | Brak filtra — dane z ruchem pracowników | 3 |  |
| 3C.9 | Strumień Web | Wysoki | all | GA4 → Admin → Strumienie → Web | Dane napływające w ciągu 48h | Brak danych >48h | 3 |  |
| 3C.10 | Cross-domain tracking | Wysoki | ecommerce | GA4 → Strumień → Konfigurowanie domen | Bramki płatności na liście własnych domen | Bramki płatności powodują nowe sesje | 3 |  |
| 3C.11 | Ignorowanie zduplikowanych konfiguracji | Wysoki | all | GA4 → Strumień → Zarządzaj tagiem → Zduplikowane tagi → Ignoruj | Włączone | Wyłączone przy GTM + hardcoded GA4 | 3 |  |
| 3C.12 | Wykluczono bramki płatności | Wysoki | ecommerce | GA4 → Strumień → Referral exclusion | PayU, Przelewy24, PayPal, Stripe na liście | Brak wykluczenia → nowe sesje z bramek | 3 |  |
| 3C.13 | Wykluczono bramki pocztowe | Średni | all | GA4 → Strumień → Referral exclusion | wp.pl, onet.pl, o2.pl, interia.pl na liście | Webmaile generują fałszywy referral | 2 |  |
| 3C.14 | Wykluczono boty CMP | Wysoki | all | GA4 → Strumień → Referral exclusion + filtry | Crawlery CMP wykluczone | Fałszywy ruch od robotów CMP | 3 |  |
| 3C.15 | Czas trwania sesji | Średni | ecommerce | GA4 → Strumień → Czas sesji | Min. 5 godzin dla e-commerce | Domyślne 30 min = zbyt krótkie | 2 |  |
| 3C.16 | Zdarzenia jako konwersje | Średni | all | GA4 → Admin → Konwersje | Min. purchase oznaczone jako konwersja | Brak jakichkolwiek konwersji | 2 |  |
| 3C.17 | Model atrybucji | Średni | all | GA4 → Admin → Ustawienia atrybucji | Data-Driven (DDA) lub Last Click | First Click, Linear, Time Decay | 2 |  |
| 3C.18 | Połączenie Google Ads | Wysoki | ads | GA4 → Admin → Połączone usługi → Google Ads | Status: Połączono | Brak połączenia | 3 |  |
| 3C.19 | BigQuery | Wysoki | all | GA4 → Admin → Połączone usługi → BigQuery | Status: aktywny | Brak eksportu | 3 |  |
| 3C.20 | Search Console | Wysoki | all | GA4 → Admin → Połączone usługi → Search Console | Status: połączono | Brak połączenia | 3 |  |
| 3C.21 | Alerty o anomaliach z emailem | Wysoki | all | GA4 → Insights → Alerty niestandardowe | Alerty dla sessions, transactions, revenue z emailem | Brak alertów lub alerty bez emaila | 3 |  |
| 3K.1 | Health check — świeżość danych | Wysoki | bq | days_lag między ostatnim dniem danych a dzisiaj | days_lag ≤1 | days_lag >3 = eksport zepsuty | 3 |  |
| 3K.2 | Wolumen — brak anomalii | Wysoki | bq | Dzienne liczby page_view, purchase → outliery | Brak dni z purchases=0 przy normalnym ruchu | Dni z 0 purchases przy normalnym page_view | 3 |  |
| 3K.3 | Schemat — kompletność pól | Wysoki | bq | Obecność: user_pseudo_id, ecommerce.*, items[], collected_traffic_source | Kluczowe pola wypełnione >95% | Kluczowe pola null >5% | 3 |  |
| 3K.4 | Jakość items[] | Wysoki | bq+ecommerce | % null/not set dla item_id, price, quantity, item_category | item_id null <2%, price=0 <1% | item_id null >2%, price=0 | 3 |  |
| 3K.5 | Duplikaty transakcji | Wysoki | bq+ecommerce | % zduplikowanych transaction_id w 30d | <1% duplikatów | >5% duplikatów | 3 |  |
| 3K.6 | Jakość źródeł ruchu | Wysoki | bq | % (not set) w collected_traffic_source.manual_source | (not set) <10% | >20% not set | 3 |  |
| 3K.7 | Delta BQ vs GA4 UI | Wysoki | bq+ecommerce | Porównanie transakcji i przychodu: BQ vs GA4 UI | Delta <5% | Delta >10% | 3 |  |

---

## Kryteria — 3B: GTM Server Side

> Pomiń tę podsekcję jeśli sGTM nieaktywny (brak server_container_url w tagu GA4).

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 3B.1 | sGTM włączony i skonfigurowany | Wysoki | sgtm | GTM → kontenery → kontener Server | Kontener Server istnieje i aktywny | ➖ jeśli brak sGTM | 3 | |
| 3B.2 | GCP skonfigurowane i płatność OK | Wysoki | sgtm | GCP Console → Cloud Run + Rozliczenia | Cloud Run aktywny, brak zaległości | Zaległości płatnicze lub nieaktywny serwis | 3 | |
| 3B.3 | Custom domain 1st party dodana | Wysoki | sgtm | DNS → sprawdź CNAME dla analytics.{domena} | Własna domena skonfigurowana | Brak własnej domeny dla sGTM | 3 | |
| 3B.4 | Transport URL ustawiony | Wysoki | sgtm | GTM Web → Tag GA4 Config → server_container_url | URL sGTM = własna domena (nie googletagmanager.com) | URL wskazuje na googletagmanager.com | 3 | |
| 3B.5 | Walidacja klienta przeszła | Wysoki | sgtm | GTM Server → Klienci → status | Status: Zweryfikowany | Status: Niezweryfikowany lub błąd | 3 | |
| 3B.6 | Preview Mode sGTM bez błędów | Wysoki | sgtm | GTM Server Preview → requesty docierają | Requesty widoczne w Preview | Brak requestów w Preview | 3 | |

---

## Kryteria — 3C–3J: Konfiguracja GA4 Admin

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 3C.1 | Alerty i powiadomienia GA4 | Wysoki | all | GA4 → Admin → ikona dzwonka | 0 powiadomień krytycznych | Nieprzeczytane alerty o problemach z danymi | 3 | |
| 3C.2 | Uprawnienia do konta | Wysoki | all | GA4 → Admin → Zarządzanie dostępem | Tylko aktywni pracownicy/agencje z adekwatnymi rolami | Byli pracownicy lub nieznane konta z rolą Edytor/Admin | 3 | |
| 3C.3 | Waluta | Średni | ecommerce | GA4 → Admin → Ustawienia usługi → Waluta | Waluta zgodna z rynkiem (PLN dla PL) | EUR lub USD dla sklepu PLN | 2 | |
| 3C.4 | Google Signals | Wysoki | all | GA4 → Admin → Zbieranie danych → Google Signals | Status: Aktywne | Wyłączone | 3 | |
| 3C.5 | User-ID | Średni | all | GA4 → Admin → Zbieranie danych → User-ID | Włączone jeśli klient ma rejestrację | Wyłączone przy sklepie z kontem klienta | 2 | |
| 3C.6 | Import danych | Średni | all | GA4 → Admin → Import danych → daty odświeżenia | Importy aktualne | Import kosztów nieaktualizowany >30 dni | 2 | |
| 3C.7 | Przechowywanie danych — 14 miesięcy | Niski | all | GA4 → Admin → Przechowywanie danych | 14 miesięcy | Domyślne 2 miesiące | 1 | |
| 3C.8 | Filtrowanie ruchu wewnętrznego | Wysoki | all | GA4 → Admin → Filtry danych | Filtr Ruch wewnętrzny aktywny z listą IP | Brak filtra — dane z ruchem pracowników | 3 | |
| 3C.9 | Strumień Web | Wysoki | all | GA4 → Admin → Strumienie → Web | Dane napływające w ciągu 48h | Brak danych >48h | 3 | |
| 3C.10 | Cross-domain tracking | Wysoki | ecommerce | GA4 → Strumień → Konfigurowanie domen | Bramki płatności na liście własnych domen | Bramki płatności powodują nowe sesje | 3 | |
| 3C.11 | Ignorowanie zduplikowanych konfiguracji | Wysoki | all | GA4 → Strumień → Zarządzaj tagiem → Zduplikowane tagi → Ignoruj | Włączone | Wyłączone przy GTM + hardcoded GA4 | 3 | |
| 3C.12 | Wykluczono bramki płatności | Wysoki | ecommerce | GA4 → Strumień → Referral exclusion | PayU, Przelewy24, PayPal, Stripe na liście | Brak wykluczenia → nowe sesje z bramek | 3 | |
| 3C.13 | Wykluczono bramki pocztowe | Średni | all | GA4 → Strumień → Referral exclusion | wp.pl, onet.pl, o2.pl, interia.pl na liście | Webmaile generują fałszywy referral | 2 | |
| 3C.14 | Wykluczono boty CMP | Wysoki | all | GA4 → Strumień → Referral exclusion + filtry | Crawlery CMP wykluczone | Fałszywy ruch od robotów CMP | 3 | |
| 3C.15 | Czas trwania sesji | Średni | ecommerce | GA4 → Strumień → Czas sesji | Min. 5 godzin dla e-commerce | Domyślne 30 min = zbyt krótkie | 2 | |
| 3C.16 | Zdarzenia jako konwersje | Średni | all | GA4 → Admin → Konwersje | Min. purchase oznaczone jako konwersja | Brak jakichkolwiek konwersji | 2 | |
| 3C.17 | Model atrybucji | Średni | all | GA4 → Admin → Ustawienia atrybucji | Data-Driven (DDA) lub Last Click | First Click, Linear, Time Decay | 2 | |
| 3C.18 | Połączenie Google Ads | Wysoki | ads | GA4 → Admin → Połączone usługi → Google Ads | Status: Połączono | Brak połączenia | 3 | |
| 3C.19 | BigQuery | Wysoki | all | GA4 → Admin → Połączone usługi → BigQuery | Status: aktywny | Brak eksportu | 3 | |
| 3C.20 | Search Console | Wysoki | all | GA4 → Admin → Połączone usługi → Search Console | Status: połączono | Brak połączenia | 3 | |
| 3C.21 | Alerty o anomaliach z emailem | Wysoki | all | GA4 → Insights → Alerty niestandardowe | Alerty dla sessions, transactions, revenue z emailem | Brak alertów lub alerty bez emaila | 3 | |

---

## Kryteria — 3K: BigQuery Export Audit

> Pomiń tę podsekcję jeśli BigQuery nieaktywny (punkt 3C.19 = ❌).

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 3K.1 | Health check — świeżość danych | Wysoki | bq | days_lag między ostatnim dniem danych a dzisiaj | days_lag ≤1 | days_lag >3 = eksport zepsuty | 3 | |
| 3K.2 | Wolumen — brak anomalii | Wysoki | bq | Dzienne liczby page_view, purchase → outliery | Brak dni z purchases=0 przy normalnym ruchu | Dni z 0 purchases przy normalnym page_view | 3 | |
| 3K.3 | Schemat — kompletność pól | Wysoki | bq | Obecność: user_pseudo_id, ecommerce.*, items[], collected_traffic_source | Kluczowe pola wypełnione >95% | Kluczowe pola null >5% | 3 | |
| 3K.4 | Jakość items[] | Wysoki | bq+ecommerce | % null/not set dla item_id, price, quantity, item_category | item_id null <2%, price=0 <1% | item_id null >2%, price=0 | 3 | |
| 3K.5 | Duplikaty transakcji | Wysoki | bq+ecommerce | % zduplikowanych transaction_id w 30d | <1% duplikatów | >5% duplikatów | 3 | |
| 3K.6 | Jakość źródeł ruchu | Wysoki | bq | % (not set) w collected_traffic_source.manual_source | (not set) <10% | >20% not set | 3 | |
| 3K.7 | Delta BQ vs GA4 UI | Wysoki | bq+ecommerce | Porównanie transakcji i przychodu: BQ vs GA4 UI | Delta <5% | Delta >10% | 3 | |

---

## Notatki rozszerzone (tylko dla agenta)

### 3K — Zapytania BigQuery do sprawdzenia
```sql
-- Świeżość danych
SELECT MAX(_TABLE_SUFFIX) AS last_date,
  DATE_DIFF(CURRENT_DATE(), PARSE_DATE('%Y%m%d', MAX(_TABLE_SUFFIX)), DAY) AS days_lag
FROM `{project}.{dataset}.INFORMATION_SCHEMA.TABLES`
WHERE table_name LIKE 'events_2%';

-- Duplikaty transakcji
SELECT COUNT(*) total, COUNTIF(event_count > 1) duplicates,
  ROUND(COUNTIF(event_count > 1)/COUNT(*)*100, 2) AS dup_pct
FROM (
  SELECT ecommerce.transaction_id, COUNT(*) AS event_count
  FROM `{project}.{dataset}.events_*`
  WHERE _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY))
    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
    AND event_name = 'purchase'
  GROUP BY 1
);
```

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| all (zawsze) | 3A.1–3A.12 + 3C.1–3C.21 | ~90 pkt |
| ads | 3A.4, 3C.18 | +6 pkt |
| ecommerce | 3C.3, 3C.10, 3C.12, 3C.15, 3C.16 | +13 pkt |
| sgtm (jeśli dotyczy) | 3B.1–3B.6 | +18 pkt |
| bq (jeśli dotyczy) | 3K.1–3K.7 | +21 pkt |
| **MINIMUM (all)** | | **~90 pkt** |
| **MAKSIMUM (all+sgtm+bq+ecomm+ads)** | | **~148 pkt** |
