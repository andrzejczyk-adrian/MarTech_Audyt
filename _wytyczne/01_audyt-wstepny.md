# Sekcja 1 — Audyt Wstępny

## Meta
sekcja_id: 1
sekcja_nazwa: Audyt Wstępny
dotyczy_domyslnie: all
agent_etap: 3
zrodla_danych: DevTools (Network+Console), TagHound, Tag Assistant, GA4 Panel, GTM Panel, kod HTML strony
ostatnia_aktualizacja: 2026-04
wersja: 2.0

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 1.1 | Adnotacje w GA4 | Wysoki | all | GA4 → Admin → Adnotacje | Wpisy przy kluczowych zmianach, max co 3 miesiące | Brak adnotacji przez >3 miesiące | 3 | |
| 1.2 | Kolejność skryptów HTML | Wysoki | all | Ctrl+U → head → sprawdź kolejność skryptów | Kolejność: 1.Consent DL → 2.DataLayer → 3.GTM → 4.inne | Jakikolwiek piksel przed GTM lub przed consent | 3 | |
| 1.3 | Przegląd wybranych podstron | Wysoki | all | DevTools F12 → Console + Network → 5 podstron: główna, kategoria, produkt, koszyk, potwierdzenie | 0 krytycznych błędów JS, requesty GA4 ze statusem 2xx | Błędy JS, requesty GA4 4xx/5xx, zduplikowane page_view | 3 | |
| 1.4 | Google Tag Assistant | Niski | all | tagassistant.google.com → homepage i 2-3 podstrony | 0 błędów i ostrzeżeń dla tagów GA4/Ads | Tagi oznaczone błędem krytycznym | 1 | |
| 1.5 | TagHound | Wysoki | all | TagHound dla: homepage, kategoria, produkt, koszyk | Brak zduplikowanych tagów, tagi na właściwych stronach | Tagi ładowane wielokrotnie lub brakujące na kluczowych stronach | 3 | |
| 1.6 | Consent Mode — wstępna weryfikacja | Średni | all | Incognito → sprawdź czy pojawia się baner zgody | Baner z opcjami personalizacji zgód | Brak banera zgody | 2 | Pełny audyt w Sekcji 2 |
| 1.7 | Brak starych kodów UA | Niski | all | DevTools → Network → filtruj analytics.js lub UA- | 0 requestów do analytics.js | Aktywne requesty analytics.js lub UA- w kodzie | 1 | |
| 1.8 | DataLayer — poprawność | Wysoki | all | DevTools → Console → wpisz dataLayer | Obiekt istnieje, push-e mają klucz event, poprawny JSON | dataLayer is not defined, puste tablice, brak event | 3 | |
| 1.9 | DataLayer GA4 — struktura e-commerce | Wysoki | ecommerce | DevTools → Console → ecommerce w DL → sprawdź items[] | items[] zawiera: item_id, item_name, price, quantity | Brak ecommerce, items[] puste, brak price lub item_id | 3 | |
| 1.10 | Google Analytics 360 | Wysoki | all | GA4 Admin → Połączone usługi → licencja 360 | Poprawnie skonfigurowane | ➖ Nie dotyczy jeśli klient bez 360 | 3 | ➖ jeśli brak 360 |
| 1.11 | Remarketing Google Ads | Średni | ads | DevTools → Network → googleadservices.com lub googlesyndication.com | Remarketing aktywny i podpięty do Ads | Brak przy aktywnych kampaniach display | 2 | |
| 1.12 | Konwersje Google Ads w GTM | Wysoki | ads | GTM → Tagi → Google Ads Conversion Tracking | Tag konwersji obecny i aktywny | Brak tagu konwersji Ads w GTM | 3 | |
| 1.13 | Meta (Facebook) Pixel | Wysoki | all | DevTools → Network → facebook.com/tr lub connect.facebook.net | Pixel Meta wywołuje się poprawnie | Brak przy aktywnych kampaniach Meta | 3 | ➖ jeśli brak kampanii Meta |
| 1.14 | Meta — API konwersji (CAPI) | Wysoki | all | GTM → Tagi → Facebook Conversions API lub sGTM client | CAPI skonfigurowane | Brak CAPI przy aktywnych kampaniach Meta | 3 | ➖ jeśli brak kampanii Meta |
| 1.15 | LinkedIn Insight Tag | Wysoki | all | DevTools → Network → snap.licdn.com | Tag LinkedIn aktywny | ➖ jeśli brak kampanii LinkedIn | 3 | ➖ jeśli nie dotyczy |
| 1.16 | Pinterest Tag | Wysoki | all | DevTools → Network → ct.pinterest.com | Tag Pinterest aktywny | ➖ jeśli brak kampanii Pinterest | 3 | ➖ jeśli nie dotyczy |
| 1.17 | Yandex Metrica | Wysoki | all | DevTools → Network → mc.yandex.ru | Brak lub aktywny jeśli wymagany | ➖ zazwyczaj nie dotyczy | 3 | ➖ jeśli nie dotyczy |
| 1.18 | Microsoft Clarity | Wysoki | all | DevTools → Network → clarity.ms | Clarity aktywne jeśli wdrożone | ➖ jeśli brak | 3 | ➖ jeśli nie dotyczy |
| 1.19 | Bing/Microsoft Ads | Średni | ads | DevTools → Network → bat.bing.com | Tag Bing aktywny jeśli używają | ➖ jeśli brak | 2 | ➖ jeśli nie dotyczy |
| 1.20 | TikTok Pixel | Wysoki | all | DevTools → Network → analytics.tiktok.com | Pixel TikTok aktywny | ➖ jeśli brak | 3 | ➖ jeśli nie dotyczy |
| 1.21 | Hotjar | Wysoki | all | DevTools → Network → static.hotjar.com | Hotjar aktywny jeśli wdrożony | ➖ jeśli brak | 3 | ➖ jeśli nie dotyczy |
| 1.22 | Criteo | Średni | all | DevTools → Network → static.criteo.net | Tag Criteo aktywny | ➖ jeśli brak | 2 | ➖ jeśli nie dotyczy |
| 1.23 | RTB House | Średni | all | DevTools → Network → creativecdn.com | Tag RTB House aktywny | ➖ jeśli brak | 2 | ➖ jeśli nie dotyczy |
| 1.24 | Allegro Ads | Średni | all | DevTools → Network → pixel.allegro.pl | Pixel Allegro aktywny | ➖ jeśli brak | 2 | ➖ jeśli nie dotyczy |

