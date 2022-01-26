# 핸드폰 번호 가리기


## 1 (나의 풀이)
def solution(phone_num):
    a = len(phone_num)
    b = phone_num[a-4:]
    answer = '*'*(a-4) + b    
    return answer

print(solution("01023103384"))

## 2 (다른 사람 풀이)
def hide_number(s):
    return '*'*(len(s)-4 + s[-4:]) # -4를 하면 뒤에서 4개의 문자열까지 된다! 유레카