# Merge Sorting

n = int(input())
data = []

for _ in range(n) :
    data.append(int(input()))

def merge_sort(data) :
    
    # merge sort가 중단되는 경우
    # 1개 이하일 경우 정렬할 필요가 없으므로 해당 리스트를 그대로 반환
    if len(data) <= 1 :
        return data
    
    # 리스트의 중간 위치를 구해서 mid에 저장
    mid = len(data) // 2

    # merge_sort() 함수를 재귀호출하여 정렬을 수행한 값을 할당
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    i, j = 0, 0
    temp = []

    # i가 left 리스트 개수 이상이거나
    # j가 right 리스트 개수 이상일 때까지 while문 작업을 반복 수행
    # 더 작은 값을 temp 리스트에 저장하고 i 혹은 j 값을 1 증가시킴
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            temp.append(left[i])
            i += 1
        else :
            temp.append(right[j])
            j += 1

    # while문이 끝난 후,
    # left 리스트나 right 리스트 내에 남은 요소들을 temp 리스트에 추가
    temp += left[i:]
    temp += right[j:]

    # temp 리스트 반환
    return temp

data = merge_sort(data)

for d in data :
    print(d)
    
