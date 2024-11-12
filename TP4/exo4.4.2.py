"""
La bosse des maths
"""

def valeur_abs(x):
    return x if x >= 0 else x * -1


def signe_different(x, y):
    
    res = False

    if (x > 0 and y > 0) or (x < 0 and y < 0):
        res = True

    return res


def f(x):

    return 3*x*x + 2*x + 3


"""
Polynôme
"""

def nb_racines(a, b, c):
    
    res = 0
    d = b**2 - 4 * a * c

    if d == 0:
        res = 1
    
    elif d > 0:
        res = 2
    
    return res


def resolution(a, b, c):

    res1 = None
    res2 = None
    if nb_racines(a, b, c):
        
        d = b**2 - 4 * a * c
        
        res1 = (-b + d**0.5)/ (2 * a)
        res2 = (-b - d**0.5)/ (2 * a)
    
    return res1, res2


if __name__ == "__main__":
    print(resolution(1, 0, 0))
