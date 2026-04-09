# -*- coding: utf-8 -*-
"""
Fetch GA4 v2 — patrizia.aryton.pl
Property: 326801658 (G-93NK3C48R3)
Pobiera: dane 30d, YoY (30d rok temu), duplikaty ecommercePurchases per transactionId,
         precyzyjne metryki mobile, lejek, produkty, landing pages.
"""
import sys, io, json, warnings, os, urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
warnings.filterwarnings('ignore')

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, Dimension, Metric, DateRange, OrderBy
)
from google.oauth2 import service_account
from datetime import date, timedelta

KEY_FILE = 'C:/Users/adria/Documents/AI/keys/ai-andrzejczyk-ga4.json'
PROPERTY_ID = '326801658'
OUT_DIR = 'AUDYT/MarTech/wykonane/v2_aryton'
OUT_FILE = os.path.join(OUT_DIR, 'ga4_raw_v2.json')

os.makedirs(OUT_DIR, exist_ok=True)

credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE, scopes=['https://www.googleapis.com/auth/analytics.readonly']
)
client = BetaAnalyticsDataClient(credentials=credentials)

# Okresy
today = date.today()
d30_end = (today - timedelta(days=1)).strftime('%Y-%m-%d')
d30_start = (today - timedelta(days=31)).strftime('%Y-%m-%d')
# YoY: ten sam okres rok temu
yoy_end = (today - timedelta(days=365)).strftime('%Y-%m-%d')
yoy_start = (today - timedelta(days=395)).strftime('%Y-%m-%d')

print(f"Okres biezacy: {d30_start} - {d30_end}")
print(f"Okres YoY:     {yoy_start} - {yoy_end}")

def run(dims, mets, date_from, date_to, limit=2000, order_metric=None):
    req = RunReportRequest(
        property=f'properties/{PROPERTY_ID}',
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        date_ranges=[DateRange(start_date=date_from, end_date=date_to)],
        limit=limit
    )
    if order_metric:
        req.order_bys = [OrderBy(
            metric=OrderBy.MetricOrderBy(metric_name=order_metric),
            desc=True
        )]
    resp = client.run_report(req)
    rows = []
    for row in resp.rows:
        r = {dims[i]: row.dimension_values[i].value for i in range(len(dims))}
        r.update({mets[i]: row.metric_values[i].value for i in range(len(mets))})
        rows.append(r)
    return rows

def run_totals(mets, date_from, date_to):
    """Pobierz totale bez wymiarow"""
    req = RunReportRequest(
        property=f'properties/{PROPERTY_ID}',
        metrics=[Metric(name=m) for m in mets],
        date_ranges=[DateRange(start_date=date_from, end_date=date_to)],
        limit=1
    )
    resp = client.run_report(req)
    if resp.rows:
        return {mets[i]: resp.rows[0].metric_values[i].value for i in range(len(mets))}
    return {m: '0' for m in mets}

data = {}

# ============================
# BLOK A: DANE BIEZACE (30d)
# ============================

print("\n=== BLOK A: DANE BIEZACE ===")

print("A1. Totale ogolne...")
data['totals_30d'] = run_totals(
    ['sessions', 'totalUsers', 'newUsers', 'transactions', 'ecommercePurchases',
     'purchaseRevenue', 'engagementRate', 'averageSessionDuration'],
    d30_start, d30_end
)

print("A2. Zdarzenia (TOP 50)...")
ev = run(['eventName'], ['eventCount', 'eventCountPerUser'], d30_start, d30_end, 50, 'eventCount')
data['events_30d'] = ev

print("A3. Zrodla ruchu (200 wierszy)...")
sm = run(['sessionSource', 'sessionMedium'],
         ['sessions', 'transactions', 'purchaseRevenue', 'engagementRate'],
         d30_start, d30_end, 200, 'sessions')
data['source_medium_30d'] = sm

print("A4. Transakcje z ecommercePurchases per ID (wykrywanie duplikatow)...")
tr = run(['transactionId'],
         ['transactions', 'ecommercePurchases', 'purchaseRevenue'],
         d30_start, d30_end, 3000, 'ecommercePurchases')

# Analiza duplikatow: gdzie ecommercePurchases > transactions > 0
real_duplicates = [r for r in tr if float(r['ecommercePurchases']) > 1.0 and float(r['purchaseRevenue']) > 0]
not_set = [r for r in tr if r['transactionId'] == '(not set)']
malformed = [r for r in tr if '&' in r['transactionId'] or '=' in r['transactionId']]
zero_revenue = [r for r in tr if float(r['purchaseRevenue']) == 0 and r['transactionId'] != '(not set)']

