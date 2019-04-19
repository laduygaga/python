def f(list):
    l = []
    l.append(list[0])
    for i in list[1:]:
        l.append(l[-1]*i)
    return l
