import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}


res = requests.get(url, headers=headers)
res.raise_for_status()

with open("coding.html", "w", encoding="utf8") as f:
    f.write(res.text)


# user agent string 을 검색 해 보자
# https://www.whatismybrowser.com/detect/what-is-my-user-agent
# 여기에 있는 것이 나와 유저정보이다!!!!
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
# 유저 정보를 입력하면 웹 정보를 가지고 올 수 있다.