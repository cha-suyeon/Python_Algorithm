# Section 03
# 큐가 꽉 찼는지 확인하는 함수 개선 버전

# 문제점: deQueue 후에 앞에 여유 공간이 생겨도 데이터가 삽입되지 않는다.

# rear != 큐 크기 -1인 경우: 큐가 가득차지 않음 -> False 반환
# rear = 큐 크기-1, front = -1인 경우: 큐가 가득참 -> True 반환
# rear = 큐 크기-1, front != -1인 경우 -> 큐가 가득차지 않음 -> False 반환

## 해결 방법 ##
# 1. front+1 위치부터 rear 위치까지 왼쪽으로 한 칸씩 이동시킨다.
# 2. front 값에서 1을 뺀다.
# 3. rear 값에서 1을 뺀다.
# 4. 큐가 꽉 차지 않았다는 의미의 false를 반환한다.

def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    
SIZE = 5
queue = [None, None, '문별', '휘인', '선미']
front = 1
rear = 4

print('큐가 꽉 찼는지 여부-->', isQueueFull())
print('큐 상태-->', queue)
