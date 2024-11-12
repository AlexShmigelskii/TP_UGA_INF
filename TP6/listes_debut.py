lst_desord = [2, 12, 7, 9, 3, 4]
lst_croiss = [2, 3, 4, 5, 9, 12]

def parcours(lst):
    i = 0
    while i < len(lst):
        print("Elt d'indice", i, ":", lst[i])
        i += 1

parcours(lst_desord)

def parcours_envers(lst):
    i = len(lst) - 1
    while i >= 0:
        print("Elt d'indice", i, "(enverse) :", lst[i])
        i -= 1

parcours_envers(lst_desord)

def croiss(lst):
    cr = True
    i = 1
    while i < len(lst):
        cr = cr and (lst[i - 1] <= lst[i])
        i += 1
    return cr

print(lst_desord, "est croissante:", croiss(lst_desord))
print(lst_croiss, "est croissante:", croiss(lst_croiss))

print("\n\n")

maliste = [1, 3, 9, 6, 4]
autre = maliste

autre[2] = 42

print(maliste)
print(autre)

def increment(i):
    i = i + 1
    return i

print("\n\n")

def incr_liste(liste):
    i = 0
    while i < len(liste):
        liste[i] = liste[i] + 1
        i = i + 1
    return liste

x = 12
maliste = [1, 3, 9, 6, 4]

print(increment(x))
print(incr_liste(maliste))

print("\n\n")

maliste = [[1], [3], [9], [4]]
print(maliste)

i = 0
while i < len(maliste):
    elt = maliste[i]
    print("indice", i, "contient: ", elt)
    i = i + 1

print("Avant", maliste)
maliste[3] = maliste[2]
maliste[2].append(0)
print("Apres:", maliste)
