 
a = [1, 2,3,4,5,6,7,8,9,10]
def add5(x):
    return x + 5

def isOdd(x):
    return x%3 != 0
                                                                                        
b = list(filter(isOdd, a))
print(b)
 
c = list(map(add5, b))
print (c)
    