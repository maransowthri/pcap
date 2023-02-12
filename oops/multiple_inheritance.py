class Vehicle:
    def move(self):
        print('Moving...')

    def introduce(self):
        print('I\'m a vehicle')


class Flyable:
    def fly(self):
        print('Flying...')

    def introduce(self):
        print('I\'m a flyable object')


class Helicopter(Flyable, Vehicle):
    def introduce(self):
        print('I\'m a helicopter')


copter1 = Helicopter()
copter1.fly()
copter1.move()
copter1.introduce()

print(Vehicle.__bases__)
print(Helicopter.__bases__)
