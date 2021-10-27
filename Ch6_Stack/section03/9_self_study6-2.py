# code06-06의 isStackEmpty() 함수를 없애고, 대신에 pop() 함수만으로 그 기능을 구현하자

# 실행 결과는 아래와 같음
# ['커피', None, None, None, None]
# 추출한 데이터--> 커피
# [None, None, None, None, None]
# 스택이 비었습니다.

def pop():
    global SIZE, stack, top
    if (top==-1):
        print("스택이 비었습니다.")
        return

    data = stack[top]
    stack[top] = None
    top -= 1
    return data

SIZE = 5
stack = ['커피', None, None, None, None]
top = 0

print(stack)
retData = pop()
print('추출한 데이터-->', retData)
print(stack)
retData = pop()