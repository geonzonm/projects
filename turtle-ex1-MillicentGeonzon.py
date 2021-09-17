#Name: Millicent Geonzon
import turtle
s=turtle.Screen()
t=turtle.Turtle()

# Place your code after this line

#move the pen
t.penup()
t.goto(-150, 0)
t.pendown()

# Horizontal Line
t.forward(300)

#move the pen
t.penup()
t.goto(0, -150)
t.pendown()

# Vertical Line
t.setheading(90)
t.forward(300)

#move the pen
t.penup()
t.goto(-125, -125)
t.pendown()

# Left Vertical Line
t.setheading(45)
t.forward(350)

#move the pen
t.penup()
t.goto(-125, 125)
t.pendown()

# Right Vertical Line
t.setheading(315)
t.forward(350)

#move the pen
t.penup()
t.goto(-70, -70)
t.pendown()

# draw the head, i.e. circle of radius 100
t.circle(100)

#move the pen
t.penup()
t.goto(-50, -50)
t.pendown()

# draw the head, i.e. circle of radius 70
t.circle(70)

#move the pen
t.penup()
t.goto(-30, -30)
t.pendown()

# draw the head, i.e. circle of radius 40
t.circle(40)

#move the pen
t.penup()
t.goto(-5, -5)
t.pendown()

# draw the head, i.e. circle of radius 7
t.circle(7)
