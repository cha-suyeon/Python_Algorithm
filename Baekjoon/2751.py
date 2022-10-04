# Merge sort
# This question needs an efficient memory e.g. o(n log n)

n=int(input())
nums = [int(input()) for _ in range(n)] # range(5) -> input the n-th into the list 'nums'

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2 # find the mid of the array
        
    # Dividing the array elements into 2 halves
    L = mergeSort(arr[:mid])
    R = mergeSort(arr[mid:])

    i = j = k = 0 # i, j, k - index 역할(index of left, right and array)
        
    # Copy data to temp array L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:    # Compare Left and Right
            arr[k] = L[i]   # L 원소가 더 작아서 arr[k] 자리에 들어감
            i += 1          # L 인덱스 i에 +1
        else:
            arr[k] = R[j]   # R 원소가 더 작아서 arr[k] 자리에 들어감
            j += 1          # R 인덱스 j에 +1
        k += 1              # 이 과정이 한 번 끝나면 k+1
        
    # Checking if any element was left
    if i == len(L):           # 한쪽 리스트가 끝난 경우, 나머지 리스트를 넣어줌
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    elif j == len(R):
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
    
    return arr

mergeSort(nums)

for i in nums:
    print(i) # print each value in nums list