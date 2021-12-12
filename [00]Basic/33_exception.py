try:
    print("나누기 전용 계산기")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번재 숫자를 입력하세요 : "))
    
    print("{0} / {1} = {2}".format(num1, num2,int(num1/num2)))
except ValueError:  # 무슨 에러이지 알 때 에러를 특정 할 수 있다.
    print("에러! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:    # 이건 들어온 값이 0 일 때 발생하는 에러이다.
    print(err)

# try: except: 문
# 에러가 없으면 위에 , 에러가 있으면 아래


try:
    nums = []
    print("나누기 전용 계산기")
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번재 숫자를 입력하세요 : ")))
    #nums.append(int(num[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력했습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:        # 위에 2가지 외에 발생한 오류에 대해 출력할 때
    # as err : 어떤 에러인지 출력하는 것이다.
    print("알 수 없는 에러가 발생 했다")