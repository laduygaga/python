def fib(n = int(input("lenght of fib:"))): 
    f = [1] * n
    for i in range(2,n):
        f[i] = f[i-1] + f[i-2]
    print(f)
fib()


#def fib_1(n):
#    a, b = 0, 1
#    while b <= n:
#        print(b, end=" ")
#        a, b = b, a + b
#    print()
#fib_1(n = int(input("Enter the nearest with last number :))")))
