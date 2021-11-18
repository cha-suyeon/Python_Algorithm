## Section 03
## 3 이진 탐색 트리에서 데이터 검색

## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
        
## 전역 변수 선언 부분 ##
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스', '잇지', '여자친구']

## 메인 코드 부분 ##
node = TreeNode()               # 이름의 배열의 첫 번째 데이터를 루트 노드로 생성하고 메모리 공간에 넣는다.
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:]:
    
    node = TreeNode()           # 새 노드 생성
    node.data = name
    
    current = root              # 항상 루트 노트부터 시작한다. 즉, 현재 작업 노드는 항상 루트 노드부터 진행한다.
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right
    
    memory.append(node)
    
findName = input('찾을 그룹 이름-->')     # 찾고자 하는 데이터

current = root          # 루트 노드부터 검색 시작
while True:             # 데이터를 찾거나 못 찾을 때까지 반복
    if findName == current.data:
        print(findName, '을(를) 찾음')
        break
    elif findName < current.data:
        if current.left == None:
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left
    else:
        if current.right == None:
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right
        