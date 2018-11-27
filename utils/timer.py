import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print time.time() - start
        return result

    return wrapper

