import optionFunctions
from Student import *
from SubMenu import *
from optionFunctions import *
re = Student("Martin", "Garcia", 34568, 789456, "seg@egs.sdgf", "5675")

while True:
    print("\t\tEAST GREAT FALLS SCHOOL\n")
    print("1.Students\n2.Teachers\n3.Subjects\n4.Exit\n")
    try:
        option = (int(input("Select option\n")))
    except ValueError:
        print("You can only use numbers, let's go again\n")

    if option ==1:
        studentOptions = ["Add student", "Show students", "Return"]
        stMenu = SubMenu(studentOptions, "STUDENTS MENU")
        stMenu.showMenu()
        op = stMenu.selectOption()
        optionFunctions.studentsOptions(op)

    elif option == 2:
        teachersOptions = ["Add Teacher", "Show teachers", "Return"]
        teMenu = SubMenu(teachersOptions, "TEACHERS MENU")
        teMenu.showMenu()
        op = teMenu.selectOption()
    elif option == 3:
        subjectOptions = ["Add subject", "Show subjects", "Return"]
        suMenu = SubMenu(teachersOptions, "SUBJECTS MENU")
        suMenu.showMenu()
        op = suMenu.selectOption()
    elif option == 4:
        exit()
