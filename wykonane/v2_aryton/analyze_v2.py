# -*- coding: utf-8 -*-
import json, os

BASE = 'AUDYT/MarTech/wykonane/v2_aryton'
with open(os.path.join(BASE, 'ga4_raw_v2.json'), encoding='utf-8') as f:
    d = json.load(f)

lines = []

def section(title):
    lines.append('')
    lines.append('=' * 60)
    lines.append(title)
    lines.append('=' * 60)

section('TOTALE 30d (9 mar - 8 kwi 2026)')
t = d['totals_30d']
lines.append(f"  Sesje:              {t['sessions']}")
lines.append(f"  Uzytkownicy:        {t['totalUsers']}")
lines.append(f"  Nowi:               {t['newUsers']}")
lines.append(f"  Transakcje:         {t['transactions']}")
lines.append(f"  ecommercePurchases: {t['ecommercePurchases']}")
lines.append(f"  Przychod PLN:       {float(t['purchaseRevenue']):.2f}")
lines.append(f"  Engagement rate:    {float(t['engagementRate']):.4f}")
lines.append(f"  Avg session dur:    {float(t['averageSessionDuration']):.1f}s")
lines.append(f"  AOV:                {float(t['purchaseRevenue'])/max(int(t['transactions']),1):.2f} PLN")
lines.append(f"  CR (trans/sess):    {int(t['transactions'])/int(t['sessions'])*100:.4f}%")

section('TOTALE YoY (10 mar - 9 kwi 2025)')
y = d['totals_yoy']
lines.append(f"  Sesje:              {y['sessions']}")
lines.append(f"  Transakcje:         {y['transactions']}")
lines.append(f"  ecommercePurchases: {y['ecommercePurchases']}")
lines.append(f"  Przychod PLN:       {float(y['purchaseRevenue']):.2f}")
lines.append(f"  AOV:                {float(y['purchaseRevenue'])/max(int(y['transactions']),1):.2f} PLN")
lines.append(f"  CR (trans/sess):    {int(y['transactions'])/int(y['sessions'])*100:.4f}%")

section('YoY DELTA')
yoy = d['yoy_delta']
for k, v in yoy.items():
    lines.append(f"  {k}: {v}")

section('KANALY 30d (transactions, CR)')
for c in d['channels_30d']:
    lines.append(f"  {c['sessionDefaultChannelGroup'][:28]:28} sess={int(c['sessions']):7} trans={int(c['transactions']):5} rev={float(c['purchaseRevenue']):10.0f} CR={c['cr_pct']:6}% rev/sess={c['rev_per_session']:6}")

section('KANALY YoY')
for c in d['channels_yoy']:
    lines.append(f"  {c['sessionDefaultChannelGroup'][:28]:28} sess={int(c['sessions']):7} trans={int(c['transactions']):5} CR={c['cr_pct']:6}%")

section('URZADZENIA 30d')
for dev in d['devices_30d']:
    lines.append(f"  {dev['deviceCategory']:8} sess={int(dev['sessions']):7} trans={int(dev['transactions']):5} rev={float(dev['purchaseRevenue']):10.0f} CR={dev['cr_transactions']:6}% AOV={dev['aov']}")

section('URZADZENIA YoY')
for dev in d['devices_yoy']:
    lines.append(f"  {dev['deviceCategory']:8} sess={int(dev['sessions']):7} trans={int(dev['transactions']):5} CR={dev['cr_transactions']:6}%")

section('HOSTNAMES (platforma)')
for h in d['hostnames_30d']:
    lines.append(f"  {h['hostname']:45} sess={int(h['sessions']):7} trans={h['transactions']}")

