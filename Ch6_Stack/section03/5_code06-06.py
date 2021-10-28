# Section 03

# 스택에서 데이터를 추출하는 함수
# 스택에서 데이터를 추출하는 함수를 작성한다
# 앞에서 생성했던 isStackEmpty() 함수를 사용해서 먼저 스택이 비었는지 확인하고, 스택에 데이터가 있다면 데이터를 추출하도록 코드를 작성하자.

def isStackEmpty():
    global SIZE, top, stack
    if (top == -1):
        return True
    else:
        return False

def pop():
    global SIZE, top, stack
    if isStackEmpty():              # 스택이 비었는지 확인
        print('Stack is Empty')     # 비었다면 메시지 출력
        return None                 # None 값 반환
    data = stack[top]               # 데이터가 있다면 top 위치의 데이터 추출
    stack[top] = None
    top -= 1                        # top 1 감소
    return data                     # 추출한 데이터 반환

SIZE = 5
stack = ['커피', None, None, None, None]
top = 0

print(stack)
retData = pop()
print('추출한 데이터-->', retData)
print(stack)
retData = pop()




