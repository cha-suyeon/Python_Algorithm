# 4. 단순 연결 리스트의 응용

dataArray = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

head = node
node.link = head
head = node

current = head
while 노드의 끝까지:
    pre = current
    current = current.link
    if 현재노드 > 입력할노드:
        pre.link = node
        node.link = current

current.link = node