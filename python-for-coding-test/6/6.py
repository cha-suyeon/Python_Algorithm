# <문제> 위에서 아래로

# N 입력 받기
n = int(input())

# 입력 받을 빈 리스트 array 생성
array = []

# n번 반복하며 n개의 정수를 입력 받음
for i in range(n):
    array.append(int(input()))

# array를 파이썬 기본 내장 라이브러리를 활용해 내림차순 정렬
array = array.sort(reverse=True)

# array에 있는 원소 하나씩 공백을 간격으로 두고 출력
for i in array:
    print(i, end=' ')
