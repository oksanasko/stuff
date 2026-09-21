import turtle
import random

# t = turtle.Turtle()

def draw_figure(turtle, size, linecl, bgcl, sides):
    turtle.color(linecl, bgcl)
    angle = 360/sides
    turtle.begin_fill()
    for _ in range(sides):
        turtle.forward(size)
        turtle.left(angle)
    turtle.end_fill()
    
def draw_star(turtle_obj, size):
    for _ in range(5): #star
        turtle_obj.forward(size)
        turtle_obj.left(216)

# turtle.getscreen().bgcolor("#000000")
# t.speed(100)
# t.color("white", "yellow")
# for _ in range(50):
#     x,y = random.randint(-300, 300), random.randint(-300,300)
#     t.penup()
#     t.goto(x,y)
#     t.pendown()
#     t.begin_fill()
#     draw_star(t, random.randint(5,25))
#     t.end_fill()

# t.setheading(0)#<-east 90-north

#turtle.getscreen().onclick(turtle.goto)

def draw_star2(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    turtle.color("red", "yellow")
    turtle.begin_fill()

    for _ in range(36):
        turtle.forward(150)
        turtle.left(170)

    turtle.end_fill()

# turtle.speed(200)
# draw_star2(0,0)

# turtle.getscreen().onclick(draw_star2)


# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# turtle.speed(500)
# turtle.bgcolor("black")

# for x in range(360):
#     turtle.pencolor(colors[x%6])
#     turtle.width(x // 100+1)
#     turtle.forward(x)
#     turtle.left(59)

# for i in range(0, 400, 20):
#     turtle.forward(i)
#     turtle.right(90)

turtle.speed(10)
# turtle.left(75)

def flower1(num, lenght, num2=1): #only for even numbbers=(
    turn = 360//num
    for _ in range(num2):
        for _ in range(num): #fullcircle
            turtle.forward(lenght)
            turtle.left(turn)
            turtle.forward(lenght)
            turtle.left(180-turn)
            turtle.forward(lenght)
            turtle.left(turn)
            turtle.forward(lenght)
            turtle.left(180)
        turtle.left(180-turn//num2)

# flower1(7,100)

# method to draw ellipse
def draw(rad):
  # rad --> radius of arc
  for i in range(2):
    # two arcs
    turtle.circle(rad,90)
    turtle.circle(rad//2,90)

# Main section
# tilt the shape to negative 45
# 
turtle.seth(-45)
# turtle.circle(200,360)

def draw_elips(width, height):
    turtle.setheading(-45)
    for i in range(2):
        # two arcs
        turtle.circle((height*height)//width,90)
        turtle.circle((width*width)//height,90)

# calling draw method
draw(100)
draw_elips(100,50)

turtle.done()

