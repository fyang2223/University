from student import Student
from database import Database


class StudentSystem:
    def __init__(self):
        self.logged_in = False

    def selection(self):
        action = input("Student System (l/r/x)")
        if action == "l":
            database = Database()
            login_email = input("Login Email:")
            login_password = input("Login Password:")
            record = database.get_record(login_email=login_email, login_password=login_password)
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
        elif action == "x":
            pass
        else:
            print("Invalid selection.")
            exit()


if __name__ == '__main__':
    menu = StudentSystem()
    menu.selection()
