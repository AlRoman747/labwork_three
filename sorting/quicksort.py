def quickSort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[(len(arr) // 2)]
    left, middle, right = [x for x in arr if x < pivot], [x for x in arr if x == pivot], [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


# print(quickSort([1,2,4,3,5]))