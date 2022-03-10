import time

def time_it(func):
    def wrapper(*args, **kw):
        start_time = time.time()
        rs = func(*args, **kw)
        end_time = time.time()
        print(f'Total time {int((end_time - start_time))}')
        return rs
    return wrapper

@time_it
def hello():
    for i in range (int(10e7)):
        pass


hello()
