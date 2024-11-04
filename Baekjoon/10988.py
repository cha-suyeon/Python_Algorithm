# 1
word = input()
reversed_word = word[::-1]

if word == reversed_word:
    print(1)
else:
    print(0)

# 2
word = input()

left = 0
right = len(word) - 1

is_palindrome = True
while left < right:
    if word[left] != word[right]:  
        is_palindrome = False
        break                   
    left += 1
    right -= 1

if is_palindrome:
    print(1)
else:
    print(0)