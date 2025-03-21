import os

import bcrypt

from SCMS.exceptions.exception import *
from SCMS.src.course import Course, read_from_file_C, save_to_file_C
from SCMS.src.student import STUDENT_FILENAME
from SCMS.src.user import User
from SCMS.src.validator import Validator

TEACHER_FILENAME = "teachers.txt"

class Teacher(User):

    def __init__(self, first_name="", last_name="", email="", password=""):
        super().__init__(first_name, last_name, email, password)
        self.is_logged_in = False

    def get_status(self):
        return self.is_logged_in

    def register(self, first_name, last_name, email, password):
        hashed_password = self.encrypt_password(self.password)

        if os.path.exists(STUDENT_FILENAME):
            with open(STUDENT_FILENAME, "r") as student_file:
                for line in student_file:
                    if email in line:
                        raise EmailAlreadyExistException(f"Email {email} already exists")

        if os.path.exists(TEACHER_FILENAME):
            with open(TEACHER_FILENAME, "r") as teacher_file:
                for line in teacher_file:
                    if email in line:
                        raise EmailAlreadyExistException(f"Email {email} already exists")
        try:
            with open(TEACHER_FILENAME, "a") as file:
                file.write(f"{first_name},{last_name},{email},{hashed_password}\n")
        except ErrorRegistering as e:
            print(f"Error registering teacher: {e}")


    def login(self, email, password):
        teachers = read_from_files(TEACHER_FILENAME)
        for teacher in teachers:
            if teacher.email == email and self.verify_password(password, teacher.password):
                self.is_logged_in = True
                return teacher
        self.is_logged_in = False
        return None

    @staticmethod
    def create_course(course_code, course_title):
        existing_course = read_from_file_C("courses.txt")
        for course in existing_course:
            if course.course_code == course_code:
                raise CourseAlreadyRegisteredException("Course already exists")

        new_course = Course(course_code, course_title)
        existing_course.append(new_course)
        save_to_file_C(existing_course, 'courses.txt')
        return new_course

    # def view_student_enrolled_in_a_course(self):

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

def save_to_files(teachers, filename="teachers.txt"):
    try:
        with open(filename, "w") as file:
            for teacher in teachers:
                file.write(f"{teacher.first_name},{teacher.last_name},{teacher.email},{teacher.password}\n")
    except FileNotFoundError:
        print(f"Error saving to file.")

def read_from_files(filename="teachers.txt"):
    teachers = []
    try:
        with open(filename, "r") as file:
            for line in file:
                first_name, last_name, email, password = line.strip().split(",")
                teacher = Teacher(first_name, last_name, email, password)
                teachers.append(teacher)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return teachers
