import math
import turtle


def drawPolygon(a,b,c):
    for i in range(a):
        b.forward(c)
        b.left(360/180)


def drawCircle(a,t,r):
    drawPolygon(a,t,(2*math.pi*r)/180)


s=turtle.Screen()
s.bgcolor("black")


#sun
sun=turtle.Turtle()
sun.shape("circle")
sun.color("yellow")



#planets
def planets(a,p,speed,r):
    p.speed(speed)
    p.shape("circle")
    p.pensize("1")
    drawCircle(a,p,r)


def move(p,r):
    p.up()
    p.goto(0,-r*4/3)
    p.pendown()
    

mercury=turtle.Turtle()
venus=turtle.Turtle()
earth=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()


def mercury_run():
    mercury.color("blue")
    planets(100,mercury,10,60)


def venus_run():
    venus.color("green")
    planets(150,venus,10,100)


def earth_run():
    earth.color("red")
    planets(160,earth,10,130)


def mars_run():
    mars.color("white")
    planets(170,mars,10,170)


def jupiter_run():
    jupiter.color("orange")
    planets(180,jupiter,10,220)


def saturn_run():
    saturn.color("sky blue")
    planets(190,saturn,10,280)


move(mercury,60)
move(venus,100)
move(earth,130)
move(mars,170)
move(jupiter,220)
move(saturn,280)


for i in range(20):
    mercury_run()
    venus_run()
    earth_run()
    mars_run()
    jupiter_run()
    saturn_run()

