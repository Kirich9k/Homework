def sumWithoutSum(a, b):
    if b == 0:
        return a
    return sumWithoutSum(a + 1, b -1)
print(sumWithoutSum(int(input('Введите первое слагаемое: ')), int(input('Введите второе слагаемое: '))))