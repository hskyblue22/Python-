# 집합(set)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)
'''1) 중복이 안되기 때문에 {1,2,3}으로 출력된다.'''

java = {"나나", "뽀", "보라돌이"}
python = set(["나나", "고슴도치"])
go = {"멍이", "냥이","뽀"}

# 교집합
print(java & python & go)
print(java & python)
print(java.intersection(python))
'''2) 교집합이 없는 경우 set()으로 출력된다. '''

# 합집합
print(java | python | go)
print(java.union(python,go))

# 차집합
print(java - python)
print(java.difference(python,go))

# 값 추가
go.add("연")
print(go)

# 값 삭제
java.remove("뽀")
print(java)


# 자료구조의 변경

menu = {"아메리카노","스무디","쥬스"}
print(menu, type(menu))
'''1) set : {} 
   2) type(object) : opject의 타입 출력 '''

menu = list(menu)
print(menu, type(menu))
'''2) list : [] '''

menu = tuple(menu)
print(menu, type(menu))
'''3) tuple : () '''
