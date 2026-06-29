#상속

#일반유닛
class Unit:
  #생성자
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    # print("유닛이름 : {0}, 체력 : {1}, 스피드 : {2} 생성완료.".format(self.name,self.hp, self.speed))
  def move(self, location):
    print("[부모 유닛 이동]")
    print(f"{self.name}")
  

#공격유닛
#클래스명은 AttackUnit, 멤버변수 : 이름 name, 체력 hp, 공격력 damage, 스피드 speed
class AttackUnit(Unit):
  #생성자
  def __init__(self, name, hp, damage, speed):
    #부모생성자를 책임진다.
    Unit.__init__(self,name,hp,speed)
    self.damage = damage
    print("유닛이름 : {0}, 체력 : {1}, 공격력 : {2}, 스피드 : {3} 생성완료.".format(self.name, self.hp, self.damage, self.speed))
  #멤버함수(공격함수)
  def attack(self,location):
    print(f"{self.name}이 {location}시 방향으로 공격력:{self.damage}(으)로 공격하고 있습니다.")
  #멤버함수(공격을 당하는 함수)
  def damaged(self, damage):
    print(f"{self.name}이(가) 상대방으로부터 공격력:{damage}로 공격을 받고 있습니다.")
    self.hp -= damage
    print(f"{self.name}이(가) 공격을 받아서 남아있는 체력은 {self.hp}입니다.")
    if(self.hp <= 0):
      print(f"{self.name} 유닛은 파괴되었습니다.")
  def move(self,llocation):
    print("[자식 유닛 이동]")
    print(f"{self.name}")

soilder1 = AttackUnit("마린1", 40, 5, 10)
soilder2 = AttackUnit("마린2", 40, 5, 10)
soilder3 = AttackUnit("마린3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 150, 35, 30)
tank2 = AttackUnit("탱크2", 150, 35, 30)

soilder1.move(5)