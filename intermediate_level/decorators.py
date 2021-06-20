def function1(function):
    def wrapper(*args, **kwargs):
        print("it worked")
    return wrapper

'''python syntactic sugar '''
@function1
def function2(name):
    
    '''using string interpolation'''
    print(f"{name}")
    
function2('dihfahsih')
    
    