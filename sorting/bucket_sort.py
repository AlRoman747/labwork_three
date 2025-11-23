from sorting.quicksort import quickSort

def bucketSort(arr):
    buckets = [[] for _ in range(10)]
    res = []
    for i in arr:
        if 0 <= i < 10: buckets[0].append(i)
        elif 10 <= i <= 20: buckets[1].append(i)
        elif 20 <= i < 30: buckets[2].append(i)
        elif 30 <= i < 40: buckets[3].append(i)
        elif 40 <= i < 50: buckets[4].append(i)
        elif 50 <= i < 60: buckets[5].append(i)
        elif 60 <= i < 70: buckets[6].append(i)
        elif 70 <= i < 80: buckets[7].append(i)
        elif 80 <= i < 90: buckets[8].append(i)
        elif 90 <= i < 100: buckets[9].append(i)

    for i in buckets:
        if i: res.extend(quickSort(i))

    return res

if __name__ == "__main__":
    print(bucketSort([10, 7, 8, 9, 1, 5]))