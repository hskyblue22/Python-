# 리스트: 순서를 가지는 객체의 집합

'''리스트를 사용하는 이유:
   숫자와 문자열만으로 프로그래밍을 하기엔 부족한 점이 많다. 
   예를 들어 1부터 10까지의 숫자 중 홀수 모음인 1, 3, 5, 7, 9의 집합에서 이런 숫자 모음을 숫자나 문자열로 표현하기는 쉽지 않다.'''

array = ["강아지", "고양이", "토끼"]
print(array)

# "토끼" 는 몇번째에 있는가?
print(array.index("토끼"))

# "패럿" 맨뒤에 추가시키기
# print(array.append("패럿"))  
''' 출력값으로 None이 나온다. 
    append함수는 return값이 없기 때문.'''

array.append("패럿")
print(array)

# "햄스터"를 강아지 / 고양이 사이에 추가시키기
array.insert(1, "햄스터")
print(array)
# "기니피그"를 고양이 / 토끼 사이에 추가시키기
array.insert(3, "기니피그")
print(array)

# 뒤에서 부터 하나 빼기
array.pop()     
print(array)

# 뒤에서 2개 빼기
# print(array.pop(-2:))    => 오류
del array[-2:]
print(array)
''' pop: 범위를 지정하여 삭제 불가능,
    del: 범위를 지정해서 삭제해준다.  '''

# 한 리스트에서 같은 요소 개수 세기
array.append("강아지")
how = array.count("강아지")
print(how)

# 정렬 가능
num_list = [10,5,8,9,3]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 리스트 확장
mix_list = ["냥이", 35, True]
# mix_list.extend(num_list)
print(mix_list)
print(num_list)

''' 위와 같이 하면 mix_list 가 확장되어 변했다.
    num_list는 변하지 않았다.
     
    print(mix_list + num_list) 로 하면 결과는 같게 나오지만 
    mix_list는 변하지 않았다.  '''