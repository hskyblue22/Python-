# method overriding 
# 부모클래스의 method를 자식클래스에서 재정의하는 것. 이때 부모클래스의 메소드는 무시된다.
# 기존에 이미 만들어진 method의 이름을 똑같이 만들어야 할 때 사용한다.

class parent:
    def overriding(self):
        print("method_parent 클래스")
class child(parent):
    def overriding(self):
        print("method_child 클래스")

example = child()                    # 상속관계에서 child class 사용
example.overriding()
'''>>> 출력결과 : "method_child 클래스"
       >>> parent class에 method 무시. '''

class parent1:
    def overriding(self):
        print("method_parent 클래스")
class child1(parent1):
    def overriding(self):
        super().overriding()
        print("method_child 클래스")

example = child1()
example.overriding()
'''>>> 출력결과 : method_parent 클래스
       method_child 클래스
       >>> parent class에 method도 출력됨. '''



# 공격을 하지 않는 지상유닛
class unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed                                # 지상 유닛 : 매개변수 speed 추가
        
    def move(self,location):
        print("[ 지상유닛 이동 ]")
        print("{0} : {1} 방향으로 이동합니다. [ 이동속도 {2}]".format(self.name,location,self.speed))                

# attackunit : unit 클래스 상속받음
class attackunit(unit):                        
    def __init__(self,name,hp,speed,damage):              # speed 추가 (필수는 아닌 것 같다.)
        unit.__init__(self,name,hp,speed)                 # speed 추가 필수로 해줘야 함(입력해야할 매개변수가 뜬다. )
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
        
    def damaged(self, damage):
       print("{0} : {1} 데미지를 입었습니다.".format(self.name , self.damage))
       self.hp -=damage
       print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
       if self.hp <= 0:
           print("{0} : 파괴되었습니다.".format(self.name))  
 

# 공중 기시
class flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        # print("[ 공중유닛 이동 ]")
        print("{0} : {1} 방향으로 비행합니다. [비행속도 {2}]".format(name,location,self.flying_speed))

# 공중기능 + 공격가능
class flyableattack(attackunit,flyable):
    def __init__(self, name, hp, damage, flying_speed):       # speed 추가 X
        attackunit.__init__(self,name,hp,0,damage)            # speed에 0 입력 (필수)
        flyable.__init__(self,flying_speed)  

    def move(self,location):
        print("[ 공중유닛 이동 ]")
        self.fly(self.name,location)             
'''2) flyableattack 클래스에서 move 함수 재정의         /  기존 move 함수 : unit클래스에서 정의했었음
   3) self.fly ==> 부모클래스(flyable)의 fly method 사용 '''

# 벌쳐 : 지상유닛
vulture = attackunit("벌쳐",80,10,20)

# 배틀크루저 : 공중유닛
battlecruiser = flyableattack("배틀크루저",500,25,3)

# 유닛 이동
vulture.move("16시")
# battlecruiser.fly(battlecruiser.name,"9")
'''1) 지상유닛일 때는 move method 써야하고 공중유닛일 때는 fly를 구분해서 써줘야함
       매번 번거로우니까 바꿔주자! '''
battlecruiser.move("9시")






#======================= pass =====================

class buildingunit(unit):
    def __init__(self, name, hp, location):
        pass

'''1) parent 클래스인 unit의 init 생성자 호출 X
      멤버변수 정의(self.location = location) X
      ===> 하지만 아래와 같이 실행해보면 아무 문제 없다.
   2) pass : 일단은 class 완성된 것처럼 넘어간다. '''


def game_start():
    print("[notice] game start")

def game_over():
    pass

game_start()           # 출력: [notice] game start 
game_over()            # 출력:                      ==> 없음
