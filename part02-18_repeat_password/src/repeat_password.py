password = input('Password: ')
while True:
    repeat_password = input('Repeat password: ')

    if password == repeat_password:
        break
    else: 
        print('They do not match!')

print('User account created!')