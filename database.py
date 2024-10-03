import pandas as pd
from student import Student


class Database:
    def __init__(self):
        pass

    def insert(self, student: Student):
        """
        Insert a student into the 'students.data' file.
        """
        existing_students_df = self.get_df()
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

    def get_df(self) -> pd.DataFrame:
        try:
            df = pd.read_csv("students.data")
        except FileNotFoundError as e:
            print("Could not find existing students.data file to load dataframe. Creating new Dataframe...")
            df = pd.DataFrame(
                columns=["id", "email", "password", "name", "subjects"]
            )

        data = {
            "id": "123456",
            "email": "testing",
            "password": "testing",
            "name": "testing",
            "subjects": "testing",
        }
        return df


if __name__ == '__main__':
    db = Database()
    student = Student(12, "adfsaf", "232asdf", "as dgf", [52345, 54737, 4567])
    db.insert(student)