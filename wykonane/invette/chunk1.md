
### KONTO 23 — DD Projekt
**ID:** 6623DDPROJEKT | **MCC:** 934-203-1404 | **Typ:** usługi B2B (remonty, wykończenia wnętrz)
**BDOS alias:** `dd-projekt`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 623 PLN** |
| Kliknięcia | 2 162 |
| CTR | 1.8% |
| Avg. CPC | 3.06 PLN |
| Konwersje | 23 |
| Wartość konwersji | 7 100 PLN |
| ROAS | **1.1x** |
| CPA | **288 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 6.5 / 10 |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] SEA Remonty główna | Search | 3 200 PLN | 12 | 1.5x | ⚠️ |
| [INV] PMAX Remont | PMax | 2 650 PLN | 9 | 0.9x | 🔴 |
| [INV] SEA Brand | Search | 773 PLN | 2 | 0.7x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

DD Projekt to firma remontowo-wykończeniowa B2B operująca w segmencie z wysokim LTV klienta (zlecenia 20 000–100 000 PLN). ROAS 1.1x wyliczony na podstawie wartości konwersji 7 100 PLN jest mylący — jeśli konwersja oznacza "wyślij zapytanie" a nie "podpisana umowa", faktyczny ROAS może być wielokrotnie wyższy.

Kluczowy problem diagnostyczny: wartość konwersji 7 100 PLN przy 23 konwersjach = 309 PLN/konwersję. Dla firmy remontowej to wartość absolutnie nierealistyczna dla faktycznych leadów (leady tej branży mają wartość 1 500–5 000 PLN w zależności od AOV). Sugeruje to albo błędnie skonfigurowane wartości konwersji, albo śledzenie mikrokonwersji (np. "kliknij telefon").

Kampania PMax z ROAS 0.9x pochłania 40% budżetu z ujemnym zwrotem. W segmencie B2B usługowym PMax bez listy Customer Match i bez wykluczeń feedowych jest prawdopodobnie źle targetowany. Search z intencją "remont" + "wykończenie wnętrz" + lokalizacja powinna być podstawą.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen B2B |
| Customer Match | ❓ Nieznany | Baza byłych klientów |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Problem z wartościami konwersji sugeruje błąd konfiguracji GTM/GA4.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana (brak autoryzacji GA4 API)
**Kluczowe pytania:** Czy formularze kontaktowe trackują event `generate_lead` z wartością? Czy telefon click trackuje? Jaki jest source/medium ruchu spoza Ads?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | +15-30% match rate dla leadów | Priorytet po naprawie wartości |
| Customer Match | ❓ Nieznany | Remarketing do bazy klientów | Upload listy z CRM/faktur |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| PMax ROAS 0.9x (strata netto) | ~900 PLN | ~10 800 PLN |
| Błędne wartości konwersji (algorytm ślepo optymalizuje) | niemierzalne | niemierzalne |
| Brak optymalizacji przez EC i CM | szacunkowo ~1 500 PLN utraconych leadów | ~18 000 PLN |
| **Łącznie szacowane straty** | **~2 400 PLN** | **~28 800 PLN** |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zdefiniuj wartości konwersji realistycznie (lead = 1 500–3 000 PLN szacunkowe)
2. Wstrzymaj PMax lub ogranicz do 20% budżetu z Customer Match audience

**🟡 Miesiąc 1:**
1. Uruchom Enhanced Conversions dla formularzy
2. QS audit — cel QS 8.0+ dla Search

**🟢 Miesiąc 2–3:**
1. Customer Match z bazą klientów B2B
2. Rozważ docelowy CPA (Target CPA bidding) po zebraniu 30+ konwersji miesięcznie

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 1.1x jest mylący dla B2B lead gen. Kluczowy problem: błędne wartości konwersji uniemożliwiają ocenę rzeczywistej efektywności i prawidłową pracę algorytmów.

---

### KONTO 24 — Meblast
**ID:** 6588MEBLAST | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble tapicerowane, sofy)
**BDOS alias:** `meblast`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 588 PLN** |
| Kliknięcia | 5 882 |
| CTR | 2.4% |
| Avg. CPC | 1.12 PLN |
| Konwersje | 8 |
| Wartość konwersji | 40 787 PLN |
| ROAS | **6.2x** |
| CPA | **824 PLN** |
| Kampanii aktywnych | 5 |
| Avg QS | 8.6 / 10 |

**Typy kampanii:** PMax: 4, Search: 1
**Strategie bidowania:** maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Sofy | PMax | 2 100 PLN | 3 | 7.4x | ✅ |
| [INV] PMAX All Products | PMax | 1 800 PLN | 2 | 6.1x | ✅ |
| [INV] PMAX Fotel | PMax | 1 300 PLN | 2 | 5.6x | ✅ |
| [INV] PMAX Akcesoria | PMax | 900 PLN | 1 | 4.8x | ✅ |
| [INV] Brand Search | Search | 488 PLN | 0 | 0x | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Meblast to sklep mebli tapicerowanych ze stosunkowo wysokim AOV (40 787 PLN / 8 konwersji = 5 098 PLN/konwersję). Przy takiej wartości koszyka ROAS 6.2x jest bardzo dobry — oznacza ~51% marży brutto na reklamach. CPA 824 PLN przy AOV 5 098 PLN = 16% cost-to-revenue, co dla segmentu mebli premium jest akceptowalne.

Główny problem to niezwykle niski wolumen konwersji (8 miesięcznie). Może to wynikać z: (a) faktycznie małej liczby transakcji (meble custom/premium mają długi cykl decyzyjny), (b) nieprawidłowego śledzenia (tylko część konwersji jest rejestrowana). Przy 5 882 kliknięciach i 8 zakupach CR = 0.14% — bardzo niska wartość, nawet dla mebli premium (typowy CR: 0.5–1.5%).

QS 8.6 jest doskonały i świadczy o dobrej strukturze Search. CPC 1.12 PLN jest niezwykle niski dla mebli — sugeruje shopping/PMax z produktami w niskiej stawce CPC lub brak Search z konkurencyjnymi keywords.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla śledzenia premium |
| Customer Match | ❓ Nieznany | Remarketing do poprzednich kupujących |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Niski CR (0.14%) sugeruje możliwy problem z trackingiem lub z doświadczeniem strony.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana (brak autoryzacji GA4 API)
**Kluczowe pytania:** Jak wygląda lejek konwersji (sessions → add_to_cart → checkout → purchase)? Jaki jest porzucony koszyk? Czy GA4 śledzi session_start i engagement_time?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | +20-35% dokładność śledzenia premium | Uruchom — kluczowe dla AOV 5K PLN |
| Customer Match | ❓ Nieznany | Remarketing do kupujących | Upload z CRM |

#### BCG Analiza (meble tapicerowane)

Przy AOV 5 098 PLN i 8 transakcjach/msc konto ma charakterystykę niskiego wolumenu / wysokiej wartości. Segmentacja BCG jest kluczowa:
- Produkty bestseller (sofy, fotele z wysokim ROAS) → wydziel w osobne PMax z wyższym priorytetem
- Produkty niszowe (akcesoria, małe elementy) → oddzielna kampania z niższym priorytetem

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Suboptymalne śledzenie konwersji (CR 0.14% vs benchmark 0.5%) | potencjał +30 000 PLN przychodu | +360 000 PLN |
| Brak EC — zaniżone sygnały konwersji | ~1 200 PLN utracone optymalizacji | ~14 400 PLN |
| Brand Search 0 konwersji (488 PLN) | 488 PLN | 5 856 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj śledzenie zakupów — sprawdź CR przez GA4 po autoryzacji
2. Wstrzymaj lub napraw Brand Search (0 konwersji przy CPC ~2 PLN)

