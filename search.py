def search():
    item = int(input())
    l = list(int(i) for i in input().split())
    a = 0
    if item in l:
        a = True
    else:
        a = False
    print(a)
search()
