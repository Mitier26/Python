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

def print_match(m):
    if m:
        print("m.group() : ", m.group())    # 일치하는 문자열 반화
        print("m.string : ", m.string)      # 입력받은 문자열
        print("m.start() : " , m.start())   # 일치하는 문자열의 시작 index
        print("m.end() : " , m.end())       # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())      # 일치하는 문자열의 시작 / 끝 index

    else:
        print("매칭되지 않음")

print_match(m)

m = p.match("careless")
print_match(m)
# 이것이 매치되다고 나온다 왜??
# 처음부터 확인해서 일치하는지 확인한다.
# 앞에서 부터 4 개가 같기 때문에!!!

# search : 주어진 문자열 중에 일치하는것이 있는지 확인
m = p.search("good care")
print_match(m)

m = p.search("careless")
print_match(m)

# 일치하는 모든 것을 리스트 형태로 반환
lis = p.findall("careless")
print(lis)


# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열")       # 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열")      # 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = findall("비교할 문자열")     # 일치하는 모든 것을 "리스트" 형태로 반환

# w3school
# RegEx 에서 공부할 수 있다.
# python re 검색