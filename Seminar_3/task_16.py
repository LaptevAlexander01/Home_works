# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

size = int(input('Введите размер массива '))
print('Введите целые чила массива N')
array = [int(input()) for _ in range(size)]
print(array)
x = int(input('какое число найти? '))
count = 0
for i in range(len(array)):
    if array[i] == x:
        count += 1
print(f'Некоторое число Х({x}) встречается {count} раз(а)')
