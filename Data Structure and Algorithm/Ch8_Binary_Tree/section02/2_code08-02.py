# Section 02
# 이진 트리의 순회(재귀 함수 사용)

# 이진 트리의 노드 전체를 한 번씩 방문하는 것을 순회(traversal)라고 한다.
# 이진 트리의 순회를 구현하는 바식으로는 스택(Stack)을 활용하는 방식과 재귀 함수(Recursion Function)을 이용하는 방식

class TreeNode():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        
node1= TreeNode()
node1.data = '화사'

node2= TreeNode()
node2.data = '솔라'
node1.left = node2

node3= TreeNode()
node3.data = '문별'
node1.right = node3

node4= TreeNode()
node4.data = '휘인'
node2.left = node4

node5= TreeNode()
node5.data = '쯔위'
node2.right = node5

node6= TreeNode()
node6.data = '선미'
node3.left = node6

# 전위 순회를 위한 재귀 함수: 루트 -> 왼쪽 -> 오른쪽 순서로 순회
def preorder(node):
    if node == None:
        return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

# 중위 순회를 위한 재귀 함수: 왼쪽 -> 루트 -> 오른쪽 순서로 순회
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)

# 후위 순회를 위한 재귀 함수: 왼쪽 -> 오른쪽 -> 루트 순서로 순회
def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')
    
print('전위 순회:', end=' ')
preorder(node1)
print('끝')

print('중위 순회:', end=' ')
inorder(node1)
print('끝')

print('후위 순회:', end=' ')
postorder(node1)
print('끝')