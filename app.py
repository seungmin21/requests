# pip install requests로 requests 라이브러리를 설치
# 요청과 응답을 통해 지정한 사이트에서 텍스트 추출까지

import requests

try:
    response = requests.get("https://www.example.com")
    response.raise_for_status()  # 에러가 발생하면 예외를 일으킴
    print(response.text)

except requests.exceptions.HTTPError as errh:
    print ("HTTP Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something went wrong",err)



