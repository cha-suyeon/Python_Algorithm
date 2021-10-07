# 단순 연결 리스트의 노드 삽입 함수

# 노드 삽입 함수의 완성!

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):                  # 매개변수로 시작 노드를 전달 받음
    current = start                     # 전달 받은 시작 노드를 현재 노드로 지정
    if current == None:                 # 노드에 데이터가 하나도 없는 연결 리스트인 경우 반환
        return
    print(current.data, end=' ')        # 현재 노드 출력
    while current.link != None:         # 노드의 링크가 빌 때까지 출력
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):   # 매개 변수로 삽입할 위치를 찾을 데이터(findData), 삽입할 데이터(insertData)를 넘겨 받는다.
    global memory, head, current, pre

    if head.data == findData :          # 첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None :        # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    
    node = Node()                       # 마지막 노드 삽입
    node.data = insertData
    current.link = node


## 전역 변수 선언 부분 ##
memory = []                             # 생성할 노드 저장할 메모리 준비
head, current, pre = None, None, None   # 시작 노드, 현재 노드, 이전 노드에 사용할 변수 준비
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드 선언 부분 ##
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]            # 첫 번째 노드 생성
    head = node
    memory.append(node)

    for data in dataArray[1:]:          # 두 번째 이후 노드
        pre = node                      # 현재 노드를 이전 노드로 저장함
        node = Node()                   # 새 노드 생성
        node.data = data                # 노드에 데이터를 넣음
        pre.link = node                 # 이전 노드 링크에 새 노드 대입
        memory.append(node)             # 새 노드를 메모리에 넣음

    printNodes(head)                    # 생성이 완료된 단순 연결 리스트 출력

    insertNode("다현", "화사")
    printNodes(head)

    insertNode("사나", "솔라")
    printNodes(head)

    insertNode("재남", "문별")
    printNodes(head)