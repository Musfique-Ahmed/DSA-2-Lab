import turtle
pen = turtle.Turtle()

def drawTriangle(vertices, depth):
    if depth == 0:
        pen.penup()
        pen.goto(vertices[0])
        pen.pendown()
        pen.goto(vertices[1])
        pen.goto(vertices[2])
        pen.goto(vertices[0])
    else:
        mid1 = midPoint(vertices[0], vertices[1])
        mid2 = midPoint(vertices[1], vertices[2])
        mid3 = midPoint(vertices[2], vertices[0])

        drawTriangle([vertices[0], mid1, mid3], depth-1)
        drawTriangle([mid1, vertices[1], mid2] , depth-1)
        drawTriangle([mid2, mid3 ,vertices[2] ], depth-1)



def midPoint(p1, p2):
    return(((p1[0] + p2[0]) / 2), ((p1[1] + p2[1]) / 2))

def sierpinskiTriangle(depth):
    
    pen.speed(0)
    pen.color('blue')
    pen.hideturtle()

    x1 = (-300, -300)
    x2 = (0, 220)
    x3 = (300, -300)
    vertices = [x1,x2,x3]

    drawTriangle(vertices, depth)
    pen.done()

sierpinskiTriangle(6)