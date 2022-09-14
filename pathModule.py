from pathlib import Path

'''chemin dossier utilisateur Path.home()'''
cheminHome = Path.home()
print(cheminHome)

'''chemin dossier courant Path.cwd()'''
chemin = Path.cwd()
print(chemin)

'''Créer un chemin personnalisé -> les anti slash sont géré par la méthode -> Path("") '''
p = Path("c:/Users/Geoffrey/Desktop/PycharmProjects/test")
print(p)

'''Récupérer dossier parent'''
print(p.parent)
print(p.parent.parent.parent)

'''Pour concaténer des chemins on utilise directement le slash'''

p = p.parent / "test2" / "fichier.py"

print(p)

'''On peut aussi utiliser la méthode joinpath()'''

q = p.parent.parent.joinpath("document", "geof", "simple.py")
print(q)

'''Information sur le chemin'''
print(q.name)
print(q.stem)
print(q.suffix)
print(q.suffixes)
print(q.parts)
print(q.exists())
print(q.is_dir())
print(q.is_file())


'''La fonction dir() permet d'obtenir tout ce qui est disponible sur l'objet'''

print(dir(q))








