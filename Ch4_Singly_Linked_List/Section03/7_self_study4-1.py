# 노드 삭제 함수의 완성

## 단순 연결 리스트의 노드 삭제 함수

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

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:         # 첫 번째 노드 삭제
        current = head
        head = head.link
        del(current)
        print("# 첫 노드가 삭제됨 #")
        return

    current = head                      # 첫 번째 외 노드 삭제
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            print("# 중간 노드가 삭제됨 #")
            return

    else: print("# 삭제된 노드가 없음 #")

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

    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("지효")
    printNodes(head)

    deleteNode("재남")
    printNodes(head)