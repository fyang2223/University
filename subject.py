import random


class Subject:
    def __init__(self, id=None, mark=None, grade=None):
        self.id = id or random.randint(0, 999)
        self.mark = mark or random.randint(25, 100)
        self.grade = grade or self.calculate_grade(mark=self.mark)
        self.enforce_types()

    def __str__(self):
        return f'"{self.id}|{self.mark}|{self.grade}"'

    def enforce_types(self):
        self.id = int(self.id) if self.id else self.id
        self.mark = int(self.mark) if self.mark else self.mark

    def calculate_grade(self, mark: int):
        if mark < 50:
            return "F"
        elif 50 <= mark < 65:
            return "P"
        elif 65 <= mark < 75:
            return "C"
        elif 75 <= mark < 85:
            return "D"
        elif mark >= 85:
            return "HD"
        else:
            raise Exception("Mark is out of bounds. Exiting...")