# with ~ as 구문 : 파일 open후에 자동으로 닫히므로 close없이 파일 입출력 가능

import pickle
with open("profile.pickle","rb") as file_profile:
    print(pickle.load(file_profile))
'''1) ~ as file_profile : profile,pickle 파일 열어서 file_profile 변수에 저장 
   2) pickle.load(file_profile) : 파일 내용을 pickle.load를 통해 불러와서 출력 '''

with open("study.txt","w", encoding = "utf8") as file_s:
    file_s.write("퇴근 후에 파이썬 공부를 하고 있어요ㅠㅅㅠ")

with open("study.txt","r", encoding = "utf8") as file_s:
    print(file_s.read())
'''3) file_s.read() : .read()를 통해 파일 내용을 불러와서 출력'''