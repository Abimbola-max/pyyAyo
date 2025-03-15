import sys

from SCMS.exceptions.exception import *
from SCMS.src import teacher
from SCMS.src.student import Student
from SCMS.src.teacher import Teacher
from SCMS.src.validator import Validator


class Main:

    def main_menu(self):
        self.welcome()
        print("""
                   1 --> Register
                   2 --> Login
                   3 --> Exit
        """)

        print("Kindly enter any choice from the above:")
        choice = input("still waiting: ")

        match choice:
            case "1":
                self.register_menu()
            case "2":
                self.login_menu()
            case "3":
                self.exit_app()
            case _:
                print("invalid choice, try again")
                self.main_menu()

    def register_menu(self):
        print("""
                        1 --> Register as a teacher
                        2 --> Register as a student
                        3 --> Exit
                    """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.register_teacher()
        elif choice == "2":
            self.register_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()

    def register_teacher(self):
        validator = Validator()
        try:
            first_name = input("Enter your First name: ")
            validator.validate_first_name(first_name)
            last_name = input("Enter Last name: ")
            validator.validate_last_name(last_name)
            email = input("Enter your email: ")
            validator.validate_email(email)
            password = input("Enter your password: ")
            validator.validate_password(password)
            teacher = Teacher(first_name, last_name, email, password)
            teacher.register(first_name, last_name, email, password)
            print(f"Dear {first_name} {last_name}, You have successfully registered")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        except ErrorRegistering as e:
            print(f"Error {e}")
        except EmailAlreadyExistException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def register_student(self):
        validator = Validator()
        try:
            first_name = input("Enter your First name: ")
            validator.validate_first_name(first_name)
            last_name = input("Enter your Last name: ")
            validator.validate_last_name(last_name)
            email = input("Enter your email: ")
            validator.validate_email(email)
            password = input("Enter your password: ")
            validator.validate_password(password)
            student = Student(first_name, last_name, email, password)
            student.register(first_name, last_name, email, password)
            print(f"Dear {first_name} {last_name}, You have successfully registered")
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        except ErrorRegistering as e:
            print(f"Error {e}")
        except EmailAlreadyExistException as e:
            print(f"Error {e}")
        finally:
            self.main_menu()

    def login_menu(self):
        print("""
                                   1 --> Login as a teacher
                                   2 --> Login as a student
                                   3 --> Exit
                               """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.login_teacher()
        # elif choice == "2":
        #     self.login_student()
        elif choice == "3":
            self.exit_app()
        else:
            self.main_menu()

    def login_teacher(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            teacher_login = Teacher()
            teacher_login.login(email, password)
            print(f"You have successfully logged in")
            self.teacher_menu()
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        # finally:
        #     self.main_menu()

    def teacher_menu(self):
        try:
            print("""
            1 -> Add course
            2 -> View number of students registered
            3 -> Grade student
            4 -> logout
             """)
            choice = input("Kindly enter any choice from the above: ")

            if choice == "1":
                self.create_course()
            # elif choice == '2':
            #     self.view_number_of_student_registered()
            # elif choice == '3':
            #     self.grade_student()
            elif choice == '4':
                print("logging out mf...")
                self.main_menu()
        except InvalidNameLengthException as e:
            print(f"Error: {e}")

    def create_course(self):
        try:
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            teacher_create = Teacher()
            teacher_create.create_course(course_code, course_title)
            print(f"You have created {course_code} successfully.")
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        except InvalidCourseTitleException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        finally:
            self.teacher_menu()

    @staticmethod
    def exit_app():
        print("Exiting App.")
        print(">>>>>>>>>>>>>>>>>>>>.")
        sys.exit(0)

    @staticmethod
    def welcome() -> None:
        print("Welcome to GROUP 6 SCMS\n")
        print("The next page Displays And Help You With Your Choice ?\n")




if __name__ == "__main__":
    app = Main()
    app.main_menu()