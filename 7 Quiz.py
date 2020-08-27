# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x 주차 주간보고 - 
# 부서 :
# 이름 : 
# 업무 요약 :

# 1주차부터 10주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듭니다.


# 방법 1
for i in range(1,11):
    report_file = open(str(i) + "주차.txt", "w" , encoding = "utf8")
    print("- {0} 주차 주간보고 - ".format(i))
    print("부서 : ")
    print("이름 : ")
    print("업무 요약 : ")
    report_file.close()

# 방법 2
# for num in range(1,11):
#     with open(str(num) + "주차.txt" , "w" , encoding = "utf8") as file_r:
#         file_r.write("- {0} 주차 주간보고 - ".format(num))
#         file_r.write("\n부서 : ")
#         file_r.write("\n이름 : ")
#         file_r.write("\n업무 요약 : ")

'''1) with open(str(num) + "주차 주간보고.txt" , "w" , encoding = "utf8) as file_name:
      ==> str(num) : str 꼭 씌워줘야 함
      ==> str(num) + "글자"

   2) \n : 한줄 띄우기
      file_name.write : print처럼 한줄 띄우기 자동으로 안됨 ''' 