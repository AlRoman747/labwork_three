def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1  # Левый потомок
    right = 2 * i + 2  # Правый потомок

    # Если левый потомок существует и больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый потомок существует и больше текущего наибольшего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами
        heapify(arr, n, largest)  # Рекурсивно преобразуем затронутое поддерево

def heapSort(a: list[int]) -> list[int]:
    n = len(a)
    # Построение максимальной кучи
    # Начинаем с последнего нелистового узла и идем до корня
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # Извлечение элементов из кучи один за другим
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень в конец
        a[i], a[0] = a[0], a[i]
        # Вызываем heapify на уменьшенной куче
        heapify(a, i, 0)

    return a


