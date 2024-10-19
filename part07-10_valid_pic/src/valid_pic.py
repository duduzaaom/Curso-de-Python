from datetime import datetime

def is_leaf_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False 
    

def is_it_valid(pic: str) -> bool:

    if len(pic) > 11:
        return False
    
    day_birth = int(pic[:2])
    month_birth = int(pic[2:4])
    year_birth = pic[4:6]
    century_marker = pic[6]
    personal_identifier = pic[7:10]
    control_character = pic[10]
    control_string = '0123456789ABCDEFHJKLMNPRSTUVWXY'

    control_character_index = int((pic[:6] + personal_identifier)) % 31

    if century_marker == '+':
        year_birth = f'18{year_birth}'
    elif century_marker == '-':
        year_birth = f'19{year_birth}'
    elif century_marker == 'A':
        year_birth = f'20{year_birth}'
    else: 
        return False
    #date_birth = datetime(year_birth, month_birth, day_birth)

    year_birth = int(year_birth)

    if is_leaf_year(year_birth):
        if month_birth == 2 and day_birth > 29:
            return False
    else:
        if month_birth == 2 and day_birth > 28:
            return False

    if day_birth > 31 or month_birth > 12 or control_string[control_character_index] != control_character:
        return False
    
    return True


if __name__ == '__main__':
    date = datetime(2001, 2, 29)

    




