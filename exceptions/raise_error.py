input_number = int(input('Enter a number: '))

try:
    a = 1 / input_number
    print(f'Reverse of {input_number} is {a}')
except:
    print('0 is not an acceptable value')
    raise