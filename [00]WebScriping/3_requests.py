# requests 를 사용하기 위해서는 
# pip install requests
# 을 설치 해야 한다.

import requests

res = requests.get("http://naver.com") # url에 접속해서 정보를 가지고 온다.
print("응답코드 : " , res.status_code)  # 200 : 정상, 403 : 접근 권한이 없다]

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 있다")

res.raise_for_status()  # 정보 접근이 되면 작동하고 실패하면 에러를 출력
print("웹 스크래핑 진행")   # 문제가 있으면 이거 실행안되고 프로그램 종료 된다.

# 그래서 보통
res = requests.get("http://google.com")
res.raise_for_status()
# 이렇게 쌍으로 사용한다.

print(len(res.text))    # 페이지에 있는 문자들의 수
print(res.text) # 페이지에 있는 문자들을 볼수 있다.

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
# mygoogle 파일이 만들어지면 기본 브라우저 열기로 확인해보자
