# 수 찾기
# 풀이 1
n = int(input())
lst1 = set(map(int,input().split())) # 탐색 시간을 줄여줌
m = int(input())
lst2 =list(map(int,input().split()))

for j in lst2:
    if j in lst1:
        print(1)
    else:
        print(0)
        
# 풀이 2
n = int(input())
lst1 = list(map(int,input().split())) # 정렬해줘야 함
m = int(input())
lst2 =list(map(int,input().split()))
lst1.sort()

def binarySearch(l1, x, start, end):
    if start > end:
        return False
    
    mid = (start+end) // 2
    
    if l1[mid] == x:
        return True
    elif l1[mid] > x:
        return binarySearch(l1, x, start, mid-1)
    else:
        return binarySearch(l1, x, mid+1, end)
    
for i in lst2:
    if binarySearch(lst1, i, 0, n-1):
        print(1)
    else:
        print(0)