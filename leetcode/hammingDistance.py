def hD():
    l = []
    a = "{0:07b}".format(int(input())) # convert int -> bin, length = 7, remove '0b'
    b = "{0:07b}".format(int(input()))
    c = [int(i) for i in a]
    d = [int(j) for j in b]
    for i in range(len(c)):
        if c[i] == d[i]:
            l.append(0)
        else:
            l.append(1)
    print("hamming-distance =",sum(l))
hD()
