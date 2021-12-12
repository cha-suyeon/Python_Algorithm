## 함수 선언 부분 ## 
def binSearch(ary, fData) :
	pos = -1
	start = 0
	end = len(ary) - 1

	while (start <= end) :
		mid = (start + end ) // 2
		if fData == ary[mid] :
			return mid
		elif fData > ary[mid] :
			start = mid + 1
		else :
			end = mid - 1

	return pos

## 전역 변수 선언 부분 ##
dataAry = [ 50, 60, 105, 120, 150, 160, 162, 168, 177, 188]
findData = 162	# 할머니키

## 메인 코드 부분 ##
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
	print(findData,'(이)가 없네요.')
else :
	print(findData,'(은)는 ', position, '위치에 있음')
