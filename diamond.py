def diamond(a):
    for i in range(-a, a+1):
        print(abs(i) * ' ' + abs(2*abs(i) - (2*a+1)) * '*')

if __name__ == "__main__":
    diamond(abs(int(input("Diamond size = "))))
