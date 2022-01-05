import random

## 클래스 및 함수 선언부 ##
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end=' ')
    while current.link != head:
        current = current.link
        print(current.data, end=' ')
    print()

def  countOddEven() :
    global memory, head, current, pre

    plus, minus = 0, 0
    if head == None :
        return False

    current = head
    while True:
        if current.data > 0:
            plus += 1
        elif  current.data < 0:
            minus += 1
        if current.link == head :
            break
        current = current.link

    return plus, minus

def makeZeroNumber(odd, even):
    if odd > even :
        reminder = 1
    else :
        reminder = 0

    current = head
    while True:
        current.data *= -1
        if current.link == head :
            break
        current = current.link

## 전역 변수 선언부
memory = []
head, current, pre = None, None, None

## 메인 코드부
if __name__ == "__main__" :

    dataArray = []
    for _ in range(7) :
        dataArray.append(random.randint(-100,100))

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:] :
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)

    plusCount, minusCount = countOddEven()
    print('양수 -->', plusCount, '\t', '음수 -->', minusCount)

    makeZeroNumber(plusCount, minusCount)
    printNodes(head)