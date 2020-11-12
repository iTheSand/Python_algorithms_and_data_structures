# Задание 1. Проанализировать скорость и сложность одного любого алгоритма
# из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# - выбрать хорошую задачу, которую имеет смысл оценивать,
# - написать 3 варианта кода (один у вас уже есть),
# - проанализировать 3 варианта и выбрать оптимальный,
# - результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# - написать общий вывод: какой из трёх вариантов лучше и почему.

# Вывод: проанализировав 3 варианта решения, видно,
# что решение №1 больше похоже на квадратичную сложность O(n*n), чем на линейную O(n).
# Решение №2 и решение №3 имеют линейную сложность O(n), но решение №3 работает гараздно быстрее за счет
# использования функций из коробки.
# Решение №2 является оптимальным, т.к. мы ничего не конкатенируем, а лишь перезаписываем переменную.
from random import randint
import timeit
import cProfile
import matplotlib.pyplot as plt


# генерация числа (длинны n)
def n(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)


# Выбранная задача.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

# Решение №1, худший из вариантов
def inverse_num(num):
    inv_num = ''
    counter = 0

    def last_num(num):
        nonlocal inv_num, counter
        length_num = len(str(num)) - counter
        for count_iter, i in enumerate(str(num), 1):
            if length_num == count_iter and length_num > 0:
                inv_num += i
                counter += 1
                return last_num(num)

    last_num(num)
    return int(inv_num)


print('#1')
a_1 = (timeit.timeit('inverse_num(n(25))', number=100, globals=globals()))
print(a_1)  # 0.005571837999999996
a_2 = (timeit.timeit('inverse_num(n(50))', number=100, globals=globals()))
print(a_2)  # 0.016282519999999967
a_3 = (timeit.timeit('inverse_num(n(100))', number=100, globals=globals()))
print(a_3)  # 0.05987160300000005
a_4 = (timeit.timeit('inverse_num(n(200))', number=100, globals=globals()))
print(a_4)  # 0.2708018609999999
print('#1')

cProfile.run('inverse_num(n(25))')
# 62 function calls (37 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:28(inverse_num)
#  26/1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:32(last_num)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    26    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('inverse_num(n(50))')
# 112 function calls (62 primitive calls) in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:28(inverse_num)
#  51/1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:32(last_num)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#    51    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('inverse_num(n(100))')
# 212 function calls (112 primitive calls) in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.001    0.001 les_4_hw_task_1.py:28(inverse_num)
# 101/1    0.001    0.000    0.001    0.001 les_4_hw_task_1.py:32(last_num)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#   101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('inverse_num(n(200))')


# 414 function calls (214 primitive calls) in 0.003 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.003    0.003 les_4_hw_task_1.py:28(inverse_num)
# 201/1    0.003    0.000    0.003    0.003 les_4_hw_task_1.py:32(last_num)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#   201    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     3    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# Решение №2, оптимальный вариант
def top(num):
    BASE = 10
    result = 0
    while num > 0:
        result = result * BASE + num % BASE
        num = num // BASE
    return result


print('#2')
b_1 = (timeit.timeit('top(n(25))', number=100, globals=globals()))
print(b_1)  # 0.0010539410000000027
b_2 = (timeit.timeit('top(n(50))', number=100, globals=globals()))
print(b_2)  # 0.002188387000000014
b_3 = (timeit.timeit('top(n(100))', number=100, globals=globals()))
print(b_3)  # 0.0056417589999999684
b_4 = (timeit.timeit('top(n(200))', number=100, globals=globals()))
print(b_4)  # 0.016503829000000025
print('#2')
cProfile.run('top(n(25))')
# 10 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:67(top)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('top(n(50))')
# 10 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:67(top)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('top(n(100))')
# 10 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:67(top)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
cProfile.run('top(n(200))')


# 10 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#         1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:67(top)
#         1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#         1    0.000    0.000    0.000    0.000 random.py:244(randint)
#         1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

# Решение №3, самый быстрый вариант, решенный с помощью функций из коробки
def rev_str(num):
    num = ''.join(reversed(str(num)))
    return (int(num))


print('#3')
c_1 = (timeit.timeit('rev_str(n(25))', number=100, globals=globals()))
print(c_1)  # 0.0004519179999999956
c_2 = (timeit.timeit('rev_str(n(50))', number=100, globals=globals()))
print(c_2)  # 0.0005458940000000467
c_3 = (timeit.timeit('rev_str(n(100))', number=100, globals=globals()))
print(c_3)  # 0.0009375140000000837
c_4 = (timeit.timeit('rev_str(n(200))', number=100, globals=globals()))
print(c_4)  # 0.001771108999999993
print('#3')
cProfile.run('rev_str(n(25))')
# 11 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:93(rev_str)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('rev_str(n(50))')
# 11 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:93(rev_str)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('rev_str(n(100))')
# 12 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:93(rev_str)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('rev_str(n(200))')
# 12 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:17(n)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_1.py:93(rev_str)
#     1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#     1    0.000    0.000    0.000    0.000 random.py:244(randint)
#     1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#     1    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}


# Построение графика для наглядности
n = [25.0, 50.0, 100.0, 200.0]
t_1 = [a_1, a_2, a_3, a_4]
t_2 = [b_1, b_2, b_3, b_4]
t_3 = [c_1, c_2, c_3, c_4]

fig, ax = plt.subplots()
ax.plot(n, t_1, color="red", label="inverse_num")
ax.plot(n, t_2, color="blue", label="top")
ax.plot(n, t_3, color="green", label="rev_str")
ax.set_xlabel("n (длина числа)")
ax.set_ylabel("t (время)")
ax.grid()
ax.legend()
plt.show()
