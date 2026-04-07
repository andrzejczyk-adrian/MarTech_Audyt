
### KONTO 55 — Smart Clinic
**ID:** 6545058068 | **MCC:** 934-203-1404 | **Typ:** lead gen (klinika medyczna — estetyczna / ogólna)
**BDOS alias:** `smart-clinic`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 570 PLN** |
| Kliknięcia | ~2 100 |
| Konwersje | **186** |
| Wartość konwersji | **186 PLN** |
| ROAS | **0.07x** 🔴 |
| CPA | **14 PLN** |

**Typ:** Search, PMax (szacowane)
**Status:** 🔴 Błąd śledzenia — 186 konwersji × 1 PLN = 186 PLN

#### Analiza Google Ads — Ocena Specjalisty

Smart Clinic to klinika z klasycznym błędem śledzenia konwersji: 186 konwersji wartości 1 PLN każda = 186 PLN łącznie. Wartość wizyty w klinice estetycznej: 200–2 000 PLN, zabieg: 500–10 000 PLN. Brak realistycznych wartości konwersji całkowicie paraliżuje algorytm.

CPA 14 PLN za lead medyczny jest podejrzanie niski — co ponownie potwierdza mikrokonwersje (kliknięcia, wyświetlenia strony). Faktyczne CPA dla kliniki: 50–300 PLN.

Konto może działać znacznie lepiej po naprawie trackingu — kliniki z dobrą stroną mają ROAS 5-15x przy właściwej konfiguracji.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | ŹRÓDŁO BŁĘDU — audyt GTM priorytet |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla kliniki — po naprawie trackingu |
| Customer Match | ❓ Nieznany | Pacjenci powracający — wysoka LTV |
| Consent Mode v2 | ❓ Nieznany | RODO — dane medyczne |

**GTM Priority: KRYTYCZNY** — 186 konwersji × 1 PLN = absurdalny błąd konfiguracji.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Błąd śledzenia — niemożność optymalizacji ROAS | 2 570 PLN (cały budżet nieefektywny) | 30 840 PLN |
| Potencjał po naprawie (klinika ROAS 6x) | +~15 000 PLN przychodu | +180 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Napraw śledzenie konwersji — zamień statyczną wartość 1 PLN na dynamiczną wycenę wizyty
2. Zdefiniuj konwersję: formularz rezerwacji = 300 PLN, call click = 200 PLN (szacunkowe)

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Błąd śledzenia 1 PLN/konwersję to kliniczny przykład misconfiguration. Naprawa → konto może być bardzo efektywne.

---

### KONTO 56 — Marina Spices
**ID:** 8917978649 | **MCC:** 934-203-1404 | **Typ:** e-commerce (przyprawy, produkty spożywcze)
**BDOS alias:** `marina-spices`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 540 PLN** |
| Kliknięcia | ~2 200 |
| Konwersje | 93 |
| Wartość konwersji | ~4 340 PLN |
| ROAS | **1.7x** |
| CPA | ~27 PLN |

**Typy kampanii:** PMax, Search (szacowane)
**Avg QS:** — (brak danych)

#### Analiza Google Ads — Ocena Specjalisty

Marina Spices to sklep z przyprawami z ROAS 1.7x — poniżej progu opłacalności. AOV = 4 340 / 93 = 47 PLN — typowy koszyk dla przypraw (pakiet 5-10 opakowań). Przy marży ~40% i AOV 47 PLN, CPA 27 PLN = 65% cost-to-revenue — absolutnie nierentowne.

Kategoria przypraw/produktów spożywczych ma często problem z Google Ads: niskie marże, niskie AOV, wysoka konkurencja od marketplace. Przed dalszym inwestowaniem należy sprawdzić czy Google Ads jest właściwym kanałem vs Allegro/marketplace.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla powtarzalnych zakupów |
| Customer Match | ❓ Nieznany | Powracający klienci — przyprawy kupowane regularnie |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — ROAS 1.7x wymaga diagnostyki.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 1.7x — strata ~650 PLN/msc (marża 40%) | ~650 PLN | ~7 800 PLN |
| Potencjał Customer Match (LTV powracających) | +~1 500 PLN przychodu | +18 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Oceń czy Google Ads jest opłacalny dla AOV 47 PLN — porównaj z organicznym i Allegro
2. Ogranicz budżet o 50% do czasu poprawy ROAS

