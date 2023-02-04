class Doctor:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__format_names()
    
    def __format_names(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        print('Please don\'t call me outside')
    
    def introduce(self):
        print('Hi, I am', self.first_name)
    
    def compare_name(self, name_to_compare):
        if self.first_name == name_to_compare:
            print('We have the same name')
        else:
            print('The names are different')
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def __str__(self):
        return self.first_name

doc_steve = Doctor('Steve', 'Smith')
doc_steve.introduce()
doc_steve.compare_name('John')
print(doc_steve.__dict__)
print(Doctor.__dict__)
doc_steve._Doctor__format_names()
print(doc_steve)