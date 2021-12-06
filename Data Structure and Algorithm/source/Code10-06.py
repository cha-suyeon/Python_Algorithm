def printStar(n) :
	if n > 0 :
		printStar(n-1)
		print('★' * n)

printStar(5)
