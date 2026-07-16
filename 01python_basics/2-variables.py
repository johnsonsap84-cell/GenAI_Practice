# #scalar varibales
from datetime import datetime

name = "John"
# age = 18
# height = 5.9
# is_student = True

# print("Name:", name, "is of type", type(name))
# print("Age:", age, "is of type", type(age))
# print("Height:", height, "is of type", type(height))
# print("Is Student:", is_student, "is of type", type(is_student))

# #type conversion
# age_str = str(age)
# print("Age as string:", age_str, "is of type", type(age_str))
# age_int = int(age_str)
# print("Age as integer:", age_int, "is of type", type(age_int))
age = int(input("Enter your age: "))
if age > 18:
    print(name, "is an adult.")
elif age == 18:
    print(name, "is eighteen.")
else:
    print(name, "is a minor.")
    
#concatenation
greeting = "Hello, " + name + "!"
print(greeting)
#concatenation with f-string
greeting_fstring = f"Hello, {name}! your age is {age} years old. today timestap{datetime.now()}"
print(greeting_fstring) 
    