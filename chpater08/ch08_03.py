# pickle

import pickle

#pickle 파일 저장
#binary 파일로 저장할때는 encoding 방식이 필요하지 않음.
# profile_handle = open("profile.pickle","wb")
# profile_dic = {"이름": "bsj", "나이": 28, "취미":["메이플","영화감상","음악"]}
# #dump: 우리가 프로그램에서 사용했던, 맵구조(dictionary)를 다시 사용하기 위해 pickle 파일에 저장
# pickle.dump(profile_dic,profile_handle)
# profile_handle.close()


# pickle 파일을 다시 가져와서 프로그램에 사용하기 위한 기능
# profile_handle = open("profile.pickle","rb")
# list_dic = pickle.load(profile_handle)
# profile_handle.close()

# for key, item in list_dic.items():
#   print(key, item)

# print(list_dic, type(list_dic))

#파일을 한번에 열고, 자동으로 닫기 : with 문(java : try with resorces)
# with open("profile.pickle","rb") as profile_handle:
#   list_dic = pickle.load(profile_handle)

# for key, value in list_dic.items():
#   if(key == "취미"):
#     for data in value:
#       print(key, data, sep = " : ")
#   else:
#     print(key, value, sep=" : ") 
# with을 쓰면 따로 .close()로 닫을 필요가 없다.

#일반파일을 with으로 처리하는 방식 (닫는기능 자동으로 처리)
# with open("data.txt","w",encoding="utf-8") as data_handle:
#   data_handle.write("파이썬\n")
#   data_handle.write("자바\n")
#   data_handle.write("스프링부트\n")

with open("data.txt","r",encoding="utf-8") as data_handle:
  print(data_handle.read())
