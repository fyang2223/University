from enrolment_system import EnrolmentSystem
from student import Student
from database import Database


class StudentSystem:
    def __init__(self):
        self.logged_in = False

    def login(self, email: str, password: str) -> Student:
        database = Database()
        df = database.get_df()
        record = df[(df["email"] == email) & (df["password"] == password)]
        if record.empty:
            print("Student not found")
            email = input("Login Email:")
            password = input("Login Password:")
            return self.login(email=email, password=password)
        student = Student(
            id=record["id"],
            email=record["email"],
            password=record["password"],
            name=record["name"],
            subjects=record["subjects"],
        )
        return student

    def run_menu(self):
        action = input("Student System (l/r/x)")
        if action == "l":
            email = input("Login Email:")
            password = input("Login Password:")
            student = self.login(email=email, password=password)
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
