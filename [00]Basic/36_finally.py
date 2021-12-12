class BigNumberError(Exception):
    #pass
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >=10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력했다. 한 자리 숫자만 입력해")
except BigNumberError as err:   
    print("에러가 발생 했다. 한 자리 숫자만 입력해")
    print(err)
finally:    # 정상 수행이건 오류이건 [마지막]에 무조건 실행
    print("계산기를 이용해 주어서 감사")