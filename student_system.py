from enrolment_system import EnrolmentSystem
from student import Student
from database import Database


class StudentSystem:
    def __init__(self):
        self.logged_in = False

    def run_menu(self):
        action = input("Student System (l/r/x)")
        if action == "l":
            database = Database()
            email = input("Login Email:")
            password = input("Login Password:")
            record = database.get_record(email=email, password=password)
            student = Student(
                id=record["id"],
                email=record["email"],
                password=record["password"],
                name=record["name"],
                subjects=record["subjects"],
            )
            self.logged_in = True
            print(f"Student is: {student}")
        elif action == "r":
            student = Student()
            student.set_id()
            student.set_email_password()
            student.set_name()
            self.logged_in = True
            print(f"Student is: {student}")
            database = Database()
            database.insert(student=student)
        elif action == "x":
            exit()
        else:
            print("Invalid selection.")
            exit()

        if self.logged_in:
            enrolment_system = EnrolmentSystem(student=student)
            enrolment_system.run_menu()
