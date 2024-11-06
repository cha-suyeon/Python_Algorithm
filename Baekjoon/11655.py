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