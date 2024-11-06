# 1
sentence = input()

orig = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
trans = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
characters = []

for i, char in enumerate(sentence):
    if char.isalpha():
        idx = orig.index(char)
        characters.append(trans[idx])
    elif char.isdigit():
        characters.append(char)
    elif char.isspace():
        characters.append(char)

characters = ''.join(characters)
print(characters)


# 2 ASCII
answer = ''
for i in input():
    if i.isupper():
        if (65 <= ord(i) <= 77):
            answer += chr(ord(i) + 13)  # A ~ M
        else:
            answer += chr(ord(i) - 13)  # N ~ Z
    elif i.islower():
        if (97 <= ord(i) <= 109):
            answer += chr(ord(i) + 13)  # a ~ m
        else:
            answer += chr(ord(i) - 13)  # n ~ z
    else:
        answer += i
        
print(answer)
