from database import Database
from student import Student
from subject import Subject


class EnrolmentSystem:
    def __init__(self, student: Student):
        self.student = student
        self.database = Database()

    def change_password(self):
        new_password = input("New password: ")
        new_password_conf = input("Confirm password: ")
        if new_password != new_password_conf:
            print("Password does not match - try again")
            self.change_password()
        if len(new_password) < 2:
            print("Password condition not met.")
            self.change_password()
        self.student.password = new_password

    def enrol_subject(self):
        subject = Subject()
        print(f"Enrolling in Subject-{subject.id}")
        self.student.subjects.append(subject)
        self.database.insert(self.student)

    def remove_subject(self):
        id = input("Remove subject by ID: ")
        self.student.subjects = [sub for sub in self.student.subjects if sub.id != ]
        # TODO: complete this
    def show_subjects(self):
        for subject in self.student.subjects:
            print(f"[ Subject::{subject.id} -- mark = {subject.mark} -- grade = {subject.grade}")

    def run_menu(self):
        while True:
            selection = input("Student Course Menu: c/e/r/s/x")
            if selection == "c":
                self.change_password()
            elif selection == "e":
                self.enrol_subject()
            elif selection == "r":
                self.remove_subject()
            elif selection == "s":
                self.show_subjects()
            elif selection == "x":
                print("Thank You.")
                exit()
            print(self.student)
