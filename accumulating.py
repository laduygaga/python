def f(list):
    lst = []
    lst.append(list[0])
    for i in list[1:]:
        lst.append(lst[-1]*i)
    return lst


print(f(list(map(lambda x: int(x), input().split()))))
