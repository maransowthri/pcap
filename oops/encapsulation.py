class Student:
    def __init__(self, name, rank=0):
        self.name = name
        if rank > 0:
            self.__rank = rank
        else:
            self.__rank = 0
    
    def study_well(self):
        if self.__rank > 0:
            self.__rank -= 1
    
    def have_fun(self):
        self.__rank += 1

    def get_rank(self):
        return self.__rank

ram = Student('Ram', -5)
ram._Student__rank = -5
print(dir(ram))
print('Rank:', ram.get_rank())
