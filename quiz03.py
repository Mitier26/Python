'''
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제와 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

예) 생성된 비밀 번호 : nav51!
'''

mstr = "http://naver.com"
mstr = mstr[7:]
print(mstr)
index = mstr.index(".")
mstr = mstr[:index]
print(mstr)

pas = mstr[:3] + str(len(mstr)) + str(mstr.count("e")) + "!"
print(pas)

url = "http://naver.com"
my_str = url.replace("http://" , "")
my_str = my_str[:my_str.index(".")]

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "1"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))

# 중요!!!
# str는 변수 기능을 쓸때 사용한다. 다른 언어에서 사용 하듯 str 을 변수로 사용하지 말자.
# 문자열을 합할 때는 str 을 앞에 적어 주어야 한다.