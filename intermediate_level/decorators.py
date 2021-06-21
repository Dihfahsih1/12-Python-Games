
from time import sleep, time
from functools import wraps
def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return wrapper
@measure
def f(sleep_time=0.1):
    '''am a programmer and i have no life'''
    sleep(sleep_time)
f(sleep_time=0.4)
print(f.__name__, ':', f.__doc__) 

# def function1(function):
#     def wrapper(*args, **kwargs):
#         print("it worked")
#     return wrapper

# '''python syntactic sugar '''
# @function1
# def function2(name):
    
#     '''using string interpolation'''
#     print(f"{name}")
    
# function2('dihfahsih')
    
    