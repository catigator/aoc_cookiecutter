import time


def time_it(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        tt = te - ts
        print(f"Time taken to execute '{method.__name__}' was {tt} seconds")
        return result
    return timed

