from Person import *
class Teacher(Person):
    def __init__(self, firstName, lastName, id, phoneNumber, email, teachFileNumber):
        super().__init__(firstName, lastName, id, phoneNumber, email)
        self.teachFileNumber = teachFileNumber