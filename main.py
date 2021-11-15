#A Maze game
import turtle
import math

wn = turtle.screen()
wn.bgcolour("black")
wn.title("A Maze Game")
wn.setup(700,700)

#Register shapes
turtle.register_shape("wizard_right.gif")
turtle.register_shape("wizard_left.gif")
turtle.register_shape("treasure.gif")
turtle.register_shape("wall.gif")

#Create Pen
class Pen(turtle.Turtle):
  def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.colour("white")
    self.penup()
    self.speed(0)
  