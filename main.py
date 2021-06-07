# import colorgram

# colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle
import random

turtle.colormode(255)
color_list = [(202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124),
              (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72),
              (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172),
              (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155),
              (175, 99, 101), (176, 192, 209)]
circle_shape = turtle.Turtle()
circle_shape.hideturtle()
circle_shape.penup()
circle_shape.setheading(225)
circle_shape.forward(300)
circle_shape.setheading(0)
circle_shape.speed("fastest")
for _ in range(10):
    for _ in range(10):
        circle_shape.dot(20, random.choice(color_list))
        circle_shape.forward(50)
    circle_shape.setheading(90)
    circle_shape.forward(50)
    circle_shape.setheading(180)
    circle_shape.forward(500)
    circle_shape.setheading(0)

screen = turtle.Screen()
screen.exitonclick()