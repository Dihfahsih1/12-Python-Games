
def func(x):
    return x+5
print(func(2))

func2 = lambda x: x+5
print(func2(3))

a=[1,2,3,4,5,6,7,8,9,10]

def func3(x):
    return list(filter(lambda x: x%2==0, a))
print(func3(4))