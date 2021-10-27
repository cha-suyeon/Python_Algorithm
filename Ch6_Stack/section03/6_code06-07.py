# Section 03
# 4. 데이터 확인

# 데이터를 pop하면 해당 데이터를 스택에서 ㅊ출해서 삭제하고 top 위치는 한 칸 내려간다.
# top 위치의 데이터를 확인만 하고 스택에 그대로 두는 것을 peek이라 한다.
# top 위치의 꿀물을 확인만 한 후 top 값은 변경 없이 그대로 두는 것

def isStackEmpty():
    global SIZE, stack, top
    if (top==-1):
        return True
    else:
        return False

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print("스택이 비었습니다")
        return None
    return stack[top]

SIZE = 5
stack = ['커피', '녹차', '꿀물', None, None]
top = 2

print(stack)
retData = peek()
print('top의 데이터 확인-->', retData)
print(stack)
