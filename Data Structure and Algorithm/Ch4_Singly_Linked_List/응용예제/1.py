## 클래스와 함수 선언 부분 ##

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def makeSimpleLinkedList(nameEmail):
    global memory, head, current, pre

    node = Node()           # 새 노드 생성
    node.data = nameEmail   # 메모리 공간에 새 노드 넣음
    memory.append(node)
    
    if head == None:        # 새 노드가 첫 노드라면
        head = node         # 노드를 헤드로 지정하고
        return              # 함수 종료

    if head.data[1] > nameEmail[1]:     # 새 노드의 이메일이 첫 노드의 이메일보다 빠르다면
        node.link = head                # 새 노드의 링크에 첫 노드 지정
        head = node                     # 헤드를 새 노드로 지정한 후
        return                          # 함수 종료

    current = head
    while current.link != None:
        pre = current                           # 이전 노드를 현재 노드로 변경
        current = current.link                  # 현재 노드는 다음 노드로 변경
        if current.data[1] > nameEmail[1]:      # 새 노드의 이메일이 현재 노드의 이메일보다 빠르다면
            pre.link = node                     # 이전 노드와 현재 노드 사이에 새 노들르 삽입
            node.link = current
            return                              # 함수 종료

    current.link = node     # 마지막 노드보다 새 노드의 이메일이 더 늦는 경우 - 새 노드를 마지막 노드로 추가

## 전역 변수 선언 부분 ## 

memory = []
head, current, pre = None, None, None

## 메인 코드 선언 부분 ##
if __name__ == '__main__':

    while True:
        name = input('이름을 입력하시오: ')
        if name == '' or name == None:
            break
        email = input('이메일을 입력하시오: ')
        makeSimpleLinkedList([name, email])
        printNodes(head)