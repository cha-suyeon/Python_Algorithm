## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start):
	current = start
	if current.link == None :
		return
	print(current.data, end=' ')
	while current.link != start:
		current = current.link
		print(current.data, end=' ')
	print()

def findNode(findData) :
	global memory, head, current, pre

	current = head
	if current.data == findData :
		return current
	while current.link != head :
		current = current.link
		if current.data == findData :
			return current
	return Node()	# 빈 노드 반환

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	node.link = head
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		node.link = head
		memory.append(node)

	printNodes(head)

	fNode = findNode("다현")
	print(fNode.data)

	fNode = findNode("쯔위")
	print(fNode.data)

	fNode = findNode("재남")
	print(fNode.data)
