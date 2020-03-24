import turtle


#1shape=square#
'''
skk=turtle.Turtle()
for i in range(4):
    skk.forward(50)
    skk.right(90)
print(skk.position())
turtle.done()
'''



#2Shape=STAR#
'''
star=turtle.Turtle()
for i in range(50):
    star.forward(50)
    star.right(144)
turtle.done()
'''



#3shape=HEXAGON#
'''
polygon=turtle.Turtle()
num_sides=6
side_length=70
angle=360.0/num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()
'''



#4shape=Spiral Square outside in and inside out
'''wn=turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk=turtle.Turtle()
skk.color("blue")

def sqrfunc(size):
    for i in range(4):
        skk.fd(size)
        skk.left(90)
        size=size-5
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
'''


#5shape=Rainbow Benzene
'''
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t=turtle.Pen()
print(type(t))
turtle.bgcolor("black")
for x in range(150):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
'''

#turtle.setheading(180)
#print(turtle.position())
#turtle.circle(120,120,4)
#turtle.speed(x)
#turtle.position()
#turtle.setpos(x,y)

#use tof turtle.undo
'''for i in range(4):
    turtle.fd(50); turtle.lt(80)
for i in range(8):
    turtle.undo()'''
