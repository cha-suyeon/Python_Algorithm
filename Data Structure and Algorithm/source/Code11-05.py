## 함수 선언 부분 ##
def findInsertIdx(ary, data) :
	findIdx = -1			# 초깃값은 없는 위치로
	for i in range(0, len(ary)) :
		if (ary[i] > data ) :
			findIdx = i
			break
	if findIdx == -1 :			# 큰 값을 못찾음 == 제일 마지막 위치
		return len(ary)
	else :
		return findIdx

## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for i in range(len(before)) :
	data = before[i]
	insPos = findInsertIdx(after, data)
	after.insert(insPos, data)
print('정렬 후 -->', after)
