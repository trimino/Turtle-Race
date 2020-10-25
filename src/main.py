from racer import * 
from time import sleep


def start_game():
    num_turtles = 8
    screen_x = 500
    screen_y = 500

    # Background
    mainwin = turtle.Screen()
    mainwin.screensize(screen_x, screen_y)
    mainwin.bgcolor('black')

    # Finish Line
    stamp_size = 20
    square_size = 15
    finish_line = 400
    finish = turtle.Turtle()
    finish.hideturtle()
    finish.color('white')
    finish.shape('square')
    finish.shapesize( square_size / stamp_size )
    finish.penup()

    for i in range( 24 ):
        finish.setpos( finish_line, ( (screen_y - 150) - (i * square_size * 2)) )
        finish.stamp()

    for j in range( 24 ):
        finish.setpos( finish_line + square_size, ( ((screen_y - 150) - square_size) - (j * square_size * 2)) )
        finish.stamp()
    

    # Create Racer Objects
    racers = []
    colors = ['yellow', 'blue', 'orange', 'grey', 'green', 'purple', 'red', 'brown']

    x = -1 * ( screen_x - 100 )
    y = screen_y - 150

    for ninja in range( num_turtles ):
        racers.append( Racer( (x, y), x, y, colors[ninja] ) )
        racers[ ninja ].showturtle()
        y = y - 100


    # AI 
    max_distance = -1000
    max_colors = [] 
    
    play  = True
    while play:
        for racer in racers:
            racer.move()

        for racer in racers:
            position = racer.get_position()

            # if there is a new first place turtle keep track of stats
            if position[0] > max_distance:
                max_distance = position[0]
                max_colors.clear()
                max_colors.append( racer.get_color() )
        
            # if we have a tie for first 
            elif position[0] == max_distance:
                max_colors.append( racer.get_color() )

            if max_distance >= finish_line:
                play = False

    sleep(2)


    # Display Winner 
    mainwin.clearscreen()
    mainwin.bgcolor('black')
    finish.hideturtle()
    finish.setpos( 0, 0 )
    
    winners = ' '.join( max_colors )
    winners = 'The winners is/are: \n' + winners
    finish.write( winners, align = 'center', font = ("Arial", 56, "normal") )


    mainwin.clearscreen()






while True:
    start_game()


