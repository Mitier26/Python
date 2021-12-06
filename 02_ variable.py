# 애완동물을 소개해 주세요~
animal = "강아지"
name = "토리"
age = 7
hobby = "산책"
is_adult = age > 4

'''
이것은 여러 문장을 한번에 주석 하는 것이다.
ctrl + /
는 주석의 단축키 이다.
'''

print("우리집 "+animal+"의 이름은 " + name +"이예요")
print(name+"는 " + str(age) + "살이며," + hobby +"을 아주 좋아해요")
# + 가 아닌 , 로 사용할 수 있다. 문자형이 아니여도 그대로 사용가능하다.
# 단, [,] 를 사용하면 띄어쓰기가 무조건 들어 간다.
print(name,"는 " , age , "살이며," , hobby ,"을 아주 좋아해요")
print(name + "는 어른인가요? " + str(is_adult))