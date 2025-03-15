import bcrypt

from SCMS.exceptions.exception import *
from SCMS.src.user import User
from SCMS.src.validator import Validator

STUDENT_FILENAME = "Student.txt"

class Student(User):

    def __init__(self, first_name, last_name, email, password):
        super().__init__(first_name, last_name, email, password)
        self.is_logged_in = False
        self.enrolled_courses = []

    def get_status(self):
        return self.is_logged_in

    def register(self, first_name, last_name, email, password):
        validator = Validator()
        validator.validate_first_name(first_name)
        validator.validate_last_name(last_name)
        validator.validate_email(email)
        hashed_password = self.encrypt_password(password)
        try:
            with open(STUDENT_FILENAME, "a") as file:
                file.write(f"{first_name},{last_name},{email},{hashed_password}\n")
        except ErrorRegistering as e:
            print(f"Error registering teacher: {e}")

    def login(self, email, password):
        students = read_from_files(STUDENT_FILENAME)
        for student in students:
            if student.email == email:
                if self.verify_password(password, student.password.encode("utf-8")):
                    self.is_logged_in = True
                    return student
                else:
                    self.is_logged_in = False
                    return "Passwords do not match"
        return None

    def enroll_in_course(self, course_code):
        for course in self.enrolled_courses:
            if course.course_code != course_code:
                self.enrolled_courses.append(course_code)
        raise CourseAlreadyRegisteredException("Course code is already registered")

    @staticmethod
    def encrypt_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def save_to_files(students, filename="students.txt"):
    try:
        with open(filename, "w") as file:
            for student in students:
                file.write(f"{student.first_name},{student.last_name},{student.email},{student.password}\n")
    except FileNotFoundError:
        print(f"Error saving to file.")

def read_from_files(filename="teachers.txt"):
    students = []
    try:
        with open(filename, "r") as file:
            for line in file:
                first_name, last_name, email, password = line.strip().split(",")
                student = Student(first_name, last_name, email, password)
                students.append(student)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return students