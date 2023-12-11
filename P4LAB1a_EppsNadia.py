import turtle
peter = turtle.Turtle()
peter.shape('turtle')
peter.color('purple')
peter.pensize(5)
for i in [0,1,2,3]:
 peter.forward(50)
 peter.left(90)
#create nick, who is a second turtle object
nick = turtle.Turtle()
nick.shape('turtle')
nick.color('orange')
nick.pensize(3)
for i in [0,1,2,3]:
 nick.forward(100)
 nick.left(120)

turtle.exitonclick()
