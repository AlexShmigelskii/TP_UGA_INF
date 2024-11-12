# Moyenne
def creer_liste_positive():
    """
    Crée et renvoie liste des nombres strictement positifs
    """
    MSG = "nb? "
    lst = []
    nb = int(input(MSG))
    while nb != 0:
        if nb > 0: lst.append(nb)
        nb = int(input(MSG))


    return lst


def calculer_moyenne(li):
    """
    Calcule la moyenne arithmétique de la liste
    """
    somme = 0
    for el in li: somme += el

    return somme / len(li)


# Inversion
def inverse(lst):
    """
    Inverse l'ordre des éléments d'une liste (modifie la liste en place).
    """
    n = len(lst)
    for i in range(n // 2):
        # Échange des éléments symétriques par rapport au centre
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

my_list = [1, 2, 3, 4]
print(my_list)
inverse(my_list)
print(my_list)
