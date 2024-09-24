"""
-----------------------------------------------------------------------------
i11_Salnikov_Shmigelskii_423.py : Bonus : affichage graphique, groupe IMA-05-A

Salnikov Artem <Artem.Salnikov@etu.univ-grenoble-alpes.fr>
Shmigelskii Aleksandr <Aleksandr.Shmigelskii@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""
import random
import matplotlib.pyplot as plt

# L'utilisateur spécifie combien de parties chaque IA doit jouer pour chaque nombre secret possible
n = int(input("Combien de parties voulez-vous que chaque IA joue pour chaque nombre secret (0 à 100) ? "))

# Vérifier que l'utilisateur a entré un nombre positif
if n <= 0:
    print("Le nombre de parties doit être positif.")

else:
    # Nous n'avons pas trouvé le moyen de le faire sans list()

    # Listes pour stocker les moyennes
    moyennes_aléatoire = []
    moyennes_intelligent = []

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
            IA intelligente (recherche dichotomique)
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

        # Calculer la moyenne
        moyenne_aléatoire = total_essais_aléatoire / n
        moyenne_intelligent = total_essais_intelligent / n
        
        # Ajouter les moyennes aux listes
        moyennes_aléatoire.append(moyenne_aléatoire)
        moyennes_intelligent.append(moyenne_intelligent)

        nombre_secret += 1

    # Création du graphique
    plt.plot(range(101), moyennes_aléatoire, color='blue', label='IA Aléatoire')
    plt.plot(range(101), moyennes_intelligent, color='red', label='IA Intelligente')
    
    # Ajout des titres et légendes
    plt.title('Moyenne d\'essais par IA pour chaque nombre secret')
    plt.xlabel('Nombre secret')
    plt.ylabel('Moyenne d\'essais')
    plt.legend()
    plt.grid()

    # Afficher le graphique
    plt.show()

# La recherche intelligente s'est avérée pire 