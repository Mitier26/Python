# 필요한 부분만 잘라내는 것
jumin = "970925-2987653"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])     # 0 ~ 2 전까지  0, 1 번째 값
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 " + jumin[:6])  # 처음 부터 6 까지
print("뒤 7 자리 " + jumin[7:]) # 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])