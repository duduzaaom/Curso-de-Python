def process_student_file(file) -> dict:
    student_dict = {}

    with open(file) as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            student_dict[parts[0]] = f'{parts[1]} {parts[2]}'

    return student_dict


def process_exercise_file(file) -> dict:
    exercises_dict = {}

    with open(file) as new_file:
        for line in new_file:
            line = line.replace('\n', '')
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            exercises_dict[parts[0]] = []
            for grade in parts[1:]:
                exercises_dict[parts[0]].append(int(grade))

    return exercises_dict


def process_exam_file(file) -> dict:
    exam_points_dict = {}

    with open(file) as new_file:
        for line in new_file:
            parts = line.split(';')
            if parts[0] == 'id':
                continue
            
            exam_points_dict[parts[0]] = 0
            for point in parts[1:]:
                exam_points_dict[parts[0]] += int(point)

    return exam_points_dict


def main():
    student_file = input('Student information: ')
    exercise_file = input('Exercises completed: ')
    exam_file = input('Exam points: ')
    #student_file = 'students1.csv'
    #exercise_file = 'exercises1.csv'
    #exam_file = 'exam_points1.csv'

    student_info = process_student_file(student_file)
    exercise_data = process_exercise_file(exercise_file)
    exam_points = process_exam_file(exam_file)
    total_points = {}

    for id, number in exercise_data.items():
        exercise_point = ((sum(number)/40) * 100) // 10
        total_points[id] = exam_points[id] + exercise_point

    #print(f'Total points: {total_points}')

    for id, point in total_points.items():
        grade = 0
        for min_point in [14, 17, 20, 23, 27]:
            if point > min_point:
                grade += 1
        print(f'{student_info[id]} {grade}')


main()