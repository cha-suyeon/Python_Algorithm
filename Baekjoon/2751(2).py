# Merge Sorting

n = int(input())
data = []

for _ in range(n) :
    data.append(int(input()))

def merge_sort(data) :
    if len(data) <= 1 :
        return data
    mid = len(data) // 2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    i, j = 0, 0
    temp = []

    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            temp.append(left[i])
            i += 1
        else :
            temp.append(right[j])
            j += 1

    temp += left[i:]
    temp += right[j:]

    return temp

data = merge_sort(data)

for d in data :
    print(d)