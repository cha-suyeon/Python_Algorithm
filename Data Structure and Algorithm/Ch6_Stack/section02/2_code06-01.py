# 2. 데이터 삽입: push
# 생성한 스택에 데이터를 넣으려면 top을 1 증가시킨 후 데이터를 넣는다.

## 크기가 5칸인 스택의 생성과 데이터 3개 입력 ##
stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'     # top을 1씩 증가시키고, 해당 위치에 데이터를 삽입하는 과정

print('------스택 상태------')
for i in range(len(stack)-1, -1, -1):
    print(stack[i])


# len(stack)-1은 스택의 맨 위쪽부터 -1씩 감소하면서 출력한다
# 즉, 4,3,2,1,0번째 데이터가 출력된다.