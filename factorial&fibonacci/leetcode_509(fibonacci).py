n = int(input())

lst = [0, 1] + n * [0]

for i in range(2, n+2):
    lst[i] = lst[i-1] + lst[i-2]

print(lst[n])