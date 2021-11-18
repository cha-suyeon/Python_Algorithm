# 응용예제 1. 현재 위치부터 가까운 편의점 관리하기

# 현재 위치를 (0,0)이라 가정. 편의점 위치 (x,y)와 거리가 가까운 순서대로 원형 연결 리스트를 생성하는 프로그램을 다음 조건에 맞게 작성

# - 편의점 10개를 A, B, C, ... 순서로 이름을 부여한다.
# - 편의점 위치 x와 y는 1부터 100까지 랜덤하게 좌표가 생성되도록 한다.
# - 현재 위치와 편의점 거리는 (x^2+y^2)의 제곱근(sqrt)로 계싼한다
# - 편의점 데이터 1개는 (편의점 이름, x좌표, y좌표) 형식의 튜플로 구성한다.

import random
import math

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printStores(start):
    current = start
    if current == None:
        return

    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리:', math.sqrt(x*x + y*y))
    print()

def makeStorelist(store):
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None:        # 첫 번째 편의점
        head = node
        node.link = head
        return
    
    # 새 편의점이 첫 번째 편의점보다 가까우면 첫 번째 편의점으로 만듦
    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX*nodeX + nodeY*nodeY)
    headX, headY = head.data[1:]
    headDist = math.sqrt(headX*headX + headY*headY)

    if headDist > nodeDist:     # 헤드 앞에 삽입
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return
    
    current = head      # 중간에 데이터를 넣을 경우
    while current.link != head:
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX*currX + currY*currY)
        if currDist > nodeDist:
            pre.link = node
            node.link = current
            return
    
    current.link = node
    node.link = head


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None


## 메인코드 부분 ##
if __name__ == '__main__':

    storeArray = []
    storeName = 'A'
    for _ in range(10):
        store = (storeName, random.randint(1,100), random.randint(1,100))
        storeArray.append(store)
        storeName = chr(ord(storeName)+1)       # 편의점 이름을 A->B->C...으로 변경

    for store in storeArray:
        makeStorelist(store)
    
    printStores(head)

## 코드 순서대로 설명 ##
# 1. 원형 연결 리스트를 출력한다. 편의점 이름 및 현재 위치(0,0)부터 편의점까지 거리를 출력한다. 각 편의점은 (편의점이름, x좌표, y좌표) 형식의 튜플이므로 17행에서의 x와 y값을 추출하고, 18행에서 편의점 거리를 계산해서 출력한다.
# 2. 매개변수로 편의점 튜플(편의점이름, x좌표, y좌표) 형식의 튜플이므로 해당 지점에서부터 x와 y값을 추출하고,편의점 거리를 계산해서 출력한다.
# 3. 첫 편의점은 그대로 원형 연결 리스트의 첫 번째 노드로 만든다.
# 4. 두 번째 편의점부터는 편의점 거리 및 첫 편의점의 거리를 계산한다.
# 5. 첫 편의점보다 입력할 편의점 거리가 가까울 때는 헤드를 입력할 편의점으로 변경한다.
# 6. 첫 편의점보다 입력할 편의점 거리가 멀 때는 해당 위치를 찾아 중간에 삽입한다.
# 7. 입력할 편의점이 원형 리스트의 모든 편의점보다 가장 거리가 멀다면 맨 뒤에 삽입한다.
# 8. 편의점 튜플을 저장할 리스트를 준비하고, 편의점 이름은 A부터 시작한다.
# 9. 편의점 튜플(편의점이름, x좌표, y좌표)을 생성해서 편의점 리스트에 추가한다.
# 10. 편의점 배열에서 편의점을 하나씩 추출해서 원형 연결 리스트로 생성한다.
# 11. 생성한 편의점의 원형 연결 리스트를 출력한다.