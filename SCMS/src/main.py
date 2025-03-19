import sys

from SCMS.exceptions.exception import *
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
                        3 --> Go Back
                        4 --> Exit
                    """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.register_teacher()
        elif choice == "2":
            self.register_student()
        elif choice == "3":
            self.main_menu()
        elif choice == "4":
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
                   3 --> Go back
                   4 --> Exit
                   """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.login_teacher()
        elif choice == "2":
            self.login_student()
        elif choice == "3":
            self.register_menu()
        elif choice == "4":
            self.exit_app()
        else:
            self.main_menu()

    def login_teacher(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            teacher_login = Teacher()
            current_teacher = teacher_login.login(email, password)
            if current_teacher is not None:
                print(f"You have successfully logged in {Teacher.first_name} {Teacher.last_name}2")
                self.teacher_menu()
            else:
                print("Invalid email or password")
                self.login_teacher()
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
            4 -> Go back
            5 -> logout
             """)
            choice = input("Kindly enter any choice from the above: ")

            if choice == "1":
                self.create_course()
            # elif choice == '2':
            #     self.view_number_of_student_registered()
            # elif choice == '3':
            #     self.grade_student()
            elif choice == "4":
                self.login_menu()
            elif choice == '4':
                print("logging out mf...")
                self.main_menu()
        except InvalidNameLengthException as e:
            print(f"Error: {e}")

    def login_student(self):
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            student_login = Student()
            current_student = student_login.login(email, password)
            if current_student is not None:
                print(f"You have successfully logged in {Student.first_name} {Student.last_name}")
                self.student_menu()
            else:
                print("Invalid email or password")
                self.login_student()
        except InvalidNameLengthException as e:
            print(f"Error {e}")
        except InvalidNameException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")

    def student_menu(self):
        print("""
            1. View Available Courses
            2. Enroll in Course(s)
            3. View enrolled Course(s)
            4. View grades
            5. Logout
            """)
        choice = input("Kindly enter any choice from the above: ")
        if choice == "1":
            self.view_courses()
        elif choice == "2":
            self.enroll()
        elif choice == "3":
            self.view_enrolled_courses()
        elif choice == "4":
            self.view_grade()
        elif choice == "5":
            self.main_menu()
        else:
            self.main_menu()

    def create_course(self):
        try:
            validate_course = Validator()
            course_code = input("Enter course code: ")
            validate_course.validate_course_code(course_code)
            course_title = input("Enter course title: ")
            validate_course.validate_course_title(course_title)
            course = Teacher.create_course(course_code, course_title)
            if course is not None:
                print(f"You have created {course_code} successfully.")
                self.teacher_menu()
            else:
                print("Invalid course")
                self.create_course()
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        except InvalidCourseTitleException as e:
            print(f"Error {e}")
        except CourseAlreadyRegisteredException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")

    def enroll(self):
        try:
            course_code = input("Enter course code: ")
            Validator.validate_course_code(course_code)
            student = Student()
            enroll = student.enroll_in_course(course_code)
            if enroll is not None:
                print(f"You have enrolled in {course_code} successfully.")
                self.student_menu()
            else:
                print("Invalid course")
                self.student_menu()
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        except NullException as e:
            print(f"Error {e}")
        except CourseAlreadyRegisteredException as e:
            print(f"Error {e}")
        except NotFoundException as e:
            print(f"Error {e}")

    def view_courses(self):
        try:
            student = Student()
            # student.available_enrolled_courses()
            print(f"Available courses are: \n{student.available_enrolled_courses()}")
            self.student_menu()
        except InvalidCourseCodeException as e:
            print(f"Error {e}")
        except CourseAlreadyRegisteredException as e:
            print(f"Error {e}")

    @staticmethod
    def exit_app():
        print("Exiting App.")
        print(">>>>>>>>>>>>>>>>>>>>.")
        sys.exit(0)

    @staticmethod
    def welcome() -> None:
        print("Welcome to GROUP 6 SCMS\n")
        print("The next page Displays And Help You With Your Choice ?\n")

    def view_enrolled_courses(self):
        try:
            student = Student()
            student.view_enrolled_courses()
        except NotFoundException as e:
            print(f"Error {e}")
        finally:
            self.student_menu()


if __name__ == "__main__":
    app = Main()
    app.main_menu()