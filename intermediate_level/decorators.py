def function1(function):
    def wrapper(*args, **kwargs):
        print("hello")
        function(*args, **kwargs)
        print("you are welcome to programming")
    return wrapper

'''python syntactic sugar '''
@function1
def function2(name):
    
    '''using string interpolation'''
    print(f"{name}")
    
function2('dihfahsih')
    
    