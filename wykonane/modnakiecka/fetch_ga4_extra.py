import json, warnings
warnings.filterwarnings('ignore')
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange
from google.oauth2 import service_account

KEY_FILE = 'C:/Users/adria/Documents/AI/keys/ai-andrzejczyk-ga4.json'
PROPERTY_ID = '291537403'
credentials = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=['https://www.googleapis.com/auth/analytics.readonly'])
client = BetaAnalyticsDataClient(credentials=credentials)

def run(dims, mets, limit=50):
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

extra = {}

# First user source/medium
fus = run(['firstUserSource', 'firstUserMedium'], ['newUsers', 'sessions'], 30)
fus.sort(key=lambda x: int(x['newUsers']), reverse=True)
extra['first_user_source'] = fus

# New vs returning
nvr = run(['newVsReturning'], ['sessions', 'ecommercePurchases', 'purchaseRevenue'], 5)
extra['new_vs_returning'] = nvr

# Engagement rate by channel
eng = run(['sessionDefaultChannelGroup'], ['sessions', 'engagedSessions', 'averageSessionDuration'], 20)
for r in eng:
    if int(r['sessions']) > 0:
        r['engagementRate'] = f"{int(r['engagedSessions'])/int(r['sessions'])*100:.1f}%"
eng.sort(key=lambda x: int(x['sessions']), reverse=True)
extra['engagement_by_channel'] = eng

with open('AUDYT/MarTech/wykonane/modnakiecka/ga4_extra.json', 'w', encoding='utf-8') as f:
    json.dump(extra, f, ensure_ascii=False, indent=2)
print('DONE')
