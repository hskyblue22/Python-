# 랜덤함수 쓸 때마다 헷갈려서 정리해 놓음

from random import *

print(random())               # 0 ~ 1 미만의 난수 생성
print(random()*10)            # 0 ~ 10 미만의 난수 생성
print(random()*100)           # 0 ~ 100 미만 난수 생성
print((random()*10) + 4 )     # 4 ~ 14 미만의 난수 생성
print((random()*35) + 1)      # 1 ~ 35 이하의 난수 생성

print(int(random()*45) +1)    # 1~ 45 이하의 난수 생성 (int를 써서 정수형태로)
print(int(random()*45) +1)    # 1~ 45 이하의 난수 생성

print(randrange(1,46))        # 1 ~ 46 미만의 난수 생성 (정수 형태)
print(randrange(1,46))        # 1 ~ 46 미만의 난수 생성

print(randint(1,45))        # 1 ~ 45 이하의 난수 생성 (정수 형태)
print(randint(1,45))        # 1 ~ 45 이하의 난수 생성