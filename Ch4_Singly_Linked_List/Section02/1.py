# 노드 생성

class Node():
    def __init__(self):     # Node라는 데이터형을 만듦
        self.data = None    # 데이터형을 생성할 때 자동으로 실행되는 부분
        self.link = None    # 데이터와 링크가 저장되는 부분

node1 = Node()
node1.data = "다현"
print(node1.data, end=' ')