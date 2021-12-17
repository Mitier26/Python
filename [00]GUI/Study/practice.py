# zip
# 이란 무엇인가!!!!!
# 리스트를 합치고 분해 한다!!!!

kor = ["사과", "바나나", "오랜지"]
eng = ["apple", "banana", "orange"]

print(list(zip(kor, eng)))

mixed = [('사과', 'apple'), ('바나나', 'banana'), ('오랜지', 'orange')]
print(list(zip(*mixed)))

kor2, eng2 = zip(*mixed)
print(kor2)
print(eng2)