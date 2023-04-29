import turtle
import random


def draw_polygon(turt, n, l):
    """'turt' is turtle object, 'n' is number of sides, 'l' is length of each side"""
    for i in range(n):
        turt.forward(l)
        turt.left(360 / n)


def radial_pattern(turt, n, l, numshapes):
    """draws an n-polygon with sides l long numshapes times in a circular pattern"""
    for i in range(numshapes):
        draw_polygon(turt, n, l)
        turt.left(360 / numshapes)


def radial_pattern_filled_random(turt, n, l, numshapes):
    turt.fillcolor(random.randint(0, 255),
                   random.randint(0, 255),
                   random.randint(0, 255))
    turt.begin_fill()
    radial_pattern(turt, n, l, numshapes)
    turt.end_fill()


def main():
    t = turtle.Turtle()
    t.screen.colormode(255)
    t.speed(1)
    t.up()

    x = -t.screen.window_width()+200
    y = -t.screen.window_height()+200
    print(x, y)
    t.goto(x, y)
    t.setheading(180)
    t.down()
    t.backward(77)

    turtle.done()


if __name__ == '__main__':
    main()
