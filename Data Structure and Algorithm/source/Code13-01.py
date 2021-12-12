## 함수 선언 부분 ## 
def seqSearch(ary, fData) :
	pos = -1
	size = len(ary)
	print('## 비교한 데이터 ==> ', end = '')
	for i in range(size) :
		print(ary[i], end = ' ')
		if ary[i] == fData :
			pos = i
			break
	print()
	return pos

## 전역 변수 선언 부분 ## 
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
findData = 0

## 메인 코드 부분 ## 
findData = int(input('* 찾을 값을 입력하세요. --> '))
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
	print(findData, '(이)가 없네요.')
else :
	print(findData,'(은)는 ', position, '위치에 있음')
