import time
import json
import os
from zapv2 import ZAPv2
import google.generativeai as genai

target = 'http://172.17.0.3'
apiKey = 'paradox0909'

search_websource_dir = './websource/search.php'
login_websource_dir = './websource/login.php'
json_path = 'vuln_check.json'

zap = ZAPv2(apikey=apiKey)

def save_to_vuln_check_json(result, prefix='vuln_check', extension='.json'):
    filename = f"{prefix}{extension}"
    
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4)
    print(f'Result saved to {filename}')

def run_spider():
    print(f'Spidering target {target}')
    scanID = zap.spider.scan(target)
    while int(zap.spider.status(scanID)) < 100:
        print(f'Spider progress %: {zap.spider.status(scanID)}')
        time.sleep(1)
    print('Spider completed!')
    print('\n'.join(map(str, zap.spider.results(scanID))))

def ajax_spider():
    print("test_code_ajax")
    print('Ajax Spider target {}'.format(target))
    scanID = zap.ajaxSpider.scan(target)
    timeout = time.time() + 60*2
    while zap.ajaxSpider.status == 'running':
        if time.time() > timeout:
            break
        print('Ajax Spider status' + zap.ajaxSpider.status)
        time.sleep(2)
    print('Ajax Spider completed')
    ajaxResults = zap.ajaxSpider.results(start=0, count=10)

def run_active_scan():
    print(f'Active Scanning target {target}')
    scanID = zap.ascan.scan(target)
    while int(zap.ascan.status(scanID)) < 100:
        print(f'Active Scan Progress %: {zap.ascan.status(scanID)}')
        time.sleep(5)
    
    print('Active Scan completed!')

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
    save_to_vuln_check_json(result)

def search():
    GOOGLE_API_KEY = "AIzaSyB4mgp-9DoH8njhPp9B66S1wf48TtjNBr0"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    with open(search_websource_dir, 'r', encoding='utf-8') as search_file:
        search_content = search_file.read()

    with open(login_websource_dir, 'r', encoding='utf-8') as login_file:
        login_content = login_file.read()

    with open(json_path, 'r', encoding='utf-8') as json_file:
        parsed_json = json.load(json_file)
    
    web_source = f"{login_content}\n{search_content}"
    
    response = model.generate_content(f"""
웹 취약점 점검을 한 결과를 json으로 받았고, 이를 토대로 웹 취약점 점검이 정탐인지 오탐인지 판별해보려고 해.{parsed_json} 이게 json 데이터야.
json 데이터를 너가 전체적으로 봤으면 좋겠어. 
점검한 웹 소스코드야. {web_source} 이 점검 결과가 실제 영향력이 있는지 "코드기반"으로 확인해줘. 
"이유를 포함해서 코드의 어느 부분이 취약한지 알려줘". 코드의 전체 부분도 출력 부탁. [취약점 명, 전체 코드,취약한 부분의 코드, 이유] 이런식으로 나눠서.
""")
    print(response.text)

if __name__ == '__main__':
    run_spider()

    time.sleep(1)
    run_active_scan()
    time.sleep(1)
    search()
    print("END CODE")