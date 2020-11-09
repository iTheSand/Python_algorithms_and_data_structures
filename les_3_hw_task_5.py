# Задача 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 10
array_1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array_1)

min_num = MAX_ITEM
max_num = MIN_ITEM

for i in array_1:
    if i <= min_num:
        min_num = i
    if i > max_num:
        max_num = i

min_idx = array_1.index(min_num)
max_idx = array_1.index(max_num)
print(f'мин. элемент = {min_num}, макс. элемент = {max_num}')

if min_idx > max_idx:
    array_2 = array_1[(max_idx + 1):min_idx]
else:
    array_2 = array_1[(min_idx + 1):max_idx]

result = 0
for i in array_2:
    result += i

print(f'{result=}')
