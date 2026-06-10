'''
Functions:
# Use case
=> Not to write a repeated code.
=> Same code can be use anywhere
=> Whenever you need to create a function you need to use def keyword.

Defining and calling functions
=> Whene you are creating a function also called as defining
=> Calling when you use the function


Parameters
=> It is written while defining the function

argument
=> The value which is passed inside the function while calling the function

Multiple parameters:
=> Yes we can pass multiple parameters

Default parameters value
=> Used to define a default value
=> Always from backwards

pass => Keyword

return statement
=> Done

Multiple return values:


=> 
Scope


=> 
'''
# name = input()
# print("Hello Raj")
# print("Hello Aditya")
# print("Hello Vivek")
# def greet(name = "Ashutosh", age = 25, college = "RJIT"): # defining the function , name is a parameter
    # print(f"Hello my is {name} and my age is {age} and i'm from college {college}")
    # print(f"I'm going to RJIT college")









# greet("Raj") # calling the function, "Raj" is a argument
# greet("Aditya") # calling the function
# greet() # calling the function

# greet("Ashutosh")

# def sum(num1, num2):
#     # print(num1 + num2)
#     # return num1 + num2
#     # print(num1 + num2)
#     # print("hello")
#     sum_result = num1 + num2 # 4
#     if sum_result < 5:
#         print(sum_result)
#     else:
#         print("not less than 5")
#     print("hello")

# print(sum(1, 3))
# sum_result = sum(2,3)
# multiply_result = sum_result * 2
# print(multiply_result)

def grade(marks):
    if 90 <= marks <=100:
        return "A"
    elif 80 <= marks <= 90:
        return "B"
    elif 70 <= marks <= 80:
        print("C")
    elif 60 <= marks <= 70:
        print("D")
    elif 50 <= marks <= 60:
        return "E"
    else:
        return "Fail"
    return marks

# grade(77)

# Vivek => B
# Aditya => B
# Raj => B

# mutliple returns
def sumAndMultiply(num1,num2):
    sum_result = num1 + num2
    multiply = num1 * num2
    return multiply, sum_result

# result1, result2 = sumAndMultiply(2, 3)
# print(f"result1 {result1}") # 6
# print(f"result2 {result2}") # 5


# scope
name = "Ashutosh" # Global scope
def printName():
    # name = "Vivek"
    if False:
        name = "Aditya"
        print(name)
    if 1 == 2:
        name = "Raj"
    print(name)


printName() # Ashutosh Ashutosh Ashutosh
print(name) # Ashutosh Ashutosh Ashutosh




