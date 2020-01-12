def Decorator(f):
    def wrapper(arg):
        print ('befor')
        f(arg)
        print ('after')
    return wrapper

@Decorator                # либо: Function = Decorator(Function)
def Function(x):
    print ('function', + x)

Function(23)                # декорированая функция