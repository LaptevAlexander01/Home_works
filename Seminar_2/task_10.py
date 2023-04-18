# Задача 10:
#  На столе лежат n монеток. Некоторые из них лежат вверх решкой, а
# некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же
# стороной. Выведите минимальное количество монет, которые нужно
# перевернуть.

n = int(input('Введите сколько монеток лежат на столе '))
count = 0
print('Введите какой стороной лежат монетки (где 1 это решка, 0 это орел)')
for i in range(n):
    side = int(input())
    if side == 1:
        count += 1
print(f'нужно перевернуть {count if count<n/2 else n-count} монетки')
