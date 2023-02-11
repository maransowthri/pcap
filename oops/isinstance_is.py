class Vehicle:
    def __init__(self, speed):
        self.speed = speed


class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count


class Car(LandVehicle):
    pass


my_vehicle = Vehicle(40)
my_land_vehicle = LandVehicle(40, 4)
my_car = Car(40, 4)

# print(isinstance(my_vehicle, Vehicle))
# print(isinstance(my_land_vehicle, Vehicle))
# print(isinstance(my_car, Vehicle))
# print()
# print(isinstance(my_vehicle, LandVehicle))
# print(isinstance(my_land_vehicle, LandVehicle))
# print(isinstance(my_car, LandVehicle))
# print()
# print(isinstance(my_vehicle, Car))
# print(isinstance(my_land_vehicle, Car))
# print(isinstance(my_car, Car))

my_new_vechicle = my_vehicle

# print(my_vehicle is my_new_vechicle)

a = 'kmaran'
b = 'kmaran'
print(a is b)

a = 'kmara'
b = 'kmaran'
print(a + 'n' is b)