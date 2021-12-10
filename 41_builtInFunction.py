# 내장함수

# input : 사용자 입력을 받는 함수
lang = input("무슨 언어를 좋아하니?")
print("{0} 은 좋다".format(lang))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())
print(dir(random))

lst = [1,2,3]
print(dir(lst))

# 구글에 파이썬 내장 함수를 검색해 보자 : 단 영어로 검색?