import json
import os
import pandas as pd
from typing import List, Optional
from student import Student
from subject import Subject


class Database:
    def __init__(self):
        pass

    def _parse_to_object(self, subjects_string: str) -> List[Subject]:
        """
        Receive a string representation of subjects, and return a list of Subject instances.
        """
        subjects = json.loads(subjects_string)
        subject_list = [Subject(*s.split(sep="|", maxsplit=2)) for s in subjects]
        return subject_list

    def _parse_to_string(self, subjects_list: List[Subject]) -> str:
        """
        Receive a list of Subject instances, and format each Subject into a pipe-separated string
        of the format "<id>|<mark>|<grade>". Then join each string representation of a subject
        with each other using commas, resulting in a string such as "111|99|HD,222|80|D".
        """
        subjects = [str(sub) for sub in subjects_list]
        subjects_string = f"[{','.join(subjects)}]"
        return subjects_string

    def update_record(self, df: pd.DataFrame, new_record: pd.DataFrame, email: str, password: str) -> pd.DataFrame:
        """
        If the student's email and password does not exist in the df, add the record. Otherwise, if
        a record matches in the df, replace the student's record with a new record.
        """
        df = df.drop(df[(df["email"] == email) & (df["password"] == password)].index)
        new_df = pd.concat([df, new_record], ignore_index=True)
        return new_df

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
        new_df = self.update_record(df=existing_students_df, new_record=new_student_df, email=student.email, password=student.password)
        new_df['subjects'] = new_df['subjects'].map(self._parse_to_string)
        new_df.to_csv("students.data", index=False, quotechar="'")

    def get_df(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(f"{os.getcwd()}/students.data", dtype="object", quotechar="'")
            df["subjects"] = df["subjects"].map(self._parse_to_object)
        except FileNotFoundError as e:
            print("Could not find existing students.data file to load dataframe. Creating new Dataframe...")
            df = pd.DataFrame(
                columns=["id", "email", "password", "name", "subjects"]
            )
        return df

    def get_student(self, email: str, password: str) -> Optional[Student]:
        df = self.get_df()
        record = df[(df["email"] == email) & (df["password"] == password)]
        assert len(record) <= 1, f"More than one matching student found for email and password combination for {email}"
        if not record.empty:
            return Student(
                id=record.iloc[0]["id"],
                email=record.iloc[0]["email"],
                password=record.iloc[0]["password"],
                name=record.iloc[0]["name"],
                subjects=record.iloc[0]["subjects"],
            )
        return None


