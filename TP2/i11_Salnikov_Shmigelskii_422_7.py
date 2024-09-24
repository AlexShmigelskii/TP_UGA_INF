"""
-----------------------------------------------------------------------------
i11_Salnikov_Shmigelskii_422_7.py : Une IA pour le prix du gros lot, groupe IMA-05-A

Salnikov Artem <Artem.Salnikov@etu.univ-grenoble-alpes.fr>
Shmigelskii Aleksandr <Aleksandr.Shmigelskii@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""

import random

# L'utilisateur spécifie combien de parties chaque IA doit jouer pour chaque nombre secret possible
n = int(input("Combien de parties voulez-vous que chaque IA joue pour chaque nombre secret (0 à 100) ? "))

# Vérifier que l'utilisateur a entré un nombre positif
if n <= 0:
    print("Le nombre de parties doit être positif.")

else:

    # Début du test pour chaque nombre secret possible de 0 à 100
    nombre_secret = 0

    while nombre_secret <= 100:

        # Variables pour suivre le nombre total d'essais pour chaque IA
        total_essais_aléatoire = 0
        total_essais_intelligent = 0

        parties_jouées = 0

        # Jouer n parties pour chaque nombre secret
        while parties_jouées < n:
            """
            IA aléatoire
            """
            essais_aléatoire = 0
            borne_inf = 0
            borne_sup = 100
            nombre_trouvé = False

            while not nombre_trouvé:

                # Proposer un nombre aléatoire
                proposition = random.randint(borne_inf, borne_sup)
                essais_aléatoire += 1

                if proposition == nombre_secret:
                    nombre_trouvé = True
                elif proposition < nombre_secret:
                    borne_inf = proposition + 1
                else:
                    borne_sup = proposition - 1

            total_essais_aléatoire += essais_aléatoire

            """
            IA intelligente
            """
            essais_intelligent = 0
            borne_inf = 0
            borne_sup = 100
            nombre_trouvé = False

            while not nombre_trouvé:

                # Proposer le milieu entre les bornes
                proposition = (borne_inf + borne_sup) // 2
                essais_intelligent += 1

                if proposition == nombre_secret:
                    nombre_trouvé = True

                elif proposition < nombre_secret:
                    borne_inf = proposition + 1
                    
                else:
                    borne_sup = proposition - 1

            total_essais_intelligent += essais_intelligent

            parties_jouées += 1

        # Calculer et afficher la moyenne d'essais pour chaque IA sur ce nombre secret
        moyenne_aléatoire = total_essais_aléatoire / n
        moyenne_intelligent = total_essais_intelligent / n

        # Affichage sous forme d'histogramme
        print("[", nombre_secret, "]" + '*' * int(moyenne_intelligent), sep='')
        print("[", nombre_secret, "]" + '-' * int(moyenne_aléatoire), sep='')
        nombre_secret += 1


# Bloc de tests
# _________________Test1___________________________
# Combien de parties voulez-vous que chaque IA joue pour chaque nombre secret (0 à 100) ? 0
# Le nombre de parties doit être positif.
# _________________________________________________
# 
# 
# _________________Test2___________________________
# Combien de parties voulez-vous que chaque IA joue pour chaque nombre secret (0 à 100) ? -5
# Le nombre de parties doit être positif.
# _________________________________________________
# 
# 
# _________________Test3___________________________
# Combien de parties voulez-vous que chaque IA joue pour chaque nombre secret (0 à 100) ? 100
# [0]******
# [0]----
# [1]*******
# [1]-----
# ...
# [98]-----
# [99]******
# [99]-----
# [100]*******
# [100]-----
# _________________________________________________

