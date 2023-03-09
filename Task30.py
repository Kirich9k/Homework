dictionary = 'аоуэыяеёюи'
poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.split()
result = [sum([True for j in word if j.lower() in dictionary]) for word in poem]
if all(result) and len(set(result)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")