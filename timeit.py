import time


def calculate_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        stop = time.time()
        print(f'Total execution time is {int((stop - start))}')
        return result
    return wrapper

@calculate_time
def hello():
    for i in range (int(10e7)):
        pass


hello()