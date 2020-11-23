# Задание 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50

array = [round(random.uniform(MIN_ITEM, MAX_ITEM - 1), 2) for _ in range(SIZE)]
print(array)


def merge_sorting(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_li = merge_sorting(arr[:mid])
    right_li = merge_sorting(arr[mid:])
    return merge(left_li, right_li)


def merge(left_li, right_li):
    result = []
    left_idx = 0
    right_idx = 0
    for _ in range(len(left_li) + len(right_li)):
        if left_idx < len(left_li) and right_idx < len(right_li):
            if left_li[left_idx] <= right_li[right_idx]:
                result.append(left_li[left_idx])
                left_idx += 1
            else:
                result.append(right_li[right_idx])
                right_idx += 1
        elif left_idx == len(left_li):
            result.append(right_li[right_idx])
            right_idx += 1
        elif right_idx == len(right_li):
            result.append(left_li[left_idx])
            left_idx += 1
    return result


print(merge_sorting(array))
