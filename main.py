from time import process_time


from factorial_fibonacci.factorial_recursion import factorial
from factorial_fibonacci.fidonacci_recursion import fibonacci
from sorting.quicksort import quickSort
from sorting.radix_sort import radixSort
from sorting.heap_sort import heapSort
from sorting.counting_sort import countingSort
from sorting.bucket_sort import bucketSort
from sorting.leetcode_75_bubble_sort import bouble_sort
from stack.stack import Stack
from tests.rand_generate import rand_int_array

s = Stack()
stack_command_dict = {
    "push": s.push,
    "pop": s.pop,
    "peek": s.peek,
    "min": s.min,
    "is_empty": s.is_empty,
    "__len__": s.__len__
}
print("Введите что вы хотите посчитать")
print("0. factorial")
print("1. fibonacci")
print("2. sorting")
print("3. stack")

comand_n = int(input())
while comand_n != -1:

    if comand_n  == 0:
        if comand_n == -1: break
        print("введите число, факториал которого вы хотите найти")
        print(factorial(int(input())))
        comand_n = int(input())


    elif comand_n == 1:
        print("введите число, номер числа Фибоначчи которого вы хотите найти")
        print(fibonacci(1, 1, int(input()), 2))
        comand_n = int(input())


    elif comand_n == 2:
        if comand_n == -1: break
        print('-' * 100)
        print("введите массив какой длинны вы хотите отсортировать(цифры через пробел)")
        n = int(input())
        if n == -1: break
        print("Введите какой сортировкой вы хотите воспользоваться")
        print("0. bucket sort")
        print("1. couting sort")
        print("2. heap sort")
        print("3. bubble sort")
        print("4. quick sort")
        print("5. radix sort")
        j = int(input())
        if j == 0:
            lst = rand_int_array(n, 1, 99, seed=748)
            start = process_time()
            res = quickSort(lst)
            end = process_time()
            print(f"coртировка этого массива заняла: {end - start}")
            print(f"массив отсортировался? {res == sorted(lst)}")
            lst.clear()

        elif j == 1:
            lst = rand_int_array(n, 1, n+10, seed=748)
            start = process_time()
            res = quickSort(lst)
            end = process_time()
            print(f"coртировка этого массива заняла: {end - start}")
            print(f"массив отсортировался? {res == sorted(lst)}")
            lst.clear()

        elif j == 2:
            lst = rand_int_array(n, 1, n + 10, seed=748)
            start = process_time()
            res = quickSort(lst)
            end = process_time()
            print(f"coртировка этого массива заняла: {end - start}")
            print(f"массив отсортировался? {res == sorted(lst)}")
            lst.clear()

        elif j == 3:
            lst = rand_int_array(n, 1, n + 10, seed=748)
            start = process_time()
            res = quickSort(lst)
            end = process_time()
            print(f"coртировка этого массива заняла: {end - start}")
            print(f"массив отсортировался? {res == sorted(lst)}")
            lst.clear()
        elif j == 4:
            lst = rand_int_array(n, 1, n + 10, seed=748)
            start = process_time()
            res = quickSort(lst)
            end = process_time()
            print(f"coртировка этого массива заняла: {end - start}")
            print(f"массив отсортировался? {res == sorted(lst)}")
            lst.clear()
        elif j == 5:
            lst = rand_int_array(n, 1, n + 10, seed=748)
            start = process_time()
            res = quickSort(lst)
            end = process_time()
            print(f"coртировка этого массива заняла: {end - start}")
            print(f"массив отсортировался? {res == sorted(lst)}")
            lst.clear()
        elif j == -1:
            break
        comand_n = int(input())
    elif comand_n == 3:
        print("Введите команду и её аргумент через пробел(если нет аргумента, введите None)")
        command, arg = input().split()
        if arg != "None": arg = int(arg); res = stack_command_dict[command](arg)
        else: res = stack_command_dict[command]()

        if res != None: print(res)

        comand_n = int(input())

