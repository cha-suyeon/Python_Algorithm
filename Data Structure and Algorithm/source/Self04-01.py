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

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData : # 첫 노드가 삭제할 노드일 때
        current = head
        head = head.link
        del(current)
        print("# 첫 노드가 삭제됨 #")
        return

    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            print("# 중간 노드가 삭제됨 #")
            return

    print("# 삭제된 노드가 없음 #")

## 전역 변수 선언부
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드부
if __name__ == "__main__" :

    # 첫번째 노드
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    # 두번째 노드 부터
    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("사나")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)