**🟡 Miesiąc 1:**
1. Customer Match — przyprawy to produkty regularnie kupowane (subskrypcja)
2. Target ROAS 3x — przebuduj kampanie pod wyższe ROAS

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 1.7x i AOV 47 PLN to trudna matematyka. Wymaga fundamentalnej oceny opłacalności kanału.

---

### KONTO 57 — Gestia
**ID:** 9285737121 | **MCC:** 934-203-1404 | **Typ:** e-commerce / lead gen (nieruchomości, zarządzanie)
**BDOS alias:** `gestia`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 463 PLN** |
| Kliknięcia | ~1 800 |
| Konwersje | 42 |
| Wartość konwersji | ~49 PLN |
| ROAS | **0.02x** 🔴 |
| CPA | ~59 PLN |
| Avg QS | 3.2 / 10 🔴 |

**Typy kampanii:** Search, PMax (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Gestia to firma z segmentu nieruchomości z ROAS 0.02x i QS 3.2 — dwa poważne problemy jednocześnie. Wartość konwersji 49 / 42 = 1.17 PLN/konwersję = błąd śledzenia (symboliczna wartość).

QS 3.2 jest krytycznie niski dla nieruchomości — segment o wysokich CPC (10–50 PLN/klik dla nieruchomości). Nawet przy obecnym niższym CPC (2 463 / 1 800 = 1.37 PLN/klik) płacą nadmiernie za zły ruch.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Źródło błędu — audyt GTM |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla lead gen nieruchomości |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — QS 3.2 + błąd trackingu = 2 463 PLN bez efektu.

#### Rekomendacje

**🔴 Tydzień 1:**
1. Napraw wartości konwersji — lead nieruchomości = 1 000–5 000 PLN (prowizja)
2. QS audit — przebuduj reklamy dla segmentu nieruchomości

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.02x i QS 3.2 = podwójna katastrofa. Pilna interwencja wymagana.

---

### KONTO 58 — Omega Kserokopiarki
**ID:** 4506143606 | **MCC:** 934-203-1404 | **Typ:** e-commerce / B2B (kserokopiarki, drukarki biurowe)
**BDOS alias:** `omega-kserokopiarki`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 427 PLN** |
| Kliknięcia | ~1 600 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |
| Avg QS | **2.3 / 10** 🔴🔴 |

**Typy kampanii:** Search

#### Analiza Google Ads — Ocena Specjalisty

Omega Kserokopiarki to dystrybutor/serwis kserokopiarek z 0 konwersjami i QS 2.3 — najniższy QS wśród kont aktywnych (poza Leśne Życie 1.4). QS 2.3 przy 2 427 PLN/msc oznacza że płacą ok. 65-70% więcej za każde kliknięcie niż powinni.

0 konwersji + QS 2.3 sugeruje że kampanie docierają do absolutnie złej grupy docelowej. Słowa kluczowe "kserokopiarki" mogą być zbyt ogólne (konsumenci szukający instrukcji obsługi vs B2B kupcy szukający wyposażenia biura).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Brak konwersji = brak trackingu |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Skonfiguruj po naprawie QS |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — 0 konwersji + QS 2.3 = całkowita dysfunkcja.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| 0 konwersji — cały budżet stracony | 2 427 PLN | 29 124 PLN |
| QS 2.3 — nadpłata CPC ~70% | ~1 420 PLN z 2 427 PLN | ~17 040 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ wszystkie kampanie — 2 427 PLN bez ani jednej konwersji
2. Przeprowadź keyword audit — keywords B2B (zakup, wynajem, serwis kserokopiarki) vs keywords informacyjne
3. Skonfiguruj konwersje (formularz zapytania, call click)

**🟡 Miesiąc 1:**
1. Restart kampanii z exact match keywords B2B
2. Cel QS ≥ 7.0 przez precyzyjne grupy reklam

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — QS 2.3 i 0 konwersji = konto w stanie krytycznym. Restart od zera jest lepszą opcją niż optymalizacja.

---

### KONTO 59 — Słodycze z pomysłem
**ID:** 6760360360 | **MCC:** 934-203-1404 | **Typ:** e-commerce (słodycze personalizowane, prezenty)
**BDOS alias:** `slodycze-z-pomyslem`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 422 PLN** |
| Kliknięcia | ~2 000 |
| Konwersje | 139 |
| Wartość konwersji | **123 PLN** |
| ROAS | **0.05x** 🔴 |
| CPA | **17 PLN** |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Słodycze z pomysłem to sklep ze słodyczami personalizowanymi z klasycznym błędem śledzenia: 139 konwersji × 0.88 PLN = 123 PLN wartości. CPA 17 PLN przy AOV faktycznym ~80–150 PLN (personalizowane słodycze) i CR >7% jest zbyt dobry by być prawdziwy.

Prawdopodobna konfiguracja: mikroevent "kliknij w produkt" = 1 PLN wycena. Algorytm generuje dużo tanich kliknięć zamiast faktycznych zakupów.

Personalizowane słodycze to kategoria z sezonowością (Walentynki, Boże Narodzenie, urodziny firm). Tracking musi uwzględniać purchase events z dynamiczną wartością.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | PILNE — zmień wartość z 1 PLN na dynamiczną |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Po naprawie — wysoki wolumen 139 konw/msc |
| Customer Match | ❓ Nieznany | Firmy zamawiające na okazje cyklicznie |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zmień wartość konwersji na dynamiczną z koszyka (purchase event)
2. Zweryfikuj faktyczne zamówienia w systemie sklepu vs 139 "konwersji"

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Błąd śledzenia 1 PLN/konwersję. Po naprawie konto może mieć ROAS 4-8x.

---

### KONTO 60 — KANCELARIA WYLĄG
**ID:** 8693803123 | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi prawne)
**BDOS alias:** `kancelaria-wylag`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **2 399 PLN** |
| Kliknięcia | ~1 400 |
| Konwersje | 14 |
| Wartość konwersji | — (lead gen) |
| CPA | ~171 PLN |
| Avg QS | 3.6 / 10 🔴 |

