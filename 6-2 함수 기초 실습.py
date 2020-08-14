def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()

def deposit(balance,money):
    print("입금이 완료되었습니다. 잔액은 %s원입니다." % (balance+money))
    print("입금이 완료되었습니다. 잔액은 %s원입니다." % int(balance+money))
    print("입금이 완료되었습니다. 잔액은 %s원입니다." % str(balance+money))
  # print("입금이 완료되었습니다. 잔액은 %s원입니다." % balance+money) 
  # >>> 오류남. TypeError: can only concatenate str (not "int") to str
    return balance + money

# balance = 0
# a = deposit(balance,1000)
# print(a)
# print(balance)
'''>>> 1000 : 변수 a에는 함수의 결과값으로 return값인 [balance + money]가 들어간다.
       0 : balance가 계속 0으로 되어있으므로 출력값은 0이다. '''

balance = 0
balance = deposit(balance,1000)
print(balance)
'''>>> 1000: balance에 함수의 반환값으로 return값인 [balance+money]가 들어간다. '''


def withdraw(balance,money):
    if balance > money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = withdraw(balance,2000)
balance = withdraw(balance,300)


def withdraw_night(balance,money):
    if balance > money:
        commission = 100
      # print("수수료는 {}원입니다. 잔액은 {}원입니다.".format(commission, balance-money-commission))
        return commission , balance-money-commission        # 반환값으로 2개 받을 수도 있다.

commission,balance = withdraw_night(balance,200)
print("수수료는 {}원입니다. 잔액은 {}원입니다.".format(commission,balance))



