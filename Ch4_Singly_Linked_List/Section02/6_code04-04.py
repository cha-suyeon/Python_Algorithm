# 노드 삭제

class Node():
    def __init__(self):
        self.data = None
        self.link = None

node1 = Node()          # 첫 번째 노드 생성
node1.data = "다현"     # 다현 입력

node2 = Node()          # 두 번째 노드 생성
node2.data = "정연"     # 정연 입력
node1.link = node2      # 첫 번째 노드의 링크에 두 번째 노드 입력하여 두 노드 연결

node3 = Node()          # 세 번째 노드 생성
node3.data = "쯔위"     # ... 반복
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

node2.link = node3.link     # 쯔위의 링크를 정연의 링크로 복사
del(node3)                  # 쯔위 삭제

current = node1
print(current.data, end=' ')
while current.link != None:
    current = current.link
    print(current.data, end=' ')