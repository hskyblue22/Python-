# 1) 입력값(전달값)이 없는 함수
def say():
    return "Hi"

say()
a = say()
print(a)
'''>>>    : print가 없어서 출력 안됨
   >>> Hi : return이 있어서 출력됨'''

# 2) 결과값(반환값)이 없는 함수(return이 없다)
def add(c,d):
    print("{0}과 {1}의 합은 {2}입니다.".format(c,d,c+d))

add(3,4)
test = add(4,7)                # 오류있음
print(test)
'''>>> 3과 4의 합은 7입니다.
   >>> 4과 7의 합은 11입니다.
   >>> None : return이 없기 때문에 none이 나온다.
              [문자열을 출력한다.(print)] 와 [반환값이 있다.(return)] 는 매우 다르다.'''

# 3) 입력값, 결과값 모두 없는 함수
def talk():
    print("Hello")

talk()
b = talk()                      # 오류있음
print(b)
'''>>> Hello
   >>> Hello
   >>> None : return이 없기 때문에 none이 나온다.'''


# <print와 Return의 차이>
# print : 함수에 영향 주지 않음. 괄호 안의 값을 단순히 입력
#         함수 내부 코드에 return이 입력되어 있지않으면 함수의 마지막 부분에 자동으로 "Return None"을 입력한다.
# return : 위치한 자리에서 함수를 종료시킴. 해당 위치의 값을 리턴값으로 출력함
          
def practice(z,y):
    print(z+y)
    # return None
print("합한 값은 %s입니다." %practice(5,8))

'''>>> None : 함수의 리턴값(결과값)을 집어넣어 출력한다. '''

def bbo(x,w):
    return x+w
print("합한 값은 %s입니다."%practice(5,8))

'''>>> 13 : 함수의 리턴값(결과값)을 집어넣어 출력한다. '''