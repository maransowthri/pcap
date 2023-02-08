class Vehicle:
    def __init__(self, speed):
        self.speed = speed
        pass

    def introduce(self):
        print('My name is Vehicle')


class LandVehicle(Vehicle):
    def __init__(self, wheel_count, speed):
        super().__init__(speed)
        self.wheel_count = wheel_count

    def introduce(self):
        print('My name is LandVehicle')

class Car(LandVehicle):
    def __init__(self):
        pass

    # def introduce(self):
    #     print('My name is Car')

# print(issubclass(LandVehicle, Vehicle))
# print(issubclass(Car, LandVehicle))
# print(issubclass(Car, Car))

lambo = Car()
print(lambo.__dict__)
mercedez = Car(4, 150)
print(mercedez.__dict__)