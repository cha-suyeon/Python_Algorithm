## 함수 선언 부분 ##
def printMaze(arr) :
	for i in range(ROW) :
		for k in range(COL) :
			print("%3d" % arr[i][k], end = ' ')
		print()
	print()

def growRich() :
	memo = [[0 for _ in range(COL)] for _ in range(ROW)]
	memo[0][0] = goldMaze[0][0]

	colSum = memo[0][0]
	for i in range(1, COL):
		colSum += goldMaze[i][0]
		memo[i][0] = colSum

	rowSum = memo[0][0]
	for i in range(1, ROW):
		rowSum += goldMaze[0][i]
		memo[0][i] = rowSum

	for row in range(1, ROW) :
		for col in range(1, len(goldMaze[row])) :
			if (memo[row][col-1] > memo[row-1][col]) :
				memo[row][col] = memo[row][col-1] + goldMaze[row][col]
			else :
				memo[row][col] = (memo[row-1][col] + goldMaze[row][col])

	retValue = memo[ROW-1][COL-1]

	print('## 메모이제이션 ##')
	printMaze(memo)

	row, col = ROW-1, COL-1
	memo[row][col] = 0
	while row != 0 or col != 0 :
		if row-1 >= 0 and col-1 >= 0 :
			if memo[row-1][col] > memo[row][col-1] :
				row -= 1
			else :
				col -= 1
		elif row-1 < 0 and col - 1 >= 0 :
			col -= 1
		else :
			row -= 1
		memo[row][col] = 0

	print('## 메모이제이션(황금 미로 길) ##')
	printMaze(memo)

	return retValue


## 전역 변수 선언 부분 ##
ROW, COL = 5, 5
goldMaze = [[1, 4, 4, 2, 2],
	[1, 3, 3, 0, 5],
	[1, 2, 4, 3, 0],
	[3, 3, 0, 4, 2],
	[1, 3, 4, 5, 3]]

## 메인 코드 부분 ##
macolGold = growRich()
print('얻은 최대 황금 개수 -->', macolGold)


