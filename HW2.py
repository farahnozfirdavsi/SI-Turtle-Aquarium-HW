
import turtle as t 
aq = t.Turtle()
# body (circle) of the fishes)
def draw_body(aq, color, x, y):
  aq.penup()
  aq.goto(x, y)
  aq.fillcolor(color)
  aq.begin_fill()
  aq.circle(50)
  aq.pendown()
  aq.end_fill()
  
# eyes (circle)
def draw_eye():
  aq.fillcolor("saddlebrown")
  aq.begin_fill()
  aq.circle(10)
  aq.end_fill()
  
# bubbles (circle)
def draw_bubble():
  aq.fillcolor("lightcyan")
  aq.begin_fill()
  aq.circle(9)
  aq.end_fill()
  
# tail of fishies (triangle)
def draw_tri(aq, color, x, y, side=75):
  aq.penup()
  aq.goto(x,y)
  aq.fillcolor(color)
  aq.begin_fill()
  for i in range(3):
    aq.forward(side)
    aq.left(120)
  aq.pendown()
  aq.end_fill()
  
  
# sand bottom (rectangle)
def draw_rec(aq, color, x, y, length=550, width=140):
  aq.penup()
  aq.goto(x,y)
  aq.fillcolor(color)
  aq.begin_fill()
  for i in range(2):
    aq.forward(length)
    aq.left(90)
    aq.forward(width)
    aq.left(90)
  aq.pendown()
  aq.end_fill()

# EXTRA CREDIT: my innitials FF
def draw_f():
  aq.pencolor("lightcyan")   
  aq.pensize(6)
  aq.setheading(90)      
  aq.pendown()
  aq.forward(60)       
  aq.setheading(0)      
  aq.forward(20)
  aq.penup()
  aq.backward(20)       
  aq.setheading(270)    
  aq.forward(10)
  aq.setheading(0)     
  aq.pendown()
  aq.forward(20)
  aq.penup()  


  
def draw_aquarium():
  aq.speed("fastest")
  # sand
  draw_rec(aq, "cornsilk", -260, -300)
  
  # tail of the fish
  draw_tri(aq, "darkorange", -140, -135)
  draw_tri(aq, "darkorange",  120,  155)

  # body of fish 
  draw_body(aq, "orange", -100, -100)
  draw_body(aq, "orange",  100,  100)
  
  # eyes for fishie top right
  aq.penup()
  aq.goto(100, 90)
  draw_eye()
  aq.pendown()
  aq.penup()
  aq.goto(60, 170)
  draw_eye()
  aq.pendown()
  # eyes for fishie bottom left
  aq.penup()
  aq.goto(-140, -30)
  draw_eye()
  aq.pendown()
  aq.penup()
  aq.goto(-55, -40)
  draw_eye()
  aq.pendown()
  # bubbles
  aq.penup()
  aq.goto(-100, 140)
  draw_bubble()
  aq.pendown()
  aq.penup()
  aq.goto(-140, 120)
  draw_bubble()
  aq.pendown()
  aq.penup()
  aq.goto(-100, 100)
  draw_bubble()
  aq.pendown()
	# EXTRA CREDIT: my innitials FF
  aq.penup()
  aq.goto(20, -70)        
  draw_f()              
  aq.setheading(0)
  aq.forward(80)         
  draw_f()              

def main():
  screen = t.Screen()
  screen.setup(width=520, height=590)
  screen.bgcolor("skyblue")
  aq.hideturtle()
  draw_aquarium()
  screen.exitonclick()
main()
