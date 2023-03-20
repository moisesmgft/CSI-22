import turtle

def draw_poly(t, n, sz):
    dg = 360/n
    for i in range(n):
        t.fd(sz)
        t.rt(dg)

if __name__ == "__main__":
    tess = turtle.Turtle()
    draw_poly(tess, 8, 50)