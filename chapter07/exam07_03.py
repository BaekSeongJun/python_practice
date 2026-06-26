def std_weight (height, gender):
  if(gender == "남자" or gender == "남"):
    return height * height * 22
  elif(gender == "여자" or gender == "여"):
    return height * height * 21
  else:
    return 0

height = float(input("키를 입력해주세요 : ")) 
gender = input("성별을 입력해주세요 : ")

cal_height = height/100

weight = std_weight(cal_height, gender)

if(weight != 0):
  print("키 {} {}의 표준체중은 {}kg입니다.".format(int(height),gender,round(weight,2)))
else:
  print("잘못된 성별 입력입니다.")