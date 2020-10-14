'''1) ID와 PW룰 입력받아 로그인한 모든 사람에게 'Welcome'라는 문장을 출력하되, ID가 'admin'이고
PW가 '1234'인 경우에는 'Welcome manager'라는 문구를 그보다 먼저 출력하는 프로그램을 작성하라.

==> ID가 'admin'이고 PW가 '1234'인 경우에는 두 개의 문구 모두 출력되어야 함 주의! '''

# id = input('ID: ')
# pw = input('PW: ')
# if id == 'admin' and pw =='1234':
#     print('Welcome manager')
# print('Welcome')


'''2) 3 2 1 이 출력된다.

==> 정수 0은 False이기 때문에 출력되지 않음 주의! ''' 

# i = 3
# while i:
#     print(i)
#     i = i-1


'''3) 다음과 같이 숫자의 개수와 여러가지 숫자를 입력받아, 각 숫자를 입력받은 순서의 반대로 출력하자. 

몇 개?: 3
숫자 1: 19
숫자 2: 34
숫자 3: 25
25
34
19

==> 숫자 입력받아 사용한다는 것 잊지 않기 
==> numbers = numbers + [x] : 리스트에 정보를 추가하기 위하여 리스트 덧셈을 이용하려면, 입력받은 정보를 
    리스트에 담긴 형태로 바꿔줘야 한다. 리스트와 정수 사이에서는 + 연산자를 사용할 수 없기 때문이다. 
==> numbers[] (O)  /  numbers.[] (X) 
    "숫자" + str(i) + ":"  : str으로 바꿔주는 것 잊지 말자
    '''

# n = int(input("몇 개?: "))
# numbers = []
# for i in range(1,n):
#     x = input("숫자 "+str(i)+":")
#     numbers = numbers + [x]
# for re in range(n-1,-1,-1):
#     print(re)

n = int(input("몇 개?: "))
numbers = []
i =1
while i <= n:
    x = input("숫자 "+str(i)+":")
    numbers = numbers + [x]
    i += 1
i = n-1
while i >= 0:
    print(numbers[i])
    i -= 1

