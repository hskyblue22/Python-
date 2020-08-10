# continue , break : for나 while 문을 이용해 반복적인 작업을 수행하다가 특정 조건일 때 반복문 자체를 빠져나오게 함
# continue : 해당 조건만 건너뜀
# break : 반복문 전체를 빠져나옴 

absent = [2,5]
cheat = [8]

for student in range(1,11):
    if student in absent:
        continue
    elif student in cheat:
        print("%d번, 교무실로 따라와."%student)
        break
    print("%d번, 이 문제 풀어보렴." %student)

'''1) if
      elif   ==> if 다음에 elif를 써주자
   2) if/elif - continue/break - break에서 빠져나감. ''' 


for student in range(1,11):
    print("%d번, 이 문제 풀어보렴." %student)
    if student in absent:
        continue
    elif student in cheat:
        print("%d번, 교무실로 따라와."%student)
        break
'''3) 1번, 이 문제 풀어보렴.            ==> 1부터 10까지 순서대로 출력됨
      2번, 이 문제 풀어보렴.            ==> continue 가 있지만 쓸모가 없다.
      3번, 이 문제 풀어보렴.                continue위에 print()가 있어서 제외되지 않음.
      4번, 이 문제 풀어보렴.
      5번, 이 문제 풀어보렴.
      6번, 이 문제 풀어보렴.
      7번, 이 문제 풀어보렴.
      8번, 이 문제 풀어보렴.
      8번, 교무실로 따라와.  '''
