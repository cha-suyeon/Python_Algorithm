# Section 03
# 2. 데이터 삽입 과정

# 스택이 꽉 찼는지 확인하는 함수가 필요하다.
# top 값이 스택 크기 - 1 했을 때 값과 같다면 스택이 꽉 찬 상황이다.

def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False
    
SIZE = 5
stack = ['커피', '녹차', '꿀물', '콜라', '환타']
top = 4

print("스택이 꽉 찼는지 여부==>", isStackFull())

# 결괏값: 스택이 꽉 찼는지 여부==> True
# 스택이 꽉 찼는지 여부를 확인하는 테스트 함수