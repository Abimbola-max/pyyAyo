import unittest

from SCMS.src.teacher import Teacher


class MyTestCase(unittest.TestCase):
    def test_that_teacher_can_create_course(self):
        self.teacher = Teacher("firstName", "lastName", "email@gmail.com", "password")
        self.teacher.create_course("courseCode121", "course title")
        self.teacher.number_of_enrolled_
