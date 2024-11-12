def approxPiRang(n):
    """
    calcule l'approximation de pi avec n terms
    """
    signe = 1
    somme = 0
    for d in range(1, n*2, 2):
        somme += signe/d
        signe = -signe
    
    return somme * 4


def approxPiPrec(p):
    """
    calcule la valeur du range n nécessaire pour
    obtenir une approx de pi ayant précesion p
    """
    from math import pi
    n = 1
    while abs(approxPiRang(n) - pi) > p:
        n += 1
    return n


# Programme principale

from random import randint

PROMT_PREC = "Precesion? "
PROMT_REJ = "Rejouer? "
flag_rejouer = True

print("Quadrature de Leibniz, bienvenue")

while flag_rejouer:
    precesion = float(input(PROMT_PREC))
    print("Estimation de precision", precesion, "atteinte au rang", approxPiPrec(precesion))
    flag_rejouer = input(PROMT_REJ) == "oui"

# tire un entier i au hasard entre 10 et 20 inclus
# et affiche l'estimation de pi obtenue au rang i

i = randint(10, 20)
print("Estimation de pi au rang", i, "=", approxPiRang(i))