section('TRANSAKCJE - ANALIZA DUPLIKATOW')
ta = d['transactions_analysis']
lines.append(f"  Unikalne transaction IDs: {ta['total_unique_ids']}")
lines.append(f"  Sum transactions:         {ta['sum_transactions']}")
lines.append(f"  Sum ecommercePurchases:   {ta['sum_ecommerce_purchases']}")
lines.append(f"  Ratio ePurch/trans:       {ta['ratio']}")
lines.append(f"  Realnie zduplikowane:     {ta['real_duplicates_count']}")
lines.append(f"  not-set count:            {ta['not_set_count']}, revenue: {ta['not_set_revenue']:.0f} PLN")
lines.append(f"  Malformed IDs:            {ta['malformed_ids_count']}")
lines.append(f"  Zero revenue IDs:         {ta['zero_revenue_count']}")
if ta.get('real_duplicates_sample'):
    lines.append(f"  Przykladowe duplikaty:")
    for r in ta['real_duplicates_sample'][:5]:
        lines.append(f"    {r}")
if ta.get('zero_revenue_sample'):
    lines.append(f"  Zero revenue sample: {ta['zero_revenue_sample'][:5]}")

section('TOP 15 TRANSAKCJI (po ecommercePurchases desc)')
for r in d['transactions_30d'][:15]:
    lines.append(f"  ID={r['transactionId'][:30]:30} trans={r['transactions']:4} ePurch={r['ecommercePurchases']:4} rev={float(r['purchaseRevenue']):8.2f}")

section('PRODUKTY - ANALIZA')
pa = d['products_analysis']
lines.append(f"  Total produktow: {pa['total_products']}")
lines.append(f"  Z przychodem>0:  {pa['with_revenue']}")
lines.append(f"  Z zakupami>0:    {pa['with_purchases']}")
lines.append(f"  Wszystkie zero:  {pa['all_zero_revenue']}")
lines.append('  TOP 10 po przychodzie:')
for p in pa['top_by_revenue'][:10]:
    lines.append(f"    [{p['itemId']:8}] {p['itemName'][:35]:35} purch={p['itemsPurchased']:4} rev={float(p['itemRevenue']):8.2f}")

section('PRODUKTY YoY (TOP 5)')
yoy_with_rev = [p for p in d['products_yoy'] if float(p['itemRevenue']) > 0]
lines.append(f"  YoY produkty z rev>0: {len(yoy_with_rev)}")
for p in yoy_with_rev[:5]:
    lines.append(f"    [{p['itemId']:8}] {p['itemName'][:35]:35} purch={p['itemsPurchased']:4} rev={float(p['itemRevenue']):8.2f}")

section('SOURCE/MEDIUM TOP 20 (30d)')
for r in d['source_medium_30d'][:20]:
    lines.append(f"  {r['sessionSource']}/{r['sessionMedium']:15} sess={int(r['sessions']):7} trans={r['transactions']:5} rev={float(r['purchaseRevenue']):10.0f}")

section('DZIENNY TREND 30d')
for day in d['daily_30d']:
    lines.append(f"  {day['date']} sess={int(day['sessions']):5} trans={day['transactions']:4} rev={float(day['purchaseRevenue']):8.0f}")

section('DZIENNY TREND YoY')
for day in d['daily_yoy']:
    lines.append(f"  {day['date']} sess={int(day['sessions']):5} trans={day['transactions']:4} rev={float(day['purchaseRevenue']):8.0f}")

section('REFERRALS TOP 15')
for r in d['referrals_30d'][:15]:
    lines.append(f"  {r['sessionSource']:40} sess={int(r['sessions']):6} trans={r['transactions']:4} rev={float(r['purchaseRevenue']):8.0f}")

section('LANDING PAGES TOP 10')
for lp in d['landing_pages_30d'][:10]:
    cr = int(lp['transactions'])/max(int(lp['sessions']),1)*100
    lines.append(f"  {lp['landingPage'][:45]:45} sess={int(lp['sessions']):7} trans={lp['transactions']:4} CR={cr:.2f}%")

output_path = os.path.join(BASE, 'analysis_output.txt')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Saved to {output_path}')
print(f'Lines: {len(lines)}')