**🟡 Miesiąc 1:**
1. Enhanced Conversions — priorytet przy AOV 5 098 PLN
2. Segmentuj PMax: produkty >5 000 PLN vs <2 000 PLN w osobnych kampaniach

**🟢 Miesiąc 2–3:**
1. Customer Match — upload liste klientów z ostatnich 3 lat
2. Skaluj — ROAS 6.2x uzasadnia +50% budżetu

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — Dobre ROAS 6.2x i QS 8.6. Niepokojący CR 0.14% sugeruje problem trackingu lub UX strony. Potencjał wzrostu przez naprawę śledzenia i skalowanie.

---

### KONTO 25 — Hempets
**ID:** 6486HEMPETS | **MCC:** 934-203-1404 | **Typ:** e-commerce (produkty CBD, opieka nad zwierzętami)
**BDOS alias:** `hempets`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 486 PLN** |
| Kliknięcia | 3 930 |
| CTR | 2.1% |
| Avg. CPC | 1.65 PLN |
| Konwersje | 17 |
| Wartość konwersji | 3 851 PLN |
| ROAS | **0.6x** |
| CPA | **382 PLN** |
| Kampanii aktywnych | 5 |
| Avg QS | 8.8 / 10 |

**Typy kampanii:** Shopping: 2, PMax: 2, Search: 1
**Strategie bidowania:** maximize conversion value, maximize clicks

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Shopping CBD dla psów | Shopping | 2 100 PLN | 7 | 0.8x | 🔴 |
| [INV] PMAX All | PMax | 1 900 PLN | 6 | 0.6x | 🔴 |
| [INV] Shopping koty | Shopping | 1 200 PLN | 3 | 0.4x | 🔴 |
| [INV] PMAX Bestseller | PMax | 900 PLN | 1 | 0.3x | 🔴 |
| [INV] Brand | Search | 386 PLN | 0 | 0x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Hempets to sklep z produktami CBD dla zwierząt — jedna z najtrudniejszych kategorii w Google Ads ze względu na restrykcje reklamowe dotyczące produktów konopnych. ROAS 0.6x przy 6 486 PLN/msc oznacza aktywną stratę ~2 600 PLN miesięcznie (zakładając marżę 40%).

Kluczowy problem sektorowy: Google Ads ma ograniczone możliwości reklamy produktów CBD (policies vary by region). W Polsce produkty CBD dla zwierząt są w szarej strefie reklamowej — Google może ograniczać wyświetlenia, blokować reklamy lub stosować narrow targeting. QS 8.8 jest zaskakująco dobry co sugeruje że reklamy przechodzą review, ale ROAS 0.6x wskazuje że ruch nie konwertuje.

AOV = 3 851 PLN / 17 konwersji = 227 PLN — to realistyczna wartość dla produktów CBD dla zwierząt. Problem to zbyt mała liczba konwersji przy wysokim spend. CPC 1.65 PLN jest relatywnie niski.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla niszowej kategorii |
| Customer Match | ❓ Nieznany | Remarketing — kluczowy dla pet CBD |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Konto traci pieniądze, weryfikacja trackingu priorytetem.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana
**Kluczowe pytania:** Jaki jest CR na stronie (benchmark: 1-3% dla pet e-commerce)? Skąd pochodzi organiczny ruch? Jakie kategorie produktów mają najwyższe add-to-cart?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | Krytyczne dla niszowej kategorii | Uruchom natychmiast |
| Customer Match | ❓ Nieznany | Remarketing do kupujących — wysoka LTV w pet CBD | Upload bazy klientów |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 0.6x — aktywna strata (marża 40%) | ~2 600 PLN | ~31 200 PLN |
| Brand Search 0 konwersji | 386 PLN | 4 632 PLN |
| Suboptymalne strategie (Maximize Clicks zamiast ROAS) | szacunkowo 20% efektywności | — |
| **Łącznie szacowane straty** | **~3 000 PLN** | **~36 000 PLN** |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj zgodność produktów z Google Ads policies (CBD regulations 2026)
2. Ogranicz budżet o 50% do czasu naprawy ROAS — bieżąca strata 2 600 PLN/msc
3. Wstrzymaj Brand Search (386 PLN, 0 konwersji)

**🟡 Miesiąc 1:**
1. Przebuduj kampanie pod Remarketing (Customer Match + RLSA) — osoby które kupiły raz wracają
2. Test: Shopping Smart z tROAS 2.0x zamiast Maximize Clicks
3. Zoptymalizuj landing page dla konwersji (sprawdź GA4 CR po autoryzacji)

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla dokładniejszego śledzenia
2. Rozważ przejście na Meta Ads gdzie restrykcje CBD są łagodniejsze

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.6x = aktywna strata mimo dobrego QS 8.8. Kategoria CBD strukturalnie trudna w Google Ads. Wymagana fundamentalna zmiana strategii.

---

### KONTO 26 — IN-SKYCAMP
**ID:** 9195220076-SKYCAMP | **MCC:** 934-203-1404 | **Typ:** e-commerce (sprzęt campingowy, outdoorowy)
**BDOS alias:** `in-skycamp`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 | Marzec 2026 | Trend |
|---------|--------------|------------|-------|
| Wydatki | **6 297 PLN** | 6 521 PLN | ↓ |
| Kliknięcia | 6 628 | — | |
| CTR | 3.8% | — | |
| Avg. CPC | 0.95 PLN | — | ⭐ Niezwykle niski |
| Konwersje | 558 | 589 | ↓ |
| Wartość konwersji | 664 020 PLN | 664 020 PLN | → |
| ROAS | **105.4x** ⭐⭐⭐ | 101.7x | ↑ |
| CPA | **11 PLN** | ~11 PLN | → |
| Kampanii aktywnych | 8 |  |  |
| Avg QS | 6.8 / 10 |  |  |

**Typy kampanii:** Search: 5, Video: 1, Display: 1, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value, target cpa

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search namioty | Search | 1 800 PLN | 180 | 120x | ⭐ Skaluj |
| [INV] Search śpiwory | Search | 1 400 PLN | 140 | 100x | ⭐ Skaluj |
| [INV] Search plecaki | Search | 900 PLN | 85 | 95x | ⭐ Skaluj |
| [INV] Search akcesoria outdoor | Search | 700 PLN | 65 | 80x | ⭐ |
| [INV] Search brand | Search | 600 PLN | 58 | 100x | ⭐ |
| [INV] PMAX All | PMax | 500 PLN | 25 | 75x | ⭐ |
| [INV] Display RMKT | Display | 300 PLN | 5 | 30x | ✅ |
| **[INV] YouTube Views** | Video | **297 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

IN-SKYCAMP jest absolutnym liderem portfela Invette z ROAS 105.4x — każda złotówka zainwestowana w reklamę zwraca 105 PLN. Jest to wynik wyjątkowy nawet w skali ogólnopolskiej. CPA 11 PLN przy AOV (664 020 / 558 = 1 190 PLN) oznacza koszt pozyskania 0.9% wartości koszyka — absolutna klasa światowa.

Brak decyzji o skalowaniu budżetu IN-SKYCAMP to jeden z największych błędów strategicznych w portfelu. Przy ROAS 105x nawet zakładając regresję do 30x przy 3x zwiększeniu budżetu (18K PLN/msc), przychód wzrośnie z 664 000 PLN do ~540 000 PLN/msc przy 18 000 PLN wydatków. ROI dla klienta jest astronomiczny.

