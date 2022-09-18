import random
import time
from pathlib import Path


# Définir le chemin du fichier ou on va envoyer à chaque fois les données à envoyer par mail
chemin = Path.cwd()
print(chemin)
chemin = chemin / "abdela.txt"
print(chemin)

# Définir les set pour la suite
set1 = set()
set2 = set()
set3 = set()
listeSend = []

# Lancer la boucle infinie qui va récolter à chaque fonctionnement des infos ou pas
while True:
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 50)
    n3 = random.randint(1, 50)

    # mettre les données dans set1
    set1.update([str(n1), str(n2), str(n3)])
    # faire la différence entre set1 et set2 (attention pas l'inverse)
    set3 = set1.difference(set2)
    # stocker les nouvelles données uniques dans set2
    set2.update(set1)

    #transformer set3 en liste pour pouvoir transformer liste en string pour envoyer dans fichier abdela.txt
    listeSend = list(set3)
    monString = ", ".join(listeSend)
    if monString == "":
        with open(chemin, "a") as f:
            f.write(f"\nPas de nouvelle donnée")
    else:
        with open(chemin, "a") as f:
            f.write(f"\n Envoyer ces données : {monString},")


    print(set1)
    print(set3)
    print(set2)
    set1.clear()

    time.sleep(1)
    if len(set2) == 49:
        break







