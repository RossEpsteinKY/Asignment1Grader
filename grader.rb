def main()
  print "What is the student's name?  : >"
  name = gets.chomp
  print "What is the class name?    >"
  className = gets.chomp
  print "Enter grade for the class: >"
  grade = gets.chomp

  user_input = [name, className, grade]
  test_if_user_input.to_i
end

def test_if_int(user_input)
  try:
    value = user_input[2].to_i
  user_input[2] = value
  # print('it is an int')
  find_grade(user_input)
  except ValueError:
           puts("You must enter a value between 0 && 100 for this to work")
  main()
  pass
end
end

def print_grade(user_input)
  puts("%s received a letter grade of %s in the class %s" % (user_input[0], user_input[3], user_input[1]))
  main()
end

def find_grade(user_input)
  grade = user_input[2]
  if grade <= 59
    grade_result = "F"
    user_input.push(grade_result)
    print_grade(user_input)
  end
  if grade <= 69 && grade >= 60
    grade_result = "D"
    user_input.push(grade_result)
    print_grade(user_input)
  end
  if grade <= 79 && grade >= 70
    grade_result = "C"
    user_input.push(grade_result)
    print_grade(user_input)
  end
  if grade <= 89 && grade >= 80
    grade_result = "B"
    user_input.push(grade_result)
    print_grade(user_input)
  end
  if grade <= 100 && grade >= 90
    grade_result = "A"
    user_input.push(grade_result)
    print_grade(user_input)
  end
  if grade > 100
    puts("You have entered a grade higher than possible.")
    main()
  end
end
main()

