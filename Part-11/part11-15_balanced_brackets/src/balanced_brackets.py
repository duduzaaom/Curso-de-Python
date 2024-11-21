def only_brackets(my_string: str):
    brackets = "()[]"
    new_string = [character for character in my_string if character in brackets]
    
    return "".join(new_string)


def balanced_brackets(my_string: str):
    my_string = only_brackets(my_string)

    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)