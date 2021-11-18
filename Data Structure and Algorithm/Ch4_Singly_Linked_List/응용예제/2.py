import random

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

def makeLottoList(num):
    global memory, head, current, pre

    node = Node()
    node.data = num
    memory.append(node)
    if head == None: # 첫 번째 노드
        head = node
        return

    if head.data > num:
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current
            return
    
    current.link = node

def findNumber(num):
    global memory, head, current, pre

    if head == None:                # 단순 연결 리스트 생성
        return False                # False 반환
    current = head                  # 헤드를 현재 노드로 지정
    if current.data == num:         # 현재 노드의 데이터가 넘겨 받은 숫자라면
        return True                 # 중복되므로 True 반환
    while current.link != None:     # 노드의 끝까지 넘겨 받은 숫자라면 중복되므로 True를 반환
        current = current.link
        if current.data == num:
            return True
    return False                    # 노드에 없는 숫자라면 False 반환

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__":

    lottoCount = 0                          # 뽑은 로또 숫자의 개수
    while True:
        lotto = random.randint(1, 45)       # 1~45 사이 숫자 랜덤 추출
        if findNumber(lotto):               # 중복된다면 무시하고 다시 추첨
            continue
        lottoCount += 1                     # 뽑지 않은 숫자라면 뽑은 개수를 1 증가 시켜준다
        makeLottoList(lotto)                # 단순 연결 리스트 생성
        if lottoCount >= 6:                 # 뽑은 숫자가 6개 이상이 되면 중단
            break
    
    printNodes(head)                        # 뽑은 로또 숫자 출력

# 로또 번호를 넘겨받아 순서대로 단순 연결 리스트를 생성한다. [응용예제01]의 makeSimpleLinkedList() 함수와 기능이 거의 비슷하다.
