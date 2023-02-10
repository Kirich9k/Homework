n = int(input('Введите число монеток: '))
countEagles = countTales = 0
token = 0
for _ in range(n):
    token = int(input("Введите 1, если это орел, или 0, если это решка: "))
    if token == 1:
        countEagles += 1
    if token == 0:
        countTales +=1
if countEagles < countTales:
    print(countEagles)
else:
    print(countTales)