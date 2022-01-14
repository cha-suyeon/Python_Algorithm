import random
## 함수 선언부
def binSearch(ary, fData) :
    global  count
    pos = -1
    start = 0
    end = len(ary) - 1

    while (start <= end) :
        count += 1
        mid = (start + end ) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return pos

## 전역 변수부
dataAry = [ ]
findData =  0
count = 0

## 메인 코드부
dataAry = [random.randint(0,100000) for _ in range(100000)]
dataAry.sort()
findData = random.randint(0,100000)
print('배열일부 -->', dataAry[:5], '~~~~', dataAry[-6:-1])
position = binSearch(dataAry, findData)
if position == -1 :
    print(findData,'(이)가 없네요.')
else :
    print(findData,'(은)는 ', position, '위치에 있음')
print('##', count, "회 검색함")