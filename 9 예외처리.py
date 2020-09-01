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
'''0) Bignumber(Exception) : 대부분의 예외클래스는 Exception 클래스의 하위 클래스이다.
   1) str 메서드[def __str__(self)] : 문자열화 해주는 함수 선언 
                                      return 으로 값 반환해주기
      init 메서드 : 클래스 생성시 자동으로 실행되는 메서드
   2) 파이썬에서는 모든 변수들이 변수이자 인스턴스이다. (까먹어서 다시 메모)
   3) 어떤 값에 대해 ‘+’, ‘-‘ 등의 연산자를 실행 => 파이썬 내부적으로 ‘__add__’, ‘__sub__’
      메소드를 실행하는 것과 동일하다. '''

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
finally:
    print("계산기를 종료합니다^^")

'''4) if 조건:
          조건 충족시 실행되는 문장
      if 조건 충족되지 않을 때 실행되는 문장  ==> if문 바로 아래에 else를 쓰지 않고도 사용가능하네? 
   5) finally : 예외처리구문에서 오류가 발생해도, 발생하지 않아도 실행된다.
                없는 파일을 열려고 하거나 리스트에 없는 값에 접근하려고 할때 프로그램 강제종료를 방지하여 완성도를 높임'''