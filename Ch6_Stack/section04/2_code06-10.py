# section04
# 괄호의 매칭 검사

def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False

# 스택이 비었는지 확인하는 함수
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

# 스택에 데이터를 삽입하는 함수
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('Stack is Full')
        return
    top += 1
    stack[top] = data


# 스택에 데이터를 추출하는 함수
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 스택에서 top 위치의 데이터를 확인하는 함수
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('Stack is Empty')
        return None
    return stack[top]


## 괄호 매칭 검사 구현 ⭐⭐⭐⭐⭐
def checkBracket(expr):
    for ch in expr:
        if ch in '([{<':
            push(ch)
        elif ch in ')]}>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == ']' and out == '[':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass
    if isStackEmpty():
        return True
    else:
        return False


## 전역 변수 선언 부분 ##
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1


## 메인 코드 선언 부분 ##
if __name__ == '__main__':

    exprAry = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expr in exprAry:
        top = -1
        print(expr, '==>', checkBracket(expr))