from math import ceil, floor, trunc, factorial, sqrt, hypot

# ceil Funtion
# Ceils the given value to the nearest highest rounded number
print('Ceil:')
print(ceil(2.1))
print(ceil(2.9))
print(ceil(2.0))
print(ceil(2.00001))
print(ceil(-2.1))
print()

# floor Funtion
# Floors the given value to the nearest least rounded number
print('Floor:')
print(floor(2.1))
print(floor(2.9))
print(floor(2.0))
print(floor(2.00001))
print(floor(-2.1))
print()

# trunc Function
# Only takes decimal values, removes everything from dot
print('Trunc:')
print(trunc(-2.1))
print(trunc(2.1))
print(trunc(-2.9))
print(trunc(2.9))
print(trunc(2.0))
print()

# int Function
# Similar to Trunc function, but also supports converting string to int
# int is not derived from math
print('Int:')
print(int('2'))
print(int(float('2.0')))
print()

# round Function
# Round is the proper mathematical rounding function
# Round is not derived from math
print('Round:')
print(round(2.1))
print(round(2.5))
print(round(2.51))
print(round(-2.51))
print()

# factorial Function
# Computes factorial of a given number
print('Factorial:')
print(factorial(5))
print()

# sqrt Function
# Computes square root of a given number
print('Sqrt:')
print(sqrt(5))

# hypot Function
# Computes the largest side of the right angle triangle from the give 2 sides
print(hypot(3, 4))