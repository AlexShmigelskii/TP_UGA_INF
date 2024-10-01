import turtle

NUM_LIGNE = 10
NUM_FIGURE= int(input("Nombre figures par ligne: "))
COTE = 10
ESPACE = 10
SPEED = 10
STARTX, STARTY = (-200, 200)

turtle.speed(SPEED)

num_ligne = 0
while num_ligne < NUM_LIGNE:

    turtle.up()
    turtle.goto(STARTX, STARTY - (COTE + ESPACE) * num_ligne)
    turtle.down()

    num_figure = 0
    while num_figure < NUM_FIGURE:

        num_cote = 0
        while num_cote < 4:
            turtle.forward(COTE)
            turtle.right(90) 
            num_cote += 1

        turtle.up()
        turtle.forward(COTE + ESPACE)
        turtle.down()

        num_figure += 1

        if num_figure < NUM_FIGURE:

            num_cote = 0
            while num_cote < 3:
                turtle.forward(COTE)
                turtle.right(120) 
                num_cote += 1

            turtle.up()
            turtle.forward(COTE + ESPACE)
            turtle.down()


        num_figure += 1
    
    num_ligne += 1

turtle.hideturtle()
turtle.done()
