# 문자열 내 p와 y의 개수

def solution(s):
    return s.lower().count('p') == s.lower().count('y')

## 다른 사람 풀이
## 1 ##
from collections import Counter
def numPY(S):
	c = Counter(s.lower())
	return c['y'] == c['p']

## 2 ## 
def numPY(s):
	if s.upper().count('P') == s.upper().count('Y'):
		return True
	return False