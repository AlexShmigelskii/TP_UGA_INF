import turtle

NUM_LIGNE = 5
NUM_FIGURE= int(input("Nombre figures par ligne: "))
RAYON = 20
NBCIRCLES = 10
ESPACE = 5
SPEED = 0
STARTX, STARTY = (-200, 200)

turtle.speed(SPEED)

def rosace(nb, r):
    """Dessin rosace"""
    num_circle = 0
    while num_circle < nb:
        turtle.circle(r)
        turtle.right(360/nb)
        num_circle += 1

    turtle.up()
    turtle.forward(RAYON * 4 + ESPACE)
    turtle.down()



num_ligne = 0
while num_ligne < NUM_LIGNE:

    turtle.up()
    turtle.goto(STARTX, STARTY - (RAYON * 4 + ESPACE) * num_ligne)
    turtle.down()

    num_figure = 0
    while num_figure < NUM_FIGURE:

        rosace(NBCIRCLES, RAYON)

        num_figure += 1
    
    num_ligne += 1

turtle.hideturtle()
turtle.done()

