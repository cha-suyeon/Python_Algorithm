# 노드 삭제

## 첫 번째 노드 삭제
current = head
head = head.link
del(current)

## 첫 번째 외 노드 삭제
current = head
while 마지막 노드까지:
    pre = current
    current = current.link
    if cuurent.data == "쯔위":
        pre.link = current.link
    del(current)
    