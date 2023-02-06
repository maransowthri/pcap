class Vehicle:
    def __init__(self):
        pass


class LandVehicle(Vehicle):
    def __init__(self):
        super().__init__()


class Car(LandVehicle):
    def __init__(self):
        super().__init__()

print(issubclass(LandVehicle, Vehicle))
print(issubclass(Car, LandVehicle))
print(issubclass(Car, Car))