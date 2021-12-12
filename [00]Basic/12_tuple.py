# tuple 튜플
# 리스트와 다르게 내용의 변경과 추가를 할 수 없다.
# 대신 리스트 보다 속도가 빠르다.

menu = ("돈까스","치즈까스")
print(menu[0])

name = "감자"
age = 44
hobby = "운동"
print(name, age, hobby)

(name, age, hobby) = ("감자", 44, "운동")
print(name, age, hobby)

# 미리 값을 정해 주고 사용해야 한다.
# 검색 기능을 만드는 것에 유용