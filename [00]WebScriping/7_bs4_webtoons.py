import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록을 가져 온다.
cartoons = soup.find_all("a", attrs={"class":"title"})
# a 태그이고 class 속성이 title인 모든 것을 가지고 온다. 리스트로 반환

for cartoon in cartoons:
    print(cartoon.get_text())