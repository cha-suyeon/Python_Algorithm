gSize  = 6
def findVertex(g, findVtx) :
	stack = []
	visitedAry = []	# 방문한 노드

	current = 0	# 시작 정점
	stack.append(current)
	visitedAry.append(current)

	while (len(stack) != 0) :
		next = None
		for vertex in range(gSize) :
			if g.graph[current][vertex] != 0 :
				if vertex in visitedAry :	# 방문한 적이 있는 정점이면 탈락
					pass
				else :			# 방문한 적이 없으면 다음 정점으로 지정
					next = vertex
					break

		if next != None :				# 다음에 방문할 정점이 있는 경우
			current = next
			stack.append(current)
			visitedAry.append(current)
		else :					# 다음에 방문할 정점이 없는 경우
			current = stack.pop()

	if findVtx in visitedAry :
		return True
	else :
		return False
