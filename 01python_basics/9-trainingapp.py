
from colorama import Fore, Style, init
init(autoreset=True)
course_catalog = {
    "UI5": {"trainer": "Anubhav", "hours": 40, "price": 2380},
    "CPI": {"trainer": "Anurag", "hours": 35, "price": 3400},
    "AOH": {"trainer": "Ammi", "hours": 40, "price": 3300},
    "CDS": {"trainer": "Suri", "hours": 40, "price": 3860},
    "BTP": {"trainer": "Som", "hours": 40, "price": 8380},
    "SAC": {"trainer": "Jain", "hours": 40, "price": 9380},
    "CAP": {"trainer": "Sid", "hours": 40, "price": 6380},
    "UI5": {"trainer": "Rid", "hours": 40, "price": 7380},
}
for course_code, details in course_catalog.items():
    print(f"Course: {course_code},Trainer: {details['trainer']},Hours: {details['hours']},Price: {details['price']}")

  
selected_course = []
print()
print(Fore.GREEN + Style.BRIGHT + "Welcome to the Trainings", end=" ")
print(Fore.YELLOW + Style.BRIGHT + "Please select the training", end=" ")

##infinite loop
while True:
    course = input("\nEnter the course name( or type 'exit to finish): ").strip().upper()
    if course == 'EXIT':
        break
    elif course in course_catalog:
        selected_course.append(course)
        print(f"added{course} to your selection.")
    else:
        print(f"Course{course} not found. Please try again.")
        
print("\nYou have selected the following courses:")
total_amount = 0

for idx, course in enumerate(selected_course, start=1):
    detials = course_catalog[course]
    print(f"{idx}.{course} - Trainer: {detials['trainer']}, Hours: {detials['hours']}, Price: ${detials['price']}")
    total_amount += detials['price']
    
print(f"\nTotal amount for selected courses: ${total_amount}")
    
    