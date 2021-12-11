from tkinter import *

## 함수 선언 부분 ##
def qSort(arr, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = arr[(low + high) // 2]  # 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리한다.
	while low <= high :
		while arr[low] < pivot :
			low += 1
		while arr[high] > pivot :
			high -= 1
		if low <= high :
			arr[low], arr[high] = arr[high], arr[low]
			low, high = low + 1, high - 1

	mid = low

	qSort(arr, start, mid-1)
	qSort(arr, mid, end)

def quickSort(ary) :
	qSort(ary, 0, len(ary)-1)

## 메인 코드 부분 ##
window = Tk()
window.geometry("600x600")
photo = PhotoImage(file = 'pet02.gif')

photoAry=[]
h = photo.height()
w = photo.width()
for i in range(h) :
	for k in range(w) :
		r, g, b = photo.get(i,k)
		value = (r + g + b) // 3
		photoAry.append(value)

dataAry = photoAry[:]
quickSort(dataAry)
midValue = dataAry[h*w // 2]

for i in range(len(photoAry)) :
	if photoAry[i] <= midValue :
		photoAry[i] = 0
	else :
		photoAry[i] = 255

pos = 0
for i in range(h) :
	for k in range(w) :
		r = g = b = photoAry[pos]
		pos += 1
		photo.put("#%02x%02x%02x" % (r, g, b), (i, k))

paper = Label(window, image=photo)
paper.pack(expand=1, anchor = CENTER)
window.mainloop()
