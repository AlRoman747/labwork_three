import sys
import os

# Добавляем путь к корневой директории проекта
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sorting.quicksort import quickSort
from sorting.bucket_sort import bucketSort
from sorting.radix_sort import radixSort
from sorting.counting_sort import countingSort
from sorting.heap_sort import heap_sort
from rand_generate import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted



def test_quickSort():
    """Тест быстрой сортировки с рандомным массивом"""
    arr = rand_int_array(10, 1, 100, seed=748)
    result = quickSort(arr.copy())
    assert result == sorted(arr)


def test_empty_array():
    """Тест пустого массива"""
    assert quickSort([]) == []

def test_single_element():
    """Тест массива с одним элементом"""
    arr = rand_int_array(1, 5, 5, seed=748)
    result = quickSort(arr.copy())
    assert result == [5]

def test_quicksort_reverse_sorted():
    """Тест быстрой сортировки на обратно отсортированном массиве"""
    arr = reverse_sorted(10)  # [10, 9, 8, ..., 1]
    result = quickSort(arr.copy())
    expected = list(range(1, 11))  # [1, 2, 3, ..., 10]
    assert result == expected


def test_with_duplicates():
    """Тест с дубликатами"""
    arr = many_duplicates(20, k_unique=3, seed=748)
    result = quickSort(arr.copy())
    assert result == sorted(arr)

def test_countingSort():
    """Тест для couting sort"""
    arr = rand_int_array(50, 0, 100, seed=748)
    result = countingSort(arr.copy())
    assert result == sorted(arr)

def test_bucketSort():
    """Тест для bucketSort"""
    arr = nearly_sorted(30, 5, seed=748)
    result = bucketSort(arr)
    assert result == sorted(arr)

def test_radixSort():
    """Тест для radixSort"""
    arr = rand_int_array(10, 1, 20, distinct=True, seed=748)
    result = radixSort(arr.copy())
    assert result == sorted(arr)

def test_heapSort():
    """Тест для heapSort"""
    arr = rand_int_array(10, 1, 20, distinct=True, seed=748)
    result = heap_sort(arr.copy())
    assert result == sorted(arr)