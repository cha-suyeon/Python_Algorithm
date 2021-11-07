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

def deleteNode(deleteData) :
	global memory, head, current, pre

	if head.data == deleteData :		# 첫 번째 노드 삭제
		current = head
		head = head.link
		last = head
		while last.link != current:		# 마지막 노드를 찾으면 반복 종료
			last = last.link		# last를 다음 노드로 변경
		last.link = head			# 마지막 노드의 링크에 head가 가리키는 노드 지정
		del(current)
		return

	current = head	                        	# 첫 번째 외 노드 삭제
	while current.link != head :
		pre = current
		current = current.link
		if current.data == deleteData :  	# 중간 노드를 찾았을 때
			pre.link = current.link
			del(current)
			return

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

	deleteNode("다현")
	printNodes(head)

	deleteNode("쯔위")
	printNodes(head)

	deleteNode("지효")
	printNodes(head)

	deleteNode("재남")
	printNodes(head)
