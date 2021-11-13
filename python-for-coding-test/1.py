# 1
def solution(s):
    try:
        int(s)
    except:
        return False
    return len(s) == 4 or len(s) == 6
        
print(solution('a234'))
print(solution('1234'))

# 2
def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
        return False
    
print(solution('a234'))
print(solution('1234'))
