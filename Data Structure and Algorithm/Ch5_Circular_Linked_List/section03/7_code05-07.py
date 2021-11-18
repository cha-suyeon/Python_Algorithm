# 5. 노드 검색
# 완성된 원형 연결 리스트에서 노드를 검색하는 방식을 구현해보자
# 검색할 데이터의 노드를 반환하는 방식으로 처리

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):                      # 시작 노드 전달 받음
    current = start                         # 현재 노드로 지정
    if current.link == None:                # 노드에 데이터가 하나도 없는 연결 리스트인 경우
        return                              # 반환한다
    print(current.data, end=' ')            # 현재 노드 출력
    while current.link != start:            # 현재 노드의 링크가 전달 받은 노드(=첫 번째 노드)가 아닐 때까지 반복
        current = current.link              # 현재 노드의 링크가 첫 번째 노드라면 원형 연결 리스트에서는 마지막 노드를 의미함
        print(current.data, end=' ')
    print()


def findNode(findData):                     # 노드를 검색하는 함수
    global memory, head, current, pre       # 전역 변수 가져오기

    current = head                          # 현재 노드를 head로 지정
    if current.data == findData:            # 현재 노드의 데이터가 찾는 데이터라면
        return current                      # current 반환
    while current.link != head:             # 노드가 끝날 때까지 반복
        current = current.link              # 현재 노드에서 다음 노드로 이동
        if current.data == findData:        # 현재 노드의 데이터가 찾는 데이터라면
            return current                  # current 반환
    return Node()                           # 빈 노드 반환


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

    printNodes(head)

## 코드 실행 확인 ##

    fNode = findNode('다현')
    print(fNode.data)

    fNode = findNode('쯔위')
    print(fNode.data)

    fNode = findNode('수연')
    print(fNode.data)