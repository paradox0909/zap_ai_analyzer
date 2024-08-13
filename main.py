import time
import os
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'paradox0909'
target = 'https://public-firing-range.appspot.com'
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
    print('Spider.py scan finished')
    print('\n'.join(map(str, zap.spider.results(scanID))))

def run_active_scan():
    print('Active Scanning target {}'.format(target))
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
        time.sleep(5)

    print('Active Scan 완료되었습니다!')

