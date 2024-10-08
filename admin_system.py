import os
import statistics
from database import Database
from subject import Subject

class AdminSystem:
    def __init__(self):
        self.database = Database()

    def clear_database(self):
        print("Clearing students database")
        filename = f"{os.getcwd()}/students.data"
        os.system(f"rm {filename}")

    def group_grades(self):
        # TODO: Handle cases where a student has no enrolled subjects
        df = self.database.get_df()
        df["avg"] = df["subjects"].apply(lambda x: statistics.mean([sub.mark for sub in x]))
        df["wam_grade"] = df["avg"].apply(Subject.calculate_grade)
        df["formatted_output"] = df.apply(lambda x: f"{x['wam_grade']}  --> [{x['name']} :: {x['id']} --> GRADE:  {x['wam_grade']} - MARK: {x['avg']}]", axis=1)
        for _, row in df.iterrows():
            print(row["formatted_output"])

    def partition(self):
        # TODO: Handle cases where a student has no enrolled subjects
        df = self.database.get_df()
        df["avg"] = df["subjects"].apply(lambda x: statistics.mean([sub.mark for sub in x]))
        df["wam_grade"] = df["avg"].apply(Subject.calculate_grade)
        df["formatted_output"] = df.apply(lambda x: f"{x['name']} :: {x['id']} --> GRADE:  {x['wam_grade']} - MARK: {x['avg']}", axis=1)
        df_failed = df[df["avg"] < 50]
        df_passed = df[df["avg"] >= 50]
        print(f"FAIL --> [{', '.join(df_failed['formatted_output'])}]")
        print(f"PASS --> [{', '.join(df_passed['formatted_output'])}]")

    def remove_student(self):
        df = self.database.get_df()
        id_to_drop = input("Remove by ID: ")
        i = df[df["id"] == id_to_drop].index
        if i.empty:
            print(f"Student {id_to_drop} does not exist")
            return
        df.drop(i, inplace=True)
        self.database.rewrite_df(df=df)

    def list_students(self):
        df = self.database.get_df()
        print("Student List")
        df["formatted_output"] = df.apply(lambda x: f"{x['name']} :: {x['id']} --> Email: {x['email']}", axis=1)
        for _, row in df.iterrows():
            print(row["formatted_output"])

    def run_menu(self):
        while True:
            action = input("Admin System (c/g/p/r/s/x): ")
            if action == "c":
                self.clear_database()
            elif action == "g":
                self.group_grades()
            elif action == "p":
                self.partition()
            elif action == "r":
                self.remove_student()
            elif action == "s":
                self.list_students()
            elif action == "x":
                break
            else:
                print("Invalid selection.")
                exit(-1)
