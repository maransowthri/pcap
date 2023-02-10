class Animal:
    def __init__(self):
        self.species = 'general'

    def produce_sound(self):
        print('General...')

    def present(self):
        print('I can do the following sound')
        self.produce_sound()


class Dog(Animal):
    def __init__(self):
        self.species = 'dog'

    def produce_sound(self):
        print('Woof....')


general = Animal()
# print(general.species)
# general.produce_sound()
general.present()

dog = Dog()
# print(dog.species)
# dog.produce_sound()
dog.present()