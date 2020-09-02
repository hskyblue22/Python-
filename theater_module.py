# module : 코드가 들어있는 파일  ==> 파일명은 모듈명으로!(모듈명.py : 모듈확장자)
# package : 모듈들의 합
# 패키지 == 라이브러리
# 패키지 == 모듈1 + 모듈2

def price(person):
    print("{0}명의 티켓 가격은 {1}입니다.".format(person,person*10000))

def price_soldier(person):
    print("{0}명의 티켓 가격은 {1}입니다.".format(person,person*5000))

def price_morning(person):
    print("{0}명의 티켓 가격은 {1}입니다.".format(person,person*6000))

