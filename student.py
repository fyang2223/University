import random


class Student:
    def __init__(self, id=None, email=None, password=None, name=None, subjects=None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.subjects = subjects

    def __str__(self):
        return f"{self.id} | {self.email} | {self.password} | {self.name} | {[str(sub) for sub in self.subjects]}"

    def set_id(self):
        id = f"{random.randint(0, 999999):06}"
        self.id = id
        print("Random ID set.")

    def set_email_password(self):
        email = input("Email:")
        password = input("Password:")
        self.email = email
        self.password = password
        print("Email and password formats acceptable.")

    def set_name(self):
        name = input("Name:")
        self.name = name
        print("Name accepted.")
        self.subjects = []
