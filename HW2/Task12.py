sumOfDigits = int(input('Введите сумму двух чисел: '))
productOfDigits = int(input('Введите произведение двух чисел: '))
d = sumOfDigits ** 2 - 4 * productOfDigits
if d >= 0:
    firstDigit = (sumOfDigits + d ** 0.5) // 2
    secondDigit = (sumOfDigits - d ** 0.5) // 2
    if firstDigit * secondDigit == productOfDigits:
        print(int(firstDigit), int(secondDigit))
else:
    print('Решений нет')