**Typ:** Search

#### Analiza Google Ads — Ocena Specjalisty

Kancelaria Wyląg to kancelaria prawna z QS 3.6 — podobna sytuacja do Adriana Romkowskiego (QS 4.4). CPA 171 PLN za lead prawny jest akceptowalny (wartość sprawy 500–10 000 PLN). Problem: QS 3.6 generuje ~35% nadpłatę CPC = ~840 PLN/msc.

Kancelarie prawne często mają niski QS przez: (1) ogólne frazy "prawnik" bez precyzji, (2) LP bez wymaganych elementów jakości (profile adwokackie, opinie, certyfikaty), (3) brak dopasowania headline'ów do zapytań.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Call tracking kluczowy dla kancelarii |
| Consent Mode v2 | ❓ Nieznany | RODO — dane prawne wrażliwe |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| QS 3.6 — nadpłata CPC ~35% | ~840 PLN | ~10 080 PLN |
| Brak wartości konwersji | niemierzalne | — |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — precise keywords + RSA dopasowane
2. Skonfiguruj wartości konwersji: lead prawny = 500–2 000 PLN

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 171 PLN OK dla prawa, ale QS 3.6 kosztuje ~840 PLN/msc niepotrzebnie.

---

### KONTO 61 — WBL Invest
**ID:** 5348437842 | **MCC:** 934-203-1404 | **Typ:** lead gen (inwestycje, nieruchomości)
**BDOS alias:** `wbl-invest`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 889 PLN** |
| Kliknięcia | ~1 200 |
| Konwersje | 17 |
| Wartość konwersji | — |
| CPA | ~111 PLN |
| Avg QS | 2.9 / 10 🔴 |

**Typ:** Search

#### Analiza Google Ads — Ocena Specjalisty

WBL Invest to firma inwestycyjna z QS 2.9 — bardzo niski dla segmentu inwestycji. Segment inwestycyjny/nieruchomościowy ma Google Ads policies wymagające specjalnych certyfikacji (financial products). Niski QS może wynikać z niezgodności reklam z politykami Google dla usług finansowych/inwestycyjnych.

CPA 111 PLN dla leadu inwestycyjnego jest świetny — wartość klienta inwestycyjnego: 10 000–500 000 PLN.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla high-value lead gen |
| Consent Mode v2 | ❓ Nieznany | RODO wymóg |

#### Rekomendacje

