def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

def peek() :
	global SIZE, stack, top
	if (isStackEmpty()) :
		print("스택이 비었습니다.")
		return None
	return stack[top]

SIZE = 5
stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print(stack)
retData = peek()
print("top의 데이터 확인 -->", retData)
print(stack)
