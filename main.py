import turtle
import random

screen = turtle.Screen()
screen.bgcolor('aquamarine')

t = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

def draw_shape(shape_type):
    t2.penup()
    t2.setposition(200, 100)
    t2.pendown()

    if shape_type == "circle":
        t2.fillcolor('purple')
        t2.begin_fill()
        t2.circle(50)
        t2.end_fill()
        t2.clear()
    elif shape_type == "square":
        t2.fillcolor('red')
        t2.begin_fill()
        for _ in range(4):
            t2.forward(100)
            t2.left(90)
        t2.end_fill()
        t2.clear()
    elif shape_type == "triangle":
        t2.fillcolor('yellow')
        t2.begin_fill()
        for _ in range(3):
            t2.forward(100)
            t2.left(120)
        t2.end_fill()
        t2.clear()
    elif shape_type == "rectangle":
        t2.begin_fill()
        t2.fillcolor('green')
        for _ in range(2):
            t2.forward(120)
            t2.left(90)
            t2.forward(60)
            t2.left(90)
        t2.end_fill()


t.write("All about me!", font=("Arial", 24, "bold"), align="center")
enter = input("Press Enter to Start")
t.clear()

t3.penup()
t3.goto(0,200)
t3.pendown()
screen.bgcolor('red')
t3.write("favorite food", font=("Arial", 24, "bold"), align="center")
screen.addshape("dump.gif")
t.shape("dump.gif")
enter = input("Press Enter to continue")


draw_shape("circle")

screen.addshape("mash.gif")
t.shape("mash.gif")
enter = input("Press Enter to continue")


draw_shape("square")

screen.addshape("pasta.gif")
t.shape("pasta.gif")
enter = input("Press Enter to continue")
t2.clear()
draw_shape("triangle")

t.clear()
t3.clear()
t3.goto(0,200)
t3.pendown()
screen.bgcolor('yellow')
t3.write("hobbys", font=("Arial", 24, "bold"), align="center")
screen.addshape("hockey.gif")
t.shape("hockey.gif")
enter = input("Press Enter to continue")

draw_shape("rectangle")

screen.addshape("piano.gif")
t.shape("piano.gif")
enter = input("Press Enter to continue")

draw_shape("circle")

screen.addshape("art.gif")
t.shape("art.gif")
enter = input("Press Enter to continue")

draw_shape("square")

screen.addshape("art.gif")
t.shape("art.gif")
enter = input("Press Enter to continue")

draw_shape("triangle")

screen.addshape("ro.gif")
t.shape("ro.gif")
enter = input("Press Enter to continue")

draw_shape("rectangle")

t3.clear()
t3.penup()
t3.goto(0,200)
t3.pendown()
screen.bgcolor('purple')
t3.write("favorite movie", font=("Arial", 24, "bold"), align="center")

screen.addshape("elf.gif")
t.shape("elf.gif")
enter = input("Press Enter to continue")

draw_shape("circle")

screen.addshape("ice.gif")
t.shape("ice.gif")

turtle.done()