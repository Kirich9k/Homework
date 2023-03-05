n = int(input("Введите количество кустов: "))
bushes = [int(i) for i in input().split()]
bushesMax = 0
for i in range(n):
    bushesSum = bushes[i - 1] + bushes[i] + bushes[i + 1 if 1 < n - 1 else 0]
    if bushesSum > bushesMax:
        bushesMax = bushesSum
print(bushesMax)
