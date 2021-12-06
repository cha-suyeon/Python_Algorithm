from tkinter import *
import random

## 함수 선언 부분 ##
def drawCircle(x, y, r) :
	canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
	if r >= 5 :
		drawCircle(x+r//2, y, r//2)
		drawCircle(x-r//2, y, r//2)

## 전역 변수 선언 부분 ##
colors = ["red", "green", "blue", "black", "orange", "indigo", "violet"]
wSize = 1000
radius = 400

## 메인 코드 부분 ##
window = Tk()
window.title("원 모양의 프랙탈")
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()
