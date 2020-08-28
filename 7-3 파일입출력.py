# 파일 열어서 내용 불러오거나 파일에 새로운 내용 추가 가능

file_score = open("score.txt", "w", encoding = "utf8")   # file_score : 파일 객체를 저장하는 변수의 이름
print("영어 : 50", file = file_score)
print("수학 : 80", file = file_score)
file_score.close()
'''1) open() : 파일 열기 , open() 안 파일이 만들어진다.
   2-1) w :  write(쓰기) 목적 ==> 아래 print() 내용을 score.txt.파일에 쓸 수 있게 한다. 
             내용추가가 아니므로 디버깅할때마다 기존 데이터가 없어지고 새 데이터로 덮어씌우기가 된다.

   2-2) a : append(추가) 목적 ==> 덮어씌우는 것이 아닌 내용 추가가 된다.
            어떤 내용이 존재하는 파일에서 내용을 이어서 쓸 때 사용
            append를 여러 번 실행해도 계속 추가되는 것이 아니고 추가된 내용만 변한다!
              예) file_score.write("과학 : 40")
                  file_score.write("\n코딩 : 70") 실행 후 

                  file_score.write("과학 : 40")
                  file_score.write("\n코딩 : 90") 으로 하면
                  
               ===  과학 : 40
               ===  코딩 : 90    => 코딩 : 70 에서 코딩 : 90 으로 값이 바뀐다. 아래에 추가되는 것 아님!

   3) encoding = "utf8" : 써줘야 한글 안 깨진다. 
   4) file.close() : open후에 꼭 close를 써서 닫아준다. 
   5) file.write() : 인자로 전달된 문자열을 파일에 쓴다.
                     print()와 달리 자동줄바꿈 X -> \n(탈출문자) 사용 
   6) file.read() : 파일내용 모두 불러오기
   7) file.readline() : 한 줄씩 읽는다. 한 줄 읽은 후에는 커서가 자동으로 아래로 간다.
   8) file.readlines() :리스트에 데이터 넣기! 한 줄 한 줄이 리스트의 원소로 들어간다.때
   9) while문  ==>  txt파일에 총 몇줄이 있는지 모를 때 사용
                    readline()으로 내용이 없을 때까지 한 줄씩 뽑아내고 while로 출력한다. '''

file_score = open("score.txt", "a", encoding = "utf8")
file_score.write("과학 : 40")
file_score.write("\n코딩 : 90")
file_score.close()

file_score = open("score.txt" , "r", encoding ="utf8")
a = file_score.read()
print(a)
file_score.close()

file_score = open("score.txt", "r", encoding = "utf8")
print(file_score.readline(), end = "")  # readline + print ==> 2줄 줄바꿈이 되므로 end ="" 사용해서 한 줄만 띄우게 한다.
print(file_score.readline(), end = "")
print(file_score.readline(), end = "")
print(file_score.readline())
file_score.close()

file_score = open("score.txt", "r", encoding = "utf8")
lines = file_score.readlines()  # 한줄 한줄이 lines라는 리스트의 원소로 들어간다.
print(lines)

for line in lines:
    print(line)      # 한 줄씩 출력되게 함
file_score.close()

# txt파일에 몇줄이 있는지 모를때
file_score = open("score.txt", "r", encoding = "utf8")
while True:
    line = file_score.readline()
    print(line)
    if not line:        # line에 내용이 없으면 break로 while문 탈출
        break
file_score.close() 