from tkinter import *

window = Tk()
window.geometry("600x600")
photo = PhotoImage(file = 'pet01.gif')

photoAry=[]
h = photo.height()
w = photo.width()
for i in range(h) :
	for k in range(w) :
		r, g, b = photo.get(i,k)
		value = (r + g + b) // 3
		photoAry.append(value)

# 이 부분에 필요한 내용을 추가


paper = Label(window, image=photo)
paper.pack(expand=1, anchor = CENTER)
window.mainloop()
