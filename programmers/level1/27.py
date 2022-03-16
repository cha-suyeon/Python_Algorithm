# k번째 수

## 나의 풀이
def solution(array, commands):
    answer = []
    for i in commands:
        slice = array[i[0]-1:i[1]]
        slice.sort()
        answer.append(slice[(i[2]-1)])
    return answer