# return 때문에 헷갈려서 가져온 코드 예제

def is_palindrome(word):
    for i in range(len(word)):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True

print(is_palindrome('word'))            # False
print(is_palindrome('wow'))             # True
print(is_palindrome('토마토'))          # True
print(is_palindrome('간장공장공장장'))   # False