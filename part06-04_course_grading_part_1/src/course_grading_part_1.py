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


def main():
    student_file = input('Student information: ')
    exercise_file = input('Exercises completed: ')

    student_info = process_student_file(student_file)
    exercise_data = process_exercise_file(exercise_file)

    for id, name in student_info.items():
        print(f'{name} {sum(exercise_data[id])}')


main()