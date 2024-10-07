import requests
import json
# API URL
url = "http://apis.data.go.kr/5050000/dstrctsTrrsrtService/getDstrctsTrrsrt"
# 파라미터 설정
params = {
    "serviceKey": "0OqIh/dSuVpGLLplebEorV4PTg6OC2ht/iiVg0ZabhBfKsX2EJwtAoizU3JjdH/uNz6G/800CT8f6YWfbI8v6w==",
    "pageNo": "1",
    "numOfRows": "164"
}
# API 호출
response = requests.get(url, params=params)
# 응답 확인
if response.status_code == 200:
    # JSON 데이터 파싱
    data = response.json()
    # 필요한 데이터 추출
    if 'response' in data and 'body' in data['response'] and 'items' in data['response']['body']:
        items = data['response']['body']['items']['item']
        for item in items:
            print(f"관광지명: {item['CON_TITLE']}")
            print(f"위도: {item['CON_LATITUDE']}")
            print(f"경도: {item['CON_LONGITUDE']}")
            print("---")
    else:
        print("데이터 구조가 예상과 다릅니다.")
else:
    print("API 호출 실패:", response.status_code)