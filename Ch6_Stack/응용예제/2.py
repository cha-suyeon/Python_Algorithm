# Chapter 06. Stack - 응용예제 2번

## 코드 설명 ##

# 스택 크기를 100으로 설정해서 텍스트 파일을 최대 100행으로 제한한다.
# 진달래꽃.txt 파일을 열어 lineAry 배열에 각 행별로 문자열을 저장한다.
# readlines - 한꺼번에 읽어 배열에 넣음
# lineAry는 ['진달래꽃\n', '나 보기가 역겨워\n', '가실 때에는\n', '말없이 고이 보내드리오리다.']
# 또한, 소스 코드가 있는 폴더에는 진달래꽃.txt 파일이 들어 있어야 한다.
# 각 행을 스택에 삽입하고 원본 형태 그대로 출력한다.
# 스택에서 글자를 추출한 후 각 행별로 다시 별도의 스택에 삽입하고, 추출해서 문자를 거꾸로 만들어 출력한다.
# 원래 순서의 반대 순서로 행이 추출된다.
# 별도의 스택을 각 행의 글자 수로 크기를 지정해서 준비한다.
# 별도의 스택에 각 글자를 삽입한다.
# 별도의 스택에서 글자를 삽입한 순서와 반대로, 즉 마지막 행부터 글자 순서도 반대로 출력한다.

## 예제 설명 ##
# 텍스트 파일에서 전체 줄을 거꾸로 하고, 각 줄의 글자도 거꾸로 출력하는 프로그램을 작성한다.
# 다음은 네 줄짜리 파일을 처리한 결과이다. (줄바꿈이 있음)
# '진달래꽃 ... 말없이 고이 보내드리오리다.' -> ' .다리오리드내보 이고 이없말 ... 꽃래달진'


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
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1


## 메인 코드 부분 ##
if __name__ == "__main__":

    with open('C:/Users/chasu/OneDrive/바탕 화면/Python_Algorithm/Ch6_Stack/응용예제/진달래꽃.txt', 'r', encoding='UTF8') as rfp:
        lineAry = rfp.readlines()

    print("-----원본-----")
    for line in lineAry:
        push(line)
        print(line, end=' ')
    print()

    print("-----거꾸로 처리된 결과-----")
    while True:
        line = pop()
        if line == None:
            break

        miniStack = [None for _ in range(len(line))]
        miniTop = -1

        for ch in line:
            miniTop += 1
            miniStack[miniTop] = ch
        
        while True:
            if miniTop == -1:
                break
            ch = miniStack[miniTop]
            miniTop = -1
            print(ch, end=' ')
