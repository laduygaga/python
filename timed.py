def timed(f):
    def wrapper():
        import time
        start = time.time()
        function = f()
        end = time.time()
        return end - start
    return wrapper
