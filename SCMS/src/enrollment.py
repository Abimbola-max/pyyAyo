class Enrollment:

    def __init__(self, student, course):
        self.student = student
        self.course = course

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, student):
        self.__student = student

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        self.__course = course


def save_enrollment(enrollments, filename="enrollment.txt"):
    try:
        with open(filename, "w") as file:
            for enrollment in enrollments:
                file.write(f"{enrollment.student},{enrollment.course}\n")
    except FileNotFoundError:
        print("Enrollment file not found.")

def load_enrollment(filename="enrollment.txt"):
    enrollments = []
    try:
        with open(filename, "r") as file:
            for enrollment in file:
                student, course = enrollment.strip().split(",")
                enrollment = Enrollment(student, course)
                enrollments.append(enrollment)
    except FileNotFoundError:
        print("Enrollment file not found.")
    return enrollments



