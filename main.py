"""Exercice ASCII art"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(1100)

#### Fonctions secondaires


def artcode_i(s):
    """ASCII art algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    n=len(s)
    c=[s[0]]
    o=[1]
    for k in range (1,n):
        if s[k] == s[k-1]:
            o[-1]+= 1
        else:
            c.append(s[k])
            o.append(1)
    return list( zip(c,o))


def artcode_r(s):
    """ASCII art avec algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """

    # votre code ici
    n=len(s)
    # cas de base
    if n==0:
        return[]
    # recherche nombre de caractères identiques au premier
    occ = 1
    while occ<n and s[occ]==s[0]:
        occ+=1
    # appel récursif
    tpl=(s[0],occ)
    return [tpl] + artcode_r(s[occ:])
#### Fonction principale


def main():
    """Fonction principal"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
