from random import *

print(random())             # 0.0 ~ 1.0 사이의 임의의 값을 생성
print(random() * 10)        # 0.0 ~ 10.0 사이의 이의의 값을 생성
print(int(random()*10))     # 0.0 ~ 10.0 사이의 정수 값을 생성
print(int(random()*10) + 1) # 1 ~ 10 이하의 임의의 정수 값을 생성

# 로또 값을 출력
print(int(random() * 45 ) + 1)

print(randrange(1, 46))     # 1 ~ 46 미만의 값을 생성

# 차이 : 위에 것은 46이 포함되지 않는다.
print(randint(1, 45))        # 1 ~ 45 이하의 값을 생성
