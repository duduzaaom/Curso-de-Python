from string import ascii_uppercase, digits

def run(program: list) -> list:
    variables = {}
    print = []
    for line in program:
        if "MOV" in line:
            parts = line.split()
            variable = parts[1]
            value = parts[2]

            if value in digits:
                variables[variable] = int(value)
            else:
                variables[variable] = int(variables[value])

        if "PRINT" in line:
            parts = line.split()
            value = parts[1]

            if value in digits:
                print.append(int(value))
            else:
                print.append(variables[value])

        if "ADD" in line:
            parts = line.split()
            variable = parts[1]
            value = parts[2]

            if value in digits:
                variables[variable] += int(value)
            else:
                variables[variable] += variables[value]

        if "SUB" in line:
            parts = line.split()
            variable = parts[1]
            value = parts[2]

            if value in digits:
                variables[variable] -= int(value)
            else:
                variables[variable] -= variables[value]

        if "MUL" in line:
            parts = line.split()
            variable = parts[1]
            value = parts[2]

            if value in digits:
                variables[variable] *= int(value)
            else:
                variables[variable] *= variables[value]

        if ":" in line:
            continue

        if "JUMP" in line:
            parts = line.split()
            location = parts[1]

    return print


if __name__ == '__main__':
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("SUB A B")
    program1.append("PRINT A")
    program1.append("MOV C 3")
    program1.append("MUL B C")
    program1.append("PRINT B")

    result = run(program1)
    print(result)
        

