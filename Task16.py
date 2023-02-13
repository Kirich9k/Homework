arrayLength = int(input('Введите количество элементов в массиве: '))
arrayForSearch = [int(input(f'Введите {i+1} элемент массива: ')) for i in range(arrayLength)]
digitForSearch = int(input('Введите число: '))
print(sum([1 for i in range(arrayLength) if arrayForSearch[i] == digitForSearch]))
#print(arrayForSearch.count(int(input('Введите число: '))))