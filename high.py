import time
import json
import os
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'paradox0909'
target = 'https://public-firing-range.appspot.com/reflected/parameter/body'
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

def get_next_filename(prefix='test_json_', extension='.json'):
    i = 1
    while os.path.exists(f"{prefix}{i}{extension}"):
        i += 1
    return f"{prefix}{i}{extension}"

def run_spider():
    print('Spidering target {}'.format(target))
    scanID = zap.spider.scan(target)
    while int(zap.spider.status(scanID)) < 100:
        print('Spider progress %: {}'.format(zap.spider.status(scanID)))
        time.sleep(1)
    print('Spider가 완료되었습니다!')
    print('\n'.join(map(str, zap.spider.results(scanID))))

def run_active_scan():
    print('Active Scanning target {}'.format(target))
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        print('Active Scan Progress %: {}'.format(zap.ascan.status(scanID)))
        time.sleep(5)
    
    print('Active Scan 완료되었습니다!')
    
    result = {
        'Hosts': zap.core.hosts,
        'Alerts': zap.core.alerts(baseurl=target)
    }

    filename = get_next_filename()
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4)
    
    print(f'Result saved to {filename}')

if __name__ == '__main__':
    run_spider()
    run_active_scan()
