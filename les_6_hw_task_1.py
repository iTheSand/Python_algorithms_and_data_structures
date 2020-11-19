# Задание 1. Подсчитать, сколько было выделено памяти под переменные
# в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Вывод: проанализировав 3 варианта решения, видно, что решение №1 показывает самое неэффективное использование памяти.
# Помимо множества, есть еще и дополнительная переменная, а так же итоговый отсортированный список,
# которые значительно увеличили объем использованной памяти.
# Решение №3 показывает наиболее эффективное использование памяти, оно полностью идентично решению №2,
# но благодаря запуску цикла в генераторе списка мы не объявляли дополнительную переменную.
# В очередной раз видим преимущество "синтаксического сахара".
import sys
import random

# Генерация исходного массива определенной длины и диапазона
SIZE = 1000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

# Выбранная задача. Во втором массиве сохранить индексы четных элементов исходного массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# Решение №1 - 32620 байт (Python 3.8.4 32bit, win x64).
complicate = set()
count = 0
for i in array:
    if i % 2 == 0:
        complicate.add(count)
    count += 1
result_one = sorted([x for x in complicate])
# print(f'Индексы четных элементов: {result_one}')

# Решение №2 - 9060 байт (Python 3.8.4 32bit, win x64).
result_two = []
for j in range(len(array)):
    if array[j] % 2 == 0:
        result_two.append(j)
# print(f'Индексы четных элементов: {result_two}')

# Решение №3 - 9046 байт (Python 3.8.4 32bit, win x64).
result_three = [i for i in range(len(array)) if array[i] % 2 == 0]


# print(f'Индексы четных элементов: {result_three}')


# Функция для подсчета затраченной памяти - count_spend_memory.
# number_var - аргумент количества переменных, которые необходимо проссуммировать
# ignore_var - аргумент количества игнорируемых переменных, которые объявлены позже суммируемых
def count_spend_memory(number_var, ignore_var):
    number_var += ignore_var
    sum_memory = 0
    global_vars = list(globals().items())
    for var, obj in global_vars[-(number_var + 1):-(ignore_var + 1):]:
        sum_memory += sys.getsizeof(obj)
        if hasattr(obj, '__iter__'):
            if hasattr(obj, 'items'):
                for key, value in obj.items():
                    sum_memory += sys.getsizeof(key)
                    sum_memory += sys.getsizeof(value)
            elif not isinstance(obj, str):
                for item in obj:
                    sum_memory += sys.getsizeof(item)
    return (f'{sum_memory=}')


print(count_spend_memory(4, 3))
print(count_spend_memory(2, 1))
print(count_spend_memory(1, 0))

