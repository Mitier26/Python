import sys

print("Python", "Java")
print("Python", "Java", sep=",")
# 문자열 사이에 ',' 넣으면 한 칸 띄어서 출력이 된다.
# 뒤에 sep= 을 넣으면 ','의 기능을 재정의 할 수 있다.
print("Python", "Java", "JavaScript", sep=" vs ")
print("Python", "Java", sep=",",end="?")
print("무었이 재미있게요?")
# end : 출력의 마지막에 ? 를 넣으라는 것
# 그리고 [줄바꿈]을 하지 말고 이어서 출력하라는 것이다.
# 왜일까요? 기본적으로 문장의 마지막에는 줄바꿈 이라는 것이 있다.
# 그것이 ? 로 변한 것이다.


print("Python", "Java", file=sys.stdout)        # 표준 출력
print("Python", "Java", file=sys.stderr)        # 표준 에러

score = {"수학" :0, "영어":50, "코딩":100}
for subject, score in score.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 두둥!!!!
# 딕셔러니일 경우
# items() 를 이용해야 한다.
# subject = "수학", "영어"
# score = 0 , 50
# for 다음 2개가 있는 이유는 반환 값이 2대 이기 때문이다.

# 문자 정렬
# print(subject.ljust(8), str(score).rjust(4))
# ljust(8)              : 8칸의 공간을 확보하고 왼족 정렬
# str(score).rjust(4)   : 4칸의 공간을 확보하고 오른쪽 정렬


# 은행 대기순번표
# 001, 002, 003....
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))
# zfill(3) : 3 개의 공간을 확보 하고 숫자를 적은 후 남은 공간을 0 으로 체운다.


# 표준 입력
answer = input("아무 값이나 입력해 : ")
print(type(answer))
print("입력한 값은 " + answer + "입니다.")

# 입력 받은 값은 항상 "문자" 형식이다.