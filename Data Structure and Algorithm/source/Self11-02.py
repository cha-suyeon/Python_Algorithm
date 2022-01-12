import  random
## 함수 선언부
def findInsertIdx(ary, data) :
    findIdx = -1  # 초기값은 없는 위치로
    for i in range(0, len(ary)) :
        if (ary[i] < data ) :
            findIdx = i
            break
    if findIdx == -1 : # 큰값을 못찾음 == 제일 마지막 위치
        return len(ary)
    else :
        return findIdx

## 전역 변수부
before = []
after = []

## 메인 코드부
before = [random.randint(0,200) for _ in range(10)]
print('정렬 전 -->', before)
for i in range(len(before)) :
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 -->', after)