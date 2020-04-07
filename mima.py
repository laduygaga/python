def _minmax(l):
    mi = ma = l[0]
    for i in l[1:]:
        if i < mi:
            mi = i
        else:
            if i > ma:
                ma = i
    return [mi, ma]
print(_minmax([3,5,2,6,1,7]))

def selecSort(l):
    a = []
    for i in range(len(l)):
       a.append(l.pop(l.index(_minmax(l)[0])))
    return a
print(selecSort([2,3,5,1,6,3]))
