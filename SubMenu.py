class SubMenu():
    def __init__(self, options, name):
        self.options = options
        self.name = name
    def showMenu(self):
        print(f'\t\t{self.name}')
        for x, option in enumerate(self.options, start = 1):
            print(f'{x}. {option}')
    def selectOption(self):
        while True:
            try:
                option = (int(input("Select an option")))
                if option < 1 or option > len(self.options):
                    print("Invalid option. Please try again")
                else:
                    return option
            except ValueError:
                print("Please enter a valid number")