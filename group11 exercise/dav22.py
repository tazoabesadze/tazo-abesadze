# დევხატოთ dey0-ის გაუმჯობესებული ვერსია

from turtle import*

width(2)
speed(15)

def squear():
    for i in range(4):
        forward(300)
        left(90)

def coordinates(x, y):
    penup()
    goto(x, y)
    pendown()

def samkutxedi():
    forward(300)
    left(120)
    forward(300)
    left(120)
    forward(300)

def panjara():
    for i in range(4):
        left(90)
        forward(80)

def garage_roof():
    forward(150)
    right(120)
    forward(150)
    right(120)
    forward(150)

coordinates(-200, -200)
color("purple")
begin_fill()
squear()
end_fill()

color("red")        # სახურავი
begin_fill()
coordinates(-200, 100)  
samkutxedi()      
end_fill()



coordinates(-100, -200)      # კარები
color("blue")
begin_fill()
right(150)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
end_fill()

coordinates(-175, -20)      # პანჯრები
color("white")
begin_fill()
panjara()
end_fill()
coordinates(-5, -20)    
color("white")
begin_fill()
panjara()
end_fill()      

color("green")          # ხე
begin_fill()
coordinates(-500, 50)
circle(80)  
end_fill()    
coordinates(-440, -29)
color("brown")
begin_fill()
forward(150)
left(90)            
forward(30)
left(90)
forward(150)
end_fill()

color("yellow")         # sun
begin_fill()
coordinates(700, 250)   
circle(90)
end_fill()

coordinates(-700, -300)     # gza
color("grey")
begin_fill()
right(90)
forward(600)
end_fill()
left(90)
forward(100)
right(90)
forward(70)
right(90)
forward(100)
left(90)
forward(700)

coordinates(100, -50)       # garage
color("Orange")
begin_fill()
forward(150)
right(90)
forward(150)
right(90)
forward(150)
end_fill()

coordinates(250, -50)
color("red")
begin_fill()
garage_roof()
end_fill()

coordinates(140, -200)
color("red")
begin_fill()
left(150)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()


exitonclick()