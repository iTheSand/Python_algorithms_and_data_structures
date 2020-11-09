# Задача 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_ngv_num = MIN_ITEM
pos = 0

for idx, i in enumerate(array):
    if i < 0 and abs(i) < abs(max_ngv_num):
        max_ngv_num = i
        pos = idx

print(f'{max_ngv_num} (макс. отрицательный элемент) = {pos} (позиция в массиве)')
