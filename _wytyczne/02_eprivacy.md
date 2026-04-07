# Sekcja 2 — ePrivacy / Consent Mode

## Meta
sekcja_id: 2
sekcja_nazwa: ePrivacy / Consent Mode
dotyczy_domyslnie: all
agent_etap: 3
zrodla_danych: DevTools (Network+Application+Console), GTM Panel Preview Mode, incognito browser
ostatnia_aktualizacja: 2026-04
wersja: 2.0

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 2.1 | Personalizacja wyboru zgód | Niski | all | Incognito → sprawdź baner → czy są kategorie cookies z indywidualnym wyborem | Baner zawiera kategorie: niezbędne, analityczne, marketingowe | Baner tylko Akceptuj/Odrzuć bez kategorii | 1 | |
| 2.2 | Możliwość odrzucenia wszystkich zgód | Niski | all | Sprawdź baner — czy Odrzuć wszystkie jest równie widoczny jak Akceptuj | Przycisk odrzucenia równie dostępny jak akceptacji | Brak opcji odrzucenia lub ukryta pod wieloma kliknięciami | 1 | |
| 2.3 | Strona domyślnie zablokowana | Wysoki | all | Incognito → czy można przeglądać stronę bez interakcji z banerem przez 30 sek | Strona zablokowana przed decyzją użytkownika | Możliwość pełnego przeglądania bez decyzji o cookies | 3 | |
| 2.4 | Poprawnie blokuje pliki cookies | Wysoki | all | DevTools → Network → wyczyść → Odrzuć wszystkie → sprawdź requesty GA4/Meta | 0 requestów analitycznych po odmowie; cookies _ga _gid nie ustawione | Jakikolwiek request analityczny lub piksel po kliknięciu Odrzuć | 3 | |
| 2.5 | Możliwość zmiany decyzji | Niski | all | Po akceptacji — szukaj ikony lub linku do zarządzania zgodami | Ikona cookie lub link w stopce umożliwiający zmianę | Brak stałego dostępu do zmiany ustawień | 1 | |
| 2.6 | Ustawienia domyślne — wymuszony wybór | Średni | all | Incognito → DevTools → Network → ładuj stronę → nie klikaj 30 sek → sprawdź requesty GA4 | 0 requestów GA4 przed decyzją użytkownika | Requesty GA4 przed jakąkolwiek interakcją | 2 | |
| 2.7 | Ustawienia domyślne — brak cookies przed decyzją | Średni | all | DevTools → Application → Storage → cookies przed wyborem | Brak cookies _ga _gid przed decyzją | Cookies analityczne ustawione bez zgody | 2 | |
| 2.8 | Wywołanie consent update w DataLayer | Średni | all | DevTools → Console → dataLayer → sprawdź sekwencję | consent default → wybór → consent update | Brak consent_update lub błędna kolejność | 2 | |
| 2.9 | Brak odświeżania strony po zgodzie | Średni | all | Kliknij Akceptuj → obserwuj czy strona się przeładowuje | Brak page reload po akceptacji | Strona przeładowuje się po kliknięciu Akceptuj | 2 | |
| 2.10 | GA4 i piksele wywołują się po zgodzie | Wysoki | all | Incognito → DevTools → Network → wyczyść → Akceptuj → sprawdź requesty GA4 | Requesty GA4 i pikseli pojawiają się po akceptacji | Tagi nie wywołują się nawet po akceptacji | 3 | |
| 2.11 | Brak podwójnego user_engagement po zgodzie | Niski | all | Network po Akceptuj → sprawdź czy nie ma 2x page_view lub natychmiastowego user_engagement | Jeden page_view, brak user_engagement w pierwszej sekundzie | Dwa page_view lub natychmiastowy user_engagement | 1 | |
| 2.12 | Przegląd ustawień zgód w GTM | Średni | all | GTM → każdy tag → zakładka Consent | Każdy tag ma przypisany tryb zgody | Jakikolwiek tag analityczny lub reklamowy bez consent setting | 2 | |
| 2.13 | CMP ładuje się z Consent Initialization | Średni | all | GTM → Tag CMP → reguła: Consent Initialization — All Pages | CMP ładuje się w Consent Initialization | CMP z regułą All Pages zamiast Consent Initialization | 2 | |
| 2.14 | Consent Mode blokuje tagi bez zgody | Wysoki | all | GTM Preview → strona bez zgody → sprawdź Blocked by consent | Tagi reklamowe i analityczne oznaczone Blocked | Tagi wywołują się bez czekania na zgodę | 3 | |
| 2.15 | Wszystkie tagi mają tryb zgody | Średni | all | GTM → lista tagów → każdy tag musi mieć consent setting | 100% tagów ma consent setting | Jakikolwiek tag bez przypisanego consent | 2 | |
| 2.16 | PING w Consent Mode | Średni | all | DevTools → Network po odmowie → sprawdź puste requesty do GA4 | Anonimowe pings wysyłane do GA4 po odmowie | Całkowity brak komunikacji z GA4 po odmowie | 2 | |
| 2.17 | url_passthrough | Wysoki | all | GTM → Tag GA4 Configuration → Pola konfiguracji → url_passthrough: true | url_passthrough włączone | Brak url_passthrough | 3 | |
| 2.18 | Brak danych wrażliwych w URL | Wysoki | all | GA4 → Raporty → Strony → szukaj wzorców email= mail= phone= w URL | Brak danych osobowych w URL-ach | URL-e z adresami email, telefonem, PESEL | 3 | |
| 2.19 | Brak danych wrażliwych w UTM | Wysoki | all | GA4 → Eksploracje → filtruj source/medium/campaign pod kątem emaili | Brak danych osobowych w UTM | Adresy email lub dane osobowe w UTM | 3 | |
| 2.20 | Brak danych wrażliwych w zdarzeniach | Wysoki | all | GA4 → DebugView lub BigQuery → sprawdź wartości parametrów zdarzeń | Brak danych osobowych w event parameters | Email, telefon, PESEL w parametrach zdarzeń | 3 | |

---

## Notatki rozszerzone (tylko dla agenta)

### 2.4 — Test skutecznego blokowania
1. Otwórz DevTools → Network → wyczyść log
2. Kliknij "Odrzuć wszystkie" na banerze
3. Obserwuj przez 5 sekund — sprawdź czy pojawia się:
   - Request do `google-analytics.com/g/collect` → ❌ BŁĄD
   - Request do `facebook.com/tr` → ❌ BŁĄD
   - Cookie `_ga` lub `_gid` w Application → Storage → ❌ BŁĄD

### 2.17 — url_passthrough
Bez url_passthrough użytkownicy odmawiający cookies nie są przypisywani do kampanii reklamowych, co zaniża mierzony ROI. Sprawdź w GTM → Tag GA4 Config → pole `url_passthrough: true` lub w gtag bezpośrednim: `gtag('set', 'url_passthrough', true)`.

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| all (zawsze) | 2.1–2.20 | 45 pkt |
| **ŁĄCZNIE** | | **45 pkt** |
