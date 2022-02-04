# 문자열 다루기 기본

## 나의 풀이 1
def solution(s):
    if len(s) == 4 or len(s) == 6:
        try:
            int(s)
            return True
        except ValueError:
            return False
    else:
        return False
    
## 남의 풀이 1
def solution1(s):
    return s.isdigit() and len(s) in (4, 6)

## 남의 풀이 2
def solution2(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6

print(solution2("a1234"))
print(solution2("1234"))
print(solution2("12345"))
print(solution2("123456"))