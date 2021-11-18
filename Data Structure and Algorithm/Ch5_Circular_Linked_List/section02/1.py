# Section02 원형 연결 리스트의 간단 구현
# 1. 노드의 생성과 연결 구현

# 원형 연결 리스트의 구현은 단순 연결 리스트의 구현과 많은 부분이 비슷합니다.

## 노드 생성 ##

class Node():               # 노드라는 데이터형을 만드는 것
    def __init__(self):     # 데이터형을 생성할 때 자동으로 실행되는 부분
        self.data = None    # 데이터와 링크가 저장되는 부분
        self.link = None

node1 = Node()
node1.data = '다현'         # 다현 노드를 생성

node1.link = node1          # 자기 자신과 연결되도록 설정

node2 = Node()              # 두 번째 노드 생성
node1.link = node2          # 첫 번째 노드의 링크에 두 번째 노드를 연결
node2.link = node1          # 두 번째 노드의 링크에는 첫 번째 노드를 연결

# 이렇게 원형 구조가 만들어집니다.




