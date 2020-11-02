# https://drive.google.com/file/d/1mFQYrqI85LA3Dyv4BQVp16mtV2KYKRB9/view?usp=sharing - diagrams
# Задача 8. Определить, является ли год, который ввел пользователь, високосным или не високосным.
x = int(input('Введите год: '))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print(f'{x} год високосный!')
        else:
            print(f'{x} год не високосный!')
    else:
        print(f'{x} год високосный!')
else:
    print(f'{x} год не високосный!')
