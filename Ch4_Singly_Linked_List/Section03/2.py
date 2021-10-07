# 2. 배열에 저장된 데이터 입력 과정

## 단순 연결 리스트의 일반 형태 ##
memory = []
head, current, pre = None, None, None

## 데이터 입력 과정 ##
node = Node()
node.data = dataArray[0]    # 첫 번째 노드
head = node
memory.append(node)

pre = node
node = Node()
node.data = data            # 두 번째 이후 노드
preNode.link = node
memory.append(node)