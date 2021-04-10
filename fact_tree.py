import turtle
t = turtle.Turtle()
t.left(90)
t.speed(150)
def tree(I):
	if I <10:
		return
	else:
		t.forward(I)	
		t.left(30)
		tree(3*I/4)
		t.right(60)
		tree(3*I/4)
		t.left(30)
		t.backward(I)
tree(400)