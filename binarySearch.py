def binarySearch(itemsList, item):
    itemsList.sort()
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

for i in range(10):
    print(binarySearch([1,2,3,4,5], i))
