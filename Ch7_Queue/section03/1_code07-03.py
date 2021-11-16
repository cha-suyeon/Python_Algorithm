# Section 03
# 2. 데이터 삽입 과정

# 삽입할 때는 큐가 이미 꽉 찼는지 확인해야 한다.
# 큐의 사이즈가 5이고, 데이터가 5개라면 rear가 4여야 한다.

## 큐가 꽉 찼는지 확인하는 함수 ##
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear == SIZE-1):
        return True
    else:
        return False
    
SIZE = 5
queue = ['화사', '솔라', '문별', '휘인', '선미']
front = -1
rear = 4

print("큐가 꽉 찼는지 여부 ==>", isQueueFull())

