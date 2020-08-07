# Dictionary: 대응 관계를 나타내는 자료형
# 리스트나 튜플처럼 순차적으로(sequential) 해당 요솟값을 구하지 않고 Key를 통해 Value를 얻는다. 
# key 중복 있을 수 없다.

cabinet = {"A-30":"한", "B-70":"돌", 100:"복"}
print(cabinet["A-30"])  
print(cabinet[100])    
'''1) 변수 = {key : value}        => 딕셔너리 {}로 표현한다.
      key 이용해서 value 찾기'''

# print(cabinet["5-10"])  => 오류!
print(cabinet.get("5-10"))
'''2) 변수에 특정 key가 없는 경우
      변수.get(key) : none값 출력 , 뒤의 값 출력됨
      변수[key]     : 오류남 , 뒤의 값 모두 출력 안됨 ''' 


print(cabinet.get("5-10", "사용 가능"))
'''3) key 에 값이 없을 경우 "사용가능" 값 출력 '''

print("A-30" in cabinet)   # True
print(100 in cabinet)      # True 
print (500 in cabinet)     # False
'''4) 변수 cabinet안에 특정 key있는지 알아보기'''

cabinet["A-30"] = "둘"
cabinet["D-87"] = "갑"
print(cabinet)
'''5) cabinet에 기존 key값 업데이트
      cabinet에 새로운 값 추가 '''

del cabinet["B-70"]
print(cabinet)
'''6) cabinet에서 "B-70" key 삭제 '''

print(cabinet.keys()) 
print(cabinet.values())           # 둘, 복, 갑 => 이렇게 출력X 
print(cabinet.items()) 
cabinet.clear()                   # 딕셔너리.clear() 괄호 잊지 말자!
print(cabinet)
'''7) key 들만 출력
      value 들만 출력 
      key, value 모두 출력
      key, value 모두 삭제 '''