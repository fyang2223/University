from typing import List

import pandas as pd
import json
from student import Student
from subject import Subject


class Database:
    def __init__(self):
        pass

    def parse_to_object(self, subjects_string: str) -> List[Subject]:
        """
        Receive a string representation of subjects, and return a list of Subject instances.
        """
        subjects = json.loads(subjects_string)
        # subjects = subjects_string.split(sep=",")
        subject_list = [Subject(*s.split(sep="|", maxsplit=2)) for s in subjects]
        return subject_list

    def parse_to_string(self, subjects_list: List[Subject]) -> str:
        """
        Receive a list of Subject instances, and format each Subject into a pipe-separated string
        of the format "<id>|<mark>|<grade>". Then join each string representation of a subject
        with each other using commas, resulting in a string such as "111|99|HD,222|80|D".
        """
        subjects = [f'"{str(sub)}"' for sub in subjects_list]
        subjects_string = f'[{",".join(subjects)}]'
        return subjects_string or []

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
        new_df['subjects'] = new_df['subjects'].map(self.parse_to_string)
        new_df.to_csv("students.data", index=False, quotechar="'")

    def get_df(self) -> pd.DataFrame:
        try:
            df = pd.read_csv("/Users/forestyang/PycharmProjects/University/students.data", dtype="object", quotechar="'")
            df["subjects"] = df["subjects"].map(self.parse_to_object)
        except FileNotFoundError as e:
            print("Could not find existing students.data file to load dataframe. Creating new Dataframe...")
            df = pd.DataFrame(
                columns=["id", "email", "password", "name", "subjects"]
            )
        return df

# TODO: Format __str__ in Subject and Student
# TODO: Use string type for all outgoing dataframes
# TODO: Override existing student with new data