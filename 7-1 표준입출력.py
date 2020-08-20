# 표준 입력(stdin)함수    ==> input()
# 표준 출력(stdout)함수   ==> print()

# sep= " , "   : 각 인자들 사이를 ,로 채우기  
# end= " ? "   : 앞 문장의 끝부분을 ?로 넣고 뒷 문장을 연달아서 한줄에 출력 
print("cake", "tart" ,"dacquoise", sep=", ", end = " 하나만 선택하세요. ")
print("전부 다 주세요!")
'''1) print("cake" "tart", "dacquoise", sep=", ", end = " 하나만 선택하세요. ") 
      ==> cake와 tart는 서로 붙어서 출력. sep로 지정한 ,가 사이에 끼지 않는다. '''

# "stdout" vs "stderr" : 출력결과는 같아 보임.
import sys
print("Python", "Java", file=sys.stdout)        # 표준출력으로 처리
print("Python", "Java", file=sys.stderr)        # 표준에러로 처리
'''3) stderr : 따로 로깅해서 에러처리 해주어야 한다. '''

# dictionary.items() : 딕셔너리의 (key, value) 값을 한꺼번에 반환
# .ljust(5), rjust(5)
scores = {"수학":40 , "외국어":70, "코딩":100}
for subject,score in scores.items():
      print(subject.ljust(2), str(score).rjust(4), sep = " : ")
    # print(subject,score)

'''2) for 뒤에 2개 변수 사용 가능  ==> subject-key  /  score-value  
   3) 변수.ljsut() : 뒤에 숫자만큼 자리 확보하여 왼쪽으로 정렬
      변수.rjust() : 뒤에 숫자만큼 자리 확보하여 오른쪽으로 정렬
   
   4) print(subject.ljust(8,"0"), str(score).rjust(4,"t"))   : 0으로 채우기 / t로 채우기
      >>> 수학000000 tt40
          외국어00000 tt70 
          코딩000000 t100
      >>> "subject.ljust(2)" == "score" : 서로 같게 출력된다.

   5) str(score).rjust(4) ===> 정수를 문자형식으로 바꿔줘야 한다.  '''   

# 은행 대기표
# .zfill(3)  ==>  001, 002, 003 처럼 0으로 3자리 채우기 
for num in range(1, 21):
   print("대기번호 : " + str(num).zfill(3))

#표준입력
# input(사용자입력) 통해서 받는 값은 항상 문자(str)
answer = input("아무 값이나 입력하세요")
print("입력하신 값은" + answer +"입니다.")
'''5) answer에 모든 값 입력해도 print로 잘 출력된다. 
      ex) 10 , 과자 , True , [1,2,3] 가능  '''