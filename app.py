# pip install requests로 requests 라이브러리를 설치
# 요청과 응답을 통해 지정한 사이트에서 텍스트 추출까지

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
response = requests.get("https://www.example.com", headers=headers)
print(response.text)



