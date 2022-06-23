class Main:
    def __init__(self):
        GetUserInput()


class GetUserInput:
    def __init__(self):
        name = input("What is the student's name?  : >")
        className = input("What is the class name?  : >")
        grade = input("Enter grade for the class: >")

        TestIfInt(name,className,grade)

class TestIfInt:
    def __init__(self, name, className, grade):
        try:
            self.name = name
            self.className = className
            self.grade = grade

            value = int(self.grade)
            self.grade = value

            user_input = [self.name, self.className, self.grade]
            # print('it is an int')
            find_grade(self.name,self.className,self.grade)
        except ValueError:
            print("You must enter a value between 0 and 100 for this to work")
            Main()
            pass

class UserInput:
    def __init__(self, name, className, grade):
        self.name = name
        self.className = className
        self.grade = grade

class find_grade:
    def __init__(self, name, className, grade):
        self.name = name
        self.className = className
        self.grade = grade
        self.grade_result = ''


        grade = self.grade
        if grade <= 59:
            self.grade_result = "F"
            print_grade(self.name,self.className,self.grade, self.grade_result)
        if grade <= 69 and grade >= 60:
            self.grade_result = "D"
            print_grade(self.name,self.className,self.grade, self.grade_result)
        if grade <= 79 and grade >= 70:
            self.grade_result = "C"
            print_grade(self.name,self.className,self.grade, self.grade_result)
        if grade <= 89 and grade >= 80:
            self.grade_result = "B"
            print_grade(self.name,self.className,self.grade, self.grade_result)
        if grade <= 100 and grade >= 90:
            self.grade_result = "A"
            print_grade(self.name,self.className,self.grade, self.grade_result)
        if grade > 100:
            print("You have entered a grade higher than possible.")
            Main()

class print_grade():
    def __init__(self, name,className,grade,grade_result):
        self.name = name
        self.className = className
        self.grade = grade
        self.grade_result = grade_result
        print("%s received a letter grade of %s in the class %s" % (self.name, self.grade_result, self.className))
        Main()

x = Main()



