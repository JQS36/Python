from curses import window
from turtle import *
import turtle
import time
import random

posponer, score, high_score = 0.1, 0 ,0

#screen
windows = turtle.Screen()
windows.title("Game Snake")
windows.bgcolor("black")
windows.setup(width=600, height=600)
windows.tracer(0)

#head snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction = "stop"

#eat
eat = turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("red")
eat.penup()
eat.goto(0,100)

#Body snake
segments = []
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0,260)
text.write("Score: 0      High Score: 0", align="center", font=("Courier", 24, "normal"))

#funtions
def up1():
    head.direction = "up"

def down1():
    head.direction = "down"

def left():
    head.direction = "left"

def right():
    head.direction = "right"


def mov1():
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

#keyboard
windows.listen()
windows.onkeypress(up1, "Up")
windows.onkeypress(down1, "Down")
windows.onkeypress(left, "Left")
windows.onkeypress(right, "Right")

while True:
    windows.update()
    #colisiones borde con la pantalla
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        
        head.goto(0,0)
        head.direction = "stop"
        #hiden the segments
        for seg in segments:
            seg.goto(1000, 1000)
        #clean list segments
        segments.clear()
        #reset mark
        score = 0
        text.clear()
        text.write(f"Score: {score}      High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    if eat.distance(head) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        eat.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #Aumenatr marcador
        score +=10
        if score > high_score:
            high_score = score
        text.clear()
        text.write(f"Score: {score}      High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    
    #Move body the snake
    totalSeg = len(segments)
    for i in range(totalSeg -1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)
    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    mov1()

    #colisiones with the body
    for seg in segments:
        if head.distance(seg) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hidden segmd
            for seg in segments:
                seg.goto(1000,1000)
            segments.clear()

    time.sleep(posponer)