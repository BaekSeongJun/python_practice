#예외처리

#1. 두수를 입력받아서 나눗셈해서 결과값을 출력하는 프로그램 작성
# exit_flag = False
# while(not exit_flag):
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>"))
#     print("{0} / {1} = {2:.2f} ".format(num1,num2,num1/num2))
#     exit_flag = True
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#   except ZeroDivisionError:
#     print("오류가 발생했습니다. 0으로 나눌 수 없습니다.")
#   except Exception as e:
#     print(e)
#   finally:
#     print("finally")
# print("프로그램이 종료되었습니다.")

# 2. 오류를 사용자가 조건에 따라서 발생시키기.
# exit_flag = False
# while(not exit_flag):
#   try:
#     num1 = int(input("number1 >>")) 
#     num2 = int(input("number2 >>"))
#     #조건을 하나 설정 (두수는 0보다 크고, 10보다 작거나 같아야만 실행)
#     if(num1 <= 0 or num2 <=0 or num1 > 10 or num2 > 10):
#       raise ValueError
#     print("{0} / {1} = {2:.2f} ".format(num1,num2,num1/num2))
#     exit_flag = True
#   except ValueError:
#     print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
#   except ZeroDivisionError:
#     print("오류가 발생했습니다. 0으로 나눌 수 없습니다.")
#   except Exception as e:
#     print(e)
#   finally:
#     print("finally")
# print("프로그램이 종료되었습니다.")

#3. 던더 메서드(dunder method) 만들고 실행하기
# class SpecialClass:
#   def __init__(self):
#     print("생성자가 발생하였습니다.")
#   #자바의 toString 같다고 생각하면 됨.
#   def __str__(self):
#     return "내가 만들고 싶은 문자열을 만들어서 전송합니다."
  
# sec = SpecialClass()
# print(sec)

#4.사용자가 정의한 예외처리 만들기 (정의한 메시지를 던지기 때문에 미시지 정의해야한다.)
class MyException(Exception):
  def __init__(self,message):
    self.message = message

  def __str__(self):
    return "발생 오류 : \"{}\"".format(self.message)

#사용자가 정의한 예외처리로 진행
exit_flag = False
while(not exit_flag):
  try:
    num1 = int(input("number1 >>")) 
    num2 = int(input("number2 >>"))
    #조건을 하나 설정 (두수는 0보다 크고, 10보다 작거나 같아야만 실행)
    if(num1 <= 0 or num2 <=0 or num1 > 10 or num2 > 10):
      raise MyException("입력값 {0}, {1} 값이 범위를 벗어남".format(num1,num2))
    print("{0} / {1} = {2:.2f} ".format(num1,num2,num1/num2))
    exit_flag = True
  except ValueError:
    print("오류가 발생했습니다. 잘못된 값을 입력했습니다.")
  except MyException as e:
    print("오류가 발생했습니다. 사용자가 정의한 예외가 발생되었습니다.\n{}".format(e))
  except ZeroDivisionError:
    print("오류가 발생했습니다. 0으로 나눌 수 없습니다.")
  except Exception as e:
    print(e)
  finally:
    print("finally")
print("프로그램이 종료되었습니다.")