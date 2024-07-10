from turtle import *



#step 1: draw a square
speed(9)
width(9)
color("blue")
begin_fill()
forward(300)
left(90)

forward(200)
left(90)

forward(300)
left(90)

forward(200)
left(90)
end_fill()


#end of square

#drawing a door


forward(120)
color("yellow")
begin_fill()
left(90)
forward(120)
right (90)
forward(80)
right(90)
forward(120)
end_fill()

penup()
goto (300, 200)
pendown()

color("black")
begin_fill()
right(150)
forward(280)
left(117)
forward(287)
end_fill()

penup()
goto (5, 50)
pendown()

left(123)
color("yellow")
begin_fill()
forward(70)
left(90)
forward(60)
left(90)
forward(70)
left(90)
forward(60)
end_fill()





exitonclick()