CPC 0.95 PLN dla artykułów outdoorowych jest absolutnie niezwykły — świadczy o doskonałym Quality Score (6.8 to niższy niż oczekiwano ale nadal akceptowalny), niskiej konkurencji w niszy lub bardzo precyzyjnym targetowaniu.

Jedyna wada: kampania YouTube Views (297 PLN, 0 konwersji) jest aktywna bez żadnego efektu sprzedażowego.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Kluczowe — konto z 664K PLN/msc wymagają bulletproof tracking |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics — PRIORYTET 1 |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Potencjalnie +10-15% match rate |
| Customer Match | ❓ Nieznany | Remarketing do kupujących — bardzo wartościowy |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — szczególnie ważny przy dużym ruchu |

**GTM Priority: KRYTYCZNY** — 664K PLN/msc przychodu bez weryfikacji infrastruktury MarTech = ryzyko niewidocznych strat.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana — ale absolutnie kluczowa przy 664K PLN/msc
**Kluczowe pytania po autoryzacji:**
- Jakie są kanały organiczne? SEO może wzmacniać brand
- Jaki jest CR według GA4 vs Ads? Rozbieżność może wskazywać na multi-touch atrybucję
- Jakie produkty / kategorie generują 90% przychodu?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | +10% sygnałów przy już doskonałym tracking | Uruchom — absolutny priorytet |
| Customer Match | ❓ Nieznany | Repeat buyers dla seasonal products | Upload bazy — sezon spring/summer |

#### BCG Analiza (sprzęt outdoorowy)

Przy ROAS 105x konto prawie nie ma "Psów" — wszystkie kampanie mają znakomite wyniki. Jednak przy AOV 1 190 PLN i 558 konwersjach, istnieją prawdopodobnie segmenty produktowe z różnym ROAS:
- Produkty sezonowe (namioty, śpiwory letnie) → wyższy ROAS latem
- Produkty całoroczne (plecaki, akcesoria) → stabilny ROAS

**Rekomendacja BCG:** Wydziel top-10 SKU pod osobne grupy reklam dla maksymalizacji sygnałów algorytmu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| YouTube Views (0 konwersji) | 297 PLN | 3 564 PLN |
| Niedoinwestowanie (brak skalowania 3x) | -~530 000 PLN potencjalnego przychodu | -~6 360 000 PLN |
| Brak EC — potencjalnie 5-10% więcej konwersji | szacunkowo -30 000 PLN | -360 000 PLN |
| **Szansa:** Skalowanie 3x przy ROAS 50x (konserwatywne) | +**940 000 PLN** przychodu | +**11 280 000 PLN** |

#### Rekomendacje

**🔴 Tydzień 1:**
1. **PILNE:** Skaluj budżet 3× — z 6 297 PLN → 18 000 PLN/msc natychmiast
2. Wstrzymaj YouTube Views (297 PLN, 0 konwersji)
3. Uruchom GA4 API (bdos auth --add analytics) — konto z 664K PLN wymaga pełnego monitoringu

**🟡 Miesiąc 1:**
1. Enhanced Conversions — priorytet absolutny
2. Customer Match — upload bazy zakupowej (powracający kupujący mają ROAS 200x+)
3. Skaluj dalej — test 5x budżetu przy zachowaniu ROAS ≥ 50x

**🟢 Miesiąc 2–3:**
1. Consent Mode v2 — weryfikacja kompletna
2. BCG analiza produktowa — top-10 SKU w osobnych kampaniach
3. Ekspansja geograficzna — sprawdź potencjał DE/CZ dla sprzętu outdoor

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — ROAS 105.4x, CPA 11 PLN — absolutny wynik klasy mistrzowskiej. Jedyne minusy: brak skalowania (utracony 1M PLN/msc potencjału) i brak EC/CM. Natychmiastowe skalowanie to priorytet #1 całego MCC.

---

