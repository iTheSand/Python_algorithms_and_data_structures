# Задание 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

dic_num_sys = {'A': 10,
               'B': 11,
               'C': 12,
               'D': 13,
               'E': 14,
               'F': 15
               }

reverse_dic_num_sys = {lett: num for num, lett in dic_num_sys.items()}

num_1 = deque(input('Введите первое шестнадцатиричное число (0-F): ').upper())
num_2 = deque(input('Введите второе шестнадцатиричное число (0-F): ').upper())

diff_length = len(num_1) - len(num_2)

if diff_length < 0:
    while diff_length < 0:
        num_1.appendleft('0')
        diff_length += 1
else:
    while diff_length > 0:
        num_2.appendleft('0')
        diff_length -= 1

sum_num = deque()
while len(num_1) > 0:
    last_num = num_1[-1] + num_2[-1]
    sum_num.appendleft(last_num)
    num_1.pop()
    num_2.pop()

finish = deque()
num_sys = 16
keep_in_mind = 0
while len(sum_num) > 0:
    result = 0
    for i in sum_num[-1]:
        if i.isdigit() == True:
            i = (int(i))
            result += i
        else:
            i = (dic_num_sys[i])
            result += i
    result += keep_in_mind
    sum_num.pop()
    keep_in_mind = 0
    if result < 10:
        finish.appendleft(str(result))
    elif 9 < result < 16:
        write_number = reverse_dic_num_sys[result]
        finish.appendleft(str(write_number))
    elif 15 < result < 26:
        result -= num_sys
        finish.appendleft(str(result))
        keep_in_mind += 1
    elif result >= 26:
        result -= num_sys
        write_number = reverse_dic_num_sys[result]
        finish.appendleft(str(write_number))
        keep_in_mind += 1
if keep_in_mind > 0:
    finish.appendleft(str(keep_in_mind))

print(f'Сумма чисел = {str("".join(finish))}')
