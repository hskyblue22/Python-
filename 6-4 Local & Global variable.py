# 1 
cake = 20                    # Global variable(전역변수)- 너무 많이 사용하면 코드 꼬임

def check(customer):
    global cake              # 전역공간에 있는 cake 사용
  #cake = 15                # Local variable(지역변수)
    cake = cake - customer
    print("[함수 내] 남은 케이크 개수: %s"%cake)

print("전체 케이크 : %s"%cake)
check(4)
'''>>>1) cake = cake - customer 만 적은 경우!!
         UnboundLocalError: local variable 'cake' referenced before assignment
         함수 내 cake(지역변수) 는 정의되지 않은 상태이다. 
         cake = 20 (전역변수)와는 다른 변수로 인식
      2) cake = 15 적은 경우!!
         [함수 내] 남은 케이크 개수: 11 
      3) global cake 적은 경우
         [함수 내] 남은 케이크 개수: 16 '''

print("남은 케이크 : %s"%cake)           
'''>>> 1) global cake 코드 X   ==> 남은 케이크 : 20
       2) global cake 코드 O   ==> 남은 케이크 : 16 '''


# 2
tart = 50

def check1(tart, togo):
    tart = tart - togo
    print("[함수 내] 남은 타르트 : {}".format(tart))
    return tart

# check1(tart,10) 
# print("남은 타르트 : %s" %tart)
'''>>> check1(tart,10) :                 [함수 내] 남은 타르트 : 40
       print("남은 타르트 : %s" %tart) :  남은 타르트 : 50 '''

tart = check1(tart,10)
print("남은 타르트 : %s" %tart)     
'''>>> return tart 없는 경우 :            남은 타르트 : None
       return tart 있는 경우 :            남은 타르트 : 40 '''
