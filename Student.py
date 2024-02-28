from Person import *
class Student(Person):

    studFileNumber = ""

    def newStudent(self):
        super().newPerson()
        self.studFileNumber = input("Enter Student's file:\n")