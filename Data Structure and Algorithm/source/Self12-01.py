import random
## 함수 선언부
def BubbleSort(ary) :
    global  count
    n = len(ary)
    for end in range(n-1, 0, -1) :
        changeYN = False
        for cur in range(0, end) :
            count += 1
            if ( ary[cur] > ary[cur+1] ) :
                ary[cur], ary[cur+1] = ary[cur+1], ary[cur]
                changeYN = True
        if not changeYN :
            break
    return ary

## 전역 변수부
dataAry = [  ]
count = 0

## 메인 코드부
dataAry = [random.randint(0,200) for _ in range(10)]
print('정렬 전 -->', dataAry)
dataAry = BubbleSort(dataAry)
print('정렬 후 -->', dataAry)
print('##', count, "회 로 정렬 완성")
