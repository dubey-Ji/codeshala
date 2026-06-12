'''
list, index, length, slicing [start:stop:step], append, insert(index, "value"), remove("value"), pop, pop(index), replace with index

check karne if value present in list, index find out karne .index("value"), sort

'''

# how many students are their in codeshala batch 1: 3
# what are their names


            # index => 0.      1.        2.        3
            # length => 1.     2.        3.        4.
codeshala_students = ['raj', 'vivek', 'aditya', 'sneha']
# print(f'code shala studetns {codeshala_students}')

students = ['raj', 2, 'vivek', 3, 'aditya', 4, True ]
# print(f'studetns {students}')
# print(f'students length {len(students)}')
# print(len(students) - 1) # 20
# Question: Do we have index 6 in students list? => Yes
# Question: What is the length of students list? => 7
# Question: What is the last index of students list? => 6 last_index = length - 1


# if i want to add any other value in end of students list how to add it?
# => With the help of .append()
students.append("ashutosh")
# print(f'studetns {students}')
# print(f'students length {len(students)}') # Aditya -> 8, Vivek -> 8, Raj -> 8
# print(len(students) - 1) # Aditya -> 7, Vivek -> 7, Raj -> 7

# if i want to add any other value in middle of students list at any index how to add it?
# => With the help of .insert(index, "value")
students.insert(len(students) - 1, "sneha")
# print(f'studetns {students}')
# original 17th line students = ['raj', 2, 'vivek', 3, 'aditya', 4, True ]
# after append line 28 students = ['raj', 2, 'vivek', 3, 'aditya', 4, True, 'ashutosh' ]
# Vivek => ['raj', 2, 'vivek', 3, 'aditya', 4, True, 'sneha','ashutosh']
# Raj => ['raj', 2, 'vivek', 3, 'aditya', 4, True, 'ashutosh']
# Aditya => ['raj', 2, 'vivek', 3,'aditya', 4, True, 'ashutosh', 'sneha']



''' Task 2 — Password checker
# Ek function banao is_strong_password(password)
# Return True agar:
#   - Length 8 se zyada ho
#   - Koi number ho
# Warna False return karo'''


# password = input("Enter the password: ") # ashutosh
def is_strong_password(password):
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
    length_of_password = len(password)
    if length_of_password > 8 and has_number:
        return True
    return False
    
# print(is_strong_password(password))

'''
for char in password:
        if char.isdigit():
            has_number = True

loop 1: char = a, char.isdigit() = False
loop 2: char = s, char.isdigit() = False
.
.
.
.
loop 8: char = h, char.isdigit() = False
'''

fruits = ['apple', 'mango', 'pineapple', 'mango'] 
# remove method
# fruits.remove('mango')

# pop => used to remove the last index value
# fruits.pop()

# pop(index) => For any reason you want to remove any idex not the last index
# fruits.pop(1)

# index('value')
# print(fruits.index('pineapple'))

# slicing method, [start:stop:step]
# print(fruits[0:5:5])
# print(fruits)

grades = [10,9,1,11,34,5]
# ascending
# grades.sort() # [1,5,9,10,11,34]
# print(f"sorted grades: {sorted(grades)}")
# print(f"original grades: {grades}")

# descending
# grades.sort() == grades.sort(reverse=False)
# grades.sort(reverse=False)
print(f"sorted grades: {sorted(grades, reverse=True)}")
print(f"original grades: {grades}")