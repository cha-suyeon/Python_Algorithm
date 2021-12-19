## 함수 선언 부분 ##
def isQueueFull() :
	global SIZE, queue, front, rear
	if ( (rear + 1) % SIZE == front) :
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
	rear = (rear + 1) % SIZE
	queue[rear] = data

def deQueue() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	front = (front + 1) % SIZE
	data = queue[front]
	queue[front] = None
	return data

def peek() :
	global SIZE, queue, front, rear
	if (isQueueEmpty()) :
		print("큐가 비었습니다.")
		return None
	return queue[(front + 1) % SIZE]

def calcTime() :
	global SIZE, queue, front, rear
	timeSum = 0
	for i in range((front+1)% SIZE, (rear+1)%SIZE) :
		timeSum += queue[i][1]
	return timeSum

## 전역 변수 선언 부분 ##
SIZE = 6
queue = [ None for _ in range(SIZE) ]
front = rear = 0

## 메인 코드 부분 ##
if __name__ == "__main__" :
	waitCall = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

	for call in waitCall :
		print("귀하의 대기 예상시간은 ", calcTime(), "분입니다.")
		print("현재 대기 콜 --> ", queue)
		enQueue(call)
		print()

	print("최종 대기 콜 --> ", queue)
	print("프로그램 종료!")
