def greet(text):
    def print_greet():
        print(text)
    return print_greet

say_hi = greet('Hi')
say_hi()

def make_multiply_closure(x):
    def multiply(y):
        return x * y
    return multiply

multiply_by_5 = make_multiply_closure(5)
multiply_by_8 = make_multiply_closure(8)
print(multiply_by_5(4))
print(multiply_by_5(6))
print(multiply_by_8(5))