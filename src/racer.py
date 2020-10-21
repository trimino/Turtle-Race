'''
David Trimino

Here is the blueprint for the Racer class for the turtle race game
Racer class inherits from the Turtle class (from the turtle module)

Methods:
    * move: move turtle in the forward postion
    * reset: helpful to make a new a game to start at the beginning postion 
    * get_positon: helpful to see if the turtle crossed the finished line first

'''

import turtle
import random 

class Racer (turtle.Turtle):
    def __init__(self, start_position, x_position, y_position, color):
        '''
        if you redefine a method (such as __init__) in a child class then it is your responsibility to
        call the parent's method in order to have the parent's behviour
        '''
        super(Racer, self).__init__( shape = 'turtle' )
        self.s = start_position 
        self.x = x_position
        self.y = y_position
        self.hideturtle()
        self.penup()
        self.color( color )
        self.setpos( self.x, self.y ) 
        self.setheading(0)

    def move(self):
        randm = random.randint( 1, 15 )
        self.x = self.x + randm 
        self.pendown()
        self.forward( randm ) 

    def reset(self):
        self.setpos( self.start ) 

    def get_position(self):
        return (self.x, self.y )

