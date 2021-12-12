cabinet = {3:"감자" , 100:"고구마"}

print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

# 오류 처리
#print(cabinet[5])       
# [] 일 경우 키가 없으면 프로그램이 멈춘다
print(cabinet.get(5))   
# get 일 경우 프로그램음 None을 출력하고 멈추지 않는다.
print(cabinet.get(5, "사용 가능"))
# None 가 아닌 다른 값을 출력하게 하는 것이 가능 하다.

# 3 이라는 키가 있냐? 확인 가능
print( 3 in cabinet)
print( 5 in cabinet)

# 새로운 키와 값을 넣는 방법
cabinet[266] = "양퍄"
# [] 안에 키를 넣고 값을 넣어야 한다.
print(cabinet)

# 키와 값을 삭제
del cabinet[100]
print(cabinet)

# 사용하는 키만 출력
print(cabinet.keys())

# 사용하는 값만 출력
print(cabinet.values())

# 키와 갑을 확인
print(cabinet.items())

# 모든 값을 제거
cabinet.clear()