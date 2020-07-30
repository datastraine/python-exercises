import turtle as t
import random as random
# crazy creepers!!
def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()
t.shape('turtle')
t.speed('fastest')
t.bgcolor('dodger blue')
def creeper(x, y):
    count = 25
    t.penup()
    while count > 0:
        # head
        t.goto(x,y)
        rectangle(60, 60, 'green')
        # face: eye1, eye2, mouth1, mouth2, mouth3
        t.goto(x+10, y-10)
        rectangle(10, 10, 'black')
        t.goto(x+40, y-10)
        rectangle(10, 10, 'black')
        t.goto(x+10, y-30)
        rectangle(10, 20, 'black')
        t.goto(x+20, y-20)
        rectangle(20, 20, 'black')
        t.goto(x+40, y-30)
        rectangle(10, 20, 'black')
        # body
        t.goto(x+10, y-50)
        rectangle(40, 80, 'green')
        # 2 feet
        t.goto(x, y-130)
        rectangle(20, 20, 'green')
        t.goto(x+40, y-130)
        rectangle(20, 20, 'green')
        x = x + random.randint(-150, 150)
        y = y + random.randint(-150, 150)
        count -= 1 
    t.mainloop()
creeper(0, 0)