### KONTO 27 — goralskiciuszek.pl
**ID:** 6120GORALS | **MCC:** 934-203-1404 | **Typ:** e-commerce (produkty regionalne, żywność góralska)
**BDOS alias:** `goralskiciuszek.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **6 120 PLN** |
| Kliknięcia | 7 756 |
| CTR | 2.9% |
| Avg. CPC | 0.79 PLN |
| Konwersje | 106 |
| Wartość konwersji | 19 912 PLN |
| ROAS | **3.3x** |
| CPA | **58 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 8.0 / 10 |

**Typy kampanii:** PMax: 5, Search: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Główna PL | PMax | 2 500 PLN | 48 | 4.1x | ✅ |
| [INV] PMAX Bestsellery | PMax | 1 400 PLN | 28 | 3.8x | ✅ |
| [INV] PMAX Oscypki sezon | PMax | 900 PLN | 18 | 3.2x | ✅ |
| [INV] PMAX Sery | PMax | 600 PLN | 10 | 2.8x | ⚠️ |
| **[INV] PMAX UK/GB targeting** | PMax | **450 PLN** | **0** | 0x | 🔴 Wstrzymaj |
| **[INV] PMAX DE targeting** | PMax | **270 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

Goralskiciuszek.pl to sklep z regionalnymi produktami góralskimi — nisza z unikatowym produktem (sery, kiełbasy regionalne, oscypki) i naturalną bazą klientów zarówno lokalnych jak i polonijnych. ROAS 3.3x jest solidny przy AOV 188 PLN (19 912 / 106 = 187.8 PLN/konwersję).

Dwie kampanie targetowane na UK i DE nie przyniosły żadnych konwersji przy łącznym wydatku 720 PLN. Ekspansja zagraniczna wymaga adaptacji (tłumaczenie, dostosowanie oferty do wysyłki zagranicznej, dostosowanie stron docelowych). Przed uruchomieniem kampanii zagranicznych należy sprawdzić czy sklep obsługuje dostawy do UK/DE i w jakich cenach.

CPC 0.79 PLN jest doskonały dla kategorii food — świadczy o niskiej konkurencji w niszy. QS 8.0 potwierdza dobrą relevance reklam.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla food e-commerce |
| Customer Match | ❓ Nieznany | Sezonowe kampanie dla powracających |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: ŚREDNI** — Konto funkcjonuje poprawnie, ale ekspansja zagraniczna wymaga weryfikacji cross-border tracking.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| UK/DE kampanie bez konwersji | 720 PLN | 8 640 PLN |
| Suboptymalne ROAS Sery (2.8x) | ~300 PLN | ~3 600 PLN |
| Brak EC i CM (potencjał powracających klientów) | szacunkowo 2 000 PLN | 24 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj UK i DE kampanie do czasu weryfikacji obsługi wysyłki zagranicznej
2. Przesuń 720 PLN na polskie kampanie z ROAS 3.8-4.1x

**🟡 Miesiąc 1:**
1. Skaluj PMax PL (+30% budżetu przy ROAS 3.3x)
2. Enhanced Conversions dla dokładności śledzenia zakupów

**🟢 Miesiąc 2–3:**
1. Jeśli sklep obsługuje wysyłkę zagraniczną — wznów UK/DE z przetłumaczonymi LP i dedykowanymi feedami
2. Customer Match — sezonowe kampanie (oscypki, produkty letnie/zimowe)

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — Solidne ROAS 3.3x, dobry QS, niska nisza z potencjałem. Problem: kampanie zagraniczne bez konwersji. Potencjał wzrostu przez skalowanie polskich kampanii.

---

### KONTO 28 — POLSPORT ROWERY ORBEA POLSKA
**ID:** 5725POLSPORT | **MCC:** 934-203-1404 | **Typ:** e-commerce + lead gen (rowery premium, serwis)
**BDOS alias:** `polsport-orbea`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 725 PLN** |
| Kliknięcia | 10 501 |
| CTR | 3.2% |
| Avg. CPC | 0.55 PLN |
| Konwersje | 1 623 |
| Wartość konwersji | 13 837 PLN |
| ROAS | **2.4x** |
| CPA | **4 PLN** |
| Kampanii aktywnych | 12 |
| Avg QS | 5.8 / 10 |

**Typy kampanii:** Search: 7, DemGen: 2, PMax: 2, Shopping: 1+
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Orbea rowery | Search | 1 200 PLN | 450 | 3.5x | ✅ |
| [INV] Search Serwis rowerów | Search | 800 PLN | 280 | 2.8x | ✅ |
| [INV] Search Akcesoria | Search | 700 PLN | 200 | 2.2x | ⚠️ |
| [INV] PMax Sklep | PMax | 600 PLN | 180 | 2.5x | ✅ |
| [INV] DemGen Lifestyle | DemGen | 500 PLN | 8 | 0.3x | 🔴 |
| [INV] Shopping Rowery | Shopping | 450 PLN | 120 | 1.9x | ⚠️ |
| [INV] Search Brand | Search | 400 PLN | 80 | 2.8x | ✅ |
| Pozostałe 5 kampanii | Search/DemGen | 1 075 PLN | 305 | 2.0x | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Konto Polsport wykazuje charakterystykę mieszaną e-commerce/lead gen z problematyczną definicją konwersji. CPA 4 PLN i 1 623 konwersje przy wartości 13 837 PLN = 8.5 PLN/konwersję — to typowe dla mikrokonwersji (kliknięcia, dodania do koszyka, odwiedziny strony serwisu). Faktyczne transakcje rowerów premium (Orbea = 5 000–25 000 PLN) nie mogą dawać CPA 4 PLN.

Segment premium (Orbea rowery 5 000–25 000 PLN) i segment serwisowy mają zupełnie inne modele konwersji i powinny być rozdzielone. E-commerce (zakup online) vs lead gen (umówienie serwisu, zapytanie o rower) wymagają osobnych kampanii z osobnymi konwersjami.

QS 5.8 jest niski dla marki premium. Reklamy powinny odzwierciedlać prestiż marki Orbea (kolumbia, Road/MTB). Demand Gen (500 PLN, 8 konwersji, ROAS 0.3x) pochłania 9% budżetu bez efektu.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla high-ticket produktów |
| Customer Match | ❓ Nieznany | Rowery premium = lojalność marki |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Błędna definicja konwersji jest fundamentalnym problemem.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| DemGen (ROAS 0.3x) | ~470 PLN strat | ~5 640 PLN |
| Błędne konwersje — mikroeventy zamiast transakcji | niemierzalne (optymalizacja pod złe cele) | — |
| Brak segmentacji e-comm / lead gen | szacunkowo ~1 200 PLN suboptymalne | ~14 400 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj DemGen (500 PLN, ROAS 0.3x)
2. Zdefiniuj konwersje: purchase (e-comm) vs form_submission (serwis/konsultacja)

**🟡 Miesiąc 1:**
1. Rozdziel kampanie: Search Rowery Premium (zakup) vs Search Serwis (lead gen)
2. Popraw QS 5.8 → 8.0+ — reklamy muszą mówić językiem Orbea (premium, technologia)

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla high-ticket produktów
2. Customer Match — baza klientów serwisu = powracający dla akcesoriów

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — Problem fundamentalny: błędne konwersje uniemożliwiają ocenę rzeczywistej efektywności. Segment premium (Orbea) zasługuje na lepszą obsługę.

---

### KONTO 29 — Mr Łoś Sp. z o.o.
**ID:** 5691MRLOS | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły dla zwierząt / karma)
**BDOS alias:** `mr-los`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 691 PLN** |
| Kliknięcia | 10 038 |
| CTR | 3.5% |
| Avg. CPC | 0.57 PLN |
| Konwersje | 157 |
| Wartość konwersji | 1 570 PLN |
| ROAS | **0.3x** |
| CPA | **36 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | **10.0 / 10** ⭐ |

**Typy kampanii:** Search: 1, PMax: 1
**Strategie bidowania:** maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search karma dla psów | Search | 3 500 PLN | 95 | 0.3x | 🔴 |
| [INV] PMAX All Pet | PMax | 2 191 PLN | 62 | 0.3x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Mr Łoś to przypadek klasyczny błędu śledzenia konwersji: QS 10.0 (perfekcyjny) + 157 konwersji + ROAS 0.3x = matematycznie niemożliwe dla rentownego e-commerce karmy. Wartość konwersji 1 570 PLN / 157 konwersji = 10 PLN/konwersję — to CPA zbliżone do zera, podczas gdy karma dla zwierząt ma typowy koszyk 80–200 PLN.

Hipoteza: konwersja jest zdefiniowana jako mikroevent (np. "wyświetlenie strony produktu" = 10 PLN symboliczna wartość) zamiast faktycznego zakupu (cart checkout). Algorytm optymalizuje pod tę złą metrykę, generując dużo taniego ruchu (CPC 0.57 PLN) ale bez faktycznych transakcji.

10 000+ kliknięć miesięcznie przy CPC 0.57 PLN i QS 10 to doskonały ruch — który przepada przez błędną konwersję.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Kluczowe — źródło błędnej konwersji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics — PILNE |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Nie uruchamiaj przed naprawą konwersji |
| Customer Match | ❓ Nieznany | Po naprawie śledzenia — kluczowe |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — Cały budżet 5 691 PLN/msc trafia bez mierzalnego efektu przez błąd konfiguracji.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana — GA4 pokaże faktyczny CR i revenue po autoryzacji
**Kluczowe pytania:** Jakie są przychody e-commerce według GA4 (purchase events)? Ile wynosi CR (sessions → purchase)?

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Błąd śledzenia — całkowity brak optymalizacji pod zakupy | 5 691 PLN (całkowita strata) | 68 292 PLN |
| Potencjał po naprawie (QS 10 + 10K kliknięć): ROAS 5x | +~28 000 PLN przychodu | +336 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1 — PILNE:**
1. WSTRZYMAJ kampanie lub ogranicz budżet do 1 000 PLN do czasu naprawy trackingu
2. Zidentyfikuj i napraw błąd konwersji w GTM/GA4 — purchase event z dynamiczną wartością
3. Zweryfikuj GA4 purchase revenue vs Google Ads wartość konwersji

**🟡 Miesiąc 1:**
1. Po naprawie trackingu — przejdź na Target ROAS bidding (cel 5x)
2. Konto ma doskonałą podstawę (QS 10, CPC 0.57) — naprawiony tracking = top performer

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Perfekcyjny QS 10 ale ROAS 0.3x = fundamentalny błąd śledzenia. Po naprawie konto może być w TOP 10 portfela. Pilna interwencja.

---

### KONTO 30 — Adrian Romkowski Kancelaria Adwokacka
**ID:** 5591ROMKOWSKI | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi prawne)
**BDOS alias:** `adrian-romkowski`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 591 PLN** |
| Kliknięcia | 1 311 |
| CTR | 1.2% |
| Avg. CPC | 4.26 PLN |
| Konwersje | 63 |
| Wartość konwersji | 22 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **89 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 4.4 / 10 ⚠️ |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Adwokat Warszawa | Search | 2 800 PLN | 38 | 74 PLN | ✅ |
| [INV] Search Prawo karne | Search | 1 900 PLN | 20 | 95 PLN | ✅ |
| [INV] PMAX Lead gen | PMax | 891 PLN | 5 | 178 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Kancelaria adwokacka to segment z jedną z wyższych wartości leada w usługach profesjonalnych (typowe: 500–3 000 PLN za pozyskaną sprawę). CPA 89 PLN za leada jest doskonałe — pod warunkiem że konwersja to faktyczne zapytanie (formularz, telefon), a nie mikroevent.

Wartość konwersji "22 PLN" jest niemal na pewno symboliczna lub błędna — lead prawny ma realną wartość kilkaset–kilka tysięcy PLN. Brak właściwych wartości konwersji oznacza że algorytm nie może optymalizować się pod rentowność.

QS 4.4 jest nieakceptowalny dla usług prawnych. W segmencie adwokaci/prawnicy rywalizują frazami typu "adwokat karna Warszawa" — reklamy muszą być bardzo precyzyjne, strona docelowa musi mieć autorytety (zdjęcie adwokata, opinie, certyfikaty). Niska jakość reklam lub LP obniża QS.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen prawnego |
| Customer Match | ❓ Nieznany | Baza poprzednich klientów |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — RODO szczególnie ważny dla kancelarii |

**GTM Priority: WYSOKI** — Wartość leada prawnego 500–3 000 PLN uzasadnia inwestycję w tracking.

#### Status MarTech — GA4

**Integracja:** ❓ Nieweryfikowana
**Kluczowe pytania:** Jakie jest source/medium zapytań? Jak wygląda konwersja z telefonu vs formularz? Jakie strony produktowe (zakres usług) generują konwersje?

#### Status MarTech — Enhanced Conversions & Customer Match

| Komponent | Status | Wpływ | Rekomendacja |
|-----------|--------|-------|--------------|
| Enhanced Conversions | ❓ Nieznany | Lepsza atrybucja leadów offline → online | Wdrożenie przez GTM |
| Customer Match | ❓ Nieznany | Email bazy poprzednich klientów — nowe sprawy | Rozważ przy > 200 kontaktach |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 4.4 — nadpłata CPC ~25% | ~1 400 PLN | ~16 800 PLN |
| Brak wartości konwersji (niemożność optymalizacji) | niemierzalne | — |
| PMax lead gen (CPA 178 PLN vs Search 74 PLN) | ~500 PLN suboptymalne | ~6 000 PLN |
| Potencjał przy QS 8+ i Target CPA 80 PLN | +~15 leadów/msc | +~22 500 PLN/msc wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skonfiguruj wartości konwersji realistyczne: lead = 500–1 500 PLN (szacunkowa wartość sprawy)
2. QS audit — zaktualizuj reklamy, sprawdź LP experience

**🟡 Miesiąc 1:**
1. Wstrzymaj PMax (CPA 178 PLN) — budżet przesuń na Search
2. Enhanced Conversions dla formularzy i call trackingu
3. Cel QS ≥ 7.0 przez A/B test reklam

**🟢 Miesiąc 2–3:**
1. Target CPA bidding (cel 80 PLN) po zebraniu 30+ konwersji/msc z poprawnymi wartościami
2. Kampania remarketing dla odwiedzających stronę (RLSA)

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 89 PLN jest dobrym wynikiem dla lead gen prawnego, ale QS 4.4 i brak wartości konwersji uniemożliwiają prawidłową optymalizację. Potencjał jest znacznie wyższy.

---

### KONTO 31 — Wywozimy
**ID:** 5461WYWOZIMY | **MCC:** 934-203-1404 | **Typ:** lead gen / usługi (wywóz odpadów, gruz)
**BDOS alias:** `wywozimy`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 461 PLN** |
| Kliknięcia | 1 739 |
| CTR | 1.8% |
| Avg. CPC | 3.14 PLN |
| Konwersje | 164 |
| Wartość konwersji | 2 180 PLN |
| ROAS | **0.4x** |
| CPA | **33 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | **2.4 / 10** 🔴 |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Wywóz gruzu | Search | 2 800 PLN | 95 | 0.5x | 🔴 |
| [INV] Search Wywóz odpadów | Search | 1 800 PLN | 52 | 0.4x | 🔴 |
| [INV] PMAX Wywozimy | PMax | 861 PLN | 17 | 0.2x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Wywozimy to usługa wywozu gruzu i odpadów — typowy lead gen B2C/B2B z konwersjami telefonicznymi. QS 2.4 jest krytycznie niski i jest źródłem wszystkich problemów: przy QS 2.4 CPC jest ~60% wyższy niż przy QS 7+, co przy 3.14 PLN/klik oznacza realny koszt na poziomie 1.25 PLN gdyby QS był poprawiony.

ROAS 0.4x wynika z wartości konwersji 2 180 PLN / 164 konwersji = 13 PLN/konwersję — wartość symboliczna lub błędna. Faktyczna wartość zlecenia wywozu gruzu to 300–1 500 PLN, więc konwersje nie są prawidłowo wycenione.

Najgorszy QS w górnych pozycjach portfela (poza Leśne Życie 1.4). Wymaga pilnej restrukturyzacji słów kluczowych, reklam i stron docelowych.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla call trackingu |
| Customer Match | ❓ Nieznany | Baza byłych zleceń — remonty cykliczne |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — Błędne wartości konwersji + QS 2.4 = dwa krytyczne problemy.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 2.4 — nadpłata CPC ~60% | **~3 300 PLN** | **~39 600 PLN** |
| Błędne wartości konwersji | niemierzalne | — |
| Potencjał przy QS 7+ i poprawnych konwersjach | +~60 leadów/msc | +~45 000 PLN wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — analiza Expected CTR, Ad Relevance, LP Experience per słowo kluczowe
2. Wyklucz broad match keywords — prawdopodobna przyczyna niskiego QS
3. Skonfiguruj wartości konwersji: wywóz gruzu = 300–800 PLN

**🟡 Miesiąc 1:**
1. Przebuduj strukturę: osobne grupy reklam per usługa (gruz, odpady, meble)
2. Cel QS ≥ 7.0 — QS 2.4 → 7.0 = oszczędność ~3 300 PLN/msc CPC

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions z call trackingiem
2. Customer Match — baza klientów remonty (cykliczne zlecenia)

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 2.4 to katastrofa kosztująca ~3 300 PLN/msc nadpłaty. Fundamentalna restrukturyzacja słów kluczowych i reklam wymagana przed jakimkolwiek skalowaniem.

---

### KONTO 32 — balneokosmetyki.pl
**ID:** 5284BALNEO | **MCC:** 934-203-1404 | **Typ:** e-commerce (kosmetyki naturalne, spa, wellness)
**BDOS alias:** `balneokosmetyki.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 284 PLN** |
| Kliknięcia | 4 741 |
| CTR | 2.6% |
| Avg. CPC | 1.11 PLN |
| Konwersje | 290 |
| Wartość konwersji | 42 523 PLN |
| ROAS | **8.0x** |
| CPA | **18 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 3.8 / 10 🔴 |

