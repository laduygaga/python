def fib(n):
    fib_list = [0] * n
    fib_list[1] = 1
    for i in range(2,n):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]
    #return fib_list
    print(fib_list)
fib(int(input("Enter nunber element of list: ")))
