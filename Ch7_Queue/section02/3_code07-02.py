# Section 02
# 3. 데이터추출: deQueue

# 데이터가 3개 있는 큐에서 데이터를 추출하려면 front를 1 증가시킨 후
# front 위치의 데이터를 밖으로 추출하고 front 위치의 데이터는 None으로 만든다.

queue = ['화사', '솔라', '문별', None, None]    # 테스트용 큐
front = -1
rear = 2

# 데이터 추출 이전의 큐 상태 확인
print("----큐 상태-----")
print('[출구] <---', end = ' ')
for i in range(0, len(queue)):
    print(queue[i], end=' ')
print('<-- [입구]')
print('----------------')

front += 1                      # front 위치를 오른쪽으로 증가
data = queue[front]             # 현재 front 위치의 데이터 추출
queue[front] = None             # front에 None을 넣어서 데이터 삭제
print('deQueue -->', data)      # 추출한 데이터 출력

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
print('----------------')

print("----큐 상태-----")
print('[출구] <---', end = ' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<-- [입구]')
