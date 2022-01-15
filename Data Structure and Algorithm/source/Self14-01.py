# ## 함수 선언부
def knapsack():
    print('## 메모이제이션 배열 ##')
    array = [[0 for _ in range(maxWeight+1)] for _ in range(rowCount+1)] # 빈 배열을 만들고 모두 0으로
    for row in range(1, rowCount+1): # 1개 ~ 4개 (4회)
        print(row, '개 -->', end=' ')
        for col in range(1, maxWeight+1): # 1colg ~ 7colg
            if weight[row] > col: # 물건의 무게가 열보다 크면 == 물건이 가방에 안 들어가면
                array[row][col] = array[row-1][col]
            else: # 물건의 부피가 s보다 작거나 같으면
                value1 = money[row] + array[row-1][col-weight[row]] # 각 그림의 1-1
                value2 = array[row-1][col] # 각 그림의 1-2
                array[row][col] = max(value1, value2)
            print('%2d' % array[row][col], end=' ')
        print()
    return array[rowCount][maxWeight]

## 전역 변수부
maxWeight = 7  # 배낭 최대 무게
rowCount = 4 # 보석 숫자
weight = [0, 5, 3, 6, 4]   # 보석 무게 (0, 진주, 루비, 금괴, 수정)
money =  [0, 12, 6, 13, 8] # 보석 가격 (0, 진주, 루비, 금괴, 수정)

## 메인 코드부
maxValue = knapsack()
print()
print('배낭에 담을 수 있는 보석의 최대 가격 -->', maxValue, '억원')