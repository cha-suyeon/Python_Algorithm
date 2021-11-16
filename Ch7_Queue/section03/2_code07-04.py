# Section 03

# 앞서 생성한 isQueueFull() 함수를 사용해서 먼저 큐가 꽉 찼는지 확인
# 여유가 있다면 데이터 삽입하도록 코드 작성

## 큐에 데이터를 삽입하는 함수 ##
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1):
        return True
    else:
        return False
    
def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', None]
front = -1
rear = 3

print(queue)
enQueue('선미')
print(queue)
enQueue('수연')