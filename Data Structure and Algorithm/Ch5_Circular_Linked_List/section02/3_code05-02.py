# 3. 노드 삽입

class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()
node1.data = '다현'
node1.link = node1

node2 = Node()
node2.data = '정연'
node1.link = node2
node2.link = node1

node3 = Node()
node3.data = '쯔위'
node2.link = node3
node3.link = node1

node4 = Node()
node4.data = '사나'
node3.link = node4
node4.link = node1

node5 = Node()
node5.data = '지효'
node4.link = node5
node5.link = node1

newNode = Node()
newNode.data = '재남'
newNode.link = node2.link       # 새 노드의 링크에 정연 노드(node2)의 링크를 복사한다. 즉, 쯔위를 가리키게 됨
node2.link = newNode            # 정연 노드(node2)의 링크에 새 노드를 지정한다.

current = node1
print(current.data, end=' ')
while current.link != node1:
    current = current.link
    print(current.data, end=' ')