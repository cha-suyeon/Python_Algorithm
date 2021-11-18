# 원형 연결 리스트의 생성 함수 완성

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

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효']

## 메인 코드 부분 ##
if __name__ == "__main__":

    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

