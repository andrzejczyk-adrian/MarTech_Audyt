import sys, json, warnings, os
warnings.filterwarnings('ignore')

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange
from google.oauth2 import service_account

KEY_FILE = 'C:/Users/adria/Documents/AI/keys/ai-andrzejczyk-ga4.json'
PROPERTY_ID = '326801658'  # G-93NK3C48R3 — patrizia.aryton.pl
OUT_FILE = 'AUDYT/MarTech/wykonane/patrizia-aryton/ga4_raw.json'

credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE, scopes=['https://www.googleapis.com/auth/analytics.readonly']
)
client = BetaAnalyticsDataClient(credentials=credentials)

def run(dims, mets, limit=100, date_from='30daysAgo'):
    req = RunReportRequest(
        property=f'properties/{PROPERTY_ID}',
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        date_ranges=[DateRange(start_date=date_from, end_date='today')],
        limit=limit
    )
    resp = client.run_report(req)
    rows = []
    for row in resp.rows:
        r = {dims[i]: row.dimension_values[i].value for i in range(len(dims))}
        r.update({mets[i]: row.metric_values[i].value for i in range(len(mets))})
        rows.append(r)
    return rows

data = {}

print("1. Zdarzenia (30d)...")
ev = run(['eventName'], ['eventCount', 'eventCountPerUser'], 60)
ev.sort(key=lambda x: int(x['eventCount']), reverse=True)
data['events'] = ev

print("2. Źródła ruchu (30d)...")
sm = run(['sessionSource', 'sessionMedium'], ['sessions', 'transactions', 'purchaseRevenue'], 200)
sm.sort(key=lambda x: int(x['sessions']), reverse=True)
data['source_medium'] = sm

print("3. Transakcje — duplikaty (30d)...")
tr = run(['transactionId'], ['transactions', 'ecommercePurchases', 'purchaseRevenue'], 2000)
tr.sort(key=lambda x: int(x['transactions']), reverse=True)
data['transactions'] = tr[:500]
data['transactions_summary'] = {
    'total_rows': len(tr),
    'total_transactions': sum(int(r['transactions']) for r in tr),
    'total_ecommerce_purchases': sum(int(r['ecommercePurchases']) for r in tr),
    'total_revenue': sum(float(r['purchaseRevenue']) for r in tr),
    'not_set_count': sum(1 for r in tr if r['transactionId'] == '(not set)'),
    'duplicated_ids': [r for r in tr if int(r['transactions']) > 1][:20]
}

print("4. Lejek zakupowy per kanał (30d)...")
funnel = run(
    ['sessionDefaultChannelGroup'],
    ['sessions', 'addToCarts', 'checkouts', 'ecommercePurchases', 'purchaseRevenue'],
    50
)
funnel.sort(key=lambda x: int(x['sessions']), reverse=True)
data['funnel'] = funnel

print("5. Top 20 miast (30d)...")
cities = run(['city'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 20)
cities.sort(key=lambda x: int(x['sessions']), reverse=True)
data['cities'] = cities

print("6. Produkty e-commerce (30d)...")
products = run(
    ['itemId', 'itemName', 'itemCategory'],
    ['itemsViewed', 'itemsPurchased', 'itemRevenue'],
    100
)
products.sort(key=lambda x: float(x['itemRevenue']), reverse=True)
data['products'] = products[:50]

print("7. Urządzenia (30d)...")
devices = run(['deviceCategory'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 10)
data['devices'] = devices

print("8. Landing pages (top 30)...")
lp = run(['landingPage'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 50)
lp.sort(key=lambda x: int(x['sessions']), reverse=True)
data['landing_pages'] = lp[:30]

print("9. Referral sources (sprawdź spam/dev)...")
ref = run(['sessionSource', 'sessionMedium'], ['sessions'], 300)
referrals = [r for r in ref if r['sessionMedium'] == 'referral']
referrals.sort(key=lambda x: int(x['sessions']), reverse=True)
data['referrals'] = referrals[:50]

print("10. Metryki ogólne (30d)...")
overall = run(
    ['date'],
    ['sessions', 'totalUsers', 'newUsers', 'ecommercePurchases', 'transactions', 'purchaseRevenue', 'engagementRate'],
    35
)
overall.sort(key=lambda x: x['date'])
data['daily_overview'] = overall

# Sumaryczne metryki ogólne
summary = run(
    ['sessionDefaultChannelGroup'],
    ['sessions', 'totalUsers', 'newUsers', 'ecommercePurchases', 'transactions', 'purchaseRevenue'],
    20
)
data['summary_by_channel'] = summary

print("11. Consent mode — sprawdzenie (not set) w source/medium...")
not_set = [r for r in sm if r['sessionSource'] == '(not set)' or r['sessionMedium'] == '(not set)']
data['not_set_traffic'] = not_set
data['not_set_pct'] = round(
    sum(int(r['sessions']) for r in not_set) / max(sum(int(r['sessions']) for r in sm), 1) * 100, 2
)

print(f"\nDane pobrane. Not-set: {data['not_set_pct']}%")
print(f"Transakcje: {data['transactions_summary']['total_transactions']}")
print(f"ecommercePurchases: {data['transactions_summary']['total_ecommerce_purchases']}")
print(f"Przychod: {data['transactions_summary']['total_revenue']:.0f} PLN")

with open(OUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\nZapisano: {OUT_FILE}")
