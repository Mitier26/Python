# 반복문
# 단어 리스트
# _ 줄 표시
# for 단어 검색
# 입력ㅡㅡ
from random import *
words = ["apple", "banana", "orange"]
word = choice(words)
print("answer : " + word)

letters = "" # 입력 받은 글자 보관

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success")
        break

    letter = input("Input Letter : ")
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")