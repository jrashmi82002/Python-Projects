#calculator
from tkinter import *

res = 0
def click(event):
	global var
	t = event.widget.cget("text")
	if t == 'C':
		var.set("")
	elif t == '=':
		e = eval(var.get())
		var.set(e)

	else:
		var.set(var.get()+t)
		
'''def calc(t):
	global res
	lst = []
	if '+' in t:
		lst = t.split('+')
		res = int(lst[0]) + int(lst[1])
	elif '-' in t:
		lst = t.split('-')
		res = int(lst[0]) - int(lst[1])
	elif '/' in t:
		lst = t.split('/')
		res =int(lst[0]) / int(lst[1])
	elif '*' in t:
		lst = t.split('*')
		res = int(lst[0]) * int(lst[1])
	return res'''


root = Tk()

root.geometry("800x800")
root.title("Calculator")
Label(root, text ="CALCULATOR").pack()
F = Frame(root)
F.pack()
var = StringVar()
Entry(F, textvariable = var ).pack()
var.set("")

#row1
f2 = Frame(root, bg = "black")

b = Button(f2, text = "9")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f2, text = "8")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f2, text = "7")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f2, text = "C")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

f2.pack()

#row2
f3 = Frame(root, bg = "black")

b = Button(f3, text = "6")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f3, text = "5")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f3, text = "4")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f3, text = "/")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

f3.pack()

#row3
f = Frame(root, bg = "black")

b = Button(f, text = "3")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f, text = "2")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f, text = "1")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f, text = "=")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

f.pack()

#row4
f1 = Frame(root, bg = "black")

b = Button(f1, text = "+")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f1, text = "0")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f1, text = "-")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

b = Button(f1, text = "*")
b.pack(side = LEFT)
b.bind('<Button-1>',click)

f1.pack()

root.mainloop()