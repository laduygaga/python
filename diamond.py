def diamond(a):
    b = abs(a) + 1
    for i in range(-a, b):
        print(abs(i) * ' ' + abs(abs(i) - a) * '*' + abs(abs(i) - b) * '*')


if __name__ == "__main__":
    diamond(int(input("Diamond size = ")))
