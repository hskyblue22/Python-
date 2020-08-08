# tuple은 list와 달리 내용 수정 불가능
# 속도가 list보다 빠르다.  => 변경되지 않는 정보에 사용

menu = ("돈까스","모밀")
print(menu)
print(menu[0])
print(menu[1])

# menu.add("생선까스")
'''1) tuple은 내용 추가 안됨 '''

# name = "버미"
# age = 30
# hobby = "산책"
# print(name, age, hobby)

(name, age, hobby) = ("버미", 30, "산책")
print(name, age, hobby)
'''2) 하나하나 변수 설정하지 않고 한번에 설정가능하다. '''