**🔴 Tydzień 1:**
1. QS audit — sprawdź Google Ads policies dla usług inwestycyjnych
2. Skonfiguruj wartości konwersji: lead inwestycyjny = 1 000–5 000 PLN

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — QS 2.9 może wynikać z policies finansowych. Wymaga weryfikacji zgodności reklam z Google Ads Financial Products policies.

---

### KONTO 62 — fitME
**ID:** 8070079590 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy, fitness)
**BDOS alias:** `fitme`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 748 PLN** |
| Kliknięcia | ~1 600 |
| Konwersje | 7 |
| Wartość konwersji | ~1 050 PLN |
| ROAS | **0.6x** |
| CPA | ~250 PLN |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

FitME to sklep z suplementami fitness z ROAS 0.6x. AOV = 1 050 / 7 = 150 PLN — typowe dla suplementów (białko, BCAA). Przy marży ~45% i AOV 150 PLN, CPA 250 PLN jest absolutnie nie do zaakceptowania (CPA > AOV).

Możliwe przyczyny: (a) błąd śledzenia (7 z kilkudziesięciu konwersji), (b) złe słowa kluczowe (ogólne "suplementy" zamiast "białko whey 1kg"), (c) wysoka konkurencja od dużych graczy (Olimp, Trec, MyProtein).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tracking zakupów |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Customer Match | ❓ Nieznany | Suplementy = powracający kupujący |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Zweryfikuj tracking — 7 konwersji z ~1 600 kliknięć = CR 0.44% (bardzo niskie dla suplementów)
2. Ogranicz budżet do 500 PLN/msc do czasu naprawy

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — ROAS 0.6x i CPA > AOV = aktywna strata. Weryfikacja trackingu i strategii.

---

### KONTO 63 — Dziewiąta Planeta
**ID:** 5160052486 | **MCC:** 934-203-1404 | **Typ:** e-commerce / usługi (agencja, kreatywna)
**BDOS alias:** `dziewiata-planeta`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 725 PLN** |
| Kliknięcia | ~1 400 |
| Konwersje | 9 |
| Wartość konwersji | ~1 900 PLN |
| ROAS | **1.1x** |
| CPA | ~192 PLN |

