'''
 Dictionary

 Dictionary iteration => .items() , .keys(), .values()
'''

# hash, Dictionary, objects (javascript)

ages = {}; # => Dictionary
# keys and values
ages = {
    "ashutosh": 27, # left side => key, right side => value
    "vivkek": 23,
    "aditya": 25,
    "raj": 21,
    "sneha": 19
}
# print(f"Before {ages}")
# How can we add any new key and values in existing dictionary
ages['subrat'] = 25 # dictionary['key'] = value
# print(f"after adding {ages}")

# If following key is present inside the dictionary
# dictionary[key] => return is the value, if the key does not exist the code will break
# or dictionary.get(key) => return the value if key exist, or else None
# print(ages.get('abhishek'))

# Iteration -> .items()
# for name, age in ages.items(): # name => key  age => value
#    print(f"{name} has {age} age")

# Iteration -> .keys()
# for name in ages.keys():
#    print(name)

# Iteration -> .values()
# for age in ages.values():
#    print(age)

print(ages.values())
print(ages.items())
print(ages.keys())





