# 방법1
import theater_module             # .py 붙이지 않기
theater_module.price(4)
theater_module.price_morning(3)
theater_module.price_soldier(5)   # theater_module 반복됨

# 방법2
import theater_module as tm       # theater_module 반복을 피하기 위해 tm으로 이름붙임
tm.price(3)
tm.price_morning(2)

# 방법3
from theater_module import *      # from random import *
price(6)
price_soldier(4)

# 방법4
from theater_module import price,price_morning    #theater_module이름의 모듈에서 price와 price_morning을 가져다 쓰겠다.
price(7)

# 방법5
from theater_module import price_soldier as cheap
cheap(5)




'''[import 모듈]
→ 해당 모듈 전체를 가져온다.
  사용하려면 항상 '모듈명.메소드' 와 같이 모듈명을 앞에 붙여주어야 한다.

   [from 모듈 import 메소드 / 변수]
→ 해당 모듈 내에 있는 특정 메소드나 모듈 내 정의된 변수를 가져온다.
  가져온 메소드나 변수를 앞에 모듈명을 붙이지 않고 그대로 사용할 수 있다.
  다만, 이름이 같은 변수나 메소드가 존재할 경우 대체된다.

  from 모듈 import * 이라고 하면 import 모듈과 동일

출처: https://driz2le.tistory.com/207 [홀로 떠나는 여행] '''
