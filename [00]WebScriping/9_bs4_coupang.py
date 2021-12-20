import requests
import re
from bs4 import BeautifulSoup


url = "https://www.coupang.com/np/search?q=%EB%AC%B4%EC%84%A0%ED%82%A4%EB%B3%B4%EB%93%9C&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=1%23attr_13347%2428317%40DEFAULT&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class" : "name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge=text"})
    if ad_badge:
        print(" <광고 상품 제외")
        continue

    name = item.find("div", attrs={"class":"name"}).get_text()

    # 애플 제품 제외
    if "Apple" in name:
        print("   <Apple 상품 제외>")
    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    # 리뷰 100개 이상, 평점 4.5 이상되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"})    # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        continue

    rate_cnt = item.find("span", attrs={"class":"ration-total-count"})
    if rate_cnt:
        rate_cnt = rate.get_text() # 출력 (25)
        rate_cnt = rate_cnt[1:-1]   # -1 젤뒤
    else:
        rate = "평점 수 없음"
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 50:
        print(name, price, rate, rate_cnt)

    
    