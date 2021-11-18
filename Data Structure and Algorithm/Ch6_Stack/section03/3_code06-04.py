# Section 03
# 2. 데이터 삽입 과정
# 스택에 데이터를 삽입하는 함수

# isFullStack() 함수로 스택이 꽉 찼는지 먼저 확인하고, 여유가 있다면 데이터를 삽입하도록 코드 작성

def isFullStack():
    global SIZE, top, stack
    if (top >= SIZE-1):
        return True
    else:
        return False

def push(data):                         # 매개변수로 넘겨 받은 data를 stack에 삽입하는 함수
    global SIZE, top, stack
    if (isFullStack()):                 # stack이 가득찼는지 확인
        print('Stack is Full')          # 꽉 찼다면 해당 메시지 출력후 함수 종료
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

# 결괏값
# ['커피', '녹차', '꿀물', '콜라', None]
# ['커피', '녹차', '꿀물', '콜라', '환타']
