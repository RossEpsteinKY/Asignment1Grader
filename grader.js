function main() {
    var className, grade, name, user_input;
    name = input("What is the student's name?  : >");
    className = input("What is the class name?  : >");
    grade = input("Enter grade for the class: >");
    user_input = [name, className, grade];
    test_if_int(user_input);
}

function test_if_int(user_input) {
    var value;

    try {
        value = Number.parseInt(user_input[2]);
        user_input[2] = value;
        find_grade(user_input);
    } catch (e) {
        if (e instanceof ValueError) {
            console.log("You must enter a value between 0 and 100 for this to work");
            main();
        } else {
            throw e;
        }
    }
}

function print_grade(user_input) {
    console.log("%s received a letter grade of %s in the class %s" % [user_input[0], user_input[3], user_input[1]]);
    main();
}

function find_grade(user_input) {
    var grade, grade_result;
    grade = user_input[2];

    if (grade <= 59) {
        grade_result = "F";
        user_input.append(grade_result);
        print_grade(user_input);
    }

    if (grade <= 69 && grade >= 60) {
        grade_result = "D";
        user_input.append(grade_result);
        print_grade(user_input);
    }

    if (grade <= 79 && grade >= 70) {
        grade_result = "C";
        user_input.append(grade_result);
        print_grade(user_input);
    }

    if (grade <= 89 && grade >= 80) {
        grade_result = "B";
        user_input.append(grade_result);
        print_grade(user_input);
    }

    if (grade <= 100 && grade >= 90) {
        grade_result = "A";
        user_input.append(grade_result);
        print_grade(user_input);
    }

    if (grade > 100) {
        console.log("You have entered a grade higher than possible.");
        main();
    }
}

main();
