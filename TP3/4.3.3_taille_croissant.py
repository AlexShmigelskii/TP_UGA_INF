import turtle

NUM_LIGNE = 1
NUM_FIGURE= int(input("Nombre figures par ligne: "))
COTE = 20
AUGMENTATION = 10
ESPACE = 5
SPEED = 0
STARTX, STARTY = (-200, 200)

def carre(cote):
    """Dessin carré avec cote donné"""
    num_cote = 0
    while num_cote < 4:
        turtle.forward(cote)
        turtle.right(90) 
        num_cote += 1

    
    turtle.up()
    turtle.forward(COTE + ESPACE)
    turtle.down()

def triangle(cote) :
    """Dessin triangle avec cote donné"""
    num_cote = 0
    while num_cote < 3:
        turtle.forward(cote)
        turtle.right(120) 
        num_cote += 1

    turtle.up()
    turtle.forward(COTE + ESPACE)
    turtle.down()


turtle.speed(SPEED)

num_ligne = 0
while num_ligne < NUM_LIGNE:

    turtle.up()
    turtle.goto(STARTX, STARTY - (COTE + ESPACE) * num_ligne)
    turtle.down()

    num_figure = 0
    while num_figure < NUM_FIGURE:

        carre(COTE)

        COTE += AUGMENTATION

        num_figure += 1

        if num_figure < NUM_FIGURE:

            triangle(COTE)

            COTE += AUGMENTATION

        num_figure += 1
    
    num_ligne += 1

turtle.hideturtle()
turtle.done()
