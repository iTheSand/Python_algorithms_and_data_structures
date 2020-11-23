# Задание 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
import random

M = 5
SIZE = 2 * M + 1
MIN_ITEM = 1
MAX_ITEM = 10

array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]


def gnome_sort(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


print(gnome_sort(array))
print(f'медиана массива = {array[len(array) // 2]}')
