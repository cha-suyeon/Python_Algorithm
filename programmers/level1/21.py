# 두 개 뽑아서 더하기

## 나의 풀이
def solution(numbers):
    
    answer = set()  # set()을 쓴 이유는 원소끼리 합의 중복을 없애주기 위해
    
    for i in range(len(numbers)):               # numbers 수많큼 반복
        for j in range(i+1, len(numbers)):      # 동일한 인덱스의 합을 막기 위해 i+1로 시작
            print(i)
            print(j)
            answer.add(numbers[i]+numbers[j])
            
    answer = list(answer) # list로 변경해줌
    answer.sort()   # 원소들 정렬을 해주어야 함
    
    return answer

numbers = [2,1,3,4,1]
print(solution(numbers))

## 남의 풀이
def solution2(numbers):
    
    answer = []
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i]+numbers[j])
    
    return sorted(set(answer))

## 남의 풀이 2
from itertools import combinations

def solution3(numbers):
    answer = []
    l = list(combinations(numbers, 2))
    
    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()
    
    return answer
    