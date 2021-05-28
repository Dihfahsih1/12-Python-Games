class car(object):
    '''a constructor function to initialize the parameters'''
    def __init__(self, make, year, condition='New'):
        self.make = make
        self.year=year
        self.condition = condition
    def display(self,showAll=True):
        if showAll:
            print("This car is a %s made in %s and is %s "%(self.make, self.year, self.condition))
        else:
            print("This is an %s car. "%(self.condition))

mycar = car('ford',2020, 'Old')
mycar.display(False)