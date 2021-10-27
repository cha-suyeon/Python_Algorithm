# Section 03
# 3. 데이터 추출 과정

# 스택에서 데이터를 추출하는 함수를 만들어 효율적으로 추출할 수 있도록 한다.
# 데이터를 추출하기 전에 먼저 스택에 데이터가 있는지 확인해야 한다.
# 스택에 데이터가 없는데 데이터를 추출하려고 시도할 때는 별도의 조치를 취해야 한다.

# 스택이 비었는지 확인하는 함수

def isStackEmpty():
    global stack, top, SiZE
    if (top == -1):
        return True
    else:
        return False

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1

print("스택이 비었는지 여부 확인==>", isStackEmpty())

# 결괏값: 스택이 비었는지 여부 확인==> True