import sys

username = input('What is your name? ')

if not username:
    print('Name can not be blank')
    sys.exit(1)

print('Hello', username)