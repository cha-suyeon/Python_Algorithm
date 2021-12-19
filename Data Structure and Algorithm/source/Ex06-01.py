import random

## 함수 선언 부분 ##
def isStackFull() :
	global SIZE, stack, top
	if (top >= SIZE-1) :
		return True
	else :
		return False

def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def push(data) :
	global SIZE, stack, top
	if (isStackFull()) :
		return
	top += 1
	stack[top] = data

def pop() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	data = stack[top]
	stack[top] = None
	top -= 1
	return data

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		return None
	return stack[top]

## 전역 변수 선언 부분 ##
SIZE = 10
stack = [ None for _ in range(SIZE) ]
top = -1

## 메인 코드 부분 ##
if __name__ == "__main__" :

	stoneAry = ["빨강", "파랑", "초록", "노랑", "보라", "주황"]
	random.shuffle(stoneAry)

	print("과자집에 가는길 : ", end = ' ')
	for stone in stoneAry :
		push(stone)
		print(stone, "-->", end = ' ')
	print("과자집")

	print("우리집에 오는길 : ", end = ' ')
	while True :
		stone = pop()
		if stone == None :
			break
		print(stone, "-->", end = ' ')
	print("우리집")
