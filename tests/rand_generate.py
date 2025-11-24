from random import Random

def rand_int_array(n, lo, hi, *, distinct=False, seed):
    rnd = Random(seed)
    if distinct:
        return rnd.sample(range(lo, hi + 1), n)
    return [rnd.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n, swaps, *, seed):
    rnd = Random(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = rnd.randrange(n), rnd.randrange(n)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def many_duplicates(n, k_unique=5, *, seed):
    rnd =  Random(seed)
    base = [rnd.randint(0, 1000) for _ in range(k_unique)]
    return [rnd.choice(base) for _ in range(n)]

def reverse_sorted(n):
    return list(range(n, 0, -1))

def rand_float_array(n, lo=0.0, hi=1.0, *, seed):
    rnd =  Random(seed)
    return [rnd.uniform(lo, hi) for _ in range(n)]
