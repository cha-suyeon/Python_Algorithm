import random

## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end=' ')
	while current.link != None:
		current = current.link
		print(current.data, end=' ')
	print()

def makeLottoList(num) :
	global memory, head, current, pre

	node = Node()
	node.data = num
	memory.append(node)
	if head == None :		# 첫 번째 노드
		head = node
		return

	if head.data > num :
		node.link = head
		head = node
		return

	current = head
	while current.link != None :
		pre = current
		current = current.link
		if current.data > num:
			pre.link = node
			node.link = current
			return

	current.link = node

def  findNumber(num) :
	global memory, head, current, pre

	if head == None :
		return False
	current = head
	if current.data == num:
		return True
	while current.link != None:
		current = current.link
		if current.data == num:
			return True
	return False

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__" :

	lottoCount = 0
	while True:
		lotto = random.randint(1,45)
		if findNumber(lotto) :
			continue
		lottoCount += 1
		makeLottoList(lotto)
		if lottoCount >= 6 :
			break

	printNodes(head)
