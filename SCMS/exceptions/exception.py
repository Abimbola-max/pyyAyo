class InvalidCourseCodeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidCourseTitleException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseIsFullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class StudentAlreadyEnrolledException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class CourseAlreadyRegisteredException(RuntimeError):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NullException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidPasswordLengthException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidEmailPatternException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidNameLengthException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidNameException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidDetailsException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class VerificationFailedException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class NotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class InvalidGradeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EmailAlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AlreadyExistException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ErrorRegistering(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)