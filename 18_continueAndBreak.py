absent = [2,5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0} 수업끝, 옥땅으로 따라와".format(student))
        break
    print("{0}, 책을 읽어라".format(student))

# contunue 아래 것을 실행 하지 않고 다음 번호로 가라
