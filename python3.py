num1 = int(input("enter number"))
num2 = int(input("enter number"))
operator = input("+,-,*,/")
def calc(num1,num2,operator):
 if operator == "+":
  print( num1 + num2)
 elif operator == "-":
  print("your sub is", num1 - num2)
 elif operator == "*":
  print("your multiple is", num1 * num2)
 elif operator == "/":
  print("your divide is", num1/num2)

 print(calc(num1,num2,operator))