import pandas as pd
from database import Database
from student import Student
from subject import Subject


class EnrolmentSystem:
    def __init__(self, student: Student):
        self.student = student

    def run_menu(self):
        while True:
            selection = input("Student Course Menu: c/e/r/s/x")
            if selection == "c":
                self.change_password()
            elif selection == "e":
                self.enrol_subject()
            elif selection == "r":
                pass
            elif selection == "s":
                self.show_subjects()
            elif selection == "x":
                exit()
            print(self.student)

    def change_password(self):
        new = input("New password:")
        self.student.password = new

    def enrol_subject(self):
        subject = Subject()
        self.student.subjects.append(subject)
        database = Database()
        database.insert(self.student)

    def show_subjects(self):
        for subject in self.student.subjects:
            print(f"Subject id: {subject.id}")
