from turtle import *

#we want to paint a house

#step 1: draw a square
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
  #end of square

  #drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("purple")
left(30)
forward(200)
left(90)
forward(200)
left(90)
forward(150)


color("purple")
left(90)
forward(6)

color("white")
forward(20)

begin_fill()
color("brown")
forward(25)
right(90)
forward(35)
right(90)
forward(25)
right(90)
forward(35)
end_fill()

color("brown")
right(90)
forward(30)

color("white")
forward(120)

begin_fill()
color("brown")
right(90)
forward(35)
right(90)
forward(25)
right(90)
forward(35)
right(90)
forward(25)
end_fill()


exitonclick()