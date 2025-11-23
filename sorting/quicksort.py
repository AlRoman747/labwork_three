def quickSort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[(len(arr) // 2)]
    left, middle, right = [x for x in arr if x < pivot], [x for x in arr if x == pivot], [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

sorted_list = quickSort([10, 7, 8, 9, 1, 5])

if __name__ == "__main__":
    print(quickSort([3, 2, 1]))