# 1. class 쓰지 않은 경우 
#    class는 어떤 경우에 쓰면 좋은지 생각해보자.

m_name = "마린"
m_hp = 30
m_damage = 6
print("{} 유닛이 생성되었습니다.".format(m_name))
print("체력 {0} 공격력 {1}\n".format(m_hp,m_damage))

t_name = "탱크"
t_hp = 150
t_damage = 40
print("{} 유닛이 생성되었습니다.".format(t_name))
print("체력 {0} 공격력 {1}\n".format(t_hp,t_damage))

t2_name = "탱크"
t2_hp = 150
t2_damage = 40
print("{} 유닛이 생성되었습니다.".format(t2_name))
print("체력 {0} 공격력 {1}\n".format(t2_hp,t2_damage))

#===========================================은
total1 = 0
total2 = 0

# 플레이어1 의 공격량 나타내기
def attack1(name, location, damage):
    global total1                        # 전역변수를 지역변수로 사용
    total1 += damage
    print("{0} : {1} 방향으로 적군을 공격합니다.[공격 {2}]".format(name,location,damage))
    print("적에게 가한 총 데미지는 {} 입니다.".format(total1))
    return total1

attack1(m_name,"1시",m_damage)
attack1(t_name,"1시",t_damage)
attack1(t2_name,"1시",t2_damage)

# 플레이어2 의 공격량 나타내기

def attack2(name, location, damage):
    global total2
    total2 += damage
    print("{0} : {1} 방향으로 적군을 공격합니다.[공격 {2}]".format(name,location,damage))
    print("적에게 가한 총 데미지는 {} 입니다.".format(total2))
    return total2

attack2(m_name,"1시",m_damage)
attack2(t_name,"1시",t_damage)

'''1) class 사용 x 
      ==> 똑같은 내용의 함수임에도 각각 다른 값을 기억하도록 하기위해서 함수를 2개 만들어줘야 한다.            
   2) 계산기에서 덧셈하는 함수를 적용하였음    '''  

#==============================================

# class사용

class unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0} 공격력 {1}".format(self.hp, self.damage))

marine1 = unit("마린",40,6)
marine2 = unit("마린",40,6)
tank = unit("탱크",150,40)
'''3) 하나의 클래스로 각각 다르게 출력이 가능하다. 
   4) class : 똑같은 어떤 것을 계속 만들어 낼 수 있다. (쉽게 생각하면 빵틀)
      object : class에 의해 만들어진 것. (쉽게 생각해서 빵)
               객체마다 고유한 성격을 가진다. 객체 서로서로 영향을 주지 않는다.
               marine1, marine2, tank 가 객체이다.
   5) marine1과 tank는 unit class의 인스턴스   '''