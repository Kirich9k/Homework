dictionary = {'AEIOULNSTRАВЕИНОРСТ': 1, 'DGДКЛМПУ ' : 2,
'BCMPБГЁЬЯ' : 3, 'FHVWYЙЫ' : 4, 'KЖЗХЦЧ' : 5,
'JXШЭЮ' : 8, 'QZФЩЪ' : 10}
word = input('Введите слово: ')
print(sum(i[1] for i in dictionary.items() for j in word if j.upper() in i[0]))