def binarySearch(itemsList, item):
    first = 0
    last = len(itemsList) - 1
    found = False
    while first <= last and not found:
        midPoint = (first + last) // 2
        if itemsList[midPoint] == item:
            found = True
        else:
            if item < itemsList[midPoint]:
                last = midPoint - 1
            else:
                first = midPoint + 1
    return found


print(binarySearch(itemsList=[int(i) for i in input().split()],
                   item=int(input("item:"))))
