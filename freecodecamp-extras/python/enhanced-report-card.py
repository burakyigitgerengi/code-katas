
# TODO Get the number of lessons
# TODO Get the lesson name
# TODO Get the number of lessons hours
# TODO Get the number of score

lessons = []

def get_the_number_of_lessons():
    while True:
        try:
            number_of_lessons = int(input("Please input the number of lessons you have: "))
            
            if number_of_lessons > 0:
                 return number_of_lessons
            else:
                print("Invalid input. Please enter a positive number.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

        
def get_the_number_of_lesson_name():
    
    while True:
        lesson_name = input("Please input the lesson name: ")
        
        if lesson_name.isalpha():
            return lesson_name
        else:
            print("Invalid input. Please enter a valid lesson name.")

def get_the_number_of_lesson_hours():
    while True:
        try:
            lesson_hours = int(input("Please input the number of lesson hours: "))
            if lesson_hours > 0:
                return lesson_hours
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_the_number_of_score():
    while True:

        try:
            score = int(input("Please input the number of score: "))
            if score>= 0:
                return score
                
            else:
                print("Invalid input. Please enter a positive number, or a zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    lesson = []
    number_of_lessons = get_the_number_of_lessons()
    lesson_name = get_the_number_of_lesson_name()
    lesson_hours = get_the_number_of_lesson_hours()
    score = get_the_number_of_score()

    lesson.append(lesson_name)
    lesson.append(lesson_hours)
    lesson.append(score)

    lessons.append(lesson)

    print("Lessons info: ", lessons)
    grade = lesson_hours * score // number_of_lessons
    print("Report Card grade: ", grade)

main()