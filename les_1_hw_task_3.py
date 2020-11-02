# https://drive.google.com/file/d/1mFQYrqI85LA3Dyv4BQVp16mtV2KYKRB9/view?usp=sharing - diagrams
# Задача 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
symbol_1 = input('введите строчную букву англ. алфавита (a-z): ')
symbol_2 = input('введите строчную букву англ. алфавита (a-z): ')
a = ord(symbol_1) - 96
b = ord(symbol_2) - 96
if b > a:
    c = (len(range(a + 1, b)))
else:
    c = (len(range(b + 1, a)))

print(f'буква {symbol_1} находится на {a} месте в алфавите')
print(f'буква {symbol_2} находится на {b} месте в алфавите')
print(f'между буквами {symbol_1} и {symbol_2} находится {c} буквы')
