'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사이다.
50명의 승객고 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해진다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 한다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 35분)

총 탑승 승객 : 1 명
'''
from random import *
ox = "O"
count = 0
for person in range(1,51):
    time = (random() * 46) + 5
    if 5 < time < 15:
        ox = "O"
        count+=1
    else:
        ox = " "
    print("[{0}] {1}번째 손님 (소요 시간 : {2}분".format(ox, person, int(time)))
print("총 탑승 승객 : {0} 명".format(count))


cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        ox = "O"
        cnt += 1
    else:
        ox = " "
    print("[{0}] {1}번째 손님 (소요 시간 : {2}분".format(ox, person, time))
print("총 탑승 승객 : {0} 명".format(count))