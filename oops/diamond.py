class Vehicle:
    def show_power_type(self):
        print('I can use power from various sources')


class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from electricity')


class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('I can use power from petrol')


class HybridCar(ElectricVehicle, PetrolVehicle):
    pass


hybrid_car = HybridCar()
hybrid_car.show_power_type()
