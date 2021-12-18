# 정규식 : 정해진 형태의 규칙
# 주민등록번호 : 000000 - 0000000
# 이메일 : ooooo@naver.com
# 차량번호 : 111가 1234
# IP 주소 : 192.168.0.2

import re   # 정규식 라이브러리
# 차량번호가 4자리 문자라면
# 만약 3개만 기억한다면
# ca?e
# care, cafe, case, cave 등 검색을 할때

p = re.compile("ca.e")  
# . (ca.e) : 하나의 문자를 의미 : ca[r]e, ca[f]e
# ^ (^de) : 문자열의 시작 : desk, destination (O) | fade (X)
# $ (se$) : 문자열의 끝 : case, base (O) | face (X)

m = p.match("case")
print(m.group())    # 메치되지 않느면 에러 발생

m = p.match("caffe")
# print(m.group())    # 메치되지 않느면 에러 발생
# ca.e 는 문자가 1개 들어 가야하는데 ff 2개가 있어서 에러가 발생했다 

if m:
    print(m.group())
else:
    print("매칭되지 않음")