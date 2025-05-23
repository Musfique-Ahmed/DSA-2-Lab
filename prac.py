# import turtle
# pen = turtle.Turtle()
# pen.speed(2)
# x1 = (-300, -300)
# x2 = (0, 220)
# x3 = (300, -300)

# def draw_triangle(x1, x2, x3):
#     pen.penup()
#     pen.goto(x1)
#     pen.pendown()
#     pen.goto(x2)
#     pen.goto(x3)
#     pen.goto(x1)
#     # draw_triangle(x1, x2, x3)

# draw_triangle(x1, x2, x3)


import turtle

def draw_triangle(vertices, depth):
    """ Recursively draws the Sierpiński Triangle """
    if depth == 0:
        # Draw the triangle by connecting the vertices
        turtle.penup()
        turtle.goto(vertices[0])
        turtle.pendown()
        turtle.goto(vertices[1])
        turtle.goto(vertices[2])
        turtle.goto(vertices[0])
    else:
        # Calculate midpoints
        mid1 = midpoint(vertices[0], vertices[1])
        mid2 = midpoint(vertices[1], vertices[2])
        mid3 = midpoint(vertices[2], vertices[0])

        # Recursively draw three smaller triangles
        draw_triangle([vertices[0], mid1, mid3], depth - 1)
        draw_triangle([mid1, vertices[1], mid2], depth - 1)
        draw_triangle([mid3, mid2, vertices[2]], depth - 1)

def midpoint(p1, p2):
    """ Returns the midpoint between two points """
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(depth):
    """ Sets up the turtle and starts recursion """
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.color("blue")
    
    # Define initial triangle vertices
    # vertices = [(-200, -150), (0, 150), (200, -150)]
    vertices = [(-300, -300), (0, 220), (300, -300)]
    
    draw_triangle(vertices, depth)
    turtle.hideturtle()
    turtle.done()

# Set recursion depth (increase for more detail)
sierpinski(6)
