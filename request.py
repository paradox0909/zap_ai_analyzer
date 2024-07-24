import request

URL = "http://google.com?user=comp&num=42"
response = requests.get(URL)
print("status code :", response.status_code)