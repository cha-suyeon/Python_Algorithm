# 같은 숫자는 싫어

## 나의 풀이
def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i == 0 :
            answer.append(arr[i])
            print(answer)
        elif arr[i] != arr[i-1]:
            answer.append(arr[i])
            print(answer)
    
    return answer