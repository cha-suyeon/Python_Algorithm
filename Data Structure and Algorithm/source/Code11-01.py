def findMinIdx(ary) :
	minIdx = 0
	for i in range(1, len(ary)) :
		if (ary[minIdx] > ary[i] ) :
			minIdx = i
	return minIdx
		
testAry = [55, 88, 33, 77]
minPos = findMinIdx(testAry)
print('최솟값 -->', testAry[minPos])