> **Zasada:** NIE zakładaj z góry co jest wdrożone. Raportuj tylko wykryte narzędzia. Nieznalezione → ➖ Nie dotyczy.

---

## Notatki rozszerzone (tylko dla agenta)

### 1.2 — Prawidłowa kolejność skryptów
Sprawdź czy struktura w `<head>` wygląda tak:
1. `gtag('consent', 'default', {...})` — Consent DataLayer
2. `window.dataLayer = window.dataLayer || []` — DataLayer init
3. `<!-- Google Tag Manager -->` snippet — GTM
4. Inne tagi (tylko jeśli absolutnie konieczne hardcoded)

Platformy e-commerce (Shoper, WooCommerce, Shopify, PrestaShop) często wstrzykują własny kontener GTM lub snippet GA4 — weryfikuj liczbę aktywnych tagów GA4.

### 1.9 — Poprawna struktura DataLayer e-commerce
```js
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: '12345',  // string, nie może zawierać & = spacji
    value: 299.00,             // number, nie string
    currency: 'PLN',
    items: [{
      item_id: 'SKU123',
      item_name: 'Nazwa produktu',
      price: 299.00,
      quantity: 1
    }]
  }
})
```

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| all (zawsze) | 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 | 19 pkt |
| ecommerce | 1.9 | +3 pkt |
| ads | 1.11, 1.12 | +5 pkt |
| integracje (jeśli wykryte) | 1.13–1.24 | +27 pkt max |
| **MINIMUM (tylko all)** | | **19 pkt** |
| **TYPOWY (all + ecomm + ads + 3 integracje)** | | **~36 pkt** |
