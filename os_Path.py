
import os

chemin = os.getcwd()
chemin2 = chemin + "\\ficher2.txt"
chemin = chemin + "\\ficher.txt"
print(chemin)
print(chemin2)
print("-"*150)


with open(chemin, "w") as f:
    f.write("Le module write \"w\" écrit dans le fichier et le module read \"r\" le lis")

with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)

with open(chemin, "w") as f:
    f.write("Avec le module \"w\" , write sur un fichier pas vide écrase le contenu.")

with open(chemin, "r") as f:
    contenu = f.read()
    print(contenu)

with open(chemin, "a") as f:
    f.write(" Avec le module \"a\" on ajoute à la fin sans écraser")

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




