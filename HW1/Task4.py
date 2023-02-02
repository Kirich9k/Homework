n = int(input('Введите 1й размер шоколадки: '))
m = int(input('Введите 2й размер шоколадки: '))
k = int(input('Введите нужное количество долек: '))
if k % n == 0:
    print('YES')
elif k % m == 0:
    print('YES')
elif k % n * m == 0:
    print('YES')
else: 
    print('NO')