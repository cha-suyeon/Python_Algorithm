# 노드 삽입

## 첫 번째 노드 삽입 ##
node = Node()
node.data = "화사"
node.link = head
head = node

## 중간 노드 삽입 ##
current = head
while 마지막 노드까지:
    pre = current
    current = current.link
    if current.data == "사나":      # 현재 노드가 "사나"라면
        node = Node()               # 새 노드(솔라 노드)를 생성한 후
        node.data = "솔라"
        node.link - current         # 이전 노드의 링크를 새 노드의 링크로 지정
        pre.link = node             # 이전 노드의 링크를 새 노드로 지정

## 마지막 노드 삽입 ##
node = Node()
node.data = "문별"
current.link = node
