import requests
import os
from dotenv import load_dotenv

from test import date_test

load_dotenv(verbose=True)

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
service_key = os.getenv('WEATHER_API_KEY')

base_date, base_time = date_test.createDateTime()

# 웹 요청시 같이 전달될 데이터 = 요청 메시지
params = {
    'serviceKey' : service_key,
    'numOfRows' : 30,
    'pageNo' : 1,
    'dataType' : 'JSON',
    'base_date' : base_date, # 오늘 날짜
    'base_time' : base_time, # 요청 가능 발표 시간
    'nx' : 62, # 성남시 운중동
    'ny' : 123
}

res = requests.get(url=url, params=params)
# print(res.status_code, type(res.text), res.url)
# print()
# print(res.text)

from pprint import pprint
data = res.json()
data = data['response']['body']['items']['item']

# category 표
categorys = {
    'T1H':'기온',
    'RN1':'1시간 강수량',
    'UUU':'동서바람성분',
    'VVV':'남북바람성분',
    'REH':'습도',
    'PTY':'강수형태',
    'VEC':'풍향',
    'WSD':'풍속',
}

# 최종 데이터 생성
results = {}
for d in data:
    results[categorys[d['category']]] = d['obsrValue']

pprint(results)