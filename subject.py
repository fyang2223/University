import random


class Subject:
    def __init__(self):
        self.id = random.randint(0, 999)
        self.mark = random.randint(25, 100)
        self.grade = self.calculate_grade(mark=self.mark)

    def __str__(self):
        return f"{self.id} | {self.mark} | {self.grade}"

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