def lundi(mot):
    return mot + " " + mot


def mardi(mot):
    if len(mot) % 2 == 0:
        res = mot + "-" + mot + "-" + mot + "-" + mot + "-" + mot + "-" + mot

    else:
        res = mot + "," + mot + "," + mot

    return res


def mercredi(mot):
    return "impair" if len(mot) % 2 != 0 else mot


def jeudi(mot):
    modulo_3 = len(mot) % 3
    return mot*modulo_3


def vendredi(mot):
    res = ''
    if "a" <= mot[0] <= "z":
        for i in range(1, len(mot)):
            res += mot[i]

    else:
        for i in range(len(mot) - 1):
            res += mot[i]

    return res


def samedi(mot):
    res = ''
    for c in mot:
        res = c + res
    return res


def dimanche(mot):
    res = ''
    for c in mot:
        res = res + c + " "
    return res


def transforme(mot, num_jour):
    if num_jour == 1:
        res = lundi(mot)
    elif num_jour == 2:
        res = mardi(mot)
    elif num_jour == 3:
        res = mercredi(mot)
    elif num_jour == 4:
        res = jeudi(mot)
    elif num_jour == 5:
        res = vendredi(mot)
    elif num_jour == 6:
        res = samedi(mot)
    elif num_jour == 7:
        res = dimanche(mot)

    return res


def replace_alphabetique(mot):
    res = ''
    for c in mot:
        res += str(ord(c) - ord('a') + 1)
    return res


def tout_min(mot):
    res = ''
    for c in mot:
        if "A" <= c <= "Z":
            res += chr(ord(c) + (ord("a") - ord("A")))
        
        else:
            res += c

    return res


def tout_maj(mot):
    res = ''
    for c in mot:
        if "a" <= c <= "z":
            res += chr(ord(c) - (ord("a") - ord("A")))
        
        else:
            res += c

    return res




