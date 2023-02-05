# Introspection 
# It is the ability of a program to check the type
# of an object or its properties at runtime

# Reflection
# It is the ability of a program to change the properties
# or methods of an object at runtime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def change_me(object):
    for key in object.__dict__:
        # Introspection
        if isinstance(getattr(object, key), str):
            # Reflection
            setattr(object, key, '')
    return object

user = User('Maran Sowthri Kalailingam', 26)
print(change_me(user).__dict__)