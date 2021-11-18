# Section 03
# 응용
# isQueueEmpty() 함수를 없애고, 대신에 deQueue() 함수 안으로 모든 기능 구현

def deQueue():
    global SIZE, queue, front, rear
    if (front == rear):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]         # 큐에서는 데이터 추출이 앞에서부터 추출이 되기 때문에
    queue[front] = None         # 추출한 데이터를 data에 저장하고 front 위치는 None 값으로 변경
    rear = 0
    return data
    
SIZE = 5
queue = ['화사', None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print('추출한 데이터==>', retData)
print(queue)
retData = deQueue
