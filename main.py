import os
import requests
import time
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'paradox0909'
target = 'https://public-firing-range.appspot.com'


zap = ZAPv2(proxies={'http': 'http://172.17.0.1:8090', 'https': 'https://172.17.0.1:8090'})

print('Active Scanning target {}'.format(target))

scanID = zap.ascan.scan(target, apikey=apiKey)

while int(zap.ascan.status(scanID)) < 100:
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)

print('Active Scan completed')
print('Hosts: {}'.format(', '.join(zap.core.hosts())))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target, apikey=apiKey))

try:
    response = requests.get("http://172.17.0.1:8090")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")

os.system('/Users/paradoxmyung/Desktop/Paradox/zap_ai_analyzer/json_parse.py')