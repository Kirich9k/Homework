a1 = int(input('Введите первый член прогрессии: '))
d = int(input('Введите разницу: '))
n = int(input('Введите количество членов прогрессии: '))
print([a1 + (n - 1) * d for n in range(1, n + 1)])