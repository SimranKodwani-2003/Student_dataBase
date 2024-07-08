import string
import random
import json
import os

class Students:
    database_10th = "10th_students.json"
    database_12th = "12th_students.json"

    def __init__(self):
        self.n = int(input("Enter your class (10 for 10th, 12 for 12th): "))
        self.data = self.load_data()

    def load_data(self):
        file_name = self.database_10th if self.n == 10 else self.database_12th
        if not os.path.exists(file_name):
            print(f"{file_name} not found, creating a new one with an empty list.")
            with open(file_name, 'w') as fs:
                json.dump([], fs)
            return []

        with open(file_name) as fs:
            return json.load(fs)

    def save_data(self):
        file_name = self.database_10th if self.n == 10 else self.database_12th
        with open(file_name, "w") as fs:
            json.dump(self.data, fs, indent=4)

    @classmethod
    def random_id(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        numbers = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=2)
        id_ = alpha + numbers + spchar
        random.shuffle(id_)
        return "".join(id_)

    def register_student(self):
        stu = {
            "id": self.random_id(),
            "name": input("Enter your name: "),
            "email": input("Enter your email: "),
            "password": input("Enter your password: "),
            "age": int(input("Enter your age: "))
        }
        self.data.append(stu)
        self.save_data()
        print("registerd successfully")

    def read_single_student(self):
        id_ = input("Enter Id: ")
        password = input("Enter your password: ")
        students = [student for student in self.data if student["id"] == id_ and student["password"] == password]

        if not students:
            print("Invalid credentials")
        else:
            for key, value in students[0].items():
                print(f"{key}: {value}")

    def access_database(self): 
        if not self.data:
            print("Database is empty!")
        else:
            for index, student in enumerate(self.data, 1):
                print(f"Student {index}:")
                for key, value in student.items():
                    print(f"{key}: {value}")
                print()

    def update_student(self):
        id_ = input("Enter Id: ")
        password = input("Enter your password: ")
        students = [student for student in self.data if student["id"] == id_ and student["password"] == password]

        if not students:
            print("Invalid credentials")
        else:
            print("Enter new information (leave empty to skip):")
            for key in students[0]:
                new_value = input(f"{key} ({students[0][key]}): ")
                if new_value:
                    if key == "age":
                        students[0][key] = int(new_value)
                    else:
                        students[0][key] = new_value
            self.save_data()

    def delete_student(self):
        id_ = input("Enter Id: ")
        password = input("Enter your password: ")
        students = [student for student in self.data if student["id"] == id_ and student["password"] == password]

        if not students:
            print("Invalid credentials")
        else:
            self.data.remove(students[0])
            self.save_data()

obj = Students()

while True:
    print("""
    Select an option:
1. Register a student
2. Login student profile
3. Access Database
4. Update student data
5. Delete student data
6. Exit the application
    """)
    response = input("Enter your response: ")

    if response == "6":
        print("Exit successfully")
        break
    elif response == "1":
        obj.register_student()
    elif response == "2":
        obj.read_single_student()
    elif response == "3":
        obj.access_database()
    elif response == "4":
        obj.update_student()
    elif response == "5":
        obj.delete_student()
    else:
        print("Invalid option")
