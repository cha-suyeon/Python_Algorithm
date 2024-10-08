# 알파벳 개수
S = input().lower()

alphabet = list('abcdefghijklmnopqrstuvwxyz')
alpha = [0] * 26

for char in S:
    if char in alphabet:
        index = alphabet.index(char)
        alpha[index] += 1

for i in alpha:
    print(i, end=' ')

# 2
S = input().lower()

alpha = [0] * 26

for char in S:
    if char.isalpha():
        # ord는 문자의 ASCII 값을 반환
        # ord(char) - ord('a')의 연산은 문자가 알파벳 리스트에서 몇 번째 인덱스에 해당하는지 알 수 있음
        index = ord(char) - ord('a') # ord(a) = 97
        alpha[index] += 1

for i in alpha:
    print(i, end=' ')
