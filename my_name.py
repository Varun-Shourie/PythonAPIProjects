# Varun Shourie, CIS345, Tuesday/Thursday 12:00PM-1:15PM, PE10

import turtle

# sets up the screen/window for further use.
turtle.setup(800, 500)
window = turtle.Screen()
window.reset()
window.bgcolor("white")

# sets up the turtle object's size, speed, and appearance.
plane = turtle.Turtle()
plane.color("cyan")
plane.pencolor("magenta")
plane.turtlesize(3)
plane.speed(9)

# sets the initial position of the turtle object without drawing all over the screen.
plane.penup()
plane.setposition(-195, 25)
plane.setheading(315)
plane.pendown()

# draws out a V to the screen.
plane.forward(80)
plane.left(90)
plane.forward(80)

# places space between V and A
plane.up()
plane.setheading(0)
plane.forward(5)

# draws out the A
plane.down()
plane.setheading(90)
plane.backward(50)
plane.forward(25)
plane.setheading(0)
plane.forward(50)
plane.backward(50)
plane.setheading(90)
plane.forward(25)
plane.right(90)
plane.forward(50)
plane.right(90)
plane.forward(50)

# places space between A and R
plane.penup()
plane.setheading(0)
plane.forward(5)
plane.left(90)

# draws the R
plane.pendown()
plane.forward(50)
plane.right(90)
plane.forward(35)
plane.right(90)
plane.forward(25)
plane.setheading(180)
plane.forward(35)
plane.backward(50)
plane.left(90)
plane.forward(25)

# space between the R and the U
plane.up()
plane.setheading(0)
plane.forward(5)
plane.setheading(90)

# U is drawn
plane.down()
plane.forward(50)
plane.backward(50)
plane.right(90)
plane.forward(50)
plane.left(90)
plane.forward(50)

# space between U and N is created and the program is ready to draw the N
plane.up()
plane.backward(50)
plane.right(90)
plane.forward(5)
plane.left(90)
plane.down()

# draws the N out to the canvas.
plane.forward(50)
plane.right(90)
plane.forward(50)
plane.right(90)
plane.forward(50)

turtle.done()
