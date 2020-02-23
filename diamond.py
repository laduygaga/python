def diamond(a):
    for i in range(-a, a+1):
        print(abs(i) * ' ' + abs( (2*a+1) - abs(2*i) ) * '*')

if __name__ == "__main__":
    diamond(abs(int(input("Diamond size = "))))
