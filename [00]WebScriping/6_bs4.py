# pip install beautifulsoup4 설치하자! 스크래핑 패키지
# pip install lxml 설치하자, 구문을 부석하는 파스어

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()  # 문제가 있으면 프로그램 종료

soup = BeautifulSoup(res.text, "lxml")
# 긁어면 문서를 lxml 파스를 이용하여 BeautifulSoup 객체로 만든다.
# soup 이 모든 정보를 가지고 있다.
print(soup.title)
print(soup.title.get_text())
print(soup.a)   # 처음으로 발견된 a 엘리먼트 부분을 가지고 온다.
print(soup.a.attrs) # a 엘리먼트가 가지고 있는 속성을 확인한다.
print(soup.a["href"])

# 콘솔창 삭제 : 콘솔창에서 cls

# 스크리핑 하려는 페이지의 정보를 모를때 사용하는 방법
print(soup.find("a", attrs={"class":"Nbtn_upload"}))   # a 태그에 해당하는데 클래스의 속성이 Nbtn_upload 것을 찾아
print(soup.find(attrs={"class":"Nbtn_upload"})) # Nbtn_upload 이 페이지 내부에 유일하기 때문에 가능

# 1 ~ 10 등의 정보
print(soup.find("li", attrs={"class":"rank01"}))
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)

# 부모, 자식, 형제 찾기
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a.get_text())   # 현재 랭킹1등의 정보를 가지고 온다
print(rank1.next_sibling)   # 이것이 출력이 안된다.
print(rank1.next_sibling.next_sibling)  # 두번해야 출력
# 이유는 개행 정보 가 있기 때문이다.
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())
rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

# 부모로 올라가기
print(rank1.parent)

# 개행이 있다고 next_sibling 을 2 번 사용하는것이 이상하다, 개형이 없는것도 있을 것이다.
rank2 = rank1.find_next_sibling("li")   # li 기준으로 li 인것들만 찾는다
print(rank2.a.get_text())
rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

# 1 ~ 10 개
print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="입학용병-59화")
print(webtoon)

