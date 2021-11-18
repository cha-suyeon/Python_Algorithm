# 4. 노드 삭제

## 첫 번째 노드 삭제 ##
current = head                  # 현재 노드를 삭제할 노드 head로 지정
head = head.link                # head를 삭제할 노드의 링크가 가리키던 노드로 변경된다.
last = head
while last.link != current:     # 마지막 노드를 찾으면 반복 종료
    last = last.link            # last를 다음 노드로 변경
last.link = head                # 마지막 노드의 링크에 head가 가리키는 노드 지정
del(current)


## 첫 번째 노드 외 삭제 ## 
current = head
while current.link != head:
    pre = current                   # 현재 노드를 이전 노드(pre)로 지정
    current = current.link          # 현재 노드를 다음 노드로 이동
    if current.data == '쯔위':      # 현재 노드가 쯔위라면
        pre.link = current.link     # 이전 노드의 링크를 현재 노드의링크로 지정
        del(current)                # 현재 노드를 메모리에서 삭제