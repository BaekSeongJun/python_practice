#내부 모듈을 가져와서 사용하기

# import theater_module

# #일반인 영화 예매 3명
# theater_module.price(3)

# theater_module.price_morning(3)

# theater_module.price_soilder(3)

#별칭으로 모듈 호충 
# import theater_module as tm 
# tm.price(3)
# tm.price_morning(3)
# tm.price_soilder(3)

#별칭 없이 모듈 호출 
# from theater_module import *
# price(3)
# price_morning(3)
# price_soilder(3)

#특정 모듈만 호출 
# from theater_module import price ,price_morning
# price(3)
# price_morning(3) 
# # price_soilder(3) # price_soilder(3) import가 안되서 사용할 수 없음.

#특정 모듈만 별칭으로 호출
from theater_module import price as p
p.price(3)
p.price_morning(3) 
# price_soilder(3) # price_soilder(3) import가 안되서 사용할 수 없음.

