## 함수 선언 부분 ##
def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

def enQueue(data) :
	global SIZE, queue, front, rear
	if (isQueueFull()) :
		print("큐가 꽉 찼습니다.")
		return
	rear += 1
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front += 1
	data = queue[front]
	queue[front] = None

	for i in range(front + 1, rear + 1): 	# 모든 사람을 한칸씩 앞으로 당긴다.
		queue[i - 1] = queue[i]
		queue[i] = None
	front = -1
	rear -= 1

	return data

def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[front+1]

## 전역 변수 선언 부분 ##
SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :
	enQueue('정국')
	enQueue('뷔')
	enQueue('지민')
	enQueue('진')
	enQueue('슈가')
	print("대기 줄 상태 : ", queue)

	for _ in range(rear+1) :
		print(deQueue(), '님 식당에 들어감')
		print("대기 줄 상태 : ", queue)

	print("식당 영업 종료!")