data['transactions_30d'] = tr[:100]  # top 100
data['transactions_analysis'] = {
    'total_unique_ids': len(tr),
    'sum_transactions': sum(float(r['transactions']) for r in tr),
    'sum_ecommerce_purchases': sum(float(r['ecommercePurchases']) for r in tr),
    'sum_revenue': sum(float(r['purchaseRevenue']) for r in tr),
    'ratio': round(sum(int(r['ecommercePurchases']) for r in tr) /
                   max(sum(int(r['transactions']) for r in tr), 1), 4),
    'real_duplicates_count': len(real_duplicates),
    'real_duplicates_sample': real_duplicates[:20],
    'not_set_count': len(not_set),
    'not_set_revenue': sum(float(r['purchaseRevenue']) for r in not_set),
    'malformed_ids_count': len(malformed),
    'malformed_ids_sample': malformed[:10],
    'zero_revenue_count': len(zero_revenue),
    'zero_revenue_sample': [r['transactionId'] for r in zero_revenue[:10]]
}

print(f"  Unikalne ID: {len(tr)}")
print(f"  Sum transactions: {data['transactions_analysis']['sum_transactions']}")
print(f"  Sum ecommercePurchases: {data['transactions_analysis']['sum_ecommerce_purchases']}")
print(f"  Ratio: {data['transactions_analysis']['ratio']}")
print(f"  Realnie zduplikowane (ePurchases>1): {len(real_duplicates)}")
if real_duplicates:
    print(f"  Przyklady duplikatow: {[r['transactionId'] for r in real_duplicates[:5]]}")

print("A5. Lejek zakupowy per kanal...")
funnel = run(
    ['sessionDefaultChannelGroup'],
    ['sessions', 'addToCarts', 'checkouts', 'ecommercePurchases', 'transactions', 'purchaseRevenue'],
    d30_start, d30_end, 20, 'sessions'
)
data['funnel_30d'] = funnel

print("A6. Top 30 miast...")
cities = run(['city', 'country'],
             ['sessions', 'transactions', 'ecommercePurchases', 'purchaseRevenue'],
             d30_start, d30_end, 30, 'sessions')
data['cities_30d'] = cities

print("A7. Urzadzenia (z CR)...")
devices = run(['deviceCategory'],
              ['sessions', 'transactions', 'ecommercePurchases', 'purchaseRevenue',
               'engagementRate', 'averageSessionDuration'],
              d30_start, d30_end, 10)
for d in devices:
    sess = int(d['sessions'])
    trans = int(d['transactions'])
    d['cr_transactions'] = round(trans/sess*100, 4) if sess > 0 else 0
    d['aov'] = round(float(d['purchaseRevenue'])/trans, 2) if trans > 0 else 0
data['devices_30d'] = devices

print("A8. Landing pages (top 30)...")
lp = run(['landingPage'],
         ['sessions', 'transactions', 'purchaseRevenue', 'engagementRate'],
         d30_start, d30_end, 50, 'sessions')
data['landing_pages_30d'] = lp[:30]

print("A9. Produkty e-commerce...")
products = run(
    ['itemId', 'itemName', 'itemCategory'],
    ['itemsViewed', 'itemsPurchased', 'itemRevenue', 'itemsAddedToCart'],
    d30_start, d30_end, 100, 'itemRevenue'
)
data['products_30d'] = products[:50]
# Sprawdz czy jakikolwiek produkt ma itemRevenue > 0
products_with_revenue = [p for p in products if float(p['itemRevenue']) > 0]
products_with_purchases = [p for p in products if int(p['itemsPurchased']) > 0]
print(f"  Produkty z przychodem > 0: {len(products_with_revenue)}")
print(f"  Produkty z zakupami > 0: {len(products_with_purchases)}")
data['products_analysis'] = {
    'total_products': len(products),
    'with_revenue': len(products_with_revenue),
    'with_purchases': len(products_with_purchases),
    'top_by_revenue': products_with_revenue[:10] if products_with_revenue else [],
    'all_zero_revenue': len(products_with_revenue) == 0
}

print("A10. Typ platformy / hostname strony...")
hostnames = run(['hostname'], ['sessions', 'transactions'], d30_start, d30_end, 20, 'sessions')
data['hostnames_30d'] = hostnames

print("A11. Dzienne metryki (trend 30d)...")
daily = run(['date'],
            ['sessions', 'transactions', 'purchaseRevenue', 'newUsers'],
            d30_start, d30_end, 35)  # bez order_metric — date jest wymiarem
daily.sort(key=lambda x: x['date'])
data['daily_30d'] = daily

print("A12. Referrals (dokladna analiza)...")
referrals_raw = run(['sessionSource', 'sessionMedium'],
                    ['sessions', 'transactions', 'purchaseRevenue'],
                    d30_start, d30_end, 300)
referrals = [r for r in referrals_raw if r['sessionMedium'] == 'referral']
referrals.sort(key=lambda x: int(x['sessions']), reverse=True)
data['referrals_30d'] = referrals[:50]

