
#set up   
#imports and image setups
import turtle as trtl
bigpineapple_ = "big_pineapple.gif"
pineapple_ = "pineapple.gif"
tree_ = "tree.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(pineapple_)
wn.addshape(tree_)
wn.addshape(bigpineapple_)
pineapple = trtl.Turtle()
tree = trtl.Turtle()
tree.shape(tree_)

#2nd 3rd 4th and 5th pineapple setup aswell as the A painter setup

painter = trtl.Turtle()
pineapple.penup()
pineapple.hideturtle()
pineapple2 = trtl.Turtle()
pineapple2.hideturtle()
pineapple2.penup()

pineapple3 = trtl.Turtle()
pineapple3.hideturtle()
pineapple3.penup()

pineapple4 = trtl.Turtle()
pineapple4.hideturtle()
pineapple4.penup()

pineapple5 = trtl.Turtle()
pineapple5.hideturtle()
pineapple5.penup()

#input statements for pinesize and pine number

pine_size = input("Do you want your pineapples do be big or small")
while pine_size != ("small") and pine_size != ("big"):
  print("invalid size!")
  pine_size = input("Do you want your pineapples do be big or small")

if pine_size == ("big"):
  pineapple.shape(bigpineapple_)
  pineapple2.shape(bigpineapple_)
  pineapple3.shape(bigpineapple_)
  pineapple4.shape(bigpineapple_)
  pineapple5.shape(bigpineapple_)
if pine_size == ("small"):
  pineapple.shape(pineapple_)
  pineapple2.shape(pineapple_)
  pineapple3.shape(pineapple_)
  pineapple4.shape(pineapple_)
  pineapple5.shape(pineapple_)

pine_number = int(input("How many pineapples do you want?(up to 5)"))

while pine_number > 5:
   print("Too many pineapples!!!")
   pine_number = int(input("How many pineapples do you want?(up to 5)"))
if pine_number == 1:
  pineapple.goto(-200, 180)
  pineapple.showturtle()
if pine_number == 2:
  pineapple.goto(-300,180)
  pineapple.showturtle()
  pineapple2.goto(-150,180)
  pineapple2.showturtle()
if pine_number == 3:
  pineapple.goto(-300,180)
  pineapple.showturtle()
  pineapple2.goto(-150,180)
  pineapple2.showturtle()
  pineapple3.goto(0,180)
  pineapple3.showturtle()
if pine_number == 4:
  pineapple.goto(-300,180)
  pineapple.showturtle()
  pineapple2.goto(-150,180)
  pineapple2.showturtle()
  pineapple3.goto(0,180)
  pineapple3.showturtle()
  pineapple4.goto(150,180)
  pineapple4.showturtle()
if pine_number == 5:
  pineapple.goto(-300,180)
  pineapple.showturtle()
  pineapple2.goto(-150,180)
  pineapple2.showturtle()
  pineapple3.goto(0,180)
  pineapple3.showturtle()
  pineapple4.goto(150,180)
  pineapple4.showturtle()
  pineapple5.goto(300,180)
  pineapple5.showturtle()
#painter making A symbol to signal to press A
def draw_an_A():

  painter.penup()
  painter.goto(250,125)
  painter.color("black")
  painter.write("A", font=("Arial", 200, "bold"))
  painter.hideturtle() 
  painter.goto(0,0)
draw_an_A()
#falling function
def pineapple_fall():
  pineapple.right(90)
  pineapple.forward(380)
  pineapple2.right(90)
  pineapple2.forward(380)
  pineapple3.right(90)
  pineapple3.forward(380)
  pineapple4.right(90)
  pineapple4.forward(380)
  pineapple5.right(90)
  pineapple5.forward(380)
  pineapple.hideturtle()
  pineapple2.hideturtle()
  pineapple3.hideturtle()
  pineapple4.hideturtle()
  pineapple5.hideturtle()
#the A
painter.goto(250,125)
painter.color("red")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("orange")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("yellow")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("green")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("blue")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("purple")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("red")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("orange")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("yellow")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("green")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("blue")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("purple")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("red")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("orange")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.color("yellow")
painter.write("A", font=("Arial", 200, "bold"))
painter.goto(250,125)
painter.hideturtle()
painter.right(360)
painter.clear()
#onkeypress commands
wn.listen()
wn.onkeypress(pineapple_fall, "a")
wn.mainloop()

