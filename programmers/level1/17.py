# 자릿수 더하기

## 나의 풀이

from numpy import number


def solution(n):
    answer = 0
    new = str(n)                # 입력값이 정수여서 문자열로 변경
    print(new)
    for i in range(len(new)):   # 문자열 길이만큼 반복
        answer += int(new[i])   # 문자열 슬라이싱하여 answer에 더해줌
    return answer

print(solution(123))

## 남의 풀이

def solution1(n):
    if n < 10:
        return n
    return (n % 10) + solution(n//10)

    """
    재귀로 구현한 코드
    n이 10보다 작으면 그냥 n을 return한다.
    한자리 수이면 더해줄 필요가 없기 때문에
    
    첫 번째 자리수: n을 10으로 나누고 남은 나머지
    두 번째 자리수: n을 10으로 나눈 몫을 남긴다
    
    예를 들어, 123이 입력되면
    
    123을 10으로 나눈 나머지는 3을 반환
    123을 10으로 나눈 몫은 12를 반환
    12를 다시 함수에 넣고 돌리게 됨(재귀의 성격)
    
    두 번째로 돌때는 아까 반환한 3과
    12%10을 한 2
    12//10을 한 1
    이 나오게 되어 1+2+3이 최종적으로 계산된다.
    """
    
## 남의 코드 2
def solution2(n):
    return sum([int(i) for i in str(n)])

## 남의 코드 3
def solution3(n):
    return sum(map(int, str(n)))