def Decorator(f):
    def wrapper():
        print ('befor')
        f()
        print ('after')
    return wrapper

@Decorator                # либо: Function = Decorator(Function)
def Function():
    print ('function')

Function()                # декорированая функция