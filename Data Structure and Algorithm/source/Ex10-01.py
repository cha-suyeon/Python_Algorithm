## 함수 선언 부분 ##
def notation(base, n):
	if n < base :
		print(numberChar[n], end = ' ')
	else :
		notation(base, n // base)
		print(numberChar[n % base], end = ' ')

## 전역 변수 선언 부분 ##
numberChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numberChar += ['A', 'B', 'C', 'D', 'E', 'F']

## 메인 코드 부분 ##
number = int(input('10진수 입력 -->'))
print('\n 2진수 : ', end = ' ')
notation(2, number)
print('\n 8진수 : ', end = ' ')
notation(8, number)
print('\n16진수 : ', end = ' ')
notation(16, number)
