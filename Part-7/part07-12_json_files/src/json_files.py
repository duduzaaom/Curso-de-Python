import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    students = json.loads(data)
    
    for student in students:
        line = f"{student['name']} {student['age']} years ("
        if student["hobbies"] != []:
            for hobbie in student["hobbies"]:
                line += hobbie + ', '
            print(line[:-2] + ")")
        else:
            print(line + ")")
              

if __name__ == '__main__':
    print_persons('file4.json')