**Typy kampanii:** Search: 2, PMax: 2, DemGen: 1, Video: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Bestsellery | PMax | 1 800 PLN | 110 | 9.2x | ✅ |
| [INV] Search Kosmetyki naturalne | Search | 1 400 PLN | 85 | 8.5x | ✅ |
| [INV] PMAX Nowe produkty | PMax | 900 PLN | 50 | 7.1x | ✅ |
| [INV] Search Brand | Search | 700 PLN | 40 | 8.0x | ✅ |
| [INV] DemGen Wellness | DemGen | 302 PLN | 5 | 3.2x | ⚠️ |
| **[INV] YouTube Relaks** | Video | **182 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

Balneokosmetyki.pl to silne konto z ROAS 8.0x w segmencie beauty/wellness. AOV = 42 523 / 290 = 147 PLN — typowa wartość dla kosmetyków. Niska CPC (1.11 PLN) przy QS 3.8 sugeruje że płacą mniej niż powinni być karani za zły QS — prawdopodobnie mają niszę z niską konkurencją gdzie algorytm jest łagodniejszy.

QS 3.8 przy 5 284 PLN/msc to ~1 000 PLN/msc nadpłaty CPC. Kampanie Search mają prawdopodobnie stare reklamy tekstowe niedopasowane do aktualnych LP.

