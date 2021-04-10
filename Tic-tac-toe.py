from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("400x400")
root.title("Tic-tac-toe")

#variables
cval = True
f = 0

#disabling after game
def disable():
    b1.configure(state = DISABLED)
    b2.configure(state = DISABLED)
    b3.configure(state = DISABLED)
    b4.configure(state = DISABLED)
    b5.configure(state = DISABLED)
    b6.configure(state = DISABLED)
    b7.configure(state = DISABLED)
    b8.configure(state = DISABLED)
    b9.configure(state = DISABLED)

# check for win
def res():
    global p1, p2
    if(b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" or 
       b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" or 
       b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" or
       b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" or
       b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" or
       b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" or
       b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" or 
       b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X"  ):
       disable()
       a = p1.get()
       tmsg.showinfo('Tic-tac-toe', f"Player1 {a} wins")

    elif(b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" or 
         b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" or 
         b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" or
         b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" or
         b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" or
         b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" or
         b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" or 
         b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O"  ):
       disable()
       a = p2.get()
       tmsg.showinfo('Tic-tac-toe', f"Player2 {a} wins")

    elif(f == 9):
        disable()
        tmsg.showinfo('Tic-tac-toe', 'There is a Tie')
    else:
        pass

#click on buttos
def bclick(b):
    global cval, f
    if(cval == True and b["text"] == " "):
        b["text"] = "X"
        cval = False
        f += 1
        res()
    elif(cval == False and b["text"] == " "):
        b["text"] = "O"
        cval = True
        f += 1
        res()
    else:
        tmsg.showinfo('Mistake', 'Already Entered')

#players
p1 = StringVar()
p2 = StringVar()
l1 = Label(root, text = "Player 1")
l1.grid(row = 0, column = 0)
e1 = Entry(root, textvariable = p1)
e1.grid(row = 0, column = 1)
l1 = Label(root, text = "Player 2")
l1.grid(row = 1, column = 0)
e1 = Entry(root, textvariable = p2)
e1.grid(row = 1, column = 1)

#buttons
b1 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b1))
b1.grid(row = 2, column = 0)
b2 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b2))
b2.grid(row = 2, column = 1)
b3 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b3))
b3.grid(row = 2, column = 2)
b4 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b4))
b4.grid(row = 3, column = 0)
b5 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b5))
b5.grid(row = 3, column = 1)
b6 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b6))
b6.grid(row = 3, column = 2)
b7 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b7))
b7.grid(row = 4, column = 0)
b8 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b8))
b8.grid(row = 4, column = 1)
b9 = Button(root, text = " ", width = 15, height = 6, bg = "grey", fg = "white", command = lambda: bclick(b9))
b9.grid(row = 4, column = 2)
root.mainloop()