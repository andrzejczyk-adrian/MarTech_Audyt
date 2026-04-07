import json, warnings, sys
warnings.filterwarnings('ignore')

with open('AUDYT/MarTech/wykonane/modnakiecka/ga4_raw.json', encoding='utf-8') as f:
    d = json.load(f)

out = []

# FUNNEL
out.append('=== FUNNEL ===')
for r in d['funnel']:
    out.append(str(r))

# DEVICES
out.append('\n=== DEVICES ===')
for r in d['devices']:
    out.append(str(r))

# CITIES
out.append('\n=== CITIES ===')
for r in d['cities']:
    out.append(str(r))

# PRODUCTS TOP 20
out.append('\n=== PRODUCTS TOP 20 ===')
for r in d['products'][:20]:
    out.append(str(r))

# TRANSACTIONS analysis
out.append('\n=== TRANSACTIONS ANALYSIS ===')
tr = d['transactions']
total_tr = sum(int(r['transactions']) for r in tr)
total_ep = sum(int(r['ecommercePurchases']) for r in tr)
total_rev = sum(float(r['purchaseRevenue']) for r in tr)
no_id = [r for r in tr if r['transactionId'] in ('(not set)', '')]
dup = [r for r in tr if int(r['transactions']) > 1]
out.append(f'Total transaction rows: {len(tr)}')
out.append(f'Sum transactions: {total_tr}')
out.append(f'Sum ecommercePurchases: {total_ep}')
out.append(f'Sum purchaseRevenue: {total_rev:.2f} PLN')
out.append(f'Rows with (not set) transactionId: {len(no_id)}')
out.append(f'Sum transactions no ID: {sum(int(r["transactions"]) for r in no_id)}')
out.append(f'Rows with >1 transaction (duplicates): {len(dup)}')
out.append('Top duplicates:')
for r in sorted(dup, key=lambda x: int(x['transactions']), reverse=True)[:10]:
    out.append(f'  ID={r["transactionId"]} tr={r["transactions"]} ep={r["ecommercePurchases"]} rev={r["purchaseRevenue"]}')

# DAILY KPI summary
out.append('\n=== DAILY KPI SUMMARY (30d) ===')
dk = d['daily_kpi']
tot_sess = sum(int(r['sessions']) for r in dk)
tot_purch = sum(int(r['ecommercePurchases']) for r in dk)
tot_rev2 = sum(float(r['purchaseRevenue']) for r in dk)
tot_atc = sum(int(r['addToCarts']) for r in dk)
tot_co = sum(int(r['checkouts']) for r in dk)
out.append(f'Sessions: {tot_sess}')
out.append(f'ecommercePurchases: {tot_purch}')
out.append(f'purchaseRevenue: {tot_rev2:.2f} PLN')
out.append(f'addToCarts: {tot_atc}')
out.append(f'checkouts: {tot_co}')
if tot_sess > 0:
    out.append(f'CR (purchases/sessions): {tot_purch/tot_sess*100:.3f}%')
if tot_purch > 0:
    out.append(f'AOV: {tot_rev2/tot_purch:.2f} PLN')

# SOURCE MEDIUM SUMMARY - key aggregations
out.append('\n=== SOURCE/MEDIUM KEY AGGREGATIONS ===')
sm = d['source_medium']

# Facebook variants
fb_sources = ['facebook', 'm.facebook.com', 'fb', 'lm.facebook.com', 'l.facebook.com', 'facebook.com', 'mobile.facebook.com', 'pl-pl.facebook.com']
fb_rows = [r for r in sm if r['sessionSource'].lower() in [x.lower() for x in fb_sources]]
fb_sess = sum(int(r['sessions']) for r in fb_rows)
fb_trans = sum(int(r['transactions']) for r in fb_rows)
fb_rev = sum(float(r['purchaseRevenue']) for r in fb_rows)
out.append(f'Facebook total (all variants): sessions={fb_sess}, transactions={fb_trans}, revenue={fb_rev:.0f}')
out.append('  Variants:')
for r in sorted(fb_rows, key=lambda x: int(x['sessions']), reverse=True):
    out.append(f'    source={r["sessionSource"]} medium={r["sessionMedium"]} sessions={r["sessions"]}')

# SALESmanago variants
sm_rows = [r for r in sm if 'salesmanago' in r['sessionSource'].lower()]
sm_sess = sum(int(r['sessions']) for r in sm_rows)
sm_trans = sum(int(r['transactions']) for r in sm_rows)
sm_rev = sum(float(r['purchaseRevenue']) for r in sm_rows)
out.append(f'\nSALESmanago total (all mediums): sessions={sm_sess}, transactions={sm_trans}, revenue={sm_rev:.0f}')
out.append('  Variants:')
for r in sorted(sm_rows, key=lambda x: int(x['sessions']), reverse=True):
    out.append(f'    medium={r["sessionMedium"]} sessions={r["sessions"]} trans={r["transactions"]} rev={r["purchaseRevenue"]}')

# TikTok variants
tt_rows = [r for r in sm if 'tiktok' in r['sessionSource'].lower()]
tt_sess = sum(int(r['sessions']) for r in tt_rows)
tt_trans = sum(int(r['transactions']) for r in tt_rows)
tt_rev = sum(float(r['purchaseRevenue']) for r in tt_rows)
out.append(f'\nTikTok total: sessions={tt_sess}, transactions={tt_trans}, revenue={tt_rev:.0f}')
out.append('  Variants:')
for r in sorted(tt_rows, key=lambda x: int(x['sessions']), reverse=True):
    out.append(f'    source={r["sessionSource"]} medium={r["sessionMedium"]} sessions={r["sessions"]}')

# (not set) analysis
ns_rows = [r for r in sm if '(not set)' in r['sessionSource'] or '(not set)' in r['sessionMedium']]
ns_sess = sum(int(r['sessions']) for r in ns_rows)
ns_trans = sum(int(r['transactions']) for r in ns_rows)
out.append(f'\n(not set) rows: sessions={ns_sess}, transactions={ns_trans}')

# Criteo variants
cr_rows = [r for r in sm if 'criteo' in r['sessionSource'].lower()]
cr_sess = sum(int(r['sessions']) for r in cr_rows)
cr_trans = sum(int(r['transactions']) for r in cr_rows)
cr_rev = sum(float(r['purchaseRevenue']) for r in cr_rows)
out.append(f'\nCriteo total: sessions={cr_sess}, transactions={cr_trans}, revenue={cr_rev:.0f}')

with open('AUDYT/MarTech/wykonane/modnakiecka/ga4_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print('DONE - saved to ga4_analysis.txt')
