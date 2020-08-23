# 표준 체중을 구하는 프로그램을 작성하시오.

# (성별에 따른 공식)
# 남자: 키(m) x 키(m) x 22
# 남자: 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력예제)
# 키 175cm 남자의 표준 체중은 67.38 kg입니다.


# 내 답안
def std_weight(g,h):  # gender : "남자","여자" 중 택일 / height : cm단위

    if g == "남자":
        a = h*h*22 / 10000
        print("키 {}cm 남자의 표준 체중은 {:.2f}입니다.".format(h,a))
        
    else:
        b = h*h*21 / 10000
        print("키 {}cm 여자의 표준 체중은 {:.2f}입니다.".format(h, b))
        
std_weight("남자",187)


'''1) retrun 반환값 : (리스트, 튜플, 딕셔너리)
   2) return값 없는 경우 
     -print : 데이터를 화면에 표시해주는 역할
              데이터가 지정된 것이 아니므로 return을 해도 none이 나오는 것 같다.

     if gender == "남자":
        a = height*height*22 / 10000
        print("키 {}cm 남자의 표준 체중은 {:.2f}입니다.".format(height,a))
        ===> print(std_weight())
        ===> 키 187cm 남자의 표준 체중은 76.93입니다.
             none

      if gender == "남자":
        a = height*height*22 / 10000
        say = print("키 {}cm 남자의 표준 체중은 {:.2f}입니다.".format(height,a))
        return say       
        ===> print(std_weight())
        ===> 키 187cm 남자의 표준 체중은 76.93입니다.
             none               
             
       if gender == "남자":
        a = height*height*22 / 10000
        return print("키 {}cm 남자의 표준 체중은 {:.2f}입니다.".format(height,a))  
        ===> print(std_weight())
        ===> 키 187cm 남자의 표준 체중은 76.93입니다.
             none           
             '''

# 답안
def stdweight(gender,height):
    if gender == "남자":
        return height*height*22
    else:
        return height*height*22

heightt =  175
genderr = "남자"
weight = round(stdweight(genderr,heightt/100),2)
print("키 {}cm {}의 표준 체중은 {}입니다.".format(heightt,genderr,weight))

