# Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = MAX_ITEM
max_num = MIN_ITEM

for i in array:
    if i <= min_num:
        min_num = i
    if i > max_num:
        max_num = i

min_idx = array.index(min_num)
max_idx = array.index(max_num)
array[min_idx] = max_num
array[max_idx] = min_num

print(f'мин. элемент = {min_num}, макс. элемент = {max_num}')
print(array)

