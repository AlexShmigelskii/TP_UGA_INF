"""
-----------------------------------------------------------------------------
i11_Salnikov_Shmigelskii_422_5.py : Une IA pour le prix du gros lot, groupe IMA-05-A

Salnikov Artem <Artem.Salnikov@etu.univ-grenoble-alpes.fr>
Shmigelskii Aleksandr <Aleksandr.Shmigelskii@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""

import random

# Demander à l'utilisateur combien de parties l'ordinateur doit jouer
n = int(input("Combien de parties voulez-vous que l'ordinateur joue ? "))

"""
IA aléatoire
"""

# Dire à l'utilisateur qu'il a tort
if n <= 0:
    print("n doit être positive si vous voulez jouer.")

# Initialiser le total des essais
total_essais_aléatoire = 0
parties_jouees_aléatoire = 0

# Boucle pour jouer n parties
while parties_jouees_aléatoire < n and n > 0:
    print("\n--------Partie", parties_jouees_aléatoire + 1, "--------")

    # Initialiser les bornes pour chaque partie
    borne_inf = 0
    borne_sup = 100
    nombre_secret = random.randint(borne_inf, borne_sup)
    essais = 0
    nombre_trouve_aléatoire = False

    # Boucle pour deviner le nombre dans chaque partie
    while not nombre_trouve_aléatoire:
        
        # Proposer un nombre aléatoire entre les bornes
        proposition = random.randint(borne_inf, borne_sup)
        essais += 1  # Incrémenter le nombre d'essais
        print("Je propose", proposition)

        if proposition == nombre_secret:
            # Le nombre a été trouvé
            print("J'ai trouvé le nombre secret", nombre_secret, "en", essais, "essais.")
            print("-----------------------------")
            nombre_trouve_aléatoire = True
        
        elif proposition < nombre_secret:
            # La proposition est trop petite, ajuster la borne inférieure
            borne_inf = proposition + 1
        
        else:
            # La proposition est trop grande, ajuster la borne supérieure
            borne_sup = proposition - 1

    # Ajouter le nombre d'essais de cette partie au total
    total_essais_aléatoire += essais

    # Incrémenter le compteur de parties jouées
    parties_jouees_aléatoire += 1

if n > 0:
    # Calculer et afficher la moyenne d'essais par partie
    moyenne_essais_aléatoire = total_essais_aléatoire / n

"""
IA intellegente
"""

# Initialiser le total des essais
total_essais_intellegent = 0
parties_jouees_intellegent = 0

# Boucle pour jouer n parties
while parties_jouees_intellegent < n:
    print("\n--------Partie", parties_jouees_intellegent + 1, "--------")

    # Initialiser les bornes pour chaque partie
    borne_inf = 0
    borne_sup = 100
    nombre_secret = random.randint(borne_inf, borne_sup)
    essais = 0
    nombre_trouve_intellegent = False

    # Boucle pour deviner le nombre dans chaque partie
    while not nombre_trouve_intellegent:

        # Proposer le milieu entre les bornes
        proposition = (borne_inf + borne_sup) // 2
        essais += 1  # Incrémenter le nombre d'essais
        print("Je propose", proposition)

        if proposition == nombre_secret:
            # Le nombre a été trouvé
            print("J'ai trouvé le nombre secret", nombre_secret, "en", essais, "essais.")
            print("-----------------------------")

            nombre_trouve_intellegent = True
            
        elif proposition < nombre_secret:
            # La proposition est trop petite, ajuster la borne inférieure
            print("Indice : trop petit (p).")
            borne_inf = proposition + 1
        else:
            # La proposition est trop grande, ajuster la borne supérieure
            print("Indice : trop grand (g).")
            borne_sup = proposition - 1

    # Ajouter le nombre d'essais de cette partie au total
    total_essais_intellegent += essais

    # Incrémenter le compteur de parties jouées
    parties_jouees_intellegent += 1

if n > 0:
    # Calculer et afficher la moyenne d'essais par partie
    moyenne_essai_intellegent = total_essais_intellegent / n
    print("\nL'ordinateur a joué", n, "parties et a utilisé en moyenne", moyenne_essais_aléatoire, "essais par partie aléatoire. ")
    print("L'ordinateur a joué", n, "parties et a utilisé en moyenne", moyenne_essai_intellegent, "essais par parti intellegent.")


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
# _________________Test3___________________________
# Combien de parties voulez-vous que l'ordinateur joue ? 2
# 
# --------Partie 1 --------
# Je propose 34
# ...
# L'ordinateur a joué 2 parties et a utilisé en moyenne 10.5 essais par partie aléatoire. 
# L'ordinateur a joué 2 parties et a utilisé en moyenne 6.5 essais par parti intellegent.
# 
# _________________________________________________
# 
# 
# _________________Test4___________________________
# Combien de parties voulez-vous que l'ordinateur joue ? 2
# 
# --------Partie 1 --------
# Je propose 34
# ...
# L'ordinateur a joué 1000 parties et a utilisé en moyenne 7.758 essais par partie aléatoire. 
# L'ordinateur a joué 1000 parties et a utilisé en moyenne 5.906 essais par parti intellegent.
# 
# _________________________________________________

