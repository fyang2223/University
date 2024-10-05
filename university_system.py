from admin_system import AdminSystem
from student_system import StudentSystem


class UniversitySystem:
    def run_menu(self):
        while True:
            selection = input("University System: (A)dmin, (S)tudent, or X:")
            if selection == "A":
                admin_system = AdminSystem()
                admin_system.run_menu()
            elif selection == "S":
                student_system = StudentSystem()
                student_system.run_menu()
            elif selection == "X":
                print("Thank You")
                exit(0)
            else:
                print("Unrecognised")
                exit(-1)


if __name__ == '__main__':
    main = UniversitySystem()
    main.run_menu()
