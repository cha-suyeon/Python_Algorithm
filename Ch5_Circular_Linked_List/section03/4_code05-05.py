# 원형 연결 리스트의 노드 삽입 함수

## 클래스와 함수 선언 부분 ## 
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:        # 현재 노드의 링크가 전달 받은 노드(첫 번째 노드)가 아닐 때까지 반복
        current = current.link          # 원형연결 리스트에서는 현재 노드의 링크가 첫 번째 노드라면 마지막 노드를 의미한다.
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):       # 첫 번째 노드 삽입
    global memory, head, current, pre      

    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        last = head                         # 마지막 노드를 첫 번째 노드로 우선 지정
        while last.link != head:            # 마지막 노드의 링크가 head가 아닐 때 -> 마지막 노드를 찾으면 반복 종료
            last = last.link                # last를 다음 노드로 변경
        last.link = node                    # 마지막 노드의 링크에서 새 노드 지정
        head = node
        return

    current = head
    while current.link != head:             # 중간 노드 삽입
        pre = current
        current = current.link
        if current.link == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
        
    node = Node()                           # 마지막 노드 삽입 -> 찾을 데이터가 없는 경우(while문이 종료되고)
    node.data = insertData
    current.link = node                     # 새 노드 생성 후 현재(current) 노드 링크를 새 노드로 지정
    node.link = head                        # 새 노드의 링크를 head로 지정(새 노드가 마지막 노드가 됨!)

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드 부분 ##
if __name__ == '__main__':

    node = Node()
    node.data = dataArray[0]        # 첫 번째 노드
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNode(head)

## 코드가 잘 실행되는지 확인 ##

    insertNode('다현', '화사')
    printNode(head)

    insertNode('사나', '솔라')
    printNode(head)

    insertNode('수연', '문별')
    printNode(head)

## 실행 결과 ##
# 다현 정연 쯔위 사나 지효 
# 화사 다현 정연 쯔위 사나 지효 
# 화사 다현 정연 쯔위 사나 지효 솔라
# 화사 다현 정연 쯔위 사나 지효 솔라 문별