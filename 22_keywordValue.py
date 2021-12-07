def profile(name , age, main_lang):
    print(name, age, main_lang)

profile("감자", 20, "자바")
profile(name="양파", main_lang="파이썬", age=43)

# 매개변수 키워드를 이용하여 값을 넣어주면
# 순서에 상관 없이 값이 대입된다.

# end = " " : end 앞의 것을 출력하고 다음 것을 이어서 출력 하겠다.
def profile1(name , age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " " )
    print(lang1, lang2, lang3, lang4, lang5)

profile1("고무마", 45, "Python", "Jana", "C", "C++", "C#")
profile1("홍길똥", 34, "Kotlin", "Swift","", "","")

# 가변 인자
# 5개의 언어를 입력해야 하지만 모두 5개만 있는 것이 아니다.
# 7개의 언어를 아는 사람도 있을 것이다.
# 그러면 함수를 새로 만들어야 하는 이상한 현상이 발생한다.
# 이때 사용하는 것이 개변 인자 이다.

def profile2(name , age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end= " " )
    for lang in language:
        print(lang, end = " ")
    print()

profile2("고무마", 45, "Python", "Jana", "C", "C++", "C#")
profile2("홍길똥", 34, "Kotlin", "Swift")