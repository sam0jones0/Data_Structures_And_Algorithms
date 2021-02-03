import turtle


# Draw Sierpinski triangle recursively using turtle library.


def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle._down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()


def get_mid(p1, p2):
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, my_turtle):
    colormap = ["blue", "red", "green", "white", "yellow", "violet", "orange"]
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski(
            [points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            my_turtle
        )
        sierpinski(
            [points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])],
            degree - 1,
            my_turtle
        )
        sierpinski(
            [points[2], get_mid(points[2], points[1]), get_mid(points[0], points[2])],
            degree - 1,
            my_turtle
        )


def main():
    my_turtle = turtle.Turtle()
    my_turtle.speed(1)
    my_win = turtle.Screen()
    my_points = [[-180, -150], [0, 150], [180, -150]]
    sierpinski(my_points, 5, my_turtle)
    my_win.exitonclick()


main()


#############################################


# def draw_spiral(my_turtle, line_len):
#     if line_len > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(91)
#         draw_spiral(my_turtle, line_len - 1)
#
#
# my_turtle = turtle.Turtle()
# my_turtle.speed(10)
# my_win = turtle.Screen()
# draw_spiral(my_turtle, 100)
# my_win.exitonclick()


#############################


# def tree(branch_len, pen_size, t):
#     if branch_len < 10:
#         t.pencolor("red")
#     if branch_len > 5 and pen_size > 0:
#         t.pensize(pen_size)
#         t.forward(branch_len)
#         t.right(20)
#         pen_size -= 1
#         tree(branch_len - 15, pen_size, t)
#         t.left(40)
#         tree(branch_len - 15, pen_size, t)
#         t.right(20)
#         t.backward(branch_len)
#
# def main():
#     t = turtle.Turtle()
#     my_win = turtle.Screen()
#     t.penup()
#     t.goto(0, -200)
#     t.pendown()
#     t.speed(1000)
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(140, 10, t)
#     my_win.exitonclick()
#
# main()









