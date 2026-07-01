#다중 상속 진행한다. (모호성 해결하는 방법을 구현한다.)

#일반유닛(지상 공격력이 없는 유닛)
class Unit:
  #생성자
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print(f"{self.name}, 체력 : {self.hp} 이동속도 : {self.speed} 유닛이 생성되었습니다.")
  
  def move(self,location):
    print(f"{self.name} 지상 유닛이 {location} 방향으로 가고 있습니다.")

#공격력이 있는 유닛(상속)
class AttackUnit(Unit):
  #생성자
  def __init__(self, name, hp, damage, speed):
    #super는 다중상속때 문제가 생긴다.
    #부모생성자를 책임진다.
    Unit.__init__(self,name,hp,speed)
    self.damage = damage
  #멤버함수(공격함수)
  def attack(self,location):
    print(f"{self.name}이 현재체력: {self.hp} {location}시 방향으로 공격력:{self.damage}(으)로 공격하고 있습니다.")
  #멤버함수(공격을 당하는 함수)
  def damaged(self, damage):
    print(f"{self.name}이(가) 상대방으로부터 공격력:{damage}로 공격을 받고 있습니다.")
    self.hp -= damage
    if(self.hp <= 0):
      print(f"{self.name} 유닛은 파괴되었습니다.")
    else:
      print(f"{self.name}이(가) 공격을 받아서 남아있는 체력은 {self.hp}입니다.")


#공중 유무 유닛(공중을 진행할 수 있는 여부 체크)
class Flyable:
  def __init__(self, flying_speed):
    self.flying_speed = flying_speed

 #멤버함수
  def fly(self, name, location):
    print(f"{name} 유닛이 {self.flying_speed}로 {location}방향으로 날아가고 있습니다.")

#다중상속  (지상공격유닛, 공중 유무 유닛)

class FlyableAttackUnit(AttackUnit,Flyable):
  def __init__(self, name, hp, damage, speed, flying_speed):
    AttackUnit.__init__(self, name, hp, damage, speed)
    Flyable.__init__(self, flying_speed)

  def move(self,location):
    print(f"{self.name} 공중 유닛이 {location} 방향으로 {self.flying_speed} 속도로 날아 가고 있습니다.")

#공격기능을 가진 interceptor 객체 생성
interceptor = FlyableAttackUnit("요격기", 300, 80, 0, 200)
# interceptor.attack(2)
# interceptor.damaged(60)
# interceptor.fly(interceptor.name,"4시")    
interceptor.move("3시")
