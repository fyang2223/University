from typing import Optional

from enrolment_system import EnrolmentSystem
from student import Student
from database import Database


class StudentSystem:
    def __init__(self):
        self.database = Database()

    def check_email_password_format(self, email: str, password: str):
        # TODO: Add email and password checking logic
        if len(email) > 1 and len(password) > 1:
            return True
        return False

    def run_enrolment(self, student: Student):
        enrolment_system = EnrolmentSystem(student=student)
        enrolment_system.run_menu()

    def run_login(self) -> Student:
        email = input("Login Email:")
        password = input("Login Password:")
        if self.check_email_password_format(email=email, password=password):
            student = self.database.get_student(email=email, password=password)
            if student:
                print(f"Proceeding to Enrolment menu with student {student}")
                return student
            print("Student does not exist")
            self.run_login()
        print("Incorrect email or password format")
        self.run_login()

    def run_registration(self) -> Optional[Student]:
        student = Student()
        student.set_id()
        email = input("Email: ")
        password = input("Password: ")
        if self.check_email_password_format(email=email, password=password):
            existing_student = self.database.get_student(email=email, password=password)
            if existing_student:
                print(f"Student {existing_student.name} already exists")
                return None
            student.email = email
            student.password = password
            name = input("Name:")
            student.name = name
            print(f"Enrolling Student {name}")
            self.database.insert(student=student)
            return student
        print("Incorrect email or password format")
        self.run_registration()

    def run_menu(self):
        while True:
            action = input("Student System (l/r/x)")
            if action == "l":
                student = self.run_login()
                self.run_enrolment(student=student)
            elif action == "r":
                student = self.run_registration()
            elif action == "x":
                print("Thank You.")
                exit()
            else:
                print("Invalid selection.")
                exit(-1)
