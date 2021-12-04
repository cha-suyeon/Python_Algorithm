## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
	print(' ', end = ' ')
	for v in range(g.SIZE) :
		print(nameAry[v], end = ' ')
	print()
	for row in range(g.SIZE) :
		print(nameAry[row], end = ' ')
		for col in range(g.SIZE) :
			print("%2d" % g.graph[row][col], end = ' ')
		print()
	print()

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


## 전역 변수 선언 부분 ##
G1 = None
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산' ]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5


## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25

print('## 자전거 도로 건설을 위한 전체 연결도 ##')
printGraph(G1)

# 가중치 간선 목록
edgeAry = []
for i in range(gSize) :
	for k in range(gSize) :
		if G1.graph[i][k] != 0 :
			edgeAry.append([G1.graph[i][k], i, k])

from operator import itemgetter
edgeAry = sorted(edgeAry, key = itemgetter(0), reverse = True)

newAry = []
for i in range(0,len(edgeAry), 2) :
	newAry.append(edgeAry[i])

index = 0
while (len(newAry) > gSize-1) :	# 간선의 개수가 '정점 개수-1'일 때까지 반복
	start = newAry[index][1]
	end = newAry[index][2]
	saveCost = newAry[index][0]

	G1.graph[start][end] = 0
	G1.graph[end][start] = 0

	startYN = findVertex(G1, start)
	endYN = findVertex(G1, end)

	if startYN and endYN :
		del (newAry[index])
	else :
		G1.graph[start][end] = saveCost
		G1.graph[end][start] = saveCost
		index += 1

print('## 최소 비용의 자전거 도로 연결도 ##')
printGraph(G1)
