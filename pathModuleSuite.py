from pathlib import Path
import shutil
p = Path.cwd()
print(p)
p = p / "dossierTest"
print(p)

# 1) créer et supprimer dossier ou fichier

'''
p.mkdir() retourne une erreur si le dossier existe déjà 
donc on place un argument pour palier à ça
'''

p.mkdir(exist_ok=True)

'''Si on veut créer plusieurs dossiers qui n'existent pas en une fois -> utiliser '''
p = p / "1" / "2" / "3"
print(p)

'''Il faut dans ce que cas un deuxième paramètre mkdir(parents=True)'''
p.mkdir(parents=True, exist_ok=True)

'''Pour créer un fichier -> p.touch() et pour supprimer -> '''
p = p / "text.txt"
p.touch()

p.unlink()

'''Pour supprimer dossier rmdir()'''

p = p.parent
print(p)
p.rmdir()

'''Si à ce stade je veux supprimer un dossier qui n'est pas vide -> il faut utiliser shutil'''

p = p.parent.parent.parent
print(p)
shutil.rmtree(p)

# 1) lire et écrire dans un fichier

l = Path.cwd()
l = l / "fichier.txt"
print(l)
l.write_text("Ajout avec le module Path")
print(l.read_text())


'''Scaner un dossier'''

dossier = Path.home()
for i in dossier.iterdir():
    print(i)

for i in dossier.iterdir():
    print(i.name)

'''Récupérer les dossiers '''


recupDossier = [f for f in Path.home().iterdir() if f.is_dir()]
print(recupDossier)

recupFichier = [f for f in Path.home().iterdir() if f.is_file()]
print(recupFichier)

'''la méthode globe et rglobe permettent de récupérer tout ce qu'on spécifie dans un dossier'''

d = Path.home() / "Downloads"
print(d)

for i in d.glob("*.pdf"):
    print(i.name)

# ou rglobe()

for i in d.rglob("*.pdf"):
    print(i.name)

# changer le nom d'un fichier

nom = Path("user/geoffrey/documents/main.py")
print(nom)

nomChange = nom.parent / (nom.stem + "_test" + nom.suffix)
print(nomChange)
