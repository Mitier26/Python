# 번호가 1 2 3 4
# 번호에 100을 더하기로 했다.

student = [1,2,3,4,5,6]
print(student)
student = [i+100 for i in student]
print(student)

# 이름을 길이로 변환
name = ["고구마", "감자", "슈퍼히어로김삼똥"]
name = [len(i) for i in name]
print(name)

# 이름을 대문자로
name = ["Long Man", "Big Man", "Super Girl"]
name = [i.upper() for i in name]
print(name)