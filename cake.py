import turtle


# Draws a rectangle
def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


# Draws a triangle
def triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)


# Draws a cake
def cake(width, height):
    turtle.pendown()
    for i in range(1, 4):
        rectangle(width, i/3*height)
    turtle.forward(1/2*width - 1/2*height)
    turtle.left(90)
    turtle.penup()
    turtle.forward(height)
    turtle.right(90)
    turtle.pendown()
    triangle(height)


# Test 1
turtle.color("blue")
cake(100, 25)

# Moves turtle back to starting position and goes forward to make space for test #2
turtle.penup()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(1/2*100 - 1/2*25)
turtle.right(180)
turtle.forward(120)

# Test 2
turtle.color("orange")
cake(50, 25)

# Keeps drawing open until window is clicked
turtle.Screen().exitonclick()
