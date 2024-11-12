def capital(nba, deb):
    return capital(nba - 1, deb*1.05 - 11) if nba != 0 else deb

def gagne(nba, deb):
    pass
