#내부에서 Package를 가져오는 방법

#travel -> thailand 모듈만 가져오기 
# import travel.thailand

# thailand_obj = travel.thailand.ThailandModule()
# thailand_obj.detail_travel()

#자바에서 사용되는 import 기능과 같다.
# from travel.thailand import ThailandModule

# thailand_obj = ThailandModule()
# thailand_obj.detail_travel()

# from travel.vietnam import VietnamModule

# vietnam_obj = VietnamModule()
# vietnam_obj.detail_travel()

#해당되는 패키지에 모든 모듈을 가져오는 방법
#해당되는 패키지 중 thailand만 공개함
# from travel import * 

# t_obj = thailand.ThailandModule()
# t_obj.detail_travel()

# v_obj = vietnam.VietnamModule()
# v_obj.detail_travel()

#패키지 모듈 위치
import inspect
import random

#inspect를 사용헤서 random패키지 위치를 검사
print(inspect.getfile(random))