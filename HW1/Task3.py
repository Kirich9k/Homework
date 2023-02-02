digits = int(input('Введите номер билета: '))
firstThreeDigits = digits // 1000
secondThreeDigits = digits % 1000
sumFirstThreeDigits = 0
sumSecondThreeDigits = 0
while firstThreeDigits != 0 and secondThreeDigits != 0:
    sumFirstThreeDigits = sumFirstThreeDigits + firstThreeDigits % 10
    sumSecondThreeDigits = sumSecondThreeDigits + secondThreeDigits % 10
    firstThreeDigits //= 10
    secondThreeDigits //= 10
if sumFirstThreeDigits == sumSecondThreeDigits:
    print("YES")
else:
    print("NO")