"""
-----------------------------------------------------------------------------
i11_Salnikov_Shmigelskii_422_1.py : Une IA pour le prix du gros lot, groupe IMA-05-A

Salnikov Artem <Artem.Salnikov@etu.univ-grenoble-alpes.fr>
Shmigelskii Aleksandr <Aleksandr.Shmigelskii@etu.univ-grenoble-alpes.fr>
-----------------------------------------------------------------------------
"""
import random

# Définir les bornes initiales
borne_inf = 0
borne_sup = 100

# Variable pour suivre si le nombre ou erreur sont deviné
nombre_trouve = False
erreur_detectee = False

print("Je cherche un nombre entre", borne_inf,"et", borne_sup, ".")

while not nombre_trouve and not erreur_detectee:
    
    # Vérifier que les bornes sont valides
    if borne_inf > borne_sup:
        print("Il semble que tu as oublié ton nombre, ou il y a eu une erreur.")
        erreur_detectee = True

    # Proposer un nombre aléatoire entre les bornes
    proposition = random.randint(borne_inf, borne_sup)
    print("Je propose", proposition, "?")

    # Demander la réponse de l'utilisateur
    reponse = input("Réponse (p pour trop petit, g pour trop grand, b pour bon) : ")

    if reponse == 'b':
        # Le nombre a été trouvé, on change l'état pour sortir de la boucle
        print("J’ai gagné !")
        nombre_trouve = True

    elif reponse == 'p':
        # Vérifier la cohérence : la proposition ne doit pas être plus grande que la borne supérieure
        if proposition < borne_sup:
            borne_inf = proposition + 1
        else:
            print("Réponse incohérente, proposition trop petite mais bornes incorrectes.")
            erreur_detectee = True

    elif reponse == 'g':
        # Vérifier la cohérence : la proposition ne doit pas être plus petite que la borne inférieure
        if proposition > borne_inf:
            borne_sup = proposition - 1
        else:
            print("Réponse incohérente, proposition trop grande mais bornes incorrectes.")
            erreur_detectee = True

    else:
        # Réponse invalide
        print("Réponse invalide. Veuillez entrer 'p', 'g' ou 'b'.")

    # Afficher les nouvelles bornes si le nombre n'est pas encore trouvé ou qu'il n'y a pas d'erreur
    if not nombre_trouve and not erreur_detectee:
        print("Je cherche un nombre entre", borne_inf, "et", borne_sup, ".")



# Bloc de tests
# _________________Test1___________________________
# Je cherche un nombre entre 0 et 100 .
# Je propose 1 ?
# Réponse (p pour trop petit, g pour trop grand, b pour bon) : p
# Je cherche un nombre entre 2 et 100 .
# Je propose 100 ?
# Réponse (p pour trop petit, g pour trop grand, b pour bon) : g
# ...
# Je propose 26 ?
# Réponse (p pour trop petit, g pour trop grand, b pour bon) : b
# J’ai gagné !
# _________________________________________________
# 
# 
# _________________Test2___________________________
# Je cherche un nombre entre 0 et 100 .
# Je propose 7 ?
# Réponse (p pour trop petit, g pour trop grand, b pour bon) : p   
# Je cherche un nombre entre 8 et 100 .
# Je propose 89 ?
# ...
# Je cherche un nombre entre 22 et 22 .
# Je propose 22 ?
# Réponse (p pour trop petit, g pour trop grand, b pour bon) : g
# Réponse incohérente, proposition trop grande mais bornes incorrectes.
# _________________________________________________
