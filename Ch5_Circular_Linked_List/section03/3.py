# 3. 노드 삽입

## 첫 번째 노드 삽입 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

node = Node()           # 새 노드 생성
node.data = '화사'      # 새 노드에 데이터 입력
node.link = head        # 새 노드의 링크로 head가 가리키는 노드 지정
last = head             # 마지막 노드를 첫 번째 노드로 우선 지정
while 마지막 노드까지:      # 마지막 노드를 찾으면 반복 종료
    last = last.link
last.link = node        # 마지막 노드의 링크에 새 노드 지정
head = node             # 헤드 노드를 새 노드로 지정

## 중간 노드 삽입 ##
current = head
while 마지막 노드까지:
    pre = current                   # 현재 노드를 pre로 지정
    current = current.link          # 현재 노드를 다음 노드로 이동
    if current.data = '사나':       # 현재 노드가 '사나'인지 확인
        node = Node()               # '사나'이면 새 노드 생성
        node.data = '솔라'          # 새 노드에 '솔라' 노드 생성
        node.link = current         # 새 노드 링크를 현재 노드로 지정
        pre.link = node             # 이전 노드의 링크를 새 노드로 지정

## 마지막 노드 삽입 ##
node = Node()
node.data = '문별'
current.link = node     # 새 노드 생성 후 현재(current) 노드의 링크를 새 노드 링크로 지정
node.link = head        # 새 노드의 링크를 head가 가리키는 노드로 지정
