import time


def prometheus_monitor(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        runtime = int(te - ts) * 1000
        print("runtime of {}". format(method.__name__), runtime, "ms")
        return result
    return timed
