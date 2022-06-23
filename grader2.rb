class Main
  #Python fields are always public whereas Ruby's are private. attr_accessor makes them public
  attr_accessor
  def initialize()
    GetUserInput()
  end
end


class GetUserInput
  #Python fields are always public whereas Ruby's are private. attr_accessor makes them public
  attr_accessor
  def initialize()
    print "What is the student's name?  : >"
    name = gets.chomp
    print "What is the class name?    >"
    className = gets.chomp
    print "Enter grade for the class: >"
    grade = gets.chomp

    TestIfInt(name,className,grade)
  end
end

class TestIfInt
  #Python fields are always public whereas Ruby's are private. attr_accessor makes them public
  attr_accessor :grade, :name, :className
  def initialize(name, className, grade)
    try:
      @name = name
    @className = className
    @grade = grade

    value = @grade.to_i
    @grade = value

    user_input = [@name, @className, @grade]
    # print('it is an int')
    find_grade(@name,@className,@grade)
    except ValueError:
             puts("You must enter a value between 0 && 100 for this to work")
    Main.new
    pass
  end
end

class UserInput
  #Python fields are always public whereas Ruby's are private. attr_accessor makes them public
  attr_accessor :grade, :name, :className
  def initialize(name, className, grade)
    @name = name
    @className = className
    @grade = grade
  end
end

class find_grade
  #Python fields are always public whereas Ruby's are private. attr_accessor makes them public
  attr_accessor :grade_result, :grade, :name, :className
  def initialize(name, className, grade)
    @name = name
    @className = className
    @grade = grade
    @grade_result = ''


    grade = @grade
    if grade <= 59
      @grade_result = "F"
      print_grade(@name,@className,@grade, @grade_result)
    end
    if grade <= 69 && grade >= 60
      @grade_result = "D"
      print_grade(@name,@className,@grade, @grade_result)
    end
    if grade <= 79 && grade >= 70
      @grade_result = "C"
      print_grade(@name,@className,@grade, @grade_result)
    end
    if grade <= 89 && grade >= 80
      @grade_result = "B"
      print_grade(@name,@className,@grade, @grade_result)
    end
    if grade <= 100 && grade >= 90
      @grade_result = "A"
      print_grade(@name,@className,@grade, @grade_result)
    end
    if grade > 100
      puts("You have entered a grade higher than possible.")
      Main.new
    end
  end
end

class print_grade()
#Python fields are always public whereas Ruby's are private. attr_accessor makes them public
attr_accessor :grade_result, :grade, :name, :className
def initialize(name,className,grade,grade_result)
  @name = name
  @className = className
  @grade = grade
  @grade_result = grade_result
  puts("%s received a letter grade of %s in the class %s" % (@name, @grade_result, @className))
  Main.new
end
end

x = Main.new



