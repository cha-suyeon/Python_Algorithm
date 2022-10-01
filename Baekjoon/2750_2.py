# Number sorting

# Insertion sort

n = int(input())
nums = [int(input()) for _ in range(n)]

def insertionSort(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i-1]:
        # 비교되는 arr[i-1]이 0까지만 가도록 and i번째 인덱스와 i-1 인덱스와 비교
            arr[i], arr[i-1] = arr[i-1], arr[i] # Swap arr[i] and arr[i-1]
            i -= 1
            print("i", i)
            print("arr", arr)

insertionSort(nums)
print("nums", nums)

for i in nums:
    print(i)