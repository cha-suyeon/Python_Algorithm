## 함수 선언부
def seqSearch(ary, fData) :
    posList = []
    size = len(ary)
    for i in range(size) :
        if ary[i] == fData :
            posList.append(i)
    return posList

## 전역 변수부
dataAry = [188, 50, 150, 168, 50, 162, 105, 120, 177, 50]
findData = 50

## 메인 코드부
print('배열 -->', dataAry)
positionList = seqSearch(dataAry, findData)
if positionList == [] :
    print(findData,'(이)가 없네요.')
else :
    print(findData,'(은)는 ', positionList, '위치에 있음')
