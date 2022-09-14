import os
import json
chemin = os.getcwd()
chemin = chemin + "\\fichierJson.txt"
print(chemin)

with open(chemin, "w") as f:
    json.dump("Bonjour", f, indent=4)

with open(chemin, "r") as f:
    contenu = json.load(f)
    print(contenu)

with open(chemin, "w") as f:
    json.dump(list(range(5)), f, indent=4)

with open(chemin, "r") as f:
    contenu2 = json.load(f)
    print(contenu2)

'''Pour ajouter du contenu dans cette dernière liste json qui va de 0 à 4 on ne peut pas
simplement utiliser le mode a avec json.dump()
- Il faut extraire la liste du json
- modifier la liste en tant que liste
- remettre cette liste dans le json en écrasant avec le mode w'''

with open(chemin, "r") as f:
    listeJson = json.load(f)

listeJson.append(5)
print(listeJson)

with open(chemin, "w") as f:
    json.dump(listeJson, f, indent=4)

with open(chemin, "r") as f:
    listeJsonModif = json.load(f)
    print(listeJsonModif)

