# Задача 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
MIN_NUM_RANGE = 2
MAX_NUM_RANGE = 99
range_num = [_ for _ in range(MIN_NUM_RANGE, MAX_NUM_RANGE + 1)]

MIN_NUM = 2
MAX_NUM = 9
array_num = [_ for _ in range(MIN_NUM, MAX_NUM + 1)]

for num in array_num:
    count = 0
    for i in range_num:
        if i % num == 0:
            count += 1
    print(f'для числа {num} - {count} кратных чисел')
