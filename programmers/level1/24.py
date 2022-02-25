# 문자열 내림차순으로 배치하기

## 나의 코드
s = "Zbcdefg"

def solution(s):
    return ''.join(sorted(list(s), reverse=True))

print(s)