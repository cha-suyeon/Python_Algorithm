# Code05-08.py를 수정해서 랜덤하게 -100~100 숫자 중 7개를 뽑고, 양수와 음수의 개수를 센다. 그리고 양수는 음수로, 음수는 양수로 변경한다. 0은 양수도 음수도 아닌 것으로 간주한다.

# 원형 연결 리스트를 활용한 홀수와 짝수 구분 프로그램

import random

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
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

def countOddEven():
    global memory, head, current, pre

    pos, neg = 0, 0
    if head == None:
        return False
    current = head
    while True:
        if current.data > 0:
            pos += 1
        else:
            neg += 1
        if current.link == head:
            break;
        current = current.link

    return pos, neg

def makeZeroNumber(pos, neg):                  # 양의 정수, 음의 정수를 매개 변수로 받음
    if pos > neg:                              # 양의 정수(pos)가 음의 정수(neg)보다 많으면 나머지값을 1
        reminder = 1
    else:                                       # neg이 크면 나머지 값을 0
        reminder = 0

    current = head
    while True:
        current.data *= -1
        if current.link == head:
            break;
        current = current.link

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None


## 메인 코드 부분 ##
if __name__ == "__main__":

    dataArray = []
    for _ in range(7):
        dataArray.append(random.randint(-100,100))

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

    posCount, negCount = countOddEven()        
    print('양수 -->', posCount, '\t', '음수 -->', negCount)

    makeZeroNumber(posCount, negCount)
    printNodes(head)


