"""
-----------------------------------------------------------------------------
i11_Salnikov_Shmigelskii_422_2.py : Une IA pour le prix du gros lot, groupe IMA-05-A

Salnikov Artem <Artem.Salnikov@etu.univ-grenoble-alpes.fr>
Shmigelskii Aleksandr <Aleksandr.Shmigelskii@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""
import random

# Le programme choisit un nombre secret aléatoire entre 0 et 100
nombre_secret = random.randint(0, 100)

# Définir les bornes initiales
borne_inf = 0
borne_sup = 100

# Variable pour compter le nombre d'essais
essais = 0

# Variable pour suivre si le nombre est deviné
nombre_trouve = False

print("Le nombre secret a été choisi.")

while not nombre_trouve:

    # Proposer un nombre aléatoire entre les bornes
    proposition = random.randint(borne_inf, borne_sup)
    essais += 1  # Incrémenter le nombre d'essais
    print("Je propose", proposition,".")

    # Vérifier si la proposition est égale au nombre secret
    if proposition == nombre_secret:
        print("J’ai trouvé le nombre secret :",proposition ,"en",essais ,"essais !")
        nombre_trouve = True
    elif proposition < nombre_secret:
        print("Indice : trop petit (p).")
        borne_inf = proposition + 1  # Ajuster la borne inférieure
    else:
        print("Indice : trop grand (g).")
        borne_sup = proposition - 1


# Bloc de tests
# _________________Test1___________________________
# Le nombre secret a été choisi.
# Je propose 76 .
# Indice : trop grand (g).
# Je propose 52 .
# Indice : trop grand (g).
# Je propose 40 .
# Indice : trop petit (p).
# Je propose 45 .
# Indice : trop petit (p).
# Je propose 50 .
# _________________________________________________

