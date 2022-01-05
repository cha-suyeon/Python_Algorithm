## 클래스 및 함수 선언부 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSimpleLinkedList(nameAge) :
    global memory, head, current, pre
    printNodes(head)

    node = Node()
    node.data = nameAge
    memory.append(node)
    if head == None : # 첫 노드
        head = node
        return

    if head.data[1] > nameAge[1] : # 첫 노드 보다 작을 때
        node.link = head
        head = node
        return

    # 중간 노드에 삽입하는 경우
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data[1] > nameAge[1]:
            pre.link = node
            node.link = current
            return

    # 입력하는 노드가 제일 큰 경우
    current.link = node

## 전역 변수 선언부
memory = []
head, current, pre = None, None, None
dataArray = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]

## 메인 코드부
if __name__ == "__main__" :

    for data in dataArray :
        makeSimpleLinkedList(data)

    printNodes(head)