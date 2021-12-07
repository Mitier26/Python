customer = "감자"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았다".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 죽었다.")

# user = "고구마"
# index = 1
# while True:
#      print("{0}, 커피가 준비 되었습니다. {1} 번 남았다".format(customer, index))
#      index += 1

# 컨트롤 + C : 프로그램 강제 종료

customer = "양파"
person = "없음"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 뭐니?")
    