# Задача 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком
from hashlib import sha256


def count_sub(str):
    len_sub = len(str)
    num_of_sub = set()
    for i in range(len_sub):
        for j in range(len_sub - 1 if i == 0 else len_sub, i, -1):
            num_of_sub.add(sha256((str[i:j]).encode('utf-8')).hexdigest())
    return len(num_of_sub)


print(count_sub('abcd'))
print(count_sub('papa'))
print(count_sub('sova'))
