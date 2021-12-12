# 사용자 정의 에러
# 클래스를 먼저 만들어야 한다.
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
        #raise BigNumberError    # 여기에 사용자 지정 에러를 적는다.
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))    # 메세지를 저장하고 에러가 있으면 반환
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력했다. 한 자리 숫자만 입력해")
# except BigNumberError:
#     print("에러가 발생 했다. 한 자리 숫자만 입력해")
except BigNumberError as err:   # 에러를 받는 것이다.
    print("에러가 발생 했다. 한 자리 숫자만 입력해")
    print(err)