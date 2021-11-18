# 2. 응용예제02 이중 연결 리스트 구현하기

# Doubly linked list (이중 연결 리스트)

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None

def printNodes(start):                  
    current = start
    if current == None:
        return
    print('정방향 -->', current.data, end=' ')        
    while current.next != None:
        current = current.next
        print(current.data, end=' ')
    print()
    print('역방향 -->', current.data, end=' ')        
    while current.prev != None:
        current = current.prev
        print(current.data, end=' ')
    print()


    
## 전역 변수 선언 부분 ##
memory = []                             # 생성할 노드 저장할 메모리 준비
head, current, pre = None, None, None   # 시작 노드, 현재 노드, 이전 노드에 사용할 변수 준비
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]            # 첫 번째 노드 생성
    head = node
    memory.append(node)

    for data in dataArray[1:]:          # 두 번째 이후 노드
        pre = node                      # 현재 노드를 이전 노드로 저장함
        node = Node()                   # 새 노드 생성
        node.data = data                # 노드에 데이터를 넣음
        pre.next = node                 # 이전 노드 링크에 다음 노드 대입
        node.prev = pre                 # 노드의 prev란 링크에 이전 노드를 대입시켜줘서 이전 노드로 이동하게 만들어준다.
        memory.append(node)             # 새 노드를 메모리에 넣음

    printNodes(head)                    # 생성이 완료된 단순 연결 리스트 출력