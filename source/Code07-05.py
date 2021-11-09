def isQueueEmpty() :
	global SIZE, queue, front, rear
	if (front == rear) :
		return True
	else :
		return False

SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear = -1

print("큐가 비었는지 여부 ==>", isQueueEmpty())
