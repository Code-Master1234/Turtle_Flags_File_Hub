import turtle
turtle.setup(width=600, height=400)
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.pensize(4)
turtle.pencolor("red")
turtle.fillcolor("red")
turtle.speed(10)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()
