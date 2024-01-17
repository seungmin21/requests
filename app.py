# pip install requests로 requests 라이브러리를 설치
# 요청과 응답을 통해 지정한 사이트에서 텍스트 추출까지

import requests

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get("https://www.example.com", params=payload)
print(response.url)



