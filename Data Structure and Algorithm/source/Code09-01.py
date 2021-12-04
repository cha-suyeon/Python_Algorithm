## 함수 선언 부분 ##
class Graph() :
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [ [0 for _ in range(size)] for _ in range(size) ]

## 전역 변수 선언 부분 ##
G1, G3 = None, None

## 메인 코드 부분 ##
G1 = Graph(4)
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4) :
	for col in range(4) :
		print(G1.graph[row][col], end=' ')
	print()

G3 = Graph(4)
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('## G3 방향 그래프 ##')
for row in range(4) :
	for col in range(4) :
		print(G3.graph[row][col], end=' ')
	print()
