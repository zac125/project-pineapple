
#set up 
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
bigpineapple = trtl.Turtle()
# other stuff now
tree.shape(tree_)

pineapple.hideturtle()
pineapple.penup()
pineapple.setposition(-200, 150)
pineapple.showturtle()
pineapple.shape(pineapple_)

bigpineapple.shape(bigpineapple_)










wn.mainloop()
