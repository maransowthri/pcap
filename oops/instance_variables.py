class Yoga:
    def __init__(self, type, duration):
        self.type = type
        self.duration = duration
        self.__count = 0

    def start(self):
        print('Hrm...Hrm...Hrm...')

yoga = Yoga('Sun Salutation', '20m')
# print(dir(yoga))
yoga._Yoga__count = 5
yoga.__burned_calories = '100mg'
print(yoga.__dict__)