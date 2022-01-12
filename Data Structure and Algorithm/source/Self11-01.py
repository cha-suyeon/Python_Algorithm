def findMaxIdx(ary) :
    maxIdx = 0
    for i in range(1, len(ary)) :
        if (ary[maxIdx] < ary[i] ) :
            maxIdx = i
    return maxIdx

testAry = [55, 88, 33, 77]
minPos = findMaxIdx(testAry)
print('최댓값 -->', testAry[minPos])