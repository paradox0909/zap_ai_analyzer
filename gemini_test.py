import google.generativeai as genai

GOOGLE_API_KEY="none"

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("해킹의 신 권현준에 대해 한 문장으로 설명해줘.")

print(response.text)