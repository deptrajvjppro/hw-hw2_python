def func_counter(func):
    def wrapper (*args,**kw):
        result = func()
        wrapper.counter += 1
        print(f'Total of time called: {wrapper.counter}')
        return result
    wrapper.counter = 0
    return wrapper

@func_counter
def funct():
    print("Hello")

funct()
funct()
funct()
funct()