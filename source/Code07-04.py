def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
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

SIZE = 5
queue = ["화사", "솔라", "문별", "휘인", None]
front = -1
rear = 3

print(queue)
enQueue("선미")
print(queue)
enQueue("재남")
