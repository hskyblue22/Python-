# pickle ==> 프로그램에서 쓰는 데이터를 binary파일 형태로 저장하는 라이브러리
''' 장점 : 용량이 매우 작아진다
    binary 파일 : 데이터 저장과 처리의 목적으로 0,1의 이진 형식으로 인코딩된 파일
    라이브러리 : 모듈과 패키지, 내장 함수를 묶어서 파이썬 표준 라이브러리(Python Standard Library, PSL)라고 함'''

# 내용저장
import pickle
file_profile = open("profile.pickle", "wb")
profile = {"name":"Molang", "age":22, "eyesight":[1.2 , 1.1]}
print(profile)
pickle.dump(profile,file_profile)
file_profile.close()
'''1) wb (write + binary) : pickle 쓸때는 꼭 binary를 명시해줘야 한다. 
   2) rb (read + binary)
   3) pickle.dump(profile,file_profile) : profile에 있는 정보를 file_profile에 저장한다.
                                          내용 저장할 때 꼭 써줘야 함.
                                          => 실행하면 profile.pickkle 파일 생긴다. 
   4) pickle.load(file_profile) : load를 통해 file의 정보를 불러와서 profile1 변수에 저장해서 쓸 수 있도록 함'''

# 내용 불러오기
file_profile = open("profile.pickle", "rb")
profile1 = pickle.load(file_profile)
print(profile1)
file_profile.close()
