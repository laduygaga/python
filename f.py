def timed(f):
    import time
    start = time.time()
    f()
    end = time.time()
    print(end - start)
    return end - -start
@timed
def func():
    for i in range(100000):
        print(i)
