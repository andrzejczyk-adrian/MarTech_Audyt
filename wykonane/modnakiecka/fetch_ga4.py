import sys, json, warnings, os
warnings.filterwarnings('ignore')

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange
from google.oauth2 import service_account

KEY_FILE = 'C:/Users/adria/Documents/AI/keys/ai-andrzejczyk-ga4.json'
PROPERTY_ID = '291537403'
OUT_FILE = 'AUDYT/MarTech/wykonane/modnakiecka/ga4_raw.json'

credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE, scopes=['https://www.googleapis.com/auth/analytics.readonly']
)
client = BetaAnalyticsDataClient(credentials=credentials)

def run(dims, mets, limit=100):
    req = RunReportRequest(
        property=f'properties/{PROPERTY_ID}',
        dimensions=[Dimension(name=d) for d in dims],
        metrics=[Metric(name=m) for m in mets],
        date_ranges=[DateRange(start_date='30daysAgo', end_date='today')],
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

# 1. Events (30d)
ev = run(['eventName'], ['eventCount', 'eventCountPerUser'], 60)
ev.sort(key=lambda x: int(x['eventCount']), reverse=True)
data['events'] = ev

# 2. Source / medium
sm = run(['sessionSource', 'sessionMedium'], ['sessions', 'transactions', 'purchaseRevenue'], 200)
sm.sort(key=lambda x: int(x['sessions']), reverse=True)
data['source_medium'] = sm

# 3. Transakcje — duplikaty
tr = run(['transactionId'], ['transactions', 'ecommercePurchases', 'purchaseRevenue'], 2000)
tr.sort(key=lambda x: int(x['transactions']), reverse=True)
data['transactions'] = tr[:200]

# 4. Lejek per kanał
funnel = run(
    ['sessionDefaultChannelGroup'],
    ['sessions', 'addToCarts', 'checkouts', 'ecommercePurchases', 'purchaseRevenue'],
    50
)
funnel.sort(key=lambda x: int(x['sessions']), reverse=True)
data['funnel'] = funnel

# 5. Top 20 miast
cities = run(['city'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 20)
cities.sort(key=lambda x: int(x['sessions']), reverse=True)
data['cities'] = cities

# 6. Produkty
products = run(
    ['itemId', 'itemName', 'itemCategory'],
    ['itemsViewed', 'itemsPurchased', 'itemRevenue'],
    100
)
products.sort(key=lambda x: float(x['itemRevenue']), reverse=True)
data['products'] = products[:50]

# 7. Device category
devices = run(['deviceCategory'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 10)
data['devices'] = devices

# 8. Landing page (top 30)
lp = run(['landingPage'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 30)
lp.sort(key=lambda x: int(x['sessions']), reverse=True)
data['landing_pages'] = lp

# 9. Overall KPIs
overall = run(
    ['date'],
    ['sessions', 'activeUsers', 'ecommercePurchases', 'purchaseRevenue', 'addToCarts', 'checkouts'],
    90
)
data['daily_kpi'] = overall

with open(OUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"DONE — saved to {OUT_FILE}")
print(f"events: {len(data['events'])}")
print(f"source_medium: {len(data['source_medium'])}")
print(f"transactions: {len(data['transactions'])}")
print(f"funnel channels: {len(data['funnel'])}")
print(f"products: {len(data['products'])}")
