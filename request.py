import request

URL = ["http://172.17.0.1:8090", "http://172.17.0.1:9001"]
response = requests.get(URL)
print("status code :", response.status_code)