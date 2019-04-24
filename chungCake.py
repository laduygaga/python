def bc():
    n = int(input("banhchung_size:"))
    banhchung = []
    for i in range(n):
        banhchung.append(n*['*'])
    for i in range(n):
        for j in range(n):
            if i != 0 and i != (n-1) \
                    and j != 0 and j != (n-1) \
                    and i != j and j != n-(i+1) \
                    and i != (n//2) and j != (n//2):
                banhchung[i][j] = " "
    for row in banhchung:
        print(' '.join(row))


bc()
