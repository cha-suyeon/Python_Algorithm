# 유명 맛집의 대기줄 구현하기
# 1. 유명 맛집의 대기줄에는 손님들이 들어온 순서대로 줄을 선다.
# 2. 대기줄이 꽉 차면 더 이상 손님을 받지 않는다.
# 3. 대기줄 자리가 생기면 1명씩 식당으로 들어간다.
# 4. 맨 앞쪽 손님이 대기줄에서 식당으로 들어갈 때마다 대기줄 뒤쪽 손님들은 한 칸씩 이동해서 줄을 다시 서도록 한다.

def isQueueFull():                      # 큐가 꽉 찼는지 확인하는 함수 개선 버전
    global SIZE, queue, front, rear
    if (rear != SIZE-1):
        return False
    elif (rear == SIZE-1) and (front == -1):
        return True
    else:
        return False
    
def isQueueEmpty():                     # 큐가 비었는지 체크하는 함수
    global SIZE, queue, rear, front
    if (front == rear):
        return True
    else:
        return False
    
def enQueue(data):                      # 큐에 데이터를 삽입하는 함수
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data
    
def deQueue():                          # 큐에서 데이터를 추출하는 함수
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None     
    
    for i in range(front+1, SIZE):      # 모든 사람을 한 칸씩 앞으로 당긴다.
        queue[i-1] = queue[i]
        queue[i] = None
    front -= 1
    rear -= 1

    return data

def peek():                             # 큐에서 front+1 위치의 데이터를 확인하는 함수
    global SIZE, queue, rear, front
    if (isQueueEmpty()):
        print('큐가 비었습니다.')
        return None
    return queue[front+1]

## 전역 변수 선언 부분 ##
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인 코드 부분 ##
if __name__ == "__main__":
    enQueue('화사')
    enQueue('문별')
    enQueue('솔라')
    enQueue('휘인')
    enQueue('수연')
    print("대기 줄 상태: ", queue)

    for _ in range(rear+1):
        print(deQueue(), '님 식당에 들어감')
        print('대기 줄 상태: ', queue)
    
    print('식당 영업 종료!')