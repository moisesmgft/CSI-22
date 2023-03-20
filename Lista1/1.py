import turtle

t = turtle.Turtle()

def square(size):
    t.pendown()
    for i in range(4):
        t.fd(size)
        t.rt(90)

def reposition():
    t.penup()
    for i in [-1,1]:
        t.fd(10*i)
        t.rt(90*i)

if __name__ == "__main__":
    for i in range(1,5):
        square(20*i)
        reposition()
