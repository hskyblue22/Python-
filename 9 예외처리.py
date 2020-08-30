A = (3,6,9)
try:
    #  print(a)                            # NameError
    #  print(A[3])                         # IndexError 
    #  melon = A[2] / 0                    # ZeroDivisionError
     print( input("아무 숫자나") / 4 )    # TypeError

except NameError:
    print("NameError")
except IndexError:
    print("IndexError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except Exception as err:                 # 위에 에러들 제외한 모든 에러 발생시 출력됨            
    print("원인 불명 에러")               # "except:""  또는   "except  Exception:"

'''1) try: ~~ except:
      try 아래 실행되다가 오류가 발생하면 -> except 순서대로 실행하면서 같은 에러일 경우 print() 출력
   2) except Exception as err : err이라는 예외변수 생성
                                발생한 예외에 대한 정보를 얻을 수 있음''' 
 
try:
    num = []
    num.append( int(input("첫 번째 숫자를 입력하시오")))
    num.append( int(input("두 번째 숫자를 입력하시오")))
    num.append( int(num[0] / num[1]))
    print("{0} / {1} = {2}".format(num[0], num[1], num[2]))
except ValueError as e:
    print(e)
except IndexError as er:
    print("에러가 발생했습니다.")
    print(er)




#==========================에러 발생시키기============================

class BignumberError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):   #str => 내장함수X , 파이썬의 기본내장클래스 (__str__메서드 호출한다.)
        return self.msg
    #pass

try:
    print("한 자리 숫자 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자 입력: "))
    num2 = int(input("두 번째 숫자 입력: "))
    if num1 >= 10 or num2 >=10:
        raise BignumberError("입력값 : {} , {}".format(num1, num2))
    print("{} / {} = {}".format(num1, num2, round(num1/num2,2)))    #여기까지 입력하고 디버깅하면 syntacError(EOF) 오류남
except ValueError:
    print("한 자리 값만 입력하세요.")
except BignumberError as errr:
    print("에러발생! 한 자리 값만 입력하세요")
    print(errr)

