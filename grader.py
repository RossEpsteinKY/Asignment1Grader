# Python 3
#command to run is python3 grader.py

global grade
def main():
    name = input("What is the student's name?  : >")
    className = input("What is the class name?  : >")
    grade = input("Enter grade for the class: >")

    user_input = [name, className, grade]
    test_if_int(user_input)

def test_if_int(user_input):
    try:
        value = int(user_input[2])
        user_input[2] = value
        # print('it is an int')
        find_grade(user_input)
    except ValueError:
        print("You must enter a value between 0 and 100 for this to work")
        main()
        pass

def print_grade(user_input):
    print("%s received a letter grade of %s in the class %s" % (user_input[0], user_input[3], user_input[1]))
    main()

def find_grade(user_input):
    grade = user_input[2]
    if grade <= 59:
        grade_result = "F"
        user_input.append(grade_result)
        print_grade(user_input)
    if grade <= 69 and grade >= 60:
        grade_result = "D"
        user_input.append(grade_result)
        print_grade(user_input)
    if grade <= 79 and grade >= 70:
        grade_result = "C"
        user_input.append(grade_result)
        print_grade(user_input)
    if grade <= 89 and grade >= 80:
        grade_result = "B"
        user_input.append(grade_result)
        print_grade(user_input)
    if grade <= 100 and grade >= 90:
        grade_result = "A"
        user_input.append(grade_result)
        print_grade(user_input)
    if grade > 100:
        print("You have entered a grade higher than possible.")
        main()
main()

