# inheritance(상속) : parent clss & child class

# 공격을 하지 않는 유닛
class unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# attackunit : unit 클래스 상속받음
class attackunit(unit):                        
    def __init__(self,name,hp,damage):
        unit.__init__(self,name,hp)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
        
    def damaged(self, damage):
       print("{0} : {1} 데미지를 입었습니다.".format(self.name , self.damage))
       self.hp -=damage
       print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
       if self.hp <= 0:
           print("{0} : 파괴되었습니다.".format(self.name))  
 
'''1) attackunit(unit) : unit클래스 ---> parent class
                         attackunit 클래스 ---> child class
   2) self.name = name : unit클래스와 일치하므로 삭제
      selp.hp = hp 
   3) unit.__init__(시elf,name,hp) : unit의 생성자 호출
   4) unit : parent class
      attack unit : child class '''

firebat = attackunit("파이어뱃",50,16)       # class의 매개변수에 내가 입력한 값 저장 / 객체=클래스("매개변수")
firebat.attack("1시")                       #  객체.클래스내 함수("매개변수")
firebat.damaged(25)
firebat.damaged(25)





# 다중상속 : 부모클래스가 둘 이상인 경우

# 공중 기능
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} : {1} 방향으로 비행합니다. [속도 {2}]".format(name,location,self.flying_speed))

# 공중기능 + 공격가능
class flyableattack(attackunit,flyable):
    def __init__(self, name, hp, damage, flying_speed):     # flyableattack 클래스가 가지는 멤버변수 
        attackunit.__init__(self,name,hp,damage)      # attackunit 클래스가 가지는 멤버변수
        flyable.__init__(self,flying_speed)           # flyable 클래스가 가지는 멤버변수


'''1) 다중 상속 : parent class들 ,로 구분해서 ()안에 적는다.
   2) attackunit.__init__(self,name,hp,damage)  
      flyable.__init__(self,flying_speed)         ===> 각 클래스가 가진 정보만 ()안에 넣어준다. '''

valkyrie = flyableattack("발키리", 200, 60, 7)
# valkyrie.fly("발키리","11시")                      # 오류 X
# valkyrie.fly(self.name,"11시")                     # 오류 O  (self.매개변수(X)  객체.매개변수(O))
valkyrie.fly(valkyrie.name,"10시")                   # flyable클래스 내 fly함수의 매개변수만 써준다.