import json
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyB4mgp-9DoH8njhPp9B66S1wf48TtjNBr0"
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


json_data = [
    "method",
    "evidence",
    "description",
    "inputVector",
    "url",
    "param",
    "name",
    ""
]
content = {search_content}, {login_content}
print("ask:", content )
response = model.generate_content(f"{content} 코드에 대해 설명해줘.")

print(response.text)