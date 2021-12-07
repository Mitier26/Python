
for waiting in [0,1,2,4,5,6]:
    print("대기번호 : {0}".format(waiting))


# 범위를 정할 수 있다.
for waiting in range(1,6):
    print("대기번호 : {0}".format(waiting))

# 리스트를 넣을 수있다는 것
start = ["아이언", "토오", "나무"]
for customer in start:
    print("{0}, 커피 완료".format(customer))