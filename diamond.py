def diamond(a):
    b = abs(a) + 1
    for i in range(-a, b):
        print(abs(i) * ' ' + abs(2*abs(i) - (2*a+1)) * '*')
        # or print(abs(i) * ' ' + abs(2abs(i) - a) * '*' + abs(abs(i) - b) * '*')


if __name__ == "__main__":
    diamond(int(input("Diamond size = ")))
