class CustomValueError(ValueError):
    pass

def round_number(n):
    if type(n) in [int, float]:
        return round(n)
    else:
        raise CustomValueError('Provided value is not a number')

# print(round_number('a'))

class UserActionException(Exception):
    def __init__(self, message='', user_id=''):
        super().__init__()
        self.user_id = user_id
        self.message = message

    def __str__(self):
        return type(self).__name__ + ' occured. Error message: ' + self.message + ', userOd: ' + self.user_id

class EmptyUserActionException(UserActionException):
    def __init__(self, user_id=''):
        super().__init__('An empty name was provided', user_id)

def say_hello(name, user_id):
    if not name:
        raise EmptyUserActionException(user_id)
    print('Hello', name)

# try:
#     say_hello('Adam', 'DT234')
#     say_hello('', 'DT2323')
# except Exception as e:
#     print(e)

class MyEx(Exception):
  def __init__(self, msg):
    Exception.__init__(self, msg+msg)
    self.args = (msg,)
 
try:
  raise MyEx('wrong!')
except Exception as e:
  print(e)

try:
  val = int(input('Provide a number: '))
  print(val/val)
except TypeError:
  print('a')
except ValueError:
  print('b')
except ZeroDivisionError:
  print('c')
except:
  print('d')