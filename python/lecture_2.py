'''
Recap of lecture 1
print(10/3)
print(10//3)
print(10%3)

***************

Python is a Dynamic typing

***************

input()

if/elif/else

for/while

for with range
range three types
range(start,end,step) start is inclusive, end is not inclusive 11, 10
range(5)
range(1,5)
range(1,10,2)

for with in => used with list

while loop

continue statement
break statement
'''
# Dynamic typing
first_name = "ashutosh"
# print(first_name)
first_name = 10
# print(first_name)

# Input
# first_name = input("Enter your first name: ")
# age = int(input("Enter you age: ")) # type conversion with the help of int()
# print(f"My first name is {first_name} and my age is {age}")
# input method always return a string

# if/elif/else
# is_it_sunny = True
# # is_it_raining = True
# if is_it_sunny: # first check
#     print("take sunglasses")
#     print("hello world")
# else: # default
#    print("Take nothing")

# Loop
# print("hello raj")
# print("hello vivek")
# print("hello aditya")
# print("hello sneha")
# for => Use when you know the number of iteration.
names = ["raj", "vivek", "aditya", "sneha"]
# print(f"hello {names[0]}")
# print(f"hello {names[1]}")
# print(f"hello {names[2]}")
# print(f"hello {names[3]}")
# for name in names:
#     print(f"hello {name}")
# Print a number for 1 to 10
'''
start = 11
end = 1
step = -1
start is inclusive
11
10
'''
# for i in range(11, 1, -1):
#     print(i)
# print(len(names))
# for names in range(4, (names)):
    # print(f)
# for i in range(len(names)):
    # print(f"hello {names[i]}")
# while => Use when you need to run the loop on condition
# Print a number for 1 to 5
# number = 1
# while number <= 5:
#     print(number)
#     number -= 1
'''
condition: number <= 5
number = 1
condition check
loop 1: 1, number += 1, number = 2
condition check
loop 2: 2, number += 1, number = 3
condition check 
loop 3: 3, number += 1, number = 4
condition check
loop 4: 4, number += 1, number = 5
condition check
loop 4: 5, number += 1, number = 6
condition check
loop terminate
'''

# continue statement
# used to skip
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
'''
loop1: i = 0, print = 0
loop2: i = 1, print = 1
loop3: i = 2, print = nothing
loop4: i = 3, print = 3
loop5: i = 4, print = 4
loop 6: i = 5, print = nothing
'''
# break statement
# used to terminate
for i in range(5):
    if i == 2:
        break
    print(i)
'''
loop1: i = 0, print = 0
loop2: i = 1, print = 1
loop3: i = 2, break, terminate
'''