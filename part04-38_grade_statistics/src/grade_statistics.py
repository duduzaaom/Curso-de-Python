lista_teste = ['15 87', '10 55', '11 40', '4 17']


def exam_points_exercises():
    input_list = []

    while True:
        points_and_exercises = input('Exam points and exercises completed: ')
        if points_and_exercises == '':
            return input_list
        else:
            input_list.append(points_and_exercises)


def get_exam_points(list):
    exam_points_list = []
    for item in list:
        exam_points_list.append(int(item.split()[0]))
                
    return exam_points_list


def get_number_exercises(list):
    number_exercises_list = []
    for item in list:
        number_exercises_list.append(int(item.split()[1]))
                
    return number_exercises_list


def statistics(list):
    print('Statistics:')
    points = 0

    exam_points = get_exam_points(list)
    number_exercises = get_number_exercises(list)


def main():
    #inputs = exam_points_exercises()
    exam_points = get_exam_points(lista_teste)
    number_exercises = get_number_exercises(lista_teste)
    print(f"Exam points: {exam_points}")
    print(f"Number of exercises completed: {number_exercises}")


main()