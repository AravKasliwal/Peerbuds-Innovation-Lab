import turtle

def polygon_draw(sides, length):
    shape = turtle.Turtle()
    angle = 360.0 / sides
    for i in range(sides):
        shape.forward(length)
        shape.right(angle)
    turtle.done()

polygon_draw(5, 100)