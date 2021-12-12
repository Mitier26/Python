weather = input("오늘의 날씨는 ? ")
# if 조건 : 실행문
if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비가 필요 없다")

temp = int(input("기온은 어떤가 ? "))
if 30 <= temp : 
    print("너무 더워")
elif 10 <= temp and temp < 30:
    print("좋은 날씨")
elif 0 <= temp < 10:
    print("약간 추워")
else:
    print("너무 추워")