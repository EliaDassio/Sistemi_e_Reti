import turtle
import time
import random

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

def eat():
    x = random.randint(-sp, sp)
    y = random.randint(-sp, t_sp - 40)
    food.goto(x, y)

    tail_new = turtle.Turtle()
    tail_new.speed(0)
    tail_new.shape("square")
    tail_new.color("black")
    tail_new.penup()
    tail.append(tail_new)

def move_tail():
    for index in range(len(tail)-1, 0, -1):
        x = tail[index-1].xcor()
        y = tail[index-1].ycor()
        tail[index].goto(x, y)

    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x, y)

def reset():
    time.sleep(1)
    for index in tail:
        index.goto(dim + 1000, dim + 1000)
    tail.clear()
    head.goto(0,0)
    head.direction = "stop"


tail = []

dim = 600
sp = dim/2 - 20
t_sp = sp - 30
delay = 0.07
score = 0
h_score = 0

sc = turtle.Screen()
sc.title("Snake")
sc.bgcolor("teal")
sc.setup(width = dim, height = dim)
sc.tracer(0)

line = turtle.Turtle()
line.speed(0)
line.color("black", "black")
line.penup()
line.hideturtle()
line.goto(dim/2, t_sp)
line.begin_fill()
line.pendown()
line.goto(-dim/2, t_sp)
line.goto(-dim/2, dim/2)
line.goto(dim/2, dim/2)
line.goto(dim/2, t_sp)
line.end_fill()

text = turtle.Turtle()
text.speed()
text.shape("square")
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 260)
text.write("Score: {} High Score: {}".format(score, h_score), align = "center", font = ("Courier", 20, "normal"))
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("purple")
food.penup()
x = random.randint(-sp, sp)
y = random.randint(-sp, sp - 40)
food.goto(x, y)

sc.listen()
sc.onkeypress(move_up, "Up")
sc.onkeypress(move_down, "Down")
sc.onkeypress(move_left, "Left")
sc.onkeypress(move_right, "Right")

sc.onkeypress(move_up, "w")
sc.onkeypress(move_down, "s")
sc.onkeypress(move_left, "a")
sc.onkeypress(move_right, "d")

while True:
    sc.update()
    if head.xcor() > sp or head.xcor() < -sp or head.ycor() > t_sp - 20 or head.ycor() < -sp:
        reset()
        score = 0
    if head.distance(food) < 20:
        eat()
        score += 10
        if score > h_score:
            h_score = score
    move_tail()
    move()
    text.clear()
    text.write("Score: {} High Score: {}".format(score, h_score), align = "center", font = ("Courier", 20, "normal"))
    for index in tail:
        if index.distance(head) <20:
            reset()
            score = 0
    time.sleep(delay)

sc.mainloop()