class Vehicle:
    message = 'Hello World!'

    def __init__(self, speed):
        self.speed = speed
        pass

    def speed_up(self):
        self.speed += 5


class LandVehicle(Vehicle):
    def __init__(self, wheel_count, speed):
        super().__init__(speed)
        self.wheel_count = wheel_count
        print(Vehicle.message)


class Car(LandVehicle):
    def super_speed(self):
        print('Super speed activated!')
        super().speed_up()
        super().speed_up()
        super().speed_up()


car = Car(4, 35)
car.super_speed()
print(car.speed)
car.speed_up()
print(car.speed)
