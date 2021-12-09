## 함수 선언 부분 ##
def findMinIdx(ary) :
	minIdx = 0
	for i in range(1, len(ary)) :
		if (ary[minIdx] > ary[i]) :
			minIdx = i
	return minIdx
	
## 전역 변수 선언 부분 ##
before = [188, 162, 168, 120, 50, 150, 177, 105]
after = []

## 메인 코드 부분 ##
print('정렬 전 -->', before)
for _ in range(len(before)) :
	minPos = findMinIdx(before)
	after.append(before[minPos])
	del(before[minPos])
print('정렬 후 -->', after)
