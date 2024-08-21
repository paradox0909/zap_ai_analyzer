import json
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyB4mgp-9DoH8njhPp9B66S1wf48TtjNBr0"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

search_websource_dir = './websource/search.php'
login_websource_dir = './websource/login.php'
json_path = 'test_json_24.json'

with open(search_websource_dir, 'r', encoding='utf-8') as search_file:
    search_content = search_file.read()

with open(login_websource_dir, 'r', encoding='utf-8') as login_file:
    login_content = login_file.read()

with open(json_path, 'r', encoding='utf-8') as json_file:
    parsed_json = json.load(json_file)

web_source = {login_content}, {search_content}

response = model.generate_content(f"""
웹 취약점 점검을 한 결과를 json으로 받았고, 이를 토대로 웹 취약점 점검이 정탐인지 오탐인지 판별해보려고 해.{parsed_json} 이게 json 데이터야.
json 데이터를 너가 전체적으로 봤으면 좋겠어. 
이게 점검한 웹 소스코드야. {web_source} 이 공격이 실제 영향력이 있는지 "코드기반"으로 확인해줘. 
"코드의 어느 부분이 취약한지 알려줘". 그 이유도 포함해서. 패치 방법은 알려주지 않아도 돼.
""")
# web_source = {login_content}, {search_content}
print(response.text)
