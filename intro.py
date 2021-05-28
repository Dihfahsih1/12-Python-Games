class car(object):
    def __init__(self, make, year, condition='New'):
        self.make = make
        self.year=year
        self.condition = condition
    def display(self,showAll):
        if showAll:
            print("This car is a %s made in %s and is %s "%(self.make, self.year, self.condition))
        else:
            print("This is a %s "%(self.condition))

mycar = car('ford',2020, 'Old')
mycar.display(False)