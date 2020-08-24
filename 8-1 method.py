# method : 클래스 내부의 함수

class unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0} 공격력 {1}".format(self.hp, self.damage))

# 공격유닛
class attackunit:
    def __init__(self,name,hp,damage):
        self.name = name                    # self 는 전달된 객체이다.
        self.hp = hp                        # 객체에 객체변수 hp를 생성하고 전달받은 hp값을 저장한다.
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
        
    def damaged(self, damage):
       print("{0} : {1} 데미지를 입었습니다.".format(self.name , self.damage))
       self.hp -=damage
       print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
       if self.hp <= 0:
           print("{0} : 파괴되었습니다.".format(self.name))  
           
firebat = attackunit("파이어뱃",50,16)      # class의 매개변수에 내가 입력한 값 저장
firebat.attack("1시")                      #  객체.함수("매개변수")
firebat.damaged(25)
firebat.damaged(25)

'''1) self.name : 앞에서 정의된 class 자기자신에 있는 멤버변수 값 출력
   2) location : attack함수에서 전달받은 값 사용 (self.location XX)
   3) class에서 2번째 함수도 class에 포함된다. 
   4) class 내 함수 즉 method에서 첫 매개변수에 self 꼭 써주자. '''
 