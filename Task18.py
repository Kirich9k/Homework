arrayLength = int(input('Введите количество элементов в массиве: '))
arrayForCompare = [int(input(f'Введите {i+1} элемент массива: ')) for i in range(arrayLength)]
digitForCompare = int(input('Введите число: '))
minDifferenceElement = arrayForCompare[0]
for i in arrayForCompare:
    if abs(i - digitForCompare) < abs(i - minDifferenceElement) and i < minDifferenceElement:
        minDifferenceElement = i
print(minDifferenceElement)