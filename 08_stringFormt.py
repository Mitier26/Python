print("a" + "b")
print("a","b")

# 방법 1
print("나는 %d살입니다." % 33)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요," % "A")
# %s 로 하면 대부분 출력 가능

print("나는 %s색과 %s색을 좋아해요" %("보라", "파랑"))

# 방법 2
print("나는 {}살입니다." .format(22))
print("나는 {}색과 {}색을 좋아해요".format("보라", "파랑"))
print("나는 {1}색과 {0}색을 좋아해요".format("보라", "파랑"))

# 방법 3
print("나는 {age}살이며, {color} 색을 좋아해요.".format(age = 20, color = "보라"))

# 방법 4 (v 3.6 이상)
age = 44
color = "검정"
print(f"나는 {age}살이며, {color} 색을 좋아해요.")
# 출력문 앞에 f 라로 적어야 한다.