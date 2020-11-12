# Задание 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

# Вывод: проанализировав 2 алгоритма, видно, что оба варианта имеют линейную сложность O(n).
# Первый вариант решения более эффективный и отрабатывает примерно в 10 раз быстрее.
# Т.к. второе решение не очень эффективное, размер массива ограничил 4000.
import timeit
import cProfile
import matplotlib.pyplot as plt


# Вариант №1, с помощью решета «Решета Эратосфена».
def sieve(num, n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in sieve:
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    li = [i for i in sieve if i != 0]
    return li[num - 1]


print('#1')
a_1 = (timeit.timeit('sieve(3, 1000)', number=100, globals=globals()))
print(a_1)  # 0.032396437000000056
a_2 = (timeit.timeit('sieve(5, 2000)', number=100, globals=globals()))
print(a_2)  # 0.06824369200000002
a_3 = (timeit.timeit('sieve(1, 4000)', number=100, globals=globals()))
print(a_3)  # 0.14568261300000007
print('#1')

cProfile.run('sieve(3, 1000)')
# 6 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:17(sieve)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:18(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:28(<listcomp>)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(5, 2000)')
# 6 function calls in 0.001 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.001    0.001    0.001    0.001 les_4_hw_task_2.py:17(sieve)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:18(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:28(<listcomp>)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('sieve(1, 4000)')


# 6 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     1    0.001    0.001    0.002    0.002 les_4_hw_task_2.py:17(sieve)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:18(<listcomp>)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:28(<listcomp>)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант №2, без использования решета «Решета Эратосфена».
def prime(num, n):
    range_num = [i for i in range(n)]
    li = []
    for i in range_num:
        count = 2
        k = 0
        while count ** 2 <= i and k != 1:
            if i % count == 0:
                k = 1
            count += 1
        if k != 1 and i != 0 and i != 1:
            li.append(i)
    return li[num - 1]


print('#2')
b_1 = (timeit.timeit('prime(3, 1000)', number=100, globals=globals()))
print(b_1)  # 0.204783033
b_2 = (timeit.timeit('prime(5, 2000)', number=100, globals=globals()))
print(b_2)  # 0.4988613810000001
b_3 = (timeit.timeit('prime(1, 4000)', number=100, globals=globals()))
print(b_3)  # 1.232119191
print('#2')

cProfile.run('prime(3, 1000)')
# 173 function calls in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     1    0.002    0.002    0.002    0.002 les_4_hw_task_2.py:47(prime)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:48(<listcomp>)
#     1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#   168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(5, 2000)')
# 308 function calls in 0.005 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#     1    0.005    0.005    0.005    0.005 les_4_hw_task_2.py:47(prime)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:48(<listcomp>)
#     1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#   303    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
cProfile.run('prime(1, 4000)')
# 555 function calls in 0.013 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.013    0.013 <string>:1(<module>)
#     1    0.012    0.012    0.013    0.013 les_4_hw_task_2.py:47(prime)
#     1    0.000    0.000    0.000    0.000 les_4_hw_task_2.py:48(<listcomp>)
#     1    0.000    0.000    0.013    0.013 {built-in method builtins.exec}
#   550    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Построение графика для наглядности
n = [1000.0, 2000.0, 4000.0]
t_1 = [a_1, a_2, a_3]
t_2 = [b_1, b_2, b_3]

fig, ax = plt.subplots()
ax.plot(n, t_1, color="blue", label="sieve")
ax.plot(n, t_2, color="red", label="prime")
ax.set_xlabel("n (размер массива)")
ax.set_ylabel("t (время)")
ax.grid()
ax.legend()
plt.show()
