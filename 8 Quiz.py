# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2016년
# 송파 빌라 월세 500/50 2000년

class House:
    # 매물 초기화
    def __init__(self,location,house_type,deal_type,price,year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.year = year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,\
            self.price, self.year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2009년")
house3 = House("송파", "빌라", "월세", "500/50", "2014년")
'''1) house1,2,3 을 House클래스(빵틀)에 대한 객체(빵)로 만들기 
   2) houses라는 [] 리스트 만들어서 값 넣기'''
  
houses.append(house1)
houses.append(house2)
houses.append(house3)
print(houses)
'''3) 객체들을 houses 리스트에 넣기 '''

print("총 {}대의 매물이 있습니다.".format(len(houses)))
for house in houses:        
    house.show_detail()     
'''4) house : house1,2,3
   5) house1.show_detail()
      house2.show_detail()
      house3.show_detail()   ===> 객체를 리스트에 넣었다 하더라도 객체에 클래스내 method 사용가능하군'''                






# 클래스 복습 #

class Animal:
    def __init__(self,name,habitat):
        self.name = name
        self.habitat = habitat

    def introduce(self):
        print("{}은/는 {}에 사는 동물입니다.".format(self.name,self.habitat))

    def color_fur(self,color):
        print(self.name + "의 털색은 " + color +"입니다.")    # init에서 초기화된 변수가 아니므로 self.color 아니다.

class sea_animal(Animal):
    def swim(self,speed_swim):
        print(self.name + "의 헤엄속도는 {}입니다.".format(speed_swim))   # self.speed_swim 아니다.

class land_animal(Animal):
    def run(self,speed_run):
        print(self.name + "의 속도는 {}입니다.".format(speed_run))


penguin = Animal("펭귄","남극")
penguin.introduce()
penguin.color_fur("흰색과 남색")

dolphin = sea_animal("돌고래","해양")       #Animal을 상속받았으므로 (name, habitat) 을 매개변수로 받는다.
dolphin.swim("50km/h")

cheetah = land_animal("치타","사바나")
cheetah.introduce()
cheetah.run("110km/h")

