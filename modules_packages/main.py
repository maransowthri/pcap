import utils.calculator as calculator
import utils.calc_helper

a = int(input('Number 1: '))
b = int(input('Number 2: '))
operator = input('Operator: ')
print(calculator.greeting)

if operator == '+':
    print(calculator.add(a, b))
elif operator == '-':
    print(calculator.subtract(a, b))
elif operator == '*':
    print(calculator.multiply(a, b))
elif operator == '/':
    print(calculator.divide(a, b))