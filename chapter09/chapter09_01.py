#클래스 설계 (스타크래프트)
#클래스 명은 Unit, 멤버변수 : 이름 name , 체력 hp, 스피드 speed
#일반유닛
class Unit:
  #생성자
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed
    print("유닛이름 : {0}, 체력 : {1}, 스피드 : {2} 생성완료.".format(self.name,self.hp, self.speed))

#공격유닛
#클래스명은 AttackUnit, 멤버변수 : 이름 name, 체력 hp, 공격력 damage, 스피드 speed
class AttackUnit:
  #생성자
  def __init__(self, name, hp, damage, speed):
    self.name = name
    self.hp = hp
    self.damage = damage
    self.speed = speed
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


#공격유닛생성
soilder1 = AttackUnit("마린1", 40, 5, 10)
soilder2 = AttackUnit("마린2", 40, 5, 10)
soilder3 = AttackUnit("마린3", 40, 5, 10)
tank1 = AttackUnit("탱크1", 150, 35, 30)
tank2 = AttackUnit("탱크2", 150, 35, 30)

#마린1 공격 10시방향
# soilder1.attack(10)
# soilder2.attack(10)
# soilder3.attack(10)
# tank1.attack(10)
# tank1.attack(10)

#배열관리 공격 지시
attack_list = []
attack_list.append(soilder1)
attack_list.append(soilder2)
attack_list.append(soilder3)
attack_list.append(tank1)
attack_list.append(tank2)

for unit in attack_list :
  unit.attack(10)

# 공격 받음
# soilder1.damaged(5)
# soilder2.damaged(5)
# soilder3.damaged(5)
# tank1.damaged(5)
# tank2.damaged(5)

#배열관리 공격 받음
for unit in attack_list:
  unit.damaged(5)

#비행 공격 유닛
#사용되는 객체가 자신만의 멤버변수를 추가하면, 자기자신에게만 해당이된다.
#같은 클래스의 다른 유닛에는 멤버변수가 추가 되지 않는다.
airunit1 = AttackUnit("레이스", 200, 30, 40)
soilder4 = AttackUnit("마린4", 40, 5, 10)

# 비행 기능(멤버변수로 추가가능)
airunit1.fly = True
if airunit1.fly == True:
  print(f"{airunit1.name} {airunit1.hp} {airunit1.damage} {airunit1.speed} 공중유닛 : {airunit1.fly}")

# 오류남
# if soilder4.fly == True:
#   print(f"{soilder4.name} {soilder4.hp} {soilder4.damage} {soilder4.speed} 공중유닛 : {soilder4.fly}")
# else :
#   print(f"{soilder4.name} {soilder4.hp} {soilder4.damage} {soilder4.speed}")
                                                                                                                                                                                                     