# While 조건:  ==> 조건 성립할 때까지 계속 반복됨
customer = "죠르디"
chance = 5
while chance >= 1:
    print("%s님, 음료 나왔습니다. %s번 남았습니다." %(customer,chance))
    chance-= 1
    if chance == 0:
        print("음료는 폐기처분되었습니다.")

# 무한루프 : 빠져나올때는 terminal창을 누르고 Ctrl + C를 입력하자.
# guest = "라이언"
# say = 1
# while True:
#     print("{0}님, 음료가 준비되었습니다. {1}번 호출되었습니다.".format(guest,say))
#     say += 1

hit = 1
while hit <= 10:
    print("나무를 {}번 쳤습니다.".format(hit))  
    hit = hit+1
    if hit == 11:
        print("나무가 쓰러졌습니다.")

'''1) if hit == 10: (X)    ===>  "나무를 9번 쳤습니다."
                                 "나무가 쓰러졌습니다."
                                 "나무를 10번 쳤습니다." '''
'''2) "나무를 10번 쳤습니다."     (hit = 10)
      11 = 10 + 1                (hit = 11 이 됨)
      if hit == 11:              (hit이 11이야? => if조건 성립한다!)
      "나무가 쓰러졌습니다."
      ===> "나무를 10번 쳤습니다." 다음에 "나무가 쓰러졌습니다."가 출력되도록 하려면 
            [if hit == 10] 이 아닌 [if hit == 11]의 조건이 다음에 와야한다. '''

# 1
customer1 = "죠르디"
customer2 = input("이름이 어떻게 되세요?")
while customer1 != customer2:
    print("%s님, 음료가 준비되었습니다. 픽업대로 와주시길 바랍니다." %customer1)
    customer2 = input("이름이 어떻게 되세요?")

'''3) "이름이 어떻게 되세요?"           ==>  첫번째로 출력됨
      "죠르디님 음료가 준비되었습니다.~  ==>  두번째로 출력됨 '''

# 2
customer1 = "죠르디"
customer2 = "unknown"

while customer1 != customer2:
    print("%s님, 음료가 준비되었으니 픽업대로 와주시길 바랍니다." %customer1)
    customer2 = input("이름이 어떻게 되세요?")

'''4) "죠르디님, 음료가 준비되었으니~ "  ==>  첫번째로 출력됨
      "이름이 어떻게 되세요?"            ==>  두번째로 출력됨'''