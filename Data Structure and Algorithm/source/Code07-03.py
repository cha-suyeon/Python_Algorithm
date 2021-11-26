def isQueueFull() :
	global SIZE, queue, front, rear
	if (rear == SIZE-1) :
		return True
	else :
		return False

SIZE = 5
queue = ["화사", "솔라", "문별", "휘인", "선미"]
front = -1
rear = 4

print("큐가 꽉 찼는지 여부 ==>", isQueueFull())
