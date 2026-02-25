# # Grocery List Manager
# # Create a list of grocery items.
# #
# # Add 3 items
# #
# # Remove 1 item
# #
# # Print the final list
#
# grocery_cart = ["Banna", "Tuna cane", "Sugar"]
# grocery_cart.append('Orange')
# grocery_cart.append('Sardine cane')
# grocery_cart.append('Bread')
# print(grocery_cart)
# grocery_cart.remove('Sugar')
# print(grocery_cart)
#
#
#
# # Daily Temperatures
# # Store daily temperatures in a list.
# #
# # Find the highest temperature
# #
# # Find the lowest temperature
# #
# # Calculate the average
#
# daily_temperature = [20, 40, 12]
#
# def find_highest_temperature(temperature_list):
#     highest_temp = max(temperature_list)
#     return highest_temp
# def find_lowest_temperature(temperature_list):
#     lowest_temp = min(temperature_list)
#     return lowest_temp
# def calculate_average(temperature_list):
#     average = sum(temperature_list) / len(temperature_list)
#     return average
# print(find_highest_temperature(daily_temperature))
# print(find_lowest_temperature(daily_temperature))
# print(calculate_average(daily_temperature))
#
#
# # Dictionary-Based Problems
# #
# # Phone Book
# # Create a dictionary with names as keys and phone numbers as values.
# #
# # Add 3 contacts
# #
# # Search for a contact
# #
# # Delete a contact
#
# phone_book = {
#     "user1": {
#         "name": "Samba",
#         "phone": 34574672
#     },
#     "user2": {
#         "name": "Vieux",
#         "phone": 345746363
#     }
# }
#
# phone_book.update({
#     "user3": {
#         "name": "Grand Hacko",
#         "phone": 3457466352
#     },
#     "user4": {
#         "name": "Sidy Hacko",
#         "phone": 3457466362
#     },
#     "user5": {
#         "name": "Sidy Hacko",
#         "phone": 3457466334
#     }
# })
#
# for item in phone_book:
#     print(phone_book[item]["name"],phone_book[item]["phone"])
#
#
# # Student Grades
# # Store student names and their grades in a dictionary.
# #
# # Find the average grade
# #
# # Print students who scored above 80
#
# student_grades = {
#     "user1": {
#         "name": "Samba",
#         "grade": [50, 60, 75, 80, 90]
#     },
#     "user2": {
#         "name": "Vieux",
#         "grade": [50, 60, 15, 80, 90]
#     }
# }
#
# # Add new grade
# student_grades["user2"]["grade"].append(100)
#
# print(student_grades)
#
# def calculate_average():
#     grades = student_grades["user2"]["grade"]
#     average = sum(grades) / len(grades)
#     return average
#
# print(calculate_average())
#
#
#
# # Bank Account System
# # Create a class BankAccount with:
# #
# # Attributes: name, balance
# #
# # Methods: deposit(), withdraw(), show_balance()
#
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount < 1:
#             print("Please enter a positive amount")
#         else:
#             self.balance += amount
#
#     def withdraw(self, amount):
#         if amount < 1:
#             print("Please enter a positive amount")
#         elif amount > self.balance:
#             print("You don't have enough money. Please deposit before you withdraw")
#         else:
#             self.balance -= amount
#     def show_balance(self):
#         print(self.balance)
#
#
# account1 = BankAccount("Ousmane", 500)
#
#
#
# account1.show_balance()
# account1.deposit(200)
# account1.withdraw(400)
# account1.show_balance()
#
#
# # Car Rental System
# # Create a class Car with:
# #
# # Attributes: model, price_per_day
# #
# # Method: calculate_rental(days)
#
# class Car:
#     def __init__(self, model, price_per_day):
#         self.model = model
#         self.price_per_day = price_per_day
#     def calculate_rental(self, days):
#         total_rental = self.price_per_day * days
#         return total_rental
#
#
# customer1 = Car("Mercedes", 2000)
#
# print(customer1.model)
#
# days = 3
# total_cost = customer1.calculate_rental(days)
#
# print(f"Total cost for {days} days: ${total_cost}")
#
#
# # Student Management System
# # Create a class Student with:
# #
# # Attributes: name, age, grades (list)
# #
# # Methods: add_grade(), average_grade()
#
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#     def average_grade(self):
#         return sum(self.grades) / len(self.grades)
#
#
# student1 = Student("Ousmane", 20, [50, 60, 75, 80, 90])
#
# print(student1.average_grade())

#Inheritence

# To-Do App
#
# Create a class Task with:
#
# Attributes: title, completed
#
# Methods: mark_complete(), show_status()

# class ToDoApp:
#     def __init__(self, title, description):
#         self.title = title
#         self.description = description
#         self.completed = False
#
#     def mark_completed(self):
#         self.completed = False
#
#     def show_status(self):
#         status = "Completed ✅" if self.completed else "Pending ⏳"
#         return f"Task: {self.title}\nDescription: {self.description}\nStatus: {status}"
#
# task1 = ToDoApp("Learning OOP", "I am learning the four pillars of OOP")
#
# print(task1.show_status())
#
# task1.mark_completed()
#
# print("\nAfter completing task:\n")
# print(task1.show_status())


# 6. Library System
#
# Create:
#
# Book class → title, author, available
#
# Library class → borrow_book(), return_book()

# class Library:
#     def __init__(self, title, author, available):
#         self.title = title
#         self.author = author
#         self.available = available
#
#     def borrow_book(self):
#         if self.available:
#             borrowed_book = self.title, self.author
#             return f"your borrowed book is {borrowed_book}"
#         else:
#             print("the book is not available")
#     def return_book(self):
#         self.available = True
#
#
# Book = Library("True master", "Ousmane", False)
# Book.borrow_book()
# Book.return_book()
# print(Book.available)
# print(Book.borrow_book())
# print(Book.return_book())
#

# School Management System
#
# Create:
#
# Teacher class
#
# Student class
#
# Classroom class
# With:
#
# Add students
#
# Assign teacher
#
# Print class summary

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def show_summary(self):
        print(f"School: {self.name}")
        print("Students:")
        for s in self.students:
            print(f" - {s.name}, Grade: {s.grade}")
        print("Teachers:")
        for t in self.teachers:
            print(f" - {t.name}, Subject: {t.subject}")


s1 = Student("Ousmane", "10th")
s2 = Student("Samba", "11th")

t1 = Teacher("Mr. John", "Math")
t2 = Teacher("Ms. Anna", "Science")

school = School("Hoboken High School")

school.add_student(s1)
school.add_student(s2)

school.add_teacher(t1)
school.add_teacher(t2)

school.show_summary()