import json

# JSON 문자열 생성
text1 = '{"이름":"최진아", "나이": 30}'
data1 = json.loads(text1)
print(data1, type(data1))

# dict를 JSON 문자열로 생성
data2 = "{'이름': '최진아', '나이': 30}"
text2 = json.dumps(data2)
print(text2, type(text2))

# dict를 JSON 문자열로 생성(유니코드 아닌 그대로 변환)
text3 = json.dumps(data2, ensure_ascii=False)
print(text3, type(text3))