def _input():
    lst = []
    for i in range(5):
        i = list(map(lambda x: int(x), input().split()))
        lst.append(i)
    return lst


inputList = _input()


def f(a):    # a = _inputList
    values = []
    for i in range(3):
        i = sum([a[m][n] for m in range(0, 3) for n in range(i, i + 3)]) \
            - sum([a[m][n] for m in [1] for n in [i, i + 2]])
        values.append(i)
    for j in range(3):
        j = sum([a[m][n] for m in range(1, 4) for n in range(j, j + 3)]) \
            - sum([a[m][n] for m in [2] for n in [j, j + 2]])
        values.append(j)
    for k in range(3):
        k = sum([a[m][n] for m in range(2, 5) for n in range(k, k + 3)]) \
            - sum([a[m][n] for m in [3] for n in [k, k + 2]])
        values.append(k)
    return max(values)


print(f(inputList))
