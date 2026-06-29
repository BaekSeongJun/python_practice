#파일 입출력 데이터베이스 => 파일에 저장 가져오고, 저장하고, 삭제하고,수정하고
#파일에서 "w" :저장 "r" : 읽어옴 "a" = 추가

#score.txt utf-8 방시으로 입력하고, 새로쓸거야
# file_handle = open("score.txt", "w",encoding = "utf8")
# print("국어 : 90", file = file_handle)
# print("영어 : 100", file = file_handle)
# print("수학 : 100", file = file_handle)
# file_handle.close()

#score.txt 추가기능을 설정해서 객체를 생성해야된다
# file_handle = open("score.txt", "a", encoding="utf8")
# print("자바 : 100", file = file_handle)
# print("파이썬 : 100", file = file_handle)
# file_handle.close()


# file_handle = open("score.txt", "a", encoding="utf8")
# # # write() /n기능이 없다. 마지막 \n기능을 입력해야된다.
# # file_handle.write("HTML : 100\n")
# file_handle.write("CSS : 90\n")
# file_handle.close()

#파일에서 "r" : 읽어옴 
# file_handle = open("score.txt", "r", encoding="utf8")
# print(file_handle.read()) #모두 읽어버린다.
# file_handle.close()

# file_handle = open("score.txt", "r", encoding="utf8")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# print(file_handle.readline(),end="")
# file_handle.close()

# file_handle = open("score.txt", "r", encoding="utf8")
# exit_flag = False
# while not exit_flag:
#   line = file_handle.readline()
#   if not line:
#     exit_flag = True
#   print(line, end="")

# file_handle.close()

file_handle = open("score.txt", "r", encoding="utf8")
list = file_handle.readlines()
file_handle.close()

# print(list, type(list))
for data in list:
  print(data,end="")