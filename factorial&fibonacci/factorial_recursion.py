def factorial(n: int):
    if n in (0, 1):
        return n
    return n * factorial(n - 1)


print(factorial(5))