#Алгоритм сортировки
def countingSort(arr):
    res = []
    s_res = ''
    lst = [0] * 100
    for i in arr:
        if i in arr: lst[i] += 1
    for i in range(len(lst)):

        if lst[i]:
            lts = []
            lts.extend([i] * lst[i])
            res.extend(lts)


    return res


