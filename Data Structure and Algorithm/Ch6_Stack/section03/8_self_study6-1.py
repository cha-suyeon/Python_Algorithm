# code06-04.py의 isStackFull() 함수를 없애고, 대신에 push() 함수만으로 그 기능을 모두 구현

# 해당 결괏값이 나와야 함
# ['커피', '녹차', '꿀물', '콜라', None]
# ['커피', '녹차', '꿀물', '콜라', '환타']
# 스택이 꽉 찼습니다.

def push(data):                         # 매개변수로 넘겨 받은 data를 stack에 삽입하는 함수
    global SIZE, top, stack
    if (top >= SIZE-1):
        print('스택이 꽉 찼습니다.')
        return
    top += 1
    stack[top] = data

SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", None]
top = 3

print(stack)
push('환타')
print(stack)
push('게토레이')