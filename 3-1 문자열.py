sentence = '나는 펭귄입니다'
print(sentence)

sentence2 = "펭귄은 귀여워요"
print(sentence2)

sentence3 = """    
나는 펭귄이고, 
펭귄은 귀여워요
"""            
print(sentence3)         # 총 4줄 출력(위, 아래로 공백)

sentence3 = """
나는 펭귄이고, 
펭귄은 귀여워요"""
print(sentence3)         # 총 3줄 출력(위 공백)

sentence3 = """나는 펭귄이고, 
펭귄은 귀여워요"""       
print(sentence3)         # 총 2줄 출력(위,아래 공백 없음)

# sentence4 = "나는 펭귄이고,     
# 펭귄은 귀여워요"
# print(sentence4)       # 오류 난다. 한 줄 띄우고 출력하고 싶다면 """을 사용하자. 


Bucketlist = "I really want to go backpacking to Switzerlad"

a = Bucketlist.lower()        # 전부 소문자로 바꾸기
print(a)
b= Bucketlist[3].upper()      # 3번째 자리만 대문자로
print(b)
c = Bucketlist[:9] + Bucketlist[9:14].upper() + Bucketlist[14:]      # want만 대문자로 전체 문장 출력
print(c)

print(len(Bucketlist[-10:]))  # Bucketlist 변수에서 Switzerland만 글자개수 세기

replace = Bucketlist.replace("Switzerlad",'Austrailia')
print(replace)

# index = print(Bucketlist.index("s"))   대문자, 소문자 구분하므로 S를 찾아야 오류나지 않음
index = Bucketlist.index("t")              
print(index)                                # 왼쪽에서부터 처음 나오는 t 자리수 찾기
index = Bucketlist.index("t", index+1)    
print(index)                                # 왼쪽에서부터 두번째로 나오는 t 자리수 찾기 
index = Bucketlist.index("t", index+1)    
print(index)                                # 왼쪽에서부터 세번째로 나오는 t 자리수 찾기 