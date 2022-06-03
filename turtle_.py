from turtle import *

def sq(w, h,c):
    color(c)
    begin_fill()
    for i in range(2):
        fd(w);  rt(90); fd(h); rt(90)
    end_fill()
def tr(w,c):
    color(c)
    begin_fill()
    fd(w);  rt(40-180)
    fd(int(w*0.6527036446661393))
    rt(heading()-360)
    end_fill()
speed(1000)
w = 300

sq(w,int(w-(w/10)),"gray")
tr(w,"red")
pu(); goto((w/7),-(w/3))
sq(int(w/5),int(w/5),"blue")
goto((w/1.5),-(w/3)); sq(int(w/5),int(w/5),"blue")
goto(int(w/2.25),-int(w-(w/10))); sq(int((w/7)),-int(w/6),"tomato")

input("")