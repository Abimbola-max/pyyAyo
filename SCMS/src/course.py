from SCMS.exceptions.exception import NotFoundException


COURSE_FILE = 'courses.txt'

class Course:

    def __init__ (self, course_code, course_title):
        self.course_code = course_code
        self.course_title = course_title
        self.__enrolled_student = []

    @property
    def course_title(self):
        return self.__course_title

    @course_title.setter
    def course_title(self, course_title):
        self.__course_title = course_title

    @property
    def course_code(self):
        return self.__course_code

    @course_code.setter
    def course_code(self, course_code):
        self.__course_code = course_code

    def add_student(self, first_name):
        if first_name not in self.__enrolled_student:
            raise NotFoundException(f"{first_name} is not enrolled")
        self.__enrolled_student.append(first_name)

    def remove_student(self, first_name):
        if first_name not in self.__enrolled_student:
            raise NotFoundException(f"{first_name} is not enrolled")
        self.__enrolled_student.remove(first_name)

    def __repr__(self):
        return f"{self.__course_code} - {self.__course_title}"

def save_to_file_C(courses, filename="courses.txt"):
    try:
        with open(filename, 'w') as file:
            for course in courses:
                file.write(f"{course.course_code},{course.course_title}\n")
    except FileNotFoundError:
        print(f"File {filename} not found")

def read_from_file_C(filename="courses.txt"):
    courses = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                file_parts = line.strip().split(',')
                if len(file_parts) == 2:
                    course_code, course_title = file_parts
                    courses.append(Course(course_code, course_title))
                elif len(file_parts) > 0:
                    print("Error")
    except FileNotFoundError:
        print(f"File {filename} not found")
    return courses


