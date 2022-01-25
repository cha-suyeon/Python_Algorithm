# 가운데 글자 가져오기

## 1
def solution(s):
    a = len(s)
    if a % 2 == 0:
        a_cen = a//2
        return s[a_cen-1:a_cen+1]
    else:
        a_cen = a//2
        return s[a_cen]
    
## 2
def sol2(str):
    
    return str[(len(str)-1)//2-(len(str)-1)//2+1]