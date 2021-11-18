# 노드 연결
# 두 번째 정연 노드 생성 후 정연 노드를 첫 번째 노드의 링크로 연결하는 코드

class Node():
    def __init__(self):     # Node라는 데이터형을 만듦
        self.data = None    # 데이터형을 생성할 때 자동으로 실행되는 부분
        self.link = None    # 데이터와 링크가 저장되는 부분

node1 = Node()
node1.data = "다현"
print(node1.data, end=' ')

node2 = Node()
node2.data = "정연"
node1.link = node2      # 첫 번째 노드의 링크에 두 번째 노드를 연결
print(node1.link.data, end=' ')