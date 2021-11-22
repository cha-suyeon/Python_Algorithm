class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

current = node1
print(current.data, end = ' ')
while current.link != None :
	 current = current.link
	 print(current.data, end = ' ')
