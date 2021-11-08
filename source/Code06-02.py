stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print("--- 스택 상태-----")
for i in range(len(stack)-1, -1, -1) :
	print(stack[i])

print("-------------------")
data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop -->", data)
print("-------------------")

print("--- 스택 상태-----")
for i in range(len(stack)-1, -1, -1) :
	print(stack[i])
