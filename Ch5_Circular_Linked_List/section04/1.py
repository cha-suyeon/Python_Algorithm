# 1. 입력할 데이터를 랜덤하게 7개 발생시켜 dataArray 배열에 저장한다
import random

dataArray = []
for _in range(7):
    dataArray.append(random.randint(1,100))

# 2. 데이터를 차례대로 가져와 원형 연결 리스트를 만든다.
# dataArray 배열에서 원형 연결 리스트를 생성하는 코드는 code05-04와 동일

node = Node()
node.data = dataArray[0]
head = node
node.link = head
memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    ode.data = data
    pre.link = node
    node.link = head
    memory.append(node)

# 3. 원형 연결 리스트 전체를 1회 방문하면서 홀쑤와 짝수의 개수를 센다
current = head
while True:
    if current.data가 짝수면:
        짝수개수 += 1
    else:
        홀수개수 += 1
    if current.link == head:
        break;
    current = current.link

# 4. 짝수 또는 홀수의 개수 중 많은 쪽 숫자를 음수로 만든다.
if 홀수개수 > 짝수개수:
    나머지값 = 1
else:
    나머지값 = 0

current = head
while True:
    if current.data % 2 == 나머지값:
        current.data *= -1
    if current.link == head:
        break;
    current = current.link