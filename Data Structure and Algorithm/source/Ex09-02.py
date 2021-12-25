## 클래스 및 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

def printGraph(g) :
	print(' ', end = ' ')
	for v in range(g.SIZE) :
		print(cityAry[v], end = ' ')
	print()
	for row in range(g.SIZE) :
		print(cityAry[row], end =' ')
		for col in range(g.SIZE) :
			print("%2d" % g.graph[row][col], end = ' ')
		print()
	print()

def findVertex(g, findVtx) :
	stack = []
	visitedAry = []

	current = 0
	stack.append(current)
	visitedAry.append(current)

	while (len(stack) != 0) :
		next = None
		for vertex in range(gSize) :
			if g.graph[current][vertex] != 0 :
				if vertex in visitedAry :
					pass
				else :
					next = vertex
					break

		if next != None :
			current = next
			stack.append(current)
			visitedAry.append(current)
		else :
			current = stack.pop()

	if findVtx in visitedAry :
		return True
	else :
		return False

## 전역 변수 선언 부분 ##
G1 = None
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리' ]
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5


## 메인 코드 부분 ##
gSize = 6
G1 = Graph(gSize)
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][북경] = 50; G1.graph[방콕][런던] = 30; G1.graph[방콕][파리] = 20
G1.graph[파리][방콕] = 20; G1.graph[파리][런던] = 60;


print('## 해저 케이블 연결을 위한 전체 연결도 ##')
printGraph(G1)

# 가중치 간선 목록
edgeAry = []
for i in range(gSize) :
	for k in range(gSize) :
		if G1.graph[i][k] != 0 :
			edgeAry.append([G1.graph[i][k], i, k])

from operator import  itemgetter
edgeAry = sorted(edgeAry, key = itemgetter(0), reverse=False)

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

print('## 가장 효율적인 해저 케이블 연결도 ##')
printGraph(G1)
