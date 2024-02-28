from Person import *
class Student(Person):
    def __init__(self, firstName, lastName, id, phoneNumber, email, studFileNumber):
        super().__init__(firstName, lastName, id, phoneNumber, email)
        self.studFileNumber = studFileNumber