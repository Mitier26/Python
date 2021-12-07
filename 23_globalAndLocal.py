gun = 10

def checkpoint(soldiers):
    #gun = 20 # 이것이 내부 변수 이다.
    global gun  # 밖에 있는 전역 변수 gun을 사용 하겠다는 의미
    gun = gun - soldiers
    print("[함수 내부] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내부] 남은 총 : {0}".format(gun))
    return gun

# 오류가 발생한다.
# checkpoint 내부에 있는 gun은 외부에 있는 gun이 아니다.
print("전체 총 :  {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))