#num1 = int(input("enter number : "))
#num2 = int(input("enter number : "))
#operator = input("+,-,*,/ : ")
#def calc(num1,num2,operator):
 #if operator == "+":
  #return( num1 + num2)
 #elif operator == "-":
  #return("your sub is", num1 - num2)
 #elif operator == "*":
  #return("your multiple is", num1 * num2)
 #elif operator == "/":
  #return("your divide is",num1/num2)
 

#print (calc(num1,num2,operator))


#no_of_times = int(input("enter loop value : "))

#def celcius_to_farhenheit(celcius):
 #return (celcius*9/5)+32

#while  (no_of_times):
# celcius = float(input("enter value : "))

 #no_of_times -= 1
 #print (celcius_to_farhenheit(celcius))


#password

password = input("enter the password : ")

def is_strong_password(password):
   
   if len(password)<8:
     return True
   elif len(password)>8:
    return False
   elif ("character present"):
     return True
   elif ("number present"):
    return False
  
print (is_strong_password("password"))
 