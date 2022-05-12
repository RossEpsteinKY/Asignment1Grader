# Python 3
import math
global grade
def main():
    grade = input("Enter grade for the class: ")
    test_if_int(grade)

def test_if_int(grade):
    try:
        value = int(grade)
        # print('it is an int')
        find_grade(value)
    except ValueError:
        print("You must enter a value between 0 and 100 for this to work")
        main()
        pass



def print_grade(grade_result):
    print("Your letter grade is " + grade_result)
    main()


def find_grade(grade):
    if grade <= 59:
        grade_result = "F"
        print_grade(grade_result)
    if grade <= 69 and grade >= 60:
        grade_result = "D"
        print_grade(grade_result)
    if grade <= 79 and grade >= 70:
        grade_result = "C"
        print_grade(grade_result)
    if grade <= 89 and grade >= 80:
        grade_result = "B"
        print_grade(grade_result)
    if grade <= 100 and grade >= 90:
        grade_result = "A"
        print_grade(grade_result)
    if grade > 100:
        print("You have entered a grade higher than possible.")
        main()
main()


# find_grade(grade)


