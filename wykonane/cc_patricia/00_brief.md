# Brief: patrizia.aryton.pl — 20260407

## Dane podstawowe
- Nazwa klienta: Patrizia Aryton (patrizia.aryton.pl)
- URL strony: https://patrizia.aryton.pl/
- Typ biznesu: e-commerce (odzież premium damska)
- Tryb audytu: single konto (stream patrizia w ramach property Aryton)

## Dostępy techniczne
- GA4 Property ID: 326801658
- GA4 Measurement ID: G-93NK3C48R3
- GA4 Stream ID: 3954589560 (patrizia.aryton.pl)
- Google Ads Conversion ID (z HTML): AW-769585117 (Customer ID: brak dostępu)
- GTM Container ID: GTM-MDGSP8
- GTM Admin: brak dostępu (weryfikacja tagów przez analizę HTML + GA4)
- BigQuery dataset: aktywny (potwierdzony w poprzednim audycie 2026-04-03)
- BDOS alias: brak dostępu
- CMP (Consent Management Platform): brak zewnętrznego dostawcy — własna implementacja Consent Mode v2 (psgdpr/PrestaShop moduł GDPR), brak widocznego bannera

## Stack MarTech wykryty z HTML
- GTM-MDGSP8 (jeden kontener)
- GA4 G-93NK3C48R3 — **DUALNIE**: hardcoded `gtag()` w HTML + przez GTM
- Google Ads AW-769585117 (conversion tag)
- Meta Pixel 268133950519975 (z server-side tracking przez AJAX → `/module/facebookconversiontrackingplus/`)
- eDrone (email marketing / personalizacja, appId: `626a8093e4423`)
- Klarna (płatności)
- DPD (logistyka, iframe widget)
- psgdpr (PrestaShop GDPR moduł — consent logging)
- Brak: Universal Analytics (UA) — usunięty ✅
- Platforma: **PrestaShop**

## Consent Mode v2
```javascript
gtag('consent', 'default', {
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'analytics_storage': 'denied',
  'wait_for_update': 500
})
```
Wszystkie kategorie domyślnie `denied`. Brak widocznego bannera CMP w HTML — psgdpr może obsługiwać consent, wymaga weryfikacji na żywej stronie.

## Zakres audytu
- Sekcje: pełny (1–10)
- Sekcje z ograniczonym dostępem: Google Ads Customer ID — sekcja 6, 8, 10 będą oparte tylko na danych GA4 + HTML
- Priorytety: duplikacja purchase events, ePrivacy, jakość danych e-commerce, UTM

## Poprzedni audyt
- Data: 2026-04-03 | Wynik: 62/138 pkt (45%) ❌ Krytyczny
- Wykryte problemy: duplikacja purchase (ratio 3.53x), malformed transactionId, add_shipping_info > begin_checkout anomalia, fragmentacja Meta, brak bannera CMP
- Nowy audyt: weryfikacja czy problemy zostały naprawione + pełny zakres sekcji 1–10
