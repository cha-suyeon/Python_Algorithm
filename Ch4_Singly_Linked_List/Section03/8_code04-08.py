# 노드 검색
# 단순 연결 리스트의 노드 검색 함수


## 클래스와 함수 선언 부분 ##
class Node():
    def __init__ (self):
        self.data = None
        self.link = None

def printNode(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def findNode(findData):
    global memory, head, current, pre

    current = head
    if current.data == findData:
        return current
    while current.link != None:
        current = current.link
        if current.data == findData:
            return current
    return Node()       # 빈 노드 반환


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

    printNode(head)                    # 생성이 완료된 단순 연결 리스트 출력

    fNode = findNode("다현")
    print(fNode.data)

    fNode = findNode("쯔위")
    print(fNode.data)

    fNode = findNode("재남")
    print(fNode.data)