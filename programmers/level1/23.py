# 이상한 문자 만들기

## 나의 풀이

def solution(s):
    answer = ''
    word_list = s.split(' ')
    new_list = []

    for word in word_list:
        new_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i].lower()
        new_list.append(new_word)

    answer = ' '.join(new_list)

    return answer
