from tkinter import *

window = Tk()
window.geometry("600x600")

photo = PhotoImage(file = 'pet01.gif')

paper = Label(window, image=photo)
paper.pack(expand=1, anchor = CENTER)
window.mainloop()
