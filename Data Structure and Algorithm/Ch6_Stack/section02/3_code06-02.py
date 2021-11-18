# 3. 데이터 추출: pop
# 데이터가 3개 있는 스택에서 데이터를 추출하려면 top 위치의 데이터를 밖으로 추출한 후, top의 위치 데이터는 None으로 만들고 top을 1씩 감소시킨다.

## 스택에서 데이터 3개 추출 ##
stack = ['커피', '녹차', '꿀물', None, None]
top = 2

print('------스택 상태------')
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

print('---------------------')
data = stack[top]                   # 현재 top 위치의 데이터를 추출
stack[top] = None                   # top 위치에 None을 대입해서 데이터 삭제
top -= -1                           # top을 1 감소 시킴
print('pop--->', data)              # 추출한 데이터를 출력

data = stack[top]
stack[top] = None
top -= -1
print('pop--->', data)

data = stack[top]
stack[top] = None
top -= -1
print('pop--->', data)
print('---------------------')

print('------스택 상태------')
for i in range(len(stack)-1, -1, -1):
    print(stack[i])


## 결괏값 ##
# ------스택 상태------
# None
# None
# 꿀물
# 녹차
# 커피
# ---------------------
# pop---> 꿀물
# pop---> None
# pop---> None
# ---------------------
# ------스택 상태------
# None
# None
# None
# 녹차
# 커피