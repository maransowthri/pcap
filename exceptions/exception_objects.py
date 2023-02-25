def return_high(a, b):
    try:
        if type(a) is not int or type(b) is not int:
            raise Exception('Something went wrong!', 34)
        a = int(a)
        b = int(b)
        return 'Max number is ' + str(a if a >= b else b)
    except Exception as e:
        print(e.args)

a = input('Enter 1st number: ')
b = input('Enter 2nd number: ')
print(return_high(a, b))