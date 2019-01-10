def fib(n):
    f = [1] * n
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    return f
a = fib(int(input("Enter nunbers element of list: ")))
print(a)


#def fib(n):
#    a, b = 0, 1
#    while b < n:
#        print(b, end=" ")
#        a, b = b, a + b
#    print()
#fib(n = int(input("Enter the nearest with last number :))")))
