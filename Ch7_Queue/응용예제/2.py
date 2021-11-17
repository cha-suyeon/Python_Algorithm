# 콜센터의 응답 대기 시간 계산하기
# 1. 9시에 영업을 시작하고, 전화 문의가 여러 건 대기하고 있다.
# 2. 전화 문의는 주제에 따라 통화 시간이 다름
# 3. 고장 수리 3분, 사용 문의 9분, 환불 문의 4분, 기타 문의 1분
# 4. 9시 이전에 고객이 전화를 하면 9시에 업무를 개시한 후 대기 시간을 알려준다.

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