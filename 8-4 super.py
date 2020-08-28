# super : child클래스에서 parent 클래스의 내용을 사용하고 싶을 경우 사용 

class unit:
    def __init__(self):
        print("unit 생성자")

class flyable:
    def __init__(self):
        print("flyable 생성자")

class flyableunit(flyable,unit):
    def __init__(self):
        # super().__init__()             # super() : self 쓰지 않는다.
        unit.__init__(self)              # self 써줘야 한다.
        flyable.__init__(self)                 


dropship = flyableunit()
'''1) class flyable(unit, flyable):  ==>  [unit 생성자] 출력
      class flyable(flyable, unit):  ==>  [flyable 생성자] 출력 
      
      super().__init__() ==> 다중상속 시 매개변수 순서에 따라 값이 달라지므로 문제가 된다.
      
   2) unit.__init__(self)
      flyable.__init__(self)
      
      ==> 부모클래스 모두 출력된다. '''

class parent1:
    def overriding(self):
        print("method_parent 클래스")

class child1(parent1):
    def overriding(self):
        super().overriding()                # parent 클래스의 overriding method => 오버라이딩으로 무시되지 않고 출력됨 
        print("method_child 클래스")


# super().__init__()   :  child클래스 매개변수 순서에 따라서 출력이 달라짐
# super().overriding() :  parent클래스 오버라이딩으로 무시되지 않고 출력됨