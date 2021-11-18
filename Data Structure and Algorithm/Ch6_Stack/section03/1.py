# Section 03
# 1. 스택 초기화

stack = [None, None, None, None, None]

# 5개로 제한된 스택을 구현하는 방법이지만, 큰 스택에 일일히 None 값을 넣어줄 수는 없다.
# 그래서 SIZE 값만 변경하면 원하는 크기의 빈 스택이 생성되는 스택 초기화가 필요하다.

SIZE = 5 
stack = [None for _ in range(SIZE)]
top = -1
