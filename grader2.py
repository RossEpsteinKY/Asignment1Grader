class Main:
    def __init__(self):
        GetUserInput()


class GetUserInput:
    def __init__(self):
        name = input("What is the student's name?  : >")
        className = input("What is the class name?  : >")
        grade = input("Enter grade for the class: >")
    # user_input = [name, className, grade]
    # test_if_int(user_input)

class UserInput:
    def __init__(self, name, className, grade):
        self.name = name
        self.className = className
        self.grade = grade

x = Main()



