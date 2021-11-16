# Section 03
# 큐가 비었는지 확인하고, 데이터가 있다면 데이터를 추출하도록 코드 작성
## 큐에서 데이터를 추출하는 함수 ##

def isQueueEmpty():
    global SIZE, queue, rear, front
    if (front == rear):
        return True
    else:
        return False
    
def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]         # 큐에서는 데이터 추출이 앞에서부터 추출이 되기 때문에
    queue[front] = None         # 추출한 데이터를 data에 저장하고 front 위치는 None 값으로 변경
    rear = 0
    
SIZE = 5
queue = ['화사', None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue
print('추출한 데이터==>', retData)
print(queue)
retData = deQueue
