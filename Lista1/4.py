from turtle import Turtle

t = Turtle()

def spiral(sz, dg, steps):
    t.rt(180)
    for i in range(1,steps+1):
        t.fd(sz*i)
        t.rt(dg)
        t.fd(sz*i)
        t.rt(dg)

if __name__ == "__main__":
    steps = 25
    spiral(5,90,steps=steps)
    spiral(5,89,steps=steps)
        