def radixSort(arr):
    max_num = len(str(max(arr)))
    res = [[] for _ in range(10)]
    for i in range(max_num):

        for x in arr:
            digit_num = (x // 10**i) % 10
            res[digit_num].append(x)

        arr = [x for queue in res for x in queue]
        res = [[] for _ in range(10)]

    return arr




