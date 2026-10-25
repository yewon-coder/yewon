
import turtle as t
import random

t.speed(0)

c = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown']
t.pensize(12)

c1 = random.choice(c)
c2 = random.choice(c)
c3 = random.choice(c)
c4 = random.choice(c)
c5 = random.choice(c)

def cou():
    # c 그리기
    t.penup()
    t.goto(-270, 0)
    t.pendown()
    t.color(c1)
    t.setheading(45)
    for i in range(2):
        t.circle(48, 90)
        t.circle(24, 90)

    t.begin_fill()
    t.penup()
    t.goto(-270, 54)
    t.pendown()
    t.color('white')
    t.setheading(45)
    t.fd(30)
    t.setheading(270)
    t.fd(84)
    t.setheading(135)
    t.fd(30)
    t.setheading(90)
    t.fd(42)
    t.end_fill()

    # o 그리기
    t.penup()
    t.color(c1)
    t.goto(-210, 0)
    t.pendown()
    t.setheading(45)
    for i in range(2):
        t.circle(48, 90)
        t.circle(24, 90)

        # u 그리기
    t.penup()
    t.color(c1)
    t.goto(-165, 74)
    t.setheading(270)
    t.pendown()
    t.fd(54)
    t.circle(24, 180)
    t.fd(54)
    t.rt(180)
    t.fd(80)






rad = 24

def p():
    # p의 둥근 부분
    t.penup()
    t.color(c2)
    t.goto(-46, 0)
    t.pendown()
    t.setheading(45)
    for i in range(2):
        t.circle(48, 90)
        t.circle(24, 90)

    # p의 세로 짝대기
    t.penup()
    t.goto(-88, 132)
    t.pendown()
    t.setheading(270)
    t.fd(186)
    t.rt(90)
    t.color('white')
    t.fd(12)
    t.rt(90)
    t.fd(144)
    t.goto(-100, -48)
    t.setheading(0)
    t.fd(30)
    t.setheading(180)
    t.fd(30)
    t.rt(90)
    t.fd(138)
    t.setheading(0)

    t.begin_fill()
    for i in range(2):
        t.fd(30)
        t.lt(90)
        t.fd(54)
        t.lt(90)
    t.end_fill()


def a():
    t.penup()
    t.goto(14, -18)
    t.pendown()
    t.color(c3)
    t.circle(30)

    t.penup()
    t.goto(44, 42)
    t.pendown()
    t.setheading(90)
    t.circle(30, 150)

    t.penup()
    t.rt(90)
    t.fd(18)
    t.pendown()
    t.color('white')
    t.lt(180)
    t.fd(30)

    t.penup()
    t.goto(44, 42)
    t.color(c3)
    t.pendown()
    t.setheading(270)
    t.fd(72)

    t.penup()
    t.color('white')
    t.goto(14, -30)
    t.pendown()
    t.setheading(0)
    t.fd(60)


def n():
    t.penup()
    t.color(c4)
    t.goto(120, -18)
    t.setheading(90)
    t.pendown()
    t.fd(54)
    t.circle(24, 180)
    t.fd(54)
    t.lt(180)
    t.fd(200)
    t.lt(180)
    t.fd(100)
    t.color('white')
    t.setheading(0)
    t.fd(50)
    t.lt(180)
    t.begin_fill()
    for i in range(2):
        t.fd(80)
        t.rt(90)
        t.fd(150)
        t.rt(90)
    t.end_fill()



def g():
    t.color(c5)
    t.penup()
    t.goto(180, 62)
    t.pendown()
    t.circle(30)
    t.penup()
    t.goto(195,62)
    t.pendown()
    t.setheading(45)
    t.penup()
    t.fd(30)
    t.pendown()
    t.lt(180)
    t.circle(200,40)
    t.setheading(0)
    t.fd(60)
    t.penup()
    t.goto(180, 32)
    t.pendown()
    t.color('white')
    t.dot(50)
    t.penup()
    t.goto(208,-100)
    t.pendown()
    t.color(c5)
    t.circle(30,150)


cou()
p()
a()
n()
g()

t.done()
