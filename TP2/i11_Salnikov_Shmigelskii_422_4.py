"""
-----------------------------------------------------------------------------
i11_Salnikov_Shmigelskii_422_4.py : Une IA pour le prix du gros lot, groupe IMA-05-A

Salnikov Artem <Artem.Salnikov@etu.univ-grenoble-alpes.fr>
Shmigelskii Aleksandr <Aleksandr.Shmigelskii@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""

import random

# Demander à l'utilisateur combien de parties l'ordinateur doit jouer
n = int(input("Combien de parties voulez-vous que l'ordinateur joue ? "))

# Dire à l'utilisateur qu'il a tort
if n <= 0:
    print("n doit être positive si vous voulez jouer.")

# Initialiser le total des essais
total_essais = 0
parties_jouees = 0

# Boucle pour jouer n parties
while parties_jouees < n:
    print("\n--------Partie", parties_jouees + 1, "--------")

    # Initialiser les bornes pour chaque partie
    borne_inf = 0
    borne_sup = 100
    nombre_secret = random.randint(borne_inf, borne_sup)
    essais = 0
    nombre_trouve = False

    # Boucle pour deviner le nombre dans chaque partie
    while not nombre_trouve:

        # Proposer le milieu entre les bornes
        proposition = (borne_inf + borne_sup) // 2
        essais += 1  # Incrémenter le nombre d'essais
        print("Je propose", proposition)

        if proposition == nombre_secret:
            # Le nombre a été trouvé
            print("J'ai trouvé le nombre secret", nombre_secret, "en", essais, "essais.")
            print("-----------------------------")

            nombre_trouve = True
        elif proposition < nombre_secret:
            # La proposition est trop petite, ajuster la borne inférieure
            print("Indice : trop petit (p).")
            borne_inf = proposition + 1
        else:
            # La proposition est trop grande, ajuster la borne supérieure
            print("Indice : trop grand (g).")
            borne_sup = proposition - 1

    # Ajouter le nombre d'essais de cette partie au total
    total_essais += essais

    # Incrémenter le compteur de parties jouées
    parties_jouees += 1

if n > 0:
    # Calculer et afficher la moyenne d'essais par partie
    moyenne_essais = total_essais / n
    print("\nL'ordinateur a joué", n, "parties et a utilisé en moyenne", moyenne_essais, "essais par partie.")



# Bloc de tests
# _________________Test1___________________________
# Combien de parties voulez-vous que l'ordinateur joue ? 0   
# n doit être positive si vous voulez jouer.
# _________________________________________________
# 
# 
# _________________Test2___________________________
# Combien de parties voulez-vous que l'ordinateur joue ? -5
# n doit être positive si vous voulez jouer.
# _________________________________________________
# 
# 
# _________________Test3___________________________
# Combien de parties voulez-vous que l'ordinateur joue ? 100
# 
# --------Partie 1 --------
# Je propose 50
# Je propose 24
# Je propose 11
# Je propose 5
# Je propose 8
# Je propose 9
# J'ai trouvé le nombre secret 9 en 6 essais.
# -----------------------------
# ...
# --------Partie 100 --------
# Je propose 50
# Je propose 75
# Je propose 88
# Je propose 81
# Je propose 84
# Je propose 82
# Je propose 83
# J'ai trouvé le nombre secret 83 en 7 essais.
# -----------------------------
# 
# L'ordinateur a joué 100 parties et a utilisé en moyenne 5.85 essais par partie.
# 
# _________________________________________________
