#가변인자: 함수에 몇개의 인자를 받을지 정해지지 않은 경우 사용

def profile(name, age, lang1, lang2, lang3):
    print("이름: {}\t나이: {}\t".format(name,age), end = " ")
    print(lang1, lang2, lang3)

profile("나나", 27, "파이썬", "자바", "C")
# profile("보라돌이", 30, "Kotrlin", "Swift")
'''>>> lang3를 쓰지 않아서 오류가 난다.
       이처럼 language를 2개 쓰고싶거나 혹은 3개 이상으로 쓰고 싶은 경우에는
       바꾸고 싶을 때마다 함수를 변경해야 하는가?
       >>> 가변인자를 사용하면 된다. '''

# 가변인자: *를 붙여주자!
def profile1(name, age, *language):                # 함수 이름같게 쓰면 문제있다고 해서 1 붙여줌...
    print("이름: {}\t나이: {}\t".format(name,age), end = " ")
    for lang in language:
        print(lang, end = " ")          
    print()                        
'''>>> end = " " : 한 줄에 출력되도록 해준다. 
       print()   : 나나와 보라돌이의 출력문이 각각 다른줄에 출력되도록 해줌 '''

  # print(*language)                 파이썬 자바 C C++
  # print(language)                ('파이썬', '자바', 'C', 'C++')
'''>>> 여러개의 매개변수로 값을 전달받는 것이 아닌
       인자들을 한개의 tuple로 처리한다. '''

profile1("나나", 27, "파이썬", "자바", "C", "C++")
profile1("보라돌이", 30, "Kotrlin", "Swift")
