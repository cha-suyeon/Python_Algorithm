## 클래스 및 함수 선언부 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current.link == None :
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData :
        print("# 첫 노드에서 찾음 #")
        return current
    while current.link != head :
        current = current.link
        if current.data == findData :
            print("# 중간 노드에서 찾음 #")
            return current
    print("# 찾는 노드가 없음 #")
    return Node() # 빈 노드 반환

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
    node.link = head
    memory.append(node)

    # 두번째 노드 부터
    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    fNode = findNode("다현")
    print(fNode.data)

    fNode = findNode("쯔위")
    print(fNode.data)

    fNode = findNode("재남")
    print(fNode.data)