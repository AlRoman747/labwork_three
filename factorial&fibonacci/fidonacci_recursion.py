def fibonacci(n1, n2, m, c):
        res = n1 + n2
        c += 1
        if c >= m:
            return res
        return fibonacci(n2, res, m, c)

print(fibonacci(1,1,int(input()),2))
