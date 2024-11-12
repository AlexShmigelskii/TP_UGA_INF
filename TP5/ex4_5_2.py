"""Chiffre de César - par décalage"""
def encrypt_lettre(lt):
    return chr(ord(lt) + 3) if "A" <= lt < "X" else chr(ord(lt) + 3 - (ord("Z") - ord("A") + 1)) 


def encrypt_mot(mot):
    res = ''
    for c in mot:
        res += encrypt_lettre(c)
    return res


assert encrypt_mot("PYTHON") == "SBWKRQ"
assert encrypt_mot("XYZ") == "ABC"


"""Chiffrement numérique"""
def encrypt_lettre_numeriquement(lt):
    if "a" <= lt <= "z":
        res = str(ord(lt) - ord("a") + 1)
    
    else:
        res = str(ord(lt) - ord("A") + 1)

    return res


def encrypt_mot_numeriquement(mot):
    res = encrypt_lettre_numeriquement(mot[0])
    for i in range(1, len(mot)):
        res = res + "+" + encrypt_lettre_numeriquement(mot[i])

    return res


def encrypt_sentence_numeriquement(ch):
    res = ''
    mot = ''
    count = 0
    l = len(ch)

    # tant_que sentence
    while count <= len(ch):

        # while pas d'espace
        while count < len(ch) and ( "a" <= ch[count] <= "z" or "A" <= ch[count] <= "Z"):
            mot += ch[count]
            count += 1

        # mot est trouvé
        if mot:
            res += encrypt_mot_numeriquement(mot)
        count += 1


        if count <= len(ch):
            res += ch[count - 1]

        mot = ''
    
    return res


assert encrypt_lettre_numeriquement("a") == "1"
assert encrypt_mot_numeriquement("Bonjour") == "2+15+14+10+15+21+18"
assert encrypt_mot_numeriquement("tous") == "20+15+21+19"
assert encrypt_sentence_numeriquement("Bonjour a tous") == "2+15+14+10+15+21+18 1 20+15+21+19"
assert encrypt_sentence_numeriquement("Bonjour, a tous!") == "2+15+14+10+15+21+18, 1 20+15+21+19!"
