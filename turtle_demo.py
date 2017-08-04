import turtle

t = turtle.Turtle()

colors = ["red", "green", "blue", "yellow"]
for c in colors:
    t.color(c)
    t.fd(100)
    t.right(90)

turtle.done()ru