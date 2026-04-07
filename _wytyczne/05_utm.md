# Sekcja 5 — UTM

## Meta
sekcja_id: 5
sekcja_nazwa: UTM — standaryzacja i kompletność
dotyczy_domyslnie: all
agent_etap: 3
zrodla_danych: 01_raw-data.md (sekcja źródła ruchu), panel Google Ads, panel Meta Ads
ostatnia_aktualizacja: 2026-04
wersja: 2.0

---

## Kryteria

| id | kryterium | priorytet | dotyczy | jak_sprawdzic | warunek_ok | czerwona_flaga | max_pkt | uwagi |
|----|-----------|-----------|---------|---------------|------------|----------------|---------|-------|
| 5.1 | Standaryzacja UTM | Niski | all | raw-data → policz warianty source/medium per kanał | Max 2 warianty na kanał | 5+ wariantów dla jednego kanału | 1 | |
| 5.2 | Google Ads — UTM source/medium | Wysoki | ads | raw-data → sprawdź czy google/cpc widoczne dla kampanii Ads | 100% kampanii Ads z source=google medium=cpc | Kampanie Ads jako direct lub (not set) | 3 | |
| 5.3 | Google Ads — UTM kampanii | Wysoki | ads | raw-data → utm_campaign → nazwy kampanii widoczne w GA4 | utm_campaign wypełnione nazwami kampanii | Brak utm_campaign lub {campaignid} zamiast nazwy | 3 | |
| 5.4 | Meta/Facebook Ads — UTM | Wysoki | all | raw-data → sprawdź czy facebook/cpc lub paid-social widoczne | Kampanie Meta widoczne z UTM w GA4 | Ruch Meta jako organic social lub direct | 3 | |
| 5.5 | Meta Ads — ID kampanii w UTM | Średni | all | raw-data → utm_content lub utm_id → czy zawiera ID kampanii/reklamy | ID Meta widoczne dla zaawansowanych analiz | Brak ID — niemożliwe powiązanie z raportami Meta | 2 | |
| 5.6 | Organiczne social media — UTM | Średni | all | raw-data → sprawdź czy posty organiczne mają UTM | Ruch z postów oznaczony UTM | Ruch z postów organicznych jako direct | 2 | |
| 5.7 | Email marketing — UTM | Średni | all | raw-data → sprawdź czy email/newsletter widoczny | Kampanie emailowe z UTM w GA4 | Ruch z emaili jako direct lub referral (webmaile) | 2 | |
| 5.8 | Wizytówka Google — UTM | Średni | all | raw-data → sprawdź czy ruch z GMB ma UTM | Wizytówka z UTM lub oznaczona gmb | Ruch z wizytówki jako organic bez identyfikacji | 2 | |
| 5.9 | Linki SEO sponsorowane — UTM | Średni | all | raw-data → sprawdź linki zewnętrzne SEO | UTM na linkach sponsorowanych | Linki bez UTM = ruch jako referral nieidentyfikowany | 2 | |
| 5.10 | Pozostałe kanały płatne — UTM | Średni | all | raw-data → sprawdź inne kanały płatne | Każdy kanał płatny widoczny z UTM | Kanały płatne jako direct lub (not set) | 2 | |

---

## Notatki rozszerzone (tylko dla agenta)

### 5.1 — Jak wykryć fragmentację UTM
Z `01_raw-data.md` sekcja "Źródła ruchu" — sprawdź ile wariantów source/medium reprezentuje ten sam kanał:

```
Meta/Facebook — warianty do sprawdzenia:
  ✅ facebook / cpc           (pożądane — kampanie z UTM)
  ⚠️ facebook.com / referral  (kliknięcia bez UTM)
  ⚠️ m.facebook.com / referral (mobile bez UTM)
  ⚠️ l.facebook.com / referral (link preview)
  ⚠️ lm.facebook.com / referral

Google Ads — oczekiwane:
  ✅ google / cpc
  ✅ google / organic (naturalny)
```

### Oczekiwane source/medium per kanał

| Kanał | source | medium |
|-------|--------|--------|
| Google Ads | google | cpc |
| Meta Ads | facebook | cpc lub paid-social |
| TikTok Ads | tiktok | cpc lub paid-social |
| Email | {nazwa_narzedzia} | email |
| Organiczne social | facebook / instagram / linkedin | social |
| Wizytówka Google | google | gmb |

---

## Scoring

| Typ | Kryteria | Max pkt |
|-----|----------|---------|
| all (zawsze) | 5.1, 5.4, 5.5, 5.6, 5.7, 5.8 | 12 pkt |
| ads | 5.2, 5.3 | +6 pkt |
| **MINIMUM (all)** | | **12 pkt** |
| **Z ADS** | | **18 pkt** |
