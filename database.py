import pandas as pd
from student import Student


class Database:
    def __init__(self):
        pass

    def insert(self, student: Student):
        """
        Insert a student into the 'students.data' file.
        """
        try:
            existing_students_df = pd.read_csv("students.data")
        except FileNotFoundError as e:
            print("Could not find existing students.data file. Creating new file...")
            existing_students_df = pd.DataFrame(
                columns=["id", "email", "password", "name", "subjects"]
            )
        new_student_df = pd.DataFrame(
            data={
                "id": [student.id],
                "email": [student.email],
                "password": [student.password],
                "name": [student.name],
                "subjects": [student.subjects],
            }
        )
        new_df = pd.concat([existing_students_df, new_student_df], ignore_index=True)
        new_df.to_csv("students.data", index=False)

    def get_record(self, email, password):
        data = {
            "id": "123456",
            "email": "testing",
            "password": "testing",
            "name": "testing",
            "subjects": "testing",
        }
        return data


if __name__ == '__main__':
    db = Database()
    student = Student(12, "adfsaf", "232asdf", "as dgf", [52345, 54737, 4567])
    db.insert(student)