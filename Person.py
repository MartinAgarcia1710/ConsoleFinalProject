class Person:
    firstName = ""
    lastName = ""
    id = ""
    phoneNumber = ""
    email = ""
    status = True

    def newPerson(self):
        self.firstName = input("Enter first name:\n")
        self.lastName = input("Enter last name:\n")
        self.id = input("Enter ID:\n")
        while True:
            try:
                self.phoneNumber = input("Enter phone number\n")
                break
            except ValueError:
                print("only numbers")
        self.email = input("Enter e-mail")



