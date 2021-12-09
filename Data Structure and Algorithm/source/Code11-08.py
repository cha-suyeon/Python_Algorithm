import os

## 함수 선언 부분 ##
def makeFileList(folderName) :
	fnameAry = []
	for dirName, subDirList, fnames in os.walk(folderName):
		for fname in fnames:
			fnameAry.append(fname)
	return fnameAry

def insertionSort(ary) :
	n = len(ary)
	for end in range(1, n) :
		for cur in range(end, 0, -1) :
			if (ary[cur-1] < ary[cur]) :
				ary[cur-1], ary[cur] = ary[cur], ary[cur-1]
	return ary

## 전역 변수 선언 부분 ##
fileAry = []

## 메인 코드 부분 ##
fileAry = makeFileList('C:/Program Files/Common Files')
fileAry = insertionSort(fileAry)
print('파일명 역순 정렬 -->', fileAry)
