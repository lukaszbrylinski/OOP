import colorgram
from turtle import Turtle, Screen
import random
# colors = colorgram.extract('C:/Users/lukas/PycharmProjects/Day-18/hirst-painting/image.jpg', 40)
# tuple_of_colors = []
# for color in colors:
#     tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     tuple_of_colors.append(tuple)
# print(tuple_of_colors)

tim = Turtle()
screen = Screen()
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188),  (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]
x_pos = -100
y_pos = -100
tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.setposition(x_pos, y_pos)
j = 1
screen.colormode(255)
tim.pendown()
for i in range (10):
    for i in range (10):
        #index_value = j % len(color_list)
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
        j += 1
    y_pos += 50
    tim.teleport(x_pos, y_pos)


screen.exitonclick()