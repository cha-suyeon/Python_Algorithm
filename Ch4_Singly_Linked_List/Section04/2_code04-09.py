# 단순 연결 리스트를 활용한 명함 관리 프로그램

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSimpleLinkedList(namePhone):    # 이름과 전화번호가 1개씩 들어 있는 배열을 넘겨 받아 단순 연결 리스트 생성
    global memory, head, current, pre
    printNodes(head)                    # 새 노드 추가 전 리스트 상태 출력

    node = Node()                       # 새 노드 생성
    node.data = namePhone               
    memory.append(node)                 # 메모리 공간에 새 노드 넣음
    if head == None:                    # 첫 번째 노드일 때
        head = node                     # 헤드로 지정하고 함수 종료
        return 
    if head.data[0] > namePhone[0]:     # 첫 번째 노드보다 작을 때
        node.link = head                # 새 노드 링크에 첫 번째 노드 지정
        head = node                     # 헤드를 새 노드로 지정
        return

    # 중간 노드로 삽입하는 경우
    current = head
    while current.link != None:
        pre = current                           # 이전 노드를 현재 노드로 변경
        current = current.link                  # 현재 노드는 다음 노드로 변경
        if current.data[0] > namePhone[0]:      # 새 노드가 현재 노드보다 작다면 중간에 삽입하고 종료
            pre.link = node
            node.link = current
            return
    
    # 삽입하는 노드가 가장 큰 경우
    current.link = node             # 마지막 노드보다 새 노드가 큰 경우이므로 새 노드를 마지막 노드로 추가

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = [["지민", "010-1111-1111"], ["정국", "010-2222-2222"], ["뷔", "010-3333-3333"], ["슈가", "010-4444-4444"], ["진", "010-5555-5555"]]

## 메인 코드 부분 ##
if __name__ == "__main__":
    for data in dataArray:
        makeSimpleLinkedList(data)

    printNodes(head)