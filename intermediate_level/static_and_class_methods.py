#static and class method

class person(object):
    population =100
    def __init__(self, name, age):
        self.age=age
        self.name = name
    
    @classmethod
    def getPopulation(cls):
        '''This can access any global variable of the class, atleast you need one parameter'''
        return cls.population
    
    @staticmethod
    def isAdult(Age):
        '''This can not access any global variable of the class because it has no class name 
        , it also doesnot need parameters'''
        return Age >= 10
    
    def display(self):
        print(self.name, 'is ', self.age, ' years old.')
        
newPerson = person('kim', 14)

print(person.isAdult(22))
        