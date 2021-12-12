def open_account():
    print("새로운 것이 생성 되었다.")

open_account()

def deposit(balance, momey):
    print("입급이 완료 되었어. 잔액은 {0} 원".format(balance + momey))
    return balance + momey

def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었어. 잔액은 {0} 원".format(balance - money))
        return balance - money
    else:
        print("잔액이 부족해. 잔액은 {0} 원 이야".format(balance))

# 듀플 형식 반환
def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission

balance = 0
balance = deposit(balance, 2000)
withdraw(balance, 2000)
withdraw(balance, 500)

# 듀플 형식으로 만들었다.
# 형식을 맞추어야 하기 때문에 값을 2개 받아야 한다. 
# 순서도 중요하다.
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원 이다".format(commission, balance))