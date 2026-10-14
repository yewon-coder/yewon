import turtle as t
import random


c=['red','orange','yellow','green','blue','purple']
t.pensize(20)

def cou():
    t.penup()
    t.goto(-300,0)
    t.pendown()
    t.color(random.choice(c))
    t.lt(150)
    for i in range(24):
        t.fd(5)
        t.lt(5)
    t.fd(30)
    for i in range(25):
        t.fd(5)
        t.lt(5)

    t.penup()
    t.fd(50)
    t.lt(90)
    t.fd(10)
    t.rt(90)
    t.rt(180)
    t.lt(58)
    t.pendown()

    for i in range(35):
        t.fd(5)
        t.lt(5)
    t.fd(30)
    for i in range(35):
        t.fd(5)
        t.lt(5)
    t.fd(30)

    t.penup()
    t.lt(90)
    t.fd(140)
    t.lt(90)
    t.fd(90)
    t.lt(190)
    t.pendown()

    t.fd(80)
    for i in range(35):
        t.fd(5)
        t.lt(5)
    t.fd(80)
    t.rt(180)
    t.fd(140)


rad = 40

def p():
    t.color(random.choice(c))
    t.penup()
    t.goto(100, -100)
    t.setheading(90)
    t.pendown()

    # 세로줄
    t.fd(150)

    # 둥근 부분을 크게 그리기
    t.setheading(0)
    t.circle(50, 180)

    t.penup()


cou()
p()


t.done()
