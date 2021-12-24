# 원형 연결 리스트의 노드 삭제 함수

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


def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:             # 삭제할 노드가 첫 번째 노드일 때
        current = head                      # 현재 노드를 헤드 노드와 동일하게 만들기
        head = head.link                    # head 노드를 다음 노드로 변경
        last = head                        
        while last.link != current:         # 마지막 노드를 찾으면 반복 종료 
            last = last.link                # last를 다음 노드로 변경
        last.link = head                    # 마지막 노드의 링크에 head가 가리키는 노드 지정
        del(current)
        return

    current = head                          # 첫 번째 외 노드 삭제
    while current.link != head:
        pre = current
        current = current.link
        if current.data == deleteData:      # 중간 노드를 찾았을 때
            pre.link = current.link
            del(current)
            return


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


## 코드 실행해서 확인하기 ##
    deleteNode('다현')
    printNodes(head)

    deleteNode('쯔위')
    printNodes(head)

    deleteNode('지효')
    printNodes(head)

    deleteNode('재남')
    printNodes(head)


## 코드 실행값 ##
# 다현 정연 쯔위 사나 지효 
# 정연 쯔위 사나 지효 
# 정연 사나 지효
# 정연 사나
# 정연 사나