# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

size = int(input('Введите размер массива '))
print('Введите целые чила массива N')
array = [int(input()) for _ in range(size)]
print(array)
x = int(input('Введите число X '))
min = abs(x - array[0])
index = 0
for i in range(1, size):
    count = abs(x - array[i])
    if count < min:
        min = count
        index = i
print(f'Число {array[index]} в массиве наиболее близко по величине к числу {x}')
