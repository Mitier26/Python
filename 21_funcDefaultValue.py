def profile(name, age, main_lang):
    print("이름 : {0} \t나이 : {1} \t주 사용 언어 : {2}" \
        .format(name, age, main_lang))
# \ : 줄 바꿈 한 줄로 인식 한다. 파이썬은 엔터를 인식 하는거 같다

profile("감자", 22, "자바")
profile("고구마", 22, "파이썬")

# 만약 같은 같은 언어를 쓴다면
# 기본값을 설정 해 준다.
# 매개변수를 만들때 기본값을 정해준다.
def profile1(name, age=24, main_lang="파이썬"):
    print("이름 : {0} \t나이 : {1} \t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile1("감자")
profile1("고구마")