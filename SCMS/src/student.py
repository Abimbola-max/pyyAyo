import bcrypt

from SCMS.exceptions.exception import *
from SCMS.src.course import read_from_file_C
from SCMS.src.enrollment import Enrollment, save_enrollment, load_enrollment
from SCMS.src.user import User
from SCMS.src.validator import Validator

STUDENT_FILENAME = "Student.txt"

class Student(User):

    def __init__(self, first_name="", last_name="", email="", password=""):
        super().__init__(first_name, last_name, email, password)
        self.is_logged_in = False
        self.enrolled_courses = []

    def get_status(self):
        return self.is_logged_in

    def register(self, first_name, last_name, email, password):
        hashed_password = self.encrypt_password(password)
        try:
            with open(STUDENT_FILENAME, "a") as file:
                file.write(f"{first_name},{last_name},{email},{hashed_password}\n")
        except ErrorRegistering as e:
            print(f"Error registering teacher: {e}")

    def login(self, email, password):
        students = read_from_files(STUDENT_FILENAME)
        for student in students:
            if student.email == email and self.verify_password(password, student.password):
                self.is_logged_in = True
                return student

        self.is_logged_in = False
        return None

    def enroll_in_course(self, course_code):
        courses = read_from_file_C("courses.txt")
        # enroll = load_enrollment("enroll.txt")

        if course_code in self.enrolled_courses:
            raise CourseAlreadyRegisteredException(f"Course code '{course_code}' is already registered.")

        enrolled = False
        for course in courses:
            if course.course_code == course_code:
                self.enrolled_courses.append(course_code)
                enrolled = True
                print(f"{Student.first_name} has successfully enrolled in course '{course_code}'.")

        if not enrolled:
            raise InvalidCourseCodeException(f"Course code '{course_code}' not found.")

    def view_enrolled_courses(self):
        if self.enrolled_courses:
            print("enrolled courses:\n")
            for course in self.enrolled_courses:
                print(f"{course}")
        raise NotFoundException("You never enroll my guy.")

    @staticmethod
    def view_courses():
        courses = read_from_file_C("courses.txt")
        return list(courses)

    @staticmethod
    def available_enrolled_courses():
        available_enrolled_courses = Student.view_courses()
        return available_enrolled_courses

    @staticmethod
    def encrypt_password(password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    @staticmethod
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    def __repr__(self):
        return f"{self.first_name},{self.last_name}"

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