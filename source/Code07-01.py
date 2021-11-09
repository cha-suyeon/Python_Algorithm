queue = [None, None, None, None, None]
front = rear = -1

rear += 1
queue[rear] = "화사"
rear += 1
queue[rear] = "솔라"
rear += 1
queue[rear] = "문별"

print("----- 큐 상태 -----")
print ( '[출구] <-- ', end='')
for i in range(0, len(queue), 1) :
	print(queue[i], end=' ')
print ( '<-- [입구] ')