print("A13. Kanaly domyslne z transactions (dla CR)...")
channels = run(
    ['sessionDefaultChannelGroup'],
    ['sessions', 'transactions', 'purchaseRevenue', 'newUsers', 'totalUsers'],
    d30_start, d30_end, 20, 'sessions'
)
for ch in channels:
    sess = int(ch['sessions'])
    trans = int(ch['transactions'])
    ch['cr_pct'] = round(trans/sess*100, 4) if sess > 0 else 0
    ch['rev_per_session'] = round(float(ch['purchaseRevenue'])/sess, 2) if sess > 0 else 0
data['channels_30d'] = channels

# ============================
# BLOK B: DANE YoY
# ============================

print("\n=== BLOK B: YoY (rok temu, ten sam okres) ===")

print("B1. Totale YoY...")
data['totals_yoy'] = run_totals(
    ['sessions', 'totalUsers', 'newUsers', 'transactions', 'ecommercePurchases',
     'purchaseRevenue', 'engagementRate'],
    yoy_start, yoy_end
)

print("B2. Zrodla ruchu YoY...")
sm_yoy = run(['sessionDefaultChannelGroup'],
             ['sessions', 'transactions', 'purchaseRevenue'],
             yoy_start, yoy_end, 20, 'sessions')
for ch in sm_yoy:
    sess = int(ch['sessions'])
    trans = int(ch['transactions'])
    ch['cr_pct'] = round(trans/sess*100, 4) if sess > 0 else 0
data['channels_yoy'] = sm_yoy

print("B3. Urzadzenia YoY...")
devices_yoy = run(['deviceCategory'],
                  ['sessions', 'transactions', 'purchaseRevenue'],
                  yoy_start, yoy_end, 10)
for d in devices_yoy:
    sess = int(d['sessions'])
    trans = int(d['transactions'])
    d['cr_transactions'] = round(trans/sess*100, 4) if sess > 0 else 0
data['devices_yoy'] = devices_yoy

print("B4. Dzienne metryki YoY...")
daily_yoy = run(['date'],
                ['sessions', 'transactions', 'purchaseRevenue'],
                yoy_start, yoy_end, 35)
daily_yoy.sort(key=lambda x: x['date'])
data['daily_yoy'] = daily_yoy

print("B5. Produkty YoY...")
products_yoy = run(
    ['itemId', 'itemName', 'itemCategory'],
    ['itemsViewed', 'itemsPurchased', 'itemRevenue'],
    yoy_start, yoy_end, 50, 'itemRevenue'
)
data['products_yoy'] = products_yoy[:30]
yoy_products_with_revenue = [p for p in products_yoy if float(p['itemRevenue']) > 0]
print(f"  YoY produkty z przychodem > 0: {len(yoy_products_with_revenue)}")

# ============================
# BLOK C: OBLICZENIA YoY
# ============================

print("\n=== BLOK C: YoY DELTA ===")

t_now = data['totals_30d']
t_yoy = data['totals_yoy']

def delta_pct(now_val, yoy_val):
    now = float(now_val)
    yoy = float(yoy_val)
    if yoy == 0:
        return None
    return round((now - yoy) / yoy * 100, 1)

data['yoy_delta'] = {
    'sessions_now': t_now['sessions'],
    'sessions_yoy': t_yoy['sessions'],
    'sessions_delta_pct': delta_pct(t_now['sessions'], t_yoy['sessions']),
    'transactions_now': t_now['transactions'],
    'transactions_yoy': t_yoy['transactions'],
    'transactions_delta_pct': delta_pct(t_now['transactions'], t_yoy['transactions']),
    'revenue_now': t_now['purchaseRevenue'],
    'revenue_yoy': t_yoy['purchaseRevenue'],
    'revenue_delta_pct': delta_pct(t_now['purchaseRevenue'], t_yoy['purchaseRevenue']),
    'aov_now': round(float(t_now['purchaseRevenue'])/max(int(t_now['transactions']),1), 2),
    'aov_yoy': round(float(t_yoy['purchaseRevenue'])/max(int(t_yoy['transactions']),1), 2),
}

d = data['yoy_delta']
print(f"  Sesje: {d['sessions_now']} vs {d['sessions_yoy']} YoY = {d['sessions_delta_pct']}%")
print(f"  Transakcje: {d['transactions_now']} vs {d['transactions_yoy']} = {d['transactions_delta_pct']}%")
print(f"  Przychod: {d['revenue_now'][:8]} vs {d['revenue_yoy'][:8]} = {d['revenue_delta_pct']}%")
print(f"  AOV: {d['aov_now']} vs {d['aov_yoy']} PLN")

# ============================
# ZAPISZ JSON
# ============================

data['meta'] = {
    'property_id': PROPERTY_ID,
    'period_current': {'start': d30_start, 'end': d30_end},
    'period_yoy': {'start': yoy_start, 'end': yoy_end},
    'fetched_at': str(date.today())
}

with open(OUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nZapisano: {OUT_FILE}")
