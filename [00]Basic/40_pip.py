# 잘만들어진 패키지를 가지고와서 사용하는 방법
# 구글에 pypi 검색 하면 패키지들이 있다.
# pypi에서 필요한것을 검색을 하고 pip install beautifulsoup4 을 복사해 온다.
# 복사해온것을 아래 터미널에서 실행 하자

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip lise 
# 지금 설치 되어 있는 패키지들을 확인 할 수 있다.

# pip show 패키지이름
# 패키지에 있는 자세한 정보를 볼 수 있다.

# pip install --upgrade 패키지이름
# 패키지 없데이트 하기

# pip uninstall 패키지이름
# 패키지 삭제 하기