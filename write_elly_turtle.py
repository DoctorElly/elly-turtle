import turtle

def write_elly(size):
    turtle.home()
    turtle.clear()
    turtle.pendown()
    turtle.color("purple")
    turtle.shape("turtle")
    turtle.speed(3)
    turtle.pensize(3)

# E
    for i in range(2):
        turtle.rt(180)
        turtle.fd(size)
        turtle.lt(90)
        turtle.fd(size)
        turtle.lt(90)
        turtle.fd(size)

    turtle.penup()
    turtle.fd(size/2)
    turtle.color("blue")

#ll
    for i in range(2):
        turtle.pendown()
        turtle.lt(90)
        turtle.fd(size* 2)
        turtle.lt(180)
        turtle.fd(size* 2)
        turtle.lt(90)
        turtle.penup()
        turtle.fd(size)
        continue

#y
    turtle.color("purple")
    turtle.pendown()
    turtle.lt(120)
    turtle.forward(size)
    turtle.lt(180)
    turtle.forward(size)
    turtle.lt(120)
    turtle.forward(size)
    turtle.lt(180)
    turtle.forward(size* 2)
    turtle.rt(60)
    turtle.forward(size* 2)

# stamp a turtle!
    turtle.penup()
    turtle.forward(size)
    turtle.pensize(7)
    turtle.color("pink")

write_elly(35)
