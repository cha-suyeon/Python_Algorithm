# Number sorting

# Insertion sort

n = int(input())
nums = [int(input()) for _ in range(n)]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # 1, ..., n
        print("i", i)
        j = i -1 # arr[i]와 비교 대상이 되는 arr[i-1]
        print("first j", j)
        while j >= 0 and key < arr[j]:
        # 비교되는 arr[i-1]이 0까지만 가도록 and i번째 인덱스와 i-1 인덱스와 비교
            arr[j+1] = arr[j] # arr[i] 자리에 arr[j-1]로 대체
            j -= 1
            print("second j", j)
        arr[j+1] = key

insertionSort(nums)

for i in nums:
    print(i)
