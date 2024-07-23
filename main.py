import requests
import time
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'paradox0909'
target = 'https://public-firing-range.appspot.com'
zap = ZAPv2(apiKey=apiKey, proxies={'http': 'http://172.17.0.1:8090', 'https': 'https://172.17.0.1:8090'})

print('Active Scanning target {}'.format(target))
scanID = zap.ascan.scan(target)
while int(zap.ascan.status(scanID)) < 100:
    # Loop until the scanner has finished
    print('Scan progress %: {}'.format(zap.ascan.status(scanID)))
    time.sleep(5)
print('Active Scan completed')
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts(baseurl=target))
responce = requests.get("http://172.17.0.1:8090")
print(responce)

