# Section 03
# 3. 데이터 추출 과정

## 큐가 비었는지 체크하는 함수 ##
def isQueueEmpty():
    global SIZE, queue, rear, front
    if (front == rear):
        return True
    else:
        return False
    
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

print('큐가 비었는지 여부 ==>', isQueueEmpty())