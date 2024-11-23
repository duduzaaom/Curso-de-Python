import re

def is_dotw(my_string: str):
    pattern = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"

    if re.search(pattern, my_string):
        return True
    
    return False

def all_vowels(my_string: str):
    pattern = "^[aeiou]+$"

    if re.search(pattern, my_string):
        return True
    
    return False


def time_of_day(my_string: str):
    pattern = "^([0-1][0-9]|[0-2][0-4]):[0-5][0-9]:[0-5][0-9]$"

    if re.search(pattern, my_string):
        return True
    
    return False


if __name__ == "__main__":
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))