import json

json_path = 'test_json_24.json'

# JSON 파일 읽기
with open(json_path, 'r', encoding='utf-8') as json_file:
    parsed_json = json.load(json_file)

# JSON 데이터가 올바르게 로드되었는지 확인
print("Loaded JSON data:", parsed_json)

# 키 리스트 정의
json_keys = [
    "method",
    "evidence",
    "description",
    "inputVector",
    "url",
    "param",
    "name",
]

# 각 키에 대해 값 출력
for key in json_keys:
    value = parsed_json.get(key)
    print(f"{key}: {value}")
