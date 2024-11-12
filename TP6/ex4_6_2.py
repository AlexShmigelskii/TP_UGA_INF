def minimum(li):
    """renvoie l'élément le plus petit de li"""
    minimal = li[0]
    for el in li:
        if el < minimal: minimal = el
    return minimal

assert minimum([1, 2, 3]) == 1
assert minimum([5, 3, 1]) == 1
assert minimum([0]) == 0


def contient(li, elem):
    """renvoie True ssi li contient elem"""
    i = 0
    i_max = len(li) - 1
    flag = False
    while i <= i_max and not flag:
        flag = li[i] == elem
        i += 1
    return flag

assert contient([1, 2, 3], 1) == True
assert contient([1, 2, 3], 2) == True
assert contient([1, 2, 3], 3) == True
assert contient([1, 2, 3], -1) == False


def min_plus_grande_que(li, x):
    """
    renvoie le plus petit élément de li qui 
    est strictiment plus grand que la valeur x
    """
    result = None
    for el in li:
        if el > x:
            if result is None or el < result:
                result = el
    return result
            
assert min_plus_grande_que([1, 2, 3], 1) == 2
assert min_plus_grande_que([1, 2, 3], 2) == 3
assert min_plus_grande_que([1, 2, 3], 3) == None


def minimum2(li):
    """
    Renvoie le deuxième valeur la plus
    petite de li
    """
    min_val = minimum(li)
    return min_plus_grande_que(li, min_val)

assert minimum2([1, 2, 3]) == 2
assert minimum2([1, 2]) == 2
assert minimum2([1, 2, 2, 3, 3]) == 2
assert minimum2([1]) == None


def minimum3(li):
    """
    Renvoie le 2e élément le plus petit
    de li mais au sens large: si li minimum est présent 
    plusieurs fois, alors le 2e minimum a la même valeur
    que le premier
    """

    if len(li) < 2:
        res = None

    else:
        # trouver min_val
        min_val = minimum(li)
        # supprimer la valeur min_val
        li.remove(min_val)
        # trouver un nouveau min_val
        res = minimum(li)

    return res

assert minimum3([1, 2, 3]) == 2
assert minimum3([1, 2]) == 2
assert minimum3([1]) == None
assert minimum3([1, 2, 2]) == 2
assert minimum3([1, 1]) == 1
assert minimum3([1, 1, 2]) == 1



# Temperatures

def proche_zero(lst):
    """
    Renvoie la plus proche de zero.
    En cas de -5 et 5 renverra 5
    """
    if not lst:
        res = 0

    else:
        min_val = lst[0]
        for el in lst:
            if abs(el) < abs(min_val) or (abs(el) == abs(min_val) and el > min_val):
                min_val = el

        res = min_val

    return  res


assert proche_zero([7, -10, 13, 8, 4, -7, -12, -3, 3, 6, -1, -6, 7]) == -1
assert proche_zero([]) == 0
assert proche_zero([6, -5, 5, -10]) == 5


# fonction pour tester proche_zero, ne pas modifier
def tester_fonction(ltemp, res_attendu, num_test) :
    sauvegarde = list(ltemp)
    res = proche_zero(ltemp)

    if res == res_attendu :
        if ltemp == sauvegarde :
            print("Test", num_test, "ok")
        else :
           print("Test", num_test,": résultat ok, mais vous avez modifie la liste en argument de la fonction !")
    else :
        print("Probleme dans test", num_test, ", vous avez trouve", res, "au lieu de", res_attendu, "pour la liste", sauvegarde)

# programme principal, pour tester la fonction proche_zero

ltest = [[1, -2, -8, 4, 5], [-12, -5, -137], [42, -5, 12, 21, 5, 24],
            [42, 5, 12, 21, -5, 24], [-5, -4, -2, 12, -40, 4, 2, 18, 11, 5],
            [3, 1, 5, -1, 4], [3, -2, 5, 12, -2, 4], []]

lres = [1, -5, 5, 5, 2, 1, -2, 0] 

i = 0
while i < len(ltest) :
    tester_fonction(ltest[i],lres[i],i+1)
    i = i + 1


