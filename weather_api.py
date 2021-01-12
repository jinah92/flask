import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst"
service_key = os.getenv('WEATHER_API_KEY')

# 웹 요청시 같이 전달될 데이터 = 요청 메시지
params = {
    'serviceKey' : service_key,
    'numOfRows' : 30,
    'pageNo' : 1,
    'dataType' : 'JSON',
    'base_date' : '20210111', # 오늘 날짜
    'base_time' : '1400', # 요청 가능 발표 시간
    'nx' : 62, # 성남시 운중동
    'ny' : 123
}

res = requests.get(url=url, params=params)
print(res.status_code, type(res.text), res.url)
print()
print(res.text)