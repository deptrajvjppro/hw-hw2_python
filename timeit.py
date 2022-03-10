import time

def calculate_time(func):
    def wrapper(*args, **kw):
        start = time.time()
        result = func(*args, **kw)
        end = time.time()
        print(f'Total time {int((end - start))}')
        return result
    return wrapper

@calculate_time
def funct():
    for i in range (int(10e7)):
        pass


funct()
