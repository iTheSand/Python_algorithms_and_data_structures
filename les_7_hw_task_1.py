# Задание 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
MIN_ITEM = - 100
MAX_ITEM = 100

array = [random.randint(MIN_ITEM, MAX_ITEM - 1) for _ in range(SIZE)]
print(array)


def bubble(arr):
    con = True
    while con:
        count_swap = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count_swap += 1
        if count_swap == 0:
            con = False
    return arr


print(bubble(array))
