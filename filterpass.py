import sys
def f():
    s = sys.argv[1]
    f = open(s, 'r')
    r = f.readlines()
    a = [i for i in r if len(i) >= 8]
    f.close()
    g = open(s, 'w')
    for i in a:
        g.write(i)
    g.close()
if __name__ == "__main__":
    f()
