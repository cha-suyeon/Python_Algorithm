# Section03 원형 연결 리스트의 일반 구현
# 1. 원형 연결 리스트의 일반 형태

# 메모리의 크기는 무한대이고, 노드는 링크로 연결된다.
# 세 가지 변수 사용 - 첫 번째 노드 head, 현재 노드 current, 이전 노드 pre

memory = []
head, current, pre = None, None, None

# 2. 배열에 저장된 데이터 입력 과정
## 데이터 입력 과정

# 사용자가 데이터를 입력하면 첫 번째 노드이므로 헤드는 첫 번째 노드를 가리킨다.
# 새 노드의 링크는 헤드가 가리키는 노드로 연결한다
# 연결 노드가 첫 번째 노드이므로 결국 자신을 가리키는 형태가 된다
# 완성된 노드를 메모리 공간에 넣는다

class Node():
    def __init__(self):
        self.data = None
        self.link = None

node = Node()
node.data = dataArray[0]
head = node
node.link = head
memory.append(node)

# 두 번째 이후의 데이터는 새 노드를 기존 노드의 링크에 저장하기 전, 기존 노드를 저장한 후 생성해야 함
# 새 노드의 링크에 헤드가 가리키는 노드를 연결함으로써 원형 연결 리스트의 구조를 유지한다
# 새 노드를 메모리에 넣는다.

pre = node
node = Node()
node.data = data
pre.link = node
node.link = head
memory.append(node)
