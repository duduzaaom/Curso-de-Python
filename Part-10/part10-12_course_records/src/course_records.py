class Course:
    def __init__(self, name: str):
        self._name = name
        self._grade = 0
        self._credits = 0

    @property
    def grade(self):
        return self._grade
    
    @property
    def credits(self):
        return self._credits

    def add_grade(self, grade: int):
        self._grade = grade

    def add_credits(self, credits: int):
        self._credits = credits

    def __str__(self):
        return f"{self._name} ({self._credits} cr) grade {self._grade}"
        

class CourseRecords:
    def __init__(self):
        self._courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if name not in self._courses:
            self._courses[name] = Course(name)

        if grade > self._courses[name].grade:
            self._courses[name].add_grade(grade)
            self._courses[name].add_credits(credits)

    def get_course_info(self, name: str):
        if name not in self._courses:
            return None
        return self._courses[name]
    
    def get_total_credits(self):
        total_credits = 0

        for course in self._courses.values():
            total_credits += course.credits

        return total_credits
    
    def get_grade_info(self):
        grades = {}
        for course in self._courses.values():
            if course.grade not in grades:
                grades[course.grade] = 0

            grades[course.grade] += 1

        return grades
    
    def get_all_courses(self):
        return self._courses

    
class CourseRecordsExecution:
    def __init__(self):
        self._records = CourseRecords()

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        if name not in self._records._courses:
            self._records._courses[name] = Course(name)
            self._records._courses[name].add_grade(grade)
            self._records._courses[name].add_credits(credits)
        else:
            if grade > self._records._courses[name].grade:
                self._records._courses[name].add_grade(grade)
                self._records._courses[name].add_credits(credits)

    def get_data(self):
        name = input("course: ")

        if self._records.get_course_info(name) is None:
            print("no entry for this course")
        else:
            print(self._records.get_course_info(name))

    def show_statistics(self):
        print(f"{len(self._records._courses)} completed courses, a total of {self._records.get_total_credits()} credits")
        grades = self._records.get_grade_info()
        total_grade = 0
        for grade, grade_amount in grades.items():
            total_grade += grade * grade_amount
        print(f"mean {total_grade/len(self._records._courses):.1f}")
        print("grade distribution")

        
        for i in range(5, 0, -1):
            if i not in self._records.get_grade_info():
                print(f"{i}:")
            else:
                print(f"{i}: {'x' * grades[i]}")

    def execute(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        
        while True:
            print("")

            command = int(input("command: "))

            if command == 0:
                break
            elif command == 1:
                self.add_course()
            elif command == 2:
                self.get_data()
            elif command == 3:
                self.show_statistics()


def main():
    program = CourseRecordsExecution()
    program.execute()

main()


# if __name__ == "__main__":
#     records = CourseRecords()
#     records.add_course("fisica", 3, 8)
#     records.add_course("calculo", 2, 1)
    
#     grades = records.get_grade_info()

#     for grade, grade_amount in grades.items():
#         print(f"{grade}: {'x' * grade_amount}")
