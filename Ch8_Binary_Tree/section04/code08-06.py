# Section04 이진 탐색 트리의 응용

# 이진 탐색 트리는 데이터 보관/검색에 효율적임
# 순서대로 보관하기 때문에 검색에서도 효율성이 큼
# 도서관에 새로 입과된 책 정보를 이진 탐색 트리에 보관해서 검색할 수 있게 만들기
# 단, 책 이름과 작가 이름을 각각 이진 탐색 트리로 따로 생성한다.


import random
from typing import no_type_check_decorator
## 함수 선언 부분 ##
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None
        
## 전역 변수 함수 선언 ##
memory = []
# 책 이름 및 작가 이름 리스트를 준비
bookAry = [ ['어린왕자', '쌩떽쥐베리'],['이방인', '까뮈'], ['부활', '톨스토이'],
        ['신곡', '단테'], ['돈키호테', '세브반테스'], ['동물농장', '조지오웰'],
		['데미안','헤르만헤세'], ['파우스트', '괴테'], ['대지', '펄벅'] ]
# 배열 내용을 랜덤하게 섞음 = ['책이름','작가']가 섞이므로 책 이름과 작가 이름 쌍은 변하지 않음
random.shuffle(bookAry)
# bookAry 배열을 랜덤하게 섞으면 이진 탐색 트리의 구성 형태는 변할 수 있지만 검색 결과는 바뀌지 않는다.

## 메인 코드 부분 ##

### 책 이름 트리 ###
node = TreeNode()
node.data = bookAry[0][0]   # 첫 번째 배열의 첫 번쨰 항목은 책 이름이다. 책 이름을 새 노드 데이터로 준비
rootBook = node             # 새 노드를 책 이름 루트 노드로 지정
memory.append(node)

for book in bookAry[1:] :   # 두 번째 책부터 책 이름으로 이진 탐색 트리를 생성한다.
	name = book[0]          # [책 이름, 작가이름] 배열에서 책 이름만 추출
	node = TreeNode()
	node.data = name

	current = rootBook
	while True :
		if name < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right

	memory.append(node)

print("책 이름 트리 구성 완료!")

### 작가 이름 트리 ###
node = TreeNode()
node.data = bookAry[0][1]       # 책 배열의 첫 번째 데이터 두 번째 항목은 작가 이름이다. 작가 이름을 새 노드 데이터로 준비
rootAuth = node                 # 새 노드를 작가 이름 루트 노드로 지정
memory.append(node)

for book in bookAry[1:] :       # 두 번째 책부터 작가 이름으로 이진 탐색 트리 생성
	name = book[1]
	node = TreeNode()
	node.data = name

	current = rootAuth
	while True :
		if name < current.data :
			if current.left == None :
				current.left = node
				break
			current = current.left
		else :
			if current.right == None :
				current.right = node
				break
			current = current.right

	memory.append(node)

print("작가 이름 트리 구성 완료!")

## 책 이름 및 작가 이름 검색 ##
bookOrAuth = int(input('책검색(1), 작가검색(2)-->'))        # 무엇을 검색할지 선택
findName = input('검색할 책 또는 작가-->')                  # 검색할 책 이름 또는 작가 이름 입력

if bookOrAuth == 1 :
	root = rootBook
else :
	root = rootAuth

current = root
while True:
	if findName == current.data :
		print(findName, '을(를) 찾음.')
		findYN = True
		break
	elif findName < current.data :
		if current.left == None :
			print(findName, '이(가) 목록에 없음')
			break
		current = current.left
	else:
		if current.right == None :
			print(findName, '이(가) 목록에 없음')
			break
		current = current.right