class User:
    __users_count = 0
    def __init__(self, name):
        self.name = name
        User.__users_count += 1


user1 = User('Maran Sowthri Kalailingam')
user2 = User('Karan Sasthiri Kalailingam')
print(dir(User))
print(User._User__users_count)
# User.__name__ = 'Student'
print(type(User.__name__))

if hasattr(user1, 'name'):
    print('Name of User 1 is', user1.name)
else:
    print('User 1 has no name')

student1 = {'name': 'Maran Sowthri Kalailingam', 'age': 26}

if 'name' in student1:
    print('Name of Student 1 is', user1.name)
else:
    print('Student 1 has no name')
