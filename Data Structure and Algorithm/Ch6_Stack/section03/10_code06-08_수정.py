# Section 03
# 5. 스택 완성

# 앞서 작성한 데이터 삽입, 추출, 확인을 통합한 코드를 작성하자
# 처음 사용자에게 스택 크기를 입력받은 후 초기화해서 입력한 크기만큼 생성한다
# 그리고 사용자가 삽입, 추출, 확인을 선택해서 작동하도록 코드를 완성해보자


# 스택이 꽉 찼는지 확인하는 함수
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


## 전역 변수 선언 부분 ##
SIZE = int(input('스택 크기를 입력하세요==>'))
stack = [None for _ in range(SIZE)]
top = -1


## 메인 코드 부분 ##
if __name__ == "__main__":
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

    while True:

        if select == 'I' or select == 'i':
            data = input('입력할 데이터==>')
            push(data)
            print('스택 상태: ', stack)

        elif select == 'E' or select == 'e':
            data = pop()
            print('추출된 데이터==>', data)
            print('스택 상태: ', stack)

        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터==>', data)
            print('스택 상태: ', stack)
        
        elif select != 'X' or select != 'x':
            break;

        else:
            print('입력이 잘못됨')
        
        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택==>")

    print('프로그램 종료!')