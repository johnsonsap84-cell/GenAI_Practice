#aarray of fruits
fruits = ["apple", "banana", "cherry"]
print(fruits)
numbers = [1, 2, 3, 4, 5]
print(numbers)

#print first and last fruit
print("First fruit:", fruits[0])    
print("Last fruit:", fruits[-1]) 
fruits.append("orange")
fruits.remove("banana")
fruits.insert(2, "kiwi")   
#print index all fruits
for index, fruit in enumerate(fruits):
    print(f"Fruit at index {index}: {fruit}")
    
#print first and last fruit
print("First fruit:", fruits[1:-1])

fruits.pop()  # Remove the last fruit 
#no loop required to check if kiwi is in the list
if "kiwi" in fruits:
    print("Kiwi is in the list.")
    
#list concatenation
fruit_numbers = fruits + numbers
print("Concatenated list:", fruit_numbers)

#list comprehension
squared_numbers = [x**2 for x in numbers]
print("Squared numbers:", squared_numbers)

#list slicing
print(fruits)
sliced_fruits = fruits[1:3]  # Get fruits from index 1 to 2
print("Sliced fruits:", sliced_fruits)

#sets
set1 = {1, 2, 2, 3, 4}
set2 = {3, 4, 5, 6} 
print("Set1:", set1)
print("Set2:", set2)

# set1.add(5)  # Add an element to set1
# set1.remove(2)  # Remove an element from set1   
set_union = set1.union(set2)  # Union of set1 and set2
set_intersection = set1.intersection(set2)  # Intersection of set1 and set2
print("Union of sets:", set_union)  
print("Intersection of sets:", set_intersection)

#tuples( immutable lists)
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
print("Tuple1:", tuple1)
print("Tuple2:", tuple2)

#mixed tuple
mixed_tuple = (1, "apple", 3.14, True)
print("Mixed tuple:", mixed_tuple)

#nested tuple
nested_tuple = (1, (2, 3), (4, 5, 6))   
print("Nested tuple:", nested_tuple)

#single tuple
single_tuple = (1,)  # Note the comma
print("Single tuple:", single_tuple)

#dictionaries
employee = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "salary": "75000.50",
    "skills": ["Python", "JavaScript", "SQL"],
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    },
    "languages": ("English", "Spanish")
}

print("Employee:", employee)  

print("Name:", employee["name"]) 

for key, value in employee.items():
    print(f"{key}: {value}")    
    
#dictionary comprehension
print("Employee Name:", employee["name"])
print("Employee Age:", employee.get("age", "Not Found"))  # Using get() method

squared_numbers = {x: x**2 for x in range(1, 6)}
print("Squared numbers dictionary:", squared_numbers)


 