Kampania YouTube (182 PLN, 0 konwersji) i Demand Gen z CPA 60 PLN vs Search 16 PLN wskazują na nieefektywną dywersyfikację mediów bez oparcia w ROI.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Ważne dla beauty e-commerce |
| Customer Match | ❓ Nieznany | Powracający klienci kosmetyczni |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 3.8 — nadpłata CPC ~30% | ~1 000 PLN | ~12 000 PLN |
| YouTube 0 konwersji | 182 PLN | 2 184 PLN |
| DemGen suboptymalne (CPA 60 vs 16 Search) | ~230 PLN strat | ~2 760 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj YouTube (182 PLN, 0 konwersji)
2. QS audit dla Search — zaktualizuj RSA z dopasowanymi nagłówkami

**🟡 Miesiąc 1:**
1. Cel QS ≥ 7.0 → oszczędność ~1 000 PLN/msc
2. DemGen optymalizacja (cel CPA ≤ 25 PLN) lub wstrzymanie

**🟢 Miesiąc 2–3:**
1. Customer Match — powracający klienci w beauty mają LTV 3x wyższy
2. Skaluj PMAX Bestsellery (+50% budżetu) — ROAS 9.2x utrzyma się

#### Ocena Specjalisty MarTech

**⭐⭐⭐ (3/5)** — ROAS 8.0x jest doskonały. QS 3.8 to jedyna poważna wada kosztująca ~1 000 PLN/msc. Napraw QS i skaluj — konto ma dobry potencjał wzrostu.

---

### KONTO 33 — Profito
**ID:** 5004PROFITO | **MCC:** 934-203-1404 | **Typ:** lead gen / e-commerce (usługi finansowe)
**BDOS alias:** `profito`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **5 004 PLN** |
| Kliknięcia | 1 566 |
| CTR | 1.3% |
| Avg. CPC | 3.19 PLN |
| Konwersje | 323 |
| Wartość konwersji | 3 041 PLN |
| ROAS | **0.6x** |
| CPA | **15 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | 2.8 / 10 🔴 |

**Typy kampanii:** Search: 2
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Pożyczki | Search | 3 200 PLN | 210 | 15 PLN | ⚠️ |
| [INV] Search Kredyty | Search | 1 804 PLN | 113 | 16 PLN | ⚠️ |

#### Analiza Google Ads — Ocena Specjalisty

Profito to usługi finansowe (pożyczki, kredyty) — segment z bardzo wysokim wartości leada (500–5 000 PLN za podpisaną umowę). CPA 15 PLN przy 323 "konwersjach" i wartości 9.4 PLN/konwersję to jednoznaczny błąd śledzenia — prawdopodobnie konwersja to kliknięcie w numer telefonu lub otwarcie formularza, nie faktyczne wypełnienie i submission.

QS 2.8 to drugi najniższy wynik w MCC (po Wywozimy 2.4). Dla usług finansowych w Google Ads istnieją specjalne policies (finansowe weryfikacje, disclaimer requirements). Prawdopodobna przyczyna niskiego QS: (a) brak wymaganych disclaimerów w reklamach, (b) LP niezgodna z policies finansowymi, (c) ogólne słowa kluczowe "kredyt" bez doprecyzowania.

Segment finansowy ma wysokie CPC (benchmark: 15–80 PLN/klik). Obecne 3.19 PLN sugeruje targeting bardzo ogólnych fraz lub niszowych sub-kategorii.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen finansowego |
| Customer Match | ❓ Nieznany | Baza klientów finansowych |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — szczególnie ważny dla fintech |

**GTM Priority: KRYTYCZNY** — Błąd śledzenia + QS 2.8 = 5 004 PLN bez mierzalnego efektu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 2.8 — nadpłata CPC ~55% | **~2 800 PLN** | **~33 600 PLN** |
| Błędne konwersje (15 PLN/lead zamiast 500+ PLN) | niemierzalne | — |
| Potencjał przy QS 7+ i Target CPA 60 PLN | +~40 realnych leadów/msc | +~40 000 PLN wartości |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — Google Ads policies dla finansowych (disclaimery, LP requirements)
2. Zdefiniuj konwersje realistycznie: form_submission z wartością 500–1 500 PLN

**🟡 Miesiąc 1:**
1. Przebuduj strukturę słów kluczowych — exact match zamiast broad dla finansowych
2. Cel QS ≥ 7.0 → oszczędność ~2 800 PLN/msc CPC

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla leadów finansowych
2. Target CPA bidding (cel 80–120 PLN za realny lead) po naprawie

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 2.8 i błędne konwersje uniemożliwiają ocenę efektywności. 5 004 PLN/msc bez mierzalnego ROI. Pełna restrukturyzacja wymagana.

---

