
import os

chemin = os.getcwd()
chemin3 = chemin + "\\fichierUdemy.txt"
chemin2 = chemin + "\\fichier2.txt"
chemin = chemin + "\\fichier.txt"
print(chemin)
print(chemin2)
print(chemin3)
print("-"*150)


with open(chemin, "w") as f:
    f.write("Le module write \"w\" écrit dans le fichier et le module read \"r\" le lis")

with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)

with open(chemin, "w") as f:
    f.write("Avec le module \"w\" : \nwrite sur un fichier pas vide écrase le contenu.")

with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)
print("-*"*150)
with open(chemin, "a") as f:
    f.write(" \nAvec le module \"a\" : \non ajoute à la fin sans écraser")

with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)


# voici une façon de faire qui oblige la fermeture mais laisse l'espace de travail ouvert
print("-"*150)

f = open(chemin2, "w")
f.write("Hello world!")


f = open(chemin2, "r")
contenu2 = f.read()
print(contenu2)


f = open(chemin2, "a")
f.write("  Avec cette solution, c'est moins lourd à écrire qu'avec la méthode with mais "
        "il faut bien faire un f.close() à la fin sinon on a des problèmes")

f = open(chemin2, "r")
contenu2 = f.read()
print(contenu2)

f.close()

# Les différentes méthodes
print("-"*150)

with open(chemin3, "r") as f:
    contenu3 = f.read()
    print(contenu3)

#pour que ce soit en une phrase -> fct repr()

with open(chemin3, "r") as f:
    contenu3 = repr(f.read())
    print(contenu3)

# pour récupérer une liste -> f.readlines()

with open(chemin3, "r") as f:
    contenu3 = f.readlines()
    print(contenu3)

# si on ne veut pas le \n de retour à la ligne dans les méthodes précédentes on peut faire ça
#  contenu3 = f.read().splitlines() -> il sépare le str sur \n

with open(chemin3, "r") as f:
    contenu3 = f.read().splitlines()
    print(contenu3)

contenu4 = "texte\ntexte"
print(contenu4)
contenu4 = "texte\ntexte".splitlines()
print(contenu4)

'''La méthode f.seek() pour replacer le curseur si jamais on lis plusieurs fois (ou certain élément)'''

f = open(chemin3, "r")
print(f.read())
f.seek(6)
contenuChemin3 = f.read()
print(contenuChemin3)
f.close()
