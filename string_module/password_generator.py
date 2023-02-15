import random

while True:
    print('-- Password generator --')
    print('Choose option: ')
    print('1: generate password ')
    print('2: exit the program ')

    choice = input('Your choice: ')

    if choice not in ['1', '2']:
        print('Please enter a correct value')
        print()
        continue
    elif int(choice) == 2:
        print('Bye!')
        break

    password_length = input('Provide password length: ')

    if password_length.isdigit() and int(password_length) in list(range(1, 31)):
        password_length = int(password_length)
        chars = 'abcdefghijklmnopqrstuvwxyz'
        generated_password = ''

        yes_choices = ['y', 'yes', 'YES']
        
        if input('Use uppercase letters? (y/n): ') in yes_choices:
            chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if input('Use digits? (y/n): ') in yes_choices:
            chars += '0123456789'
        if input('Use special characters? (y/n): ') in yes_choices:
            chars += '!@#$%^&*()_+'
        
        for i in range(password_length):
            generated_password += random.choice(chars)
        
        print()
        print('Generated password: ' + generated_password)
        print()
    else:
        print('Please enter a value between 1 to 30')
        print()
