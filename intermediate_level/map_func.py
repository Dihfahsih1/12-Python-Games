#using map function


li = [1, 2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

'''Using a normal function'''
newList = []
for x in li:
    newList.append(func(x))
print(newList)

'''Using a map function'''
print(list(map(func, li)))

 