import turtle


def draw_square(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    # Start top-left.
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle._down()
    my_turtle.begin_fill()
    # Go top-right.
    my_turtle.goto(points[1][0], points[1][1])
    # Go bottom-right.
    my_turtle.goto(points[2][0], points[2][1])
    # Go bottom-left.
    my_turtle.goto(points[3][0], points[3][1])
    # Go back to top-left.
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()

    my_points = [[-200, 200], [200, 200], [200, -200], [-200, -200]]

def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski_square(points, degree, my_turtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_square(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski_square(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2]), get_mid(points[0], points[3])],
            degree - 1,
            my_turtle
        )
        sierpinski_square(
            [points[1], get_mid(points[1], points[0]), get_mid(points[1], points[2]), get_mid(points[1], points[2])],
            degree - 1,
            my_turtle
        )
        # sierpinski_square(
        #     [points[2], get_mid(points[2], points[1]), get_mid(points[1], points[2]), get_mid(points[2], points[3])],
        #     degree - 1,
        #     my_turtle
        # )
        # sierpinski_square(
        #     [points[3], get_mid(points[3], points[1]), get_mid(points[3], points[2]), get_mid(points[1], points[3])],
        #      degree - 1,
        #      my_turtle
        # )


def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed(5)
    my_win = turtle.Screen()
    my_points = [[-200, 200], [200, 200], [200, -200], [-200, -200]]
    sierpinski_square(my_points, 5, my_turtle)
    my_win.exitonclick()

main()