# Brief: modnakiecka — 20260407

## Dane podstawowe
- Nazwa klienta: modnakiecka.pl
- URL strony: https://modnakiecka.pl
- Typ biznesu: e-commerce (fashion / odzież damska)
- Tryb audytu: single konto

## Dostępy techniczne
- GA4 Property ID: 291537403 (measurement ID: G-6S5QRBJ4EF)
- Google Ads Customer ID: brak dostępu
- GTM Container ID: GTM-N4D6KSC (właściciel) + GTM-T68LWS (Shoper — automatyczny)
- GTM Admin: brak dostępu (weryfikacja tagów wyłącznie przez analizę HTML + GA4)
- BigQuery dataset: brak
- BDOS alias Google Ads: brak
- CMP (Consent Management Platform): własne rozwiązanie (`window.customerPrivacy`) — brak zewnętrznego dostawcy (Cookiebot / OneTrust / Usercentrics)

## Zakres audytu
- Sekcje: pełny (1–10)
- Sekcje wymagające Google Ads (sekcja 6 BCG, sekcja 8 GA4↔Ads, sekcja 10): oznaczone 🔒 Brak dostępu
- Sekcje wymagające BigQuery: oznaczone 🔒 Brak dostępu
- Priorytety: GA4 data quality, ePrivacy, śledzenie e-commerce, UTM, lejki

## Informacje dodatkowe
- Platforma sklepu: Shoper (appstore-bridge.prod.shoper.cloud)
- Agencja prowadząca: (do potwierdzenia)
- Stack MarTech wykryty z HTML (poprzedni audyt):
  - 2× GTM (właściciela + Shopera)
  - GA4 G-6S5QRBJ4EF
  - Universal Analytics UA-82686028-1 (martwy tag)
  - Meta Pixel 973622559419130
  - Google Ads Conversion Tag (ID: 798911571)
  - Criteo (account 40373)
  - Admitad (affiliate)
  - SALESmanago (Shop ID: 4257)
  - Przelewy24, PayPo
  - WP Pixel, Onet DL API
- Uwagi: Poprzedni audyt (2026-04-03) wykrył krytyczne problemy: duplikacja tagów GTM, begin_checkout nie działa, 11.8% purchase bez transactionId. Nowy audyt weryfikuje aktualne dane i pełny zakres wytycznych.
