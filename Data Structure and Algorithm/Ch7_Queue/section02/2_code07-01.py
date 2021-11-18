# Section 02
# 2. 데이터삽입: enQueue

# 생성한 큐에 화사를 넣으려면 우선 rear를 1 증가 시킨 뒤, rear 위치에 데이터를 넣는다.

queue = [None, None, None, None, None]  # 크기가 5인 빈 큐 준비
front = rear = -1                       # 초깃값 설정

rear += 1               # rear를 1 증가 시키며 데이터 삽입
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'

print('-----큐 상태-----')
print('[출구]<--', end = ' ')
for i in range(0, len(queue), 1):
    print(queue[i], end=' ')
print('<--[입구]')