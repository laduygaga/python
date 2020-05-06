def mergesort(l):
    if len(l) <=1:
        return l
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    l1_sorted = mergesort(l1)
    l2_sorted = mergesort(l2)
    return merge(l1_sorted, l2_sorted)

def merge(l1,l2):
    merge_list= []
    i =j =0
    while i < len(l1)  and j < len(l2):
        if l1[i] < l2[j]:
            merge_list.append(l1[i])
            i+=1
        else:
            merge_list.append(l2[j])
            j+=1
    if i< len(l1):
        merge_list.extend(l1[i:])
    elif j < len(l2):
        merge_list.extend(l2[j:])
    return merge_list

print(mergesort([3,2,1,4,5]))
