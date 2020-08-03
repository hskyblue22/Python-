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