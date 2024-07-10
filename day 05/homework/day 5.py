from turtle import *



#step 1: draw a square
speed(20)
width(9)
color("black")
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
goto (280, 200)
pendown()

left (180)
forward(25)
left (90)
forward(40)
left (180)
left(270)
forward (25)
right(90)
forward(60)
right(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
right(90)
forward(60)
right(90)
forward(25)
left(90)
forward(40)
left(90)
forward(25)
right(90)
forward(45)
left(180)
forward(308)

penup()
goto (20, 10)
pendown()


left(90)
forward(70)
right(90)
forward(13)
left(90)
forward(13)
right(90)
forward(15)
right(90)
forward(13)
left(90)
forward(10)
right(90)
forward(73)
right(90)
forward(9)
right(90)
forward(35)
left(90)
forward(15)
left(90)
forward(35)
right(90)
forward(7)
left(180)
forward(1)
left(90)
forward(70)
left(90)
forward(10)
left(90)
forward(40)
left(90)

penup()
goto (55, 40)
pendown()

forward(7)
left(90)
forward(41)
left(90)
forward(10)



penup()
goto(230,12)
pendown()



right(90)
forward(70)
right(90)
forward(10)
left(90)
forward(13)
right(90)
forward(13)
right(90)
forward(10)
left(90)
forward(10)
right(90)
forward(73)
right(90)
forward(9)
right(90)
forward(35)
left(90)
forward(15)
left(90)
forward(35)
right(90)
forward(7)
left(180)
forward(1)
left(90)
forward(70)
left(90)
forward(10)
left(90)
forward(40)
left(90)

penup()
goto (263, 40)
pendown()

forward(7)
left(90)
forward(43)
left(90)
forward(10)







color("black")
penup()
goto( 200, 300)
pendown()

begin_fill()
left(90)
forward(70)
right(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

#GOA
penup()
goto( 110, 320)
pendown()

#G
color("green")
right(90)
forward(2)
right(90)
forward(10)
right(90)
forward(10)
right(90)
forward(15)
right(90)
forward(20)
right(90)
forward(15)

#O
color("brown")
penup()
goto( 140, 325)
pendown()

circle(10)

#A
color("green")
penup()
goto( 160, 310)
pendown()

left(240)
forward(25)
right(150)
forward(25)

left(180)
forward(15)
left(100)
forward(10)


















exitonclick()