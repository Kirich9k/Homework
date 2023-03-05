n, m = input('Введите количество элементов в множествах: ').split()
firstList = [int(i) for i in input('Введите первое множество: ').split()]
secondList = [int(j) for j in input('Введите второе множество: ').split()]
print(*sorted(set(firstList).intersection(secondList)))