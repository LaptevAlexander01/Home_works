# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

x = int(input('Введите трехзначное число: '))
a = x // 100
b = (x // 10) - (a * 10)
c = x % 10
result = a + b + c
print(f'сумма чисел числа {x} равна {result}')

# Возможно не самый простой способ, однако на большее пока мозги не настроились. =)