**Typy kampanii:** Search, PMax (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Dziewiąta Planeta to agencja kreatywna z ROAS 1.1x — na granicy opłacalności. AOV = 1 900 / 9 = 211 PLN sugeruje albo niedrogie usługi, albo błędne wartości konwersji (agencje mają AOV 2 000–30 000 PLN).

Dla agencji kreatywnej Google Ads nie jest zwykle głównym kanałem pozyskiwania klientów — portfolio, referrale i content marketing są zazwyczaj efektywniejsze. Warto ocenić ROI Google Ads vs inne kanały.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla lead gen agencja |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Zdefiniuj wartości konwersji — projekt agencyjny = 5 000–30 000 PLN
2. Zrewiduj strategię — czy Google Ads to właściwy kanał dla agencji?

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 1.1x i niskie wartości konwersji. Wymaga redefinicji wartości i oceny kanału.

---

### KONTO 64 — KrainaHerbaty PL
**ID:** 8863196067 | **MCC:** 934-203-1404 | **Typ:** e-commerce (herbaty premium, akcesoria)
**BDOS alias:** `kraina-herbaty-pl`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 648 PLN** |
| Kliknięcia | ~1 500 |
| Konwersje | 32 |
| Wartość konwersji | ~3 500 PLN |
| ROAS | **2.1x** |
| CPA | ~52 PLN |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

KrainaHerbaty PL to sklep z herbatami premium. AOV = 3 500 / 32 = 109 PLN — dobra wartość dla herbat premium (zestawy, czajniki, herbaty specialty). ROAS 2.1x jest na granicy opłacalności przy marży ~40% (break-even ROAS = 2.5x).

Konto ma siostrzane konto KrainaHerbaty CSS (ID: 1379324580) z zaledwie 39 PLN wydatków ale ROAS 30x! To sugeruje że CSS jest nowym lub testowym kontem z lepszą strukturą kampanii. Warto przeanalizować różnicę w podejściu między oboma kontami.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla powracających klientów |
| Customer Match | ❓ Nieznany | Herbaciarze kupują regularnie — wysoka LTV |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| ROAS 2.1x — na granicy opłacalności | ~330 PLN potencjalnych strat | ~3 960 PLN |
| Nieoptymalne vs CSS konto (ROAS 30x) | szacunkowo 1 000 PLN suboptymalne | ~12 000 PLN |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Porównaj struktury kampanii PL vs CSS — co CSS robi lepiej?
2. Customer Match — herbaty to produkt regularnych zakupów (wysoka LTV)
3. Target ROAS 3x — cel: break-even przy marży 33%

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 2.1x za niskie. Analiza siostrzanego konta CSS (ROAS 30x) może dostarczyć insightów do poprawy.

---

### KONTO 65 — Desque
**ID:** 5058017094 | **MCC:** 934-203-1404 | **Typ:** e-commerce (meble designerskie, wnętrza premium)
**BDOS alias:** `desque`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 614 PLN** |
| Kliknięcia | ~1 400 |
| Konwersje | 58 |
| Wartość konwersji | ~24 700 PLN |
| ROAS | **15.3x** ⭐⭐ |
| CPA | ~28 PLN |

**Typy kampanii:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Desque to sklep z designerskimi meblami z ROAS 15.3x — doskonały wynik. AOV = 24 700 / 58 = 426 PLN. Przy ROAS 15x i zaledwie 1 614 PLN/msc, konto jest zdecydowanie niedoinwestowane.

Meblarnia premium z ROAS 15x to perełka portfela — skalowanie 5x (→8 070 PLN/msc) przy ROAS 10x (konserwatywna regresja) dałoby +~80 000 PLN przychodu miesięcznie dla klienta.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe przy AOV 426 PLN |
| Customer Match | ❓ Nieznany | Klienci meblowi powracają |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: WYSOKI** — ROAS 15x uzasadnia solidną infrastrukturę.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| Niedoinwestowanie (ROAS 15.3x) | -~80 000 PLN potencjalnego przychodu (przy 5x skalowaniu) | -~960 000 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Skaluj budżet 3-5x natychmiast — ROAS 15x uzasadnia bez wahania

**🟡 Miesiąc 1:**
1. Enhanced Conversions i Customer Match

#### Ocena Specjalisty MarTech

**⭐⭐⭐⭐ (4/5)** — ROAS 15.3x wybitny. Krytyczny problem: konto jest 5x za małe. Skalowanie natychmiastowe = priorytet.

---

### KONTO 66 — LycopenPRO
**ID:** 7498542821 | **MCC:** 934-203-1404 | **Typ:** e-commerce (suplementy — likopen, antyoksydanty)
**BDOS alias:** `lycopen-pro`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 553 PLN** |
| Kliknięcia | ~1 300 |
| Konwersje | 9 |
| Wartość konwersji | ~3 100 PLN |
| ROAS | **2.0x** |
| CPA | ~173 PLN |

**Typy kampanii:** PMax, Shopping (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

LycopenPRO to sklep z suplementami likopenowymi — wąska nisza medyczna. ROAS 2.0x i AOV = 3 100 / 9 = 344 PLN to wyniki na granicy opłacalności przy marży suplementów ~50% (break-even ROAS = 2.0x). Konto dosłownie na poziomie break-even.

Nisza likopenowa ma niską konkurencję w Google Ads ale i niskie wolumeny wyszukiwań. Możliwe że zbyt małe wolumeny nie pozwalają algorytmowi się nauczyć (9 konwersji/msc < minimum 30 dla Smart Bidding).

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Customer Match | ❓ Nieznany | Suplementy — LTV przez abonament |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Zmień strategię na Target ROAS 3x (Maximize Clicks tymczasowo dla więcej danych)
2. Rozważ rozszerzenie na frazy: "antyoksydanty", "zdrowie prostaty", "witamina C"
3. Customer Match — subskrypcja suplementów = stały przychód

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — ROAS 2.0x = break-even. Nisza z potencjałem ale wymaga optymalizacji.

---

### KONTO 67 — PenPol (stare konto)
**ID:** 8403686233 | **MCC:** 934-203-1404 | **Typ:** e-commerce (artykuły biurowe, szkolne)
**BDOS alias:** `penpol-stare`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 532 PLN** |
| Kliknięcia | ~1 200 |
| Konwersje | 2 |
| Wartość konwersji | ~0 PLN |
| ROAS | **0x** |

**Typ:** PMax, Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

PenPol Stare to stare konto, które prawdopodobnie powinno zostać wstrzymane od czasu uruchomienia konta PenPol Nowe (ID: 7482901847). Kanibalizacja budżetu między dwoma kontami tej samej marki obniża efektywność obu.

2 konwersje bez wartości = brak trackingu zakupów. Konto powinno zostać wstrzymane lub połączone z nowym.

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ — kanibalizacja z nowym kontem + 0 efektywnych konwersji

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Stare konto kanibalizujące nowe. Wstrzymaj natychmiast.

---

### KONTO 68 — Życie bez protez
**ID:** 2218547292 | **MCC:** 934-203-1404 | **Typ:** lead gen / e-commerce (implanty dentystyczne, stomatologia)
**BDOS alias:** `zycie-bez-protez`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 479 PLN** |
| Kliknięcia | ~1 100 |
| Konwersje | 49 |
| Wartość konwersji | **49 PLN** |
| ROAS | **0.03x** 🔴 |
| CPA | **30 PLN** |

**Typy kampanii:** Search, PMax (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Życie bez protez to klinika implantów z klasycznym błędem: 49 konwersji × 1 PLN = 49 PLN. Implant dentystyczny kosztuje 3 000–8 000 PLN — jeden faktyczny klient stomatologiczny ma wartość wielokrotnie wyższą niż cały miesięczny budżet reklamowy.

CPA 30 PLN za lead stomatologiczny jest marzeniem — ale najpierw trzeba zweryfikować czy to są realne leady (zapytania o implanty) czy mikrokonwersje.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Naprawa wartości konwersji — PILNE |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla kliniki — call tracking |
| Consent Mode v2 | ❓ Nieznany | RODO — dane medyczne |

#### Rekomendacje

**🔴 Tydzień 1:**
1. Napraw wartości konwersji — konsultacja implant = 200 PLN, zabieg = 5 000 PLN
2. Zweryfikuj faktyczne zapytania vs mikrokonwersje

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 1 PLN/konwersję dla kliniki implantów = rażący błąd. Naprawa może ujawnić doskonały ROAS.

---

### KONTO 69 — CRMC
**ID:** 4750835647 | **MCC:** 934-203-1404 | **Typ:** lead gen / e-commerce (CRM, oprogramowanie)
**BDOS alias:** `crmc`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 449 PLN** |
| Kliknięcia | ~900 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |
| Avg QS | **3.9 / 10** 🔴 |

**Typ:** Search

#### Analiza Google Ads — Ocena Specjalisty

CRMC to oprogramowanie CRM z 0 konwersjami i QS 3.9 — dwa fundamentalne problemy. Segment CRM/SaaS ma wysoką konkurencję (Salesforce, HubSpot, Pipedrive) i wysokie CPC (15–50 PLN/klik). Obecne CPC (1 449 / 900 = 1.61 PLN/klik) sugeruje targetowanie bardzo ogólnych lub niechowych fraz.

QS 3.9 generuje ~40% nadpłatę CPC. 0 konwersji = brak prawidłowego trackingu lub kampanie na zupełnie złe frazy.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | PILNE — brak konwersji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Kluczowe dla SaaS |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

**GTM Priority: KRYTYCZNY** — 0 konwersji + QS 3.9 = 1 449 PLN bez efektu.

#### Impact Finansowy

| Problem | Koszt/msc | Koszt/rok |
|---------|----------|----------|
| 0 konwersji — cały budżet stracony | 1 449 PLN | 17 388 PLN |
| QS 3.9 — nadpłata CPC ~40% | ~580 PLN z 1 449 | ~6 960 PLN |

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ do czasu naprawy QS i trackingu
2. Keyword audit — frazy SaaS CRM muszą być high-intent
3. Skonfiguruj konwersje: trial signup, demo request

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — 0 konwersji i QS 3.9 przy 1 449 PLN/msc. Stop + restart.

---

### KONTO 70 — Wiksonspas
**ID:** 8245192186 | **MCC:** 934-203-1404 | **Typ:** lead gen (SPA, wellness, zabiegi)
**BDOS alias:** `wiksonspas`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 328 PLN** |
| Kliknięcia | ~900 |
| Konwersje | 5 |
| Wartość konwersji | — (lead gen) |
| CPA | ~266 PLN |

**Typy kampanii:** Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Wiksonspas to SPA z 5 konwersjami miesięcznie i CPA 266 PLN. Dla SPA/wellness CPA 266 PLN jest wysoki — zabieg SPA kosztuje 150–500 PLN, więc CPA > AOV dla pojedynczych zabiegów. Jednak LTV klienta SPA jest wysoka (regularne wizyty = 1 000–5 000 PLN/rok).

Brak wartości konwersji uniemożliwia ocenę faktycznego ROI. 5 konwersji/msc to za mało dla Smart Bidding.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Call tracking + formularz rezerwacji |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Ważne dla rezerwacji SPA |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Skonfiguruj wartości konwersji: zabieg = 200 PLN, pakiet = 500 PLN
2. Dodaj call extension i tracking telefoniczny

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — Niska liczba konwersji (5/msc) i brak wartości. Konfiguracja wymagana.

---

### KONTO 71 — Vago
**ID:** 2417186044 | **MCC:** 934-203-1404 | **Typ:** lead gen (usługi profesjonalne)
**BDOS alias:** `vago`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 258 PLN** |
| Kliknięcia | ~900 |
| Konwersje | 11 |
| Wartość konwersji | — (lead gen) |
| CPA | ~114 PLN |

**Typy kampanii:** Search (szacowane)

#### Analiza Google Ads — Ocena Specjalisty

Vago to konto lead gen z 11 konwersjami i CPA 114 PLN. Bez wartości konwersji trudno ocenić ROI. Przy typowych wartościach lead gen (500–5 000 PLN/klient) CPA 114 PLN jest akceptowalny.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | Sprawdź tagmanager.google.com |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Konfiguracja konwersji priorytet |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU |

#### Rekomendacje

**🟡 Miesiąc 1:**
1. Skonfiguruj wartości konwersji — ustal z klientem wartość leadu
2. Enhanced Conversions

#### Ocena Specjalisty MarTech

**⭐⭐ (2/5)** — CPA 114 PLN może być OK zależnie od wartości usługi. Konfiguracja wartości priorytetem.

---

### KONTO 72 — NOWE medihurt.com
**ID:** 7280666733 | **MCC:** 934-203-1404 | **Typ:** e-commerce B2B (sprzęt medyczny hurt)
**BDOS alias:** `medihurt-nowe`

#### Wyniki Google Ads (30d)

| Metryka | Kwiecień 2026 |
|---------|--------------|
| Wydatki | **1 162 PLN** |
| Kliknięcia | ~900 |
| Konwersje | **0** |
| Wartość konwersji | 0 PLN |
| ROAS | **0x** |

**Typy kampanii:** PMax, Search (szacowane)
**Status:** ❌ 0 konwersji — nowe konto

#### Analiza Google Ads — Ocena Specjalisty

Medihurt.com to nowy sklep B2B ze sprzętem medycznym hurtowym. Jako nowe konto (uruchomione w 2026) nie zebrało jeszcze danych historycznych. Dla B2B medycznego cold start algorytmu jest szczególnie trudny — produkty niszowe, wysokie CPC, długi cykl decyzyjny.

Segment sprzętu medycznego B2B hurtowego ma inne stawki niż B2C — AOV może wynosić 10 000–200 000 PLN przy hurtowych zamówieniach. CPA 50–500 PLN byłby absolutnie akceptowalny.

#### Status MarTech — GTM

| Komponent | Status | Rekomendacja |
|-----------|--------|--------------|
| GTM kontener | ❓ Wymaga weryfikacji | NOWE konto — konfiguruj od razu |
| GA4 property | ❓ Wymaga autoryzacji | bdos auth --add analytics |
| Enhanced Conversions | ❓ Nieznany | Konfiguruj jako standard dla nowego konta |
| Consent Mode v2 | ❓ Nieznany | Wymóg EU — szczególnie ważny dla B2B medycznego |

**GTM Priority: KRYTYCZNY** — Nowe konto musi mieć prawidłowy tracking od dnia 1.

#### Rekomendacje

**🔴 Tydzień 1:**
1. WSTRZYMAJ i skonfiguruj tracking (purchase/form_submit) przed restart
2. Uruchom z małym budżetem (300 PLN/msc) po naprawie
3. Strategia: Maximize Clicks (cold start) → Maximize Conversions (po 15+ konw) → Target ROAS

#### Ocena Specjalisty MarTech

**⭐ (1/5)** — Nowe konto bez trackingu = 1 162 PLN/msc stracone. Prawidłowa konfiguracja od podstaw jest warunkiem sukcesu.

