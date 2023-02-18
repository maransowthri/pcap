try:
    number = int(input('Enter a number: '))
    print(f'Inverse of given number is {1/number}')
except ValueError:
    print('Given input is not a number')
except ZeroDivisionError:
    print('The number should not be equal to zero')
except:
    print('Something went wrong!')
