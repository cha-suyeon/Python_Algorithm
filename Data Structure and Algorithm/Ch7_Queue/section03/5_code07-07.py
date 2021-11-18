# Section 03
# 4. 데이터 확인

def isQueueEmpty():
    global SIZE, queue, rear, front
    if (front == rear):
        return True
    else:
        return False
    
def peek():
    global SIZE, queue, rear, front
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    return queue[front+1]

SIZE = 5
queue = ['화사', '솔라', '문별', None, None]
front = -1
rear = 2

print(queue)
retData = peek()
print('다음에 추출될 데이터 확인-->', retData)
print(queue)