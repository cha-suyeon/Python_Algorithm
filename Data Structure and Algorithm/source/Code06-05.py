def isStackEmpty() :
	global SIZE, stack, top
	if (top == -1) :
		return True
	else :
		return False

SIZE = 5
stack = [ None for _ in range(SIZE) ]
top = -1

print("스택이 비었는지 여부 ==>", isStackEmpty())
