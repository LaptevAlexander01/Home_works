# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

array = []
a1 = int(input('Введите первое число: '))
d = int(input('Введите разность(шаг): '))
n = int(input('Введитеде количество элементов: '))
for i in range(n):
    array.append(a1 + i * d)
print(array)