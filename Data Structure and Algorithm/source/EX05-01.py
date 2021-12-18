import random
import math

## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printStores(start) :
	current = start
	if current == None :
		return

	while current.link != head:
		current = current.link
		x, y = current.data[1:]
		print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))
	print()

def  makeStoreList(store) :
	global memory, head, current, pre

	node = Node()
	node.data = store
	memory.append(node)

	if head == None : # 첫 번째 편의점
		head = node
		node.link = head
		return

	# 새 편의점이 첫 번째 편의점보다 가까우면 첫 편의점으로 만듦
	nodeX, nodeY = node.data[1:]
	nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
	headX, headY = head.data[1:]
	headDist = math.sqrt(headX*headX + headY*headY)

	if headDist > nodeDist :	# 헤드 앞에 삽입
		node.link = head
		last = head
		while last.link != head :
			last = last.link
		last.link = node
		head = node
		return

	current = head		# 중간에 데이터를 넣을 경우
	while current.link != head :
		pre = current
		current = current.link
		currX, currY = current.data[1:]
		currDist = math.sqrt(currX*currX + currY*currY)
		if currDist > nodeDist :
			pre.link = node
			node.link = current
			return

	current.link = node
	node.link = head


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__" :

	storeArray = []
	storeName = 'A'
	for _ in range(10) :
		store = (storeName, random.randint(1, 100), random.randint(1, 100) )
		storeArray.append(store)
		storeName = chr(ord(storeName) + 1)	# 편의점 이름을 A->B->C… 으로 변경

	for store in storeArray :
		makeStoreList(store)

	printStores(head)
