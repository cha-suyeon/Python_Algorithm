def addNumber(num1, num2) :
    if num2 <= num1 :
        return num1
    return num2 + addNumber( num1, num2 - 1 )

num1 = int(input('숫자1-->'))
num2 = int(input('숫자2-->'))
if num1 > num2 :
    num1, num2 = num2, num1
print(addNumber(num1, num2))