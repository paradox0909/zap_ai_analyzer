import requests
import json

zap_base_url = 'http://localhost:8080'

scan_report_url = f'{zap_base_url}/OTHER/core/other/jsonreport/'
response = requests.get(scan_report_url)
scan_results = response.json()
output_file = 'zap_scan_results.json'
with open(output_file, 'w') as file:
    json.dump(scan_results, file, indent=4)
