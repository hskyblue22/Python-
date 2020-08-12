# print( "대기번호 : 1")
# print( "대기번호 : 2")
# print( "대기번호 : 3")
# print( "대기번호 : 4")
# print( "대기번호 : 5")
# ===> for문 없이는 같은 문장을 반복해서 출력해 줘야 한다.

# ======== for 문 ========
# for 변수 in 리스트(튜플, 문자열):
#    수행될 문장
# ===> 리스트나 튜플, 문자열의 첫 번째 요소부터 마지막 요소까지 차례로 변수에 대입되어 수행할 문장이 수행된다.

# 방법 1
for wait_num in [1,2,3,4,5]:
    print("대기번호 : {}".format(wait_num))

# 방법 2 
wait_num = range(1,6)
for number in wait_num:
    print("대기번호 : {0}".format(number)) 

'''1) waiting = range(1,6)
      for number in waiting:
          print("대기번호 : {0}".format(waiting))
    ===> "대기번호 : range(1,6)" 만 5번 출력된다. 주의하자. 
   2) waiting = list(range(1,6))
      for number in waiting:
          print("대기번호 : {0}".format(waiting))
    ===> "대기번호 : [1,2,3,4,5]" 만 5번 출력된다. 주의하자. '''

# 방법 2-1
cafe = ["몰랑이" , "삐약이", "캥거루"]
for customer in cafe:
    print("{}님, 음료가 준비되었습니다.".format(customer))


# for 한 줄로 (updated 8.10)
students = ["몰랑이", "죠르디", "라이언"]
students = [i + "S2" for i in students]
print(students)

people = ["Spider man", "Star lord","Gamora"]
people = [i.upper() for i in people]
print(people)

'''1) i.upper() : ()꼭 적어주자!'''