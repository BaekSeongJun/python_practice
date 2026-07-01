#라이브러리 함수 기능만 있는 모듈

#일반인이 영화를 관람했을때 요금을 계산하는 라이브러리
def price(count):
  price = 14000
  print(f"{count}명은 영화의 1인당 영화가격은 {price}이며 전체 금액은 {count * price}입니다.")

#죠죠할인
def price_morning(count):
  price = int(14000 * 0.6)
  print(f"{count}명은 영화의 1인당 조조영화 할인가격은 {price}이며 전체 금액은 {count * price}입니다.")

#군인 할인(60퍼 할인)
def price_soilder(count):
  price = int(14000 * 0.4)
  print(f"{count}명은 영화의 1인당 군인의 영화 할인가격은 {price}이며 전체 금액은 {count * price}입니다.")