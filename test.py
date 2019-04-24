def a():
    lst = []
    for i in range(5):
        i = list(map(lambda x: int(x), input().split()))
        lst.append(i)
    return lst


lst = a()


def f(a):
    values = []
    for i in range(3):
        i = sum([a[m][n] for m in range(0, 3) for n in range(i, i + 3)])
        values.append(i)
    for j in range(3):
        j = sum([a[m][n] for m in range(1, 4) for n in range(j, j + 3)])
        values.append(j)
    for k in range(3):
        k = sum([a[m][n] for m in range(2, 5) for n in range(k, k + 3)])
        values.append(k)
    return values


print(f(lst))
