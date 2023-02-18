# Syntax errors which are automatically detected and raised by python can't be caught

try:
    print('hello'')
except SyntaxError:
    print('Please correct the syntax')

# However all the user raised syntax errors can be caught

try:
    raise SyntaxError('Correct the syntax please')
except SyntaxError:
    print('Syntax is wrong')