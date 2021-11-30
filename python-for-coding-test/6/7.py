# <문제> 성적이 낮은 순서로 학생 출력하기

# N 입력 받기
n = int(input())

# 입력 받을 빈 리스트 array 생성
array = []

# n명의 학생 정보 입력 받기
for i in range(n):
    # '학생 점수' 입력 받고 공백을 기준으로 split함
    input_data = input().split()
    # array 빈 리스트에 split 한 '학생', '이름' 값 추가
    array.append((input_data[0], int(input_data[1])))

# 키(key)를 이용하여, 점수를 기준으로 정렬
# 정렬하는 것이 sorted, 기준값 설정을 key로
# 따라서 student[1]은 점수이므로 점수대로 오름차순 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력 - 결과는 이름순으로 출력하라 하였으므로
for student in array:
    print(student[0], end=' ')