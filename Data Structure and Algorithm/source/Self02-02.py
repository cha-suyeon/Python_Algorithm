list1 = []
list2 = []
value = 12
for i in range(0, 4) :
	for k in range(0, 3) :
		list1.append(value)
		value -= 1
	list2.append(list1)
	list1 = []

for i in range(0, 4) :
	for k in range(0, 3) :
		print("%3d" % list2[i][k], end = " ")
	print("")

hap = 0
for i in range(0, 4) :
	for k in range(0, 3) :
		hap += list2[i][k]

print("배열의 합계 ==>", hap)