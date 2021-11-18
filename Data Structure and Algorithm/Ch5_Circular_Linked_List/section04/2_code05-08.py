# 원형 연결 리스트를 활용한 홀수와 짝수 구분 프로그램
# head로부터 홀수와 짝수 개수를 세고, 홀수와 짝수 중 더 많은 것을 모두 음수로 변경한다.

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

    odd, even = 0, 0
    if head == None:
        return False
    current = head
    while True:
        if current.data % 2 == 0:
            even += 1
        else:
            odd += 1
        if current.link == head:
            break;
        current = current.link

    return odd, even

def makeZeroNumber(odd, even):                  # 홀수, 짝수를 매개변수로 받음
    if odd > even:                              # odd가 크면 나머지 값을 1
        reminder = 1
    else:                                       # even이 크면 나머지 값을 0
        reminder = 0

    current = head
    while True:
        if current.data % 2 == reminder:
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
        dataArray.append(random.randint(1,100))

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

    oddCount, evenCount = countOddEven()        
    print('홀수 -->', oddCount, '\t', '짝수 -->', evenCount)

    makeZeroNumber(oddCount, evenCount)
    printNodes(head)


## 코드 실행값 ##
# 14 8 14 79 69 2 55 
# 홀수 --> 3       짝수 --> 4
# -14 -8 -14 79 69 -2 55