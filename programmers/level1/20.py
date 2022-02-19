# 시저 암호

## 풀이 1
U = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L = U.lower()

def solution(s, n):
    return s.translate(str.maketrans(U+L), U[n:]+U[:n]+L[n:]+L[:n]) if n else s

## 풀이 2
def solution1(s,n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n) % 26 + ord('A'))
        if s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n) % 26 + ord('a'))
            
    return ''.join(s)

s = 'a z'
print('s: ', s)
new_list = list(s)
print('new_list: ', new_list)

for i in range(len(s)):
    print(ord(new_list[i]))
    print(chr(ord(new_list[i])-ord('a') + 1 ) % 26 + ord('a'))

print(ord('A'))
print(ord('a'))
