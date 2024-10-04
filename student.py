import random

import pandas as pd

from database import Database


class Student:
    def __init__(self, id=None, email=None, password=None, name=None, subjects=None):
        self.id = id
        self.email = email
        self.password = password
        self.name = name
        self.subjects = subjects if subjects else []

    def __str__(self):
        return f"{self.id}|{self.email}|{self.password}|{self.name}|[{','.join([str(sub) for sub in self.subjects])}]"

    def set_id(self):
        id = f"{random.randint(0, 999999):06}"
        self.id = id
        print("Random ID set.")
