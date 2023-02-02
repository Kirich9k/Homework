digitsForSum = int(input('Введите число: '))
sumOfDigits = 0
while digitsForSum != 0:
    sumOfDigits = sumOfDigits + digitsForSum % 10
    digitsForSum //= 10
print(sumOfDigits)