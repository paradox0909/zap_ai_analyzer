import time
import json
import os
from zapv2 import ZAPv2

target = 'https://public-firing-range.appspot.com/reflected/parameter/body'

apiKey = 'paradox0909'

zap = ZAPv2(apikey=apiKey)

def get_next_filename(prefix='test_json_', extension='.json'):
    i = 1
    while os.path.exists(f"{prefix}{i}{extension}"):
        i += 1
    return f"{prefix}{i}{extension}"

def run_spider():
    print(f'Spidering target {target}')
    scanID = zap.spider.scan(target)
    while int(zap.spider.status(scanID)) < 100:
        print(f'Spider progress %: {zap.spider.status(scanID)}')
        time.sleep(1)
    print('Spider가 완료되었습니다!')
    print('\n'.join(map(str, zap.spider.results(scanID))))

def run_active_scan():
    print(f'Active Scanning target {target}')
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        print(f'Active Scan Progress %: {zap.ascan.status(scanID)}')
        time.sleep(5)
    
    print('Active Scan 완료되었습니다!')

    st = 0
    pg = 5000
    alert_dict = {}
    alert_count = 0
    alerts = zap.alert.alerts(baseurl=target, start=st, count=pg)
    high_risk_alerts = []
    
    blacklist = [1, 2]
    
    while len(alerts) > 0:
        print(f'Reading {pg} alerts from {st}')
        alert_count += len(alerts)
        
        for alert in alerts:
            plugin_id = alert.get('pluginId')
            risk_level = alert.get('risk')
            
            if plugin_id in blacklist:
                continue
            
            if risk_level == 'High':
                high_risk_alerts.append(alert)
        
        st += pg
        alerts = zap.alert.alerts(baseurl=target, start=st, count=pg)
    
    print(f'Total number of alerts: {alert_count}')
    print(f'Number of high-risk alerts: {len(high_risk_alerts)}')
    
    result = {
        'Hosts': zap.core.hosts,
        'Alerts': high_risk_alerts
    }

    filename = get_next_filename()
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4)
    
    print(f'Result saved to {filename}')

if __name__ == '__main__':
    run_spider()
    run_active_scan()
