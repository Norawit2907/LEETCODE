def quickSort(ls: list):
    if len(ls) <= 1:
        return ls
    else:
        pivot = ls[0]
        left = [x for x in ls[1:] if x < pivot]
        right = [x for x in ls[1:] if x >= pivot]

        return quickSort(left) + [pivot] + quickSort(right)


def BubbleSort(ls: list):
    for i in range(len(ls)):
        for j in range(len(ls)-i-1):
            if(ls[j] > ls[j+1]):
                ls[j], ls[j+1] = ls[j+1], ls[j]

    return ls


numlist = [5, 6, 9, 8, 3, 1, 2 , 4, 7, 0]
arr = [64, 34, 25, 12, 22, 11, 90]
output = BubbleSort(arr)
print(output)