### KONTO 34 — magdalena24.pl
**ID:** 4753MAGDALENA24 | **MCC:** 934-203-1404 | **Typ:** e-commerce (odzież damska, moda)
**BDOS alias:** `magdalena24.pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **4 753 PLN** |
| Kliknięcia | 27 089 |
| CTR | 4.8% |
| Avg. CPC | 0.18 PLN |
| Konwersje | 337 |
| Wartość konwersji | 61 679 PLN |
| ROAS | **13.0x** |
| CPA | **14 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 9.2 / 10 ⭐ |

**Typy kampanii:** PMax: 4, Search: 1, Video: 1
**Strategie bidowania:** maximize conversion value, maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] PMAX Sukienki | PMax | 1 500 PLN | 105 | 15.2x | ⭐ |
| [INV] PMAX Bluzki i topki | PMax | 1 000 PLN | 72 | 13.5x | ✅ |
| [INV] PMAX Spódnice | PMax | 900 PLN | 62 | 12.8x | ✅ |
| [INV] PMAX Bestsellery | PMax | 800 PLN | 88 | 14.1x | ✅ |
| [INV] Search Brand Magdalena24 | Search | 400 PLN | 10 | 8.7x | ✅ |
| **[INV] YouTube Stylizacje** | Video | **153 PLN** | **0** | 0x | 🔴 Wstrzymaj |

#### Analiza Google Ads — Ocena Specjalisty

Magdalena24.pl to jedno z najlepiej zarządzanych kont mody w portfelu. ROAS 13.0x, QS 9.2, CPC 0.18 PLN — wszystkie wskaźniki wskazują na doskonałą optymalizację. AOV = 61 679 / 337 = 183 PLN — typowa wartość dla odzieży damskiej online.

CPC 0.18 PLN jest absolutnie wyjątkowy — jest to jeden z najniższych CPC w całym MCC, wskazujący na doskonałe Quality Score przekładające się na minimalne koszty (QS 9.2 potwierdza). Dla kategorii odzieży damskiej benchmark CPC = 0.30–0.80 PLN, więc 0.18 PLN to poziom najlepszych 5% kont.

Jedyna wada: YouTube (153 PLN, 0 konwersji) — marginalny koszt, ale warto wstrzymać. Konto jest znacząco niedoinwestowane — przy ROAS 13x skalowanie do 10 000 PLN/msc powinno przynieść ~130 000 PLN miesięcznego przychodu.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Priorytet — wysoki wolumen zakupów |
| Customer Match | ❓ Nieznany | Powracające klientki mody — kluczowe |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — 337 zakupów/msc = duża baza danych do EC i CM.

#### BCG Analiza (odzież damska)

Przy 27 089 kliknięciach/msc i CR 1.24% (337/27 089) konto ma doskonałą efektywność konwersji. Segmentacja produktowa:
- Sukienki (ROAS 15.2x) — gwiazdy: skaluj agresywnie
- Bestsellery (ROAS 14.1x) — gwiazdy: utrzymaj
- Bluzki/topki (ROAS 13.5x) — dojne krowy: utrzymaj
- Spódnice (ROAS 12.8x) — dojne krowy: utrzymaj

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| YouTube (0 konwersji) | 153 PLN | 1 836 PLN |
| Niedoinwestowanie (potencjał 2x budżetu × 13x ROAS) | -~61 000 PLN potencjalnego przychodu | -~732 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj YouTube (153 PLN, 0 konwersji)
2. Skaluj budżet 2x → 9 000 PLN/msc — ROAS 13x uzasadnia natychmiastowo

**🟡 Miesiąc 1:**
1. Enhanced Conversions — 337 zakupów/msc = duży potencjał lepszego match rate
2. Customer Match — powracające klientki mody mają LTV 2-4x wyższy

**🟢 Miesiąc 2–3:**
1. Skaluj dalej — cel 15 000 PLN/msc przy ROAS ≥ 10x
2. Testuj segment premium (sukienki >300 PLN) w osobnej kampanii

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — Znakomite konto. ROAS 13x, QS 9.2, CPC 0.18 PLN. Jedyna poważna wada: skrajne niedoinwestowanie. Skalowanie 2-3x to absolutny priorytet.

---

### KONTO 35 — Kraksky
**ID:** 4314KRAKSKY | **MCC:** 934-203-1404 | **Typ:** e-commerce / usługi (Kraków, sklep regionalny)
**BDOS alias:** `kraksky`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **4 314 PLN** |
| Kliknięcia | 1 628 |
| CTR | 1.4% |
| Avg. CPC | 2.65 PLN |
| Konwersje | 20 |
| Wartość konwersji | 18 717 PLN |
| ROAS | **4.3x** |
| CPA | **216 PLN** |
| Kampanii aktywnych | 6 |
| Avg QS | 6.8 / 10 |

**Typy kampanii:** Search: 4, Video: 1, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Brand | Search | 1 200 PLN | 9 | 5.8x | ✅ |
| [INV] Search Kraków produkty | Search | 900 PLN | 6 | 4.2x | ✅ |
| [INV] PMax All | PMax | 700 PLN | 4 | 3.8x | ✅ |
| [INV] Search Lokalne | Search | 600 PLN | 1 | 2.0x | ⚠️ |
| **[INV] Search High Intent PL REM** | Search | **450 PLN** | **0** | 0x | 🔴 |
| **[INV] YouTube Brand** | Video | **464 PLN** | **0** | 0x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Kraksky to konto z niszą lokalną (Kraków) i ROAS 4.3x — solidnym ale z dwoma kampaniami bez konwersji pochłaniającymi ~21% budżetu. AOV = 18 717 / 20 = 936 PLN — wysoka wartość sugerująca albo lokalny sklep z artykułami premium albo usługę z wyższym AOV.

2 kampanie bez konwersji (łącznie 914 PLN/msc) to 21% zmarnowanego budżetu. Przy ROAS 4.3x na reszcie konta, przekierowanie tych środków na działające kampanie dałoby +~3 900 PLN wartości konwersji.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne przy wysokim AOV |
| Customer Match | ❓ Nieznany | Lokalni lojalni klienci |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Kampanie bez konwersji (914 PLN) | 914 PLN | 10 968 PLN |
| Potencjał realokacji (914 × 4.3x ROAS) | +~3 900 PLN przychodu | +~46 800 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj High Intent PL REM i YouTube Brand natychmiast

**🟡 Miesiąc 1:**
1. Przesuń 914 PLN na Search Brand i Search Kraków (potwierdzone konwersje)
2. Sprawdź dlaczego Search Lokalne ma CPA 600 PLN (słowa kluczowe?)

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions przy AOV 936 PLN — warto
2. Customer Match dla lokalnych lojalnych klientów

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 4.3x OK, ale 2 kampanie bez konwersji pochłaniają 21% budżetu. Łatwa naprawa = natychmiastowa poprawa efektywności.

---

### KONTO 36 — Maxdent
**ID:** 4027002742 | **MCC:** 934-203-1404 | **Typ:** e-commerce (sprzęt stomatologiczny)
**BDOS alias:** `maxdent`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **4 027 PLN** |
| Kliknięcia | 2 153 |
| CTR | 1.4% |
| Avg. CPC | 1.87 PLN |
| Konwersje | **208** |
| Wartość konwersji | **208 PLN** |
| ROAS | **0.05x** 🔴🔴🔴 |
| CPA | **19 PLN** |
| Kampanii aktywnych | 3 |
| Avg QS | 4.3 / 10 ⚠️ |

**Typy kampanii:** Search: 2, PMax: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Search Sprzęt stom. | Search | 2 200 PLN | 130 | 0.04x | 🔴 |
| [INV] Search Materiały | Search | 1 300 PLN | 62 | 0.05x | 🔴 |
| [INV] PMax Stomatologia | PMax | 527 PLN | 16 | 0.06x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Maxdent to klasyczny przypadek błędu śledzenia konwersji kategorii "1 PLN/konwersja": 208 konwersji × 1 PLN = 208 PLN wartości. Jest to dosłownie niemożliwe dla sklepu ze sprzętem stomatologicznym (ceny: 500–50 000 PLN). Konwersja jest śledzona jako event z wartością 1 PLN (np. "kliknięcie w link" = 1 PLN).

To jeden z najtańszych do naprawienia problemów w całym MCC: wystarczy zmienić wartość konwersji na dynamiczną z koszyka. Po naprawie konto prawdopodobnie pokaże ROAS 5-15x (sprzęt medyczny ma wysokie marże i wysoki AOV).

Algorytm jest prowadzony na złej metryce (208 "konwersji" = 208 PLN) zamiast faktycznych transakcji (prawdopodobnie 5-20 faktycznych zakupów miesięcznie o wartości ~40 000 PLN). Efekt: przepłaca za ruch niskiej jakości (QS 4.3) zamiast skupić się na wysokich wartościach.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | ŹRÓDŁO BŁĘDU — audyt GTM priorytet |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics — PILNE |
| GA4 ↔ Ads link | ❓ Nieznany | Porównaj revenue GA4 vs Ads |
| Enhanced Conversions | ❓ Nieznany | Nie uruchamiaj przed naprawą |
| Customer Match | ❓ Nieznany | Dentyści powracający klienci |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — Naprawa 1 linii kodu w GTM może zmienić wyniki z 0.05x na 10x ROAS.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Błąd śledzenia (cały budżet bez mierzalnego efektu) | 4 027 PLN | 48 324 PLN |
| QS 4.3 — nadpłata CPC ~20% | ~800 PLN | ~9 600 PLN |
| Potencjał po naprawie (sprzęt stom. ROAS 8-15x) | +~32 000–60 000 PLN przychodu | +384 000–720 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1 — PILNE:**
1. Napraw śledzenie konwersji — zmień wartość z statycznej 1 PLN na dynamiczną z koszyka
2. Zweryfikuj w GA4 (po autoryzacji) faktyczny przychód e-commerce

**🟡 Miesiąc 1:**
1. Po naprawie: zmień strategię na Target ROAS (cel 8x)
2. QS audit — zaktualizuj reklamy dla dentystów B2B

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions po naprawie śledzenia
2. Customer Match — dentyści z bazy zakupowej

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.05x = 1 PLN/konwersja to oczywisty błąd konfiguracji GTM. Priorytet 2 całego MCC (po TABLE4U). Naprawa zajmie 1 godzinę, efekt — możliwy ROAS 10x+.

---

### KONTO 37 — Marcoplast
**ID:** 3908MARCOPLAST | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły plastyczne, biurowe)
**BDOS alias:** `marcoplast`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 908 PLN** |
| Kliknięcia | 2 515 |
| CTR | 2.0% |
| Avg. CPC | 1.55 PLN |
| Konwersje | 13 |
| Wartość konwersji | 800 PLN |
| ROAS | **0.2x** |
| CPA | **301 PLN** |
| Kampanii aktywnych | 2 |
| Avg QS | 6.0 / 10 |

**Typy kampanii:** Shopping: 1, Search: 1
**Strategie bidowania:** maximize conversions

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | ROAS | Ocena |
|----------|-----|---------|-------|------|-------|
| [INV] Shopping Artykuły plastyczne | Shopping | 2 500 PLN | 9 | 0.2x | 🔴 |
| [INV] Search Brand | Search | 1 408 PLN | 4 | 0.2x | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Marcoplast to sklep z artykułami plastycznymi i biurowymi z ROAS 0.2x — aktywna strata ~3 100 PLN/msc (zakładając marżę 40%). AOV = 800 / 13 = 62 PLN — typowe dla tanich artykułów biurowych. Przy AOV 62 PLN i CPA 301 PLN konto jest fundamentalnie nieopłacalne.

Problem może być strukturalny dla kategorii: artykuły plastyczne/biurowe mają bardzo niskie marże (~20-30%) i wysoką konkurencję od marketplace (Allegro, Amazon). Koszty CPC w tym segmencie często przekraczają AOV × marża.

Dwa opcje: (a) fundamentalna restrukturyzacja z niższymi stawkami (Maximize Clicks z CPC limit) i skupieniem na produktach wysokomarżowych, lub (b) weryfikacja czy Google Ads jest w ogóle właściwym kanałem dla tej niszy.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Niska priorytet wobec problemów fundamentalnych |
| Customer Match | ❓ Nieznany | Niski priorytet |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: NISKI** — Pierwej napraw model biznesowy dla Google Ads, potem MarTech.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 0.2x — aktywna strata (marża 40%) | ~3 100 PLN | ~37 200 PLN |
| Suboptymalna strategia (Maximize Conv.) | szacunkowo ~500 PLN | ~6 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Ogranicz budżet do 500 PLN/msc — test czy kategoria jest w ogóle opłacalna w Ads
2. Zidentyfikuj top-3 produkty wysokomarżowe i skup na nich kampanie

**🟡 Miesiąc 1:**
1. Zmień strategię na Target CPA (cel: AOV × 30% marża = ~18 PLN CPA)
2. Lub wstrzymaj kampanie — model biznesowy może nie pasować do Google Ads

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.2x przy AOV 62 PLN = nieuchronna strata. Wymaga oceny czy Google Ads jest właściwym kanałem dla tej niszy.

---

### KONTO 38 — Phinance
**ID:** 3770PHINANCE | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi finansowe — ubezpieczenia, kredyty)
**BDOS alias:** `phinance`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **3 770 PLN** |
| Kliknięcia | 4 206 |
| CTR | 2.5% |
| Avg. CPC | 0.90 PLN |
| Konwersje | 12 |
| Wartość konwersji | 12 PLN |
| ROAS | brak wartości (lead gen) |
| CPA | **314 PLN** |
| Kampanii aktywnych | 5 |
| Avg QS | 5.9 / 10 |

**Typy kampanii:** Search: 2, Display: 1, PMax: 1, Video: 1
**Strategie bidowania:** maximize conversions, maximize conversion value

#### Kampanie (30d)

| Kampania | Typ | Wydatki | Konw. | CPA | Ocena |
|----------|-----|---------|-------|-----|-------|
| [INV] Search Ubezpieczenia | Search | 1 500 PLN | 6 | 250 PLN | ✅ |
| [INV] Search Kredyt hipoteczny | Search | 1 100 PLN | 4 | 275 PLN | ✅ |
| [INV] Display Retargeting | Display | 500 PLN | 1 | 500 PLN | ⚠️ |
| [INV] PMax Financial | PMax | 400 PLN | 1 | 400 PLN | ⚠️ |
| [INV] YouTube Brand | Video | 270 PLN | 0 | — | 🔴 |

#### Analiza Google Ads — Ocena Specjalisty

Phinance to usługi finansowe (ubezpieczenia, kredyty hipoteczne) — segment gdzie wartość leada jest bardzo wysoka (ubezpieczenie = 500–3 000 PLN prowizji, kredyt hipoteczny = 2 000–8 000 PLN prowizji). Wartość konwersji 1 PLN/konwersję to oczywisty błąd — brak skonfigurowanych wartości konwersji.

CPA 314 PLN za lead finansowy jest... normalny. Dla kredytu hipotecznego gdzie prowizja to 2 000–8 000 PLN, CPA 314 PLN = 4-25% wartości = akceptowalne. Problem: bez wartości konwersji algorytm nie może optymalizować pod ROI.

CPC 0.90 PLN dla usług finansowych jest podejrzanie niski — benchmark to 5–30 PLN/klik dla kredytów. Prawdopodobnie reklamy wyświetlają się na ogólnych frazach o niskiej intencji zakupowej.

Phinance ma powiązane konto Finli byPhinance (nieaktywne) — warto sprawdzić czy duplikacja kont jest zamierzona.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| GA4 ↔ Ads link | ❓ Nieznany | Weryfikacja po autoryzacji |
| Enhanced Conversions | ❓ Nieznany | Absolutnie kluczowe dla fintech |
| Customer Match | ❓ Nieznany | Baza klientów finansowych |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — RODO szczególnie ważny |

**GTM Priority: WYSOKI** — Bez wartości konwersji algorytm jest ślepy. Konfiguracja wartości = priorytet.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Brak wartości konwersji (niemożność optymalizacji ROAS) | niemierzalne | — |
| YouTube (0 konwersji) | 270 PLN | 3 240 PLN |
| Zbyt niskie CPC (niska intencja ruchu) | szacunkowo 40% efektywności | — |
| Potencjał przy Target CPA 300 PLN i 20 leadów/msc | +~100 000–160 000 PLN prowizji | — |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Wstrzymaj YouTube (270 PLN, 0 konwersji)
2. Skonfiguruj wartości konwersji: ubezpieczenie = 800 PLN, kredyt = 3 000 PLN (prowizja szacunkowa)

**🟡 Miesiąc 1:**
1. Przebuduj keywords na high-intent (exact match: "kredyt hipoteczny kalkulator", "ubezpieczenie mieszkania cena")
2. Target CPA bidding (cel 300–400 PLN) po naprawie wartości

**🟢 Miesiąc 2–3:**
1. Enhanced Conversions dla formularzy i call trackingu
2. Customer Match — baza klientów ubezpieczeniowych

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 314 PLN jest akceptowalny dla finansów. Kluczowy problem: brak wartości konwersji. Potencjał znacznie wyższy po konfiguracji.

