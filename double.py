def doubler(funct):
    def wrapper(*args, **kw):
        funct(*args, **kw)
        funct(*args,**kw)
        return None
    return wrapper

@doubler
def func():
    print("Hello")

func()