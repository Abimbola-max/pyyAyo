from SCMS.exceptions.exception import NotFoundException


COURSE_FILE = 'course.txt'

class Course:

    def __init__ (self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title
        self.__enrolled_student = []

    @property
    def course_title(self):
        return self.__course

    @course_title.setter
    def course_title(self, course_title):
        self.__course = course_title

    @property
    def course_code(self):
        return self.__course

    @course_code.setter
    def course_code(self, course_code):
        self.__course = course_code

    def add_student(self, first_name):
        if first_name not in self.__enrolled_student:
            raise NotFoundException(f"{first_name} is not enrolled")
        self.__enrolled_student.append(first_name)

    def remove_student(self, first_name):
        if first_name not in self.__enrolled_student:
            raise NotFoundException(f"{first_name} is not enrolled")
        self.__enrolled_student.remove(first_name)

def save_to_file_C(courses, COURSE_FILE):
    try:
        with open(COURSE_FILE, 'a') as file:
            for course in courses:
                file.write(f"{course.course_code},{course.course_title},\n")
    except FileNotFoundError:
        print(f"File {COURSE_FILE} not found")

def read_from_file_C(COURSE_FILE):
    courses = []
    try:
        with open(COURSE_FILE, 'r') as file:
            for line in file:
                course_code, course_title = line.strip().split(',')
                courses.append(Course(course_code, course_title))
    except FileNotFoundError:
        print(f"File {COURSE_FILE} not found")
    return courses


