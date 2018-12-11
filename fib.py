def fib(n):
    f = [1] * n
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f
a = fib(int(input("Enter nunbers element of list: ")))
print(a)
