# 당신의 학교에서 파이썬 코딩대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
# 조건3: random 모듈의 shuffle과 sample을 활용

# (출력예제)
#  -- 당첨자 발표 --
#  치킨 당첨자 : 1
#  커피 당첨자 : [2,3,4]
#  -- 축하합니다 --

# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

print("="*10 +" 방법 1 " + "="*10)
from random import *
id = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(id)
print(id)

prize = sample(id,4)
(chiken , coffee) = (prize[0] , prize[1:])

sentence =  f""" -- 당첨자 발표 -- 
치킨 당첨자 : {chiken}
커피 당첨자 : {coffee}
 -- 축하합니다 -- """
print(sentence)


print("="*10 +" 방법 2 " + "="*10)
users = range(1,21)
print(type(users))

users = list(users)
shuffle(users)
print(users)

winners = sample(users,4)

print(""" -- 당첨자 발표 -- 
치킨 당첨자 : {0}
커피 당첨자 : {1}
 -- 축하합니다 -- """.format(winners[0],winners[1:]))

'''1) range함수 : 1~21 미만의 연속된 정수 출력
   2) type(users) : users 의 type 출력(class 'range') 
   3) shuffle함수 : 리스트 원소 무작위로 섞기 (오직 list만 가능)
   4) sample(변수, 뽑을 개수) : 랜덤하게 정한 개수에 맞게 추출해준다.'''