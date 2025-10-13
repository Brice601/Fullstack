import random

# Lire le fichier et créer une liste propre
with open('noms.txt', 'r', encoding='utf-8') as f:
    contenu = f.read()
    
# Séparer sur les espaces, tabs, retours à la ligne
noms = contenu.split()

# Afficher le résultat
# print(noms)


# Mélanger aléatoirement
random.shuffle(noms)

# Créer des groupes de 3 personnes
taille_groupe = 3
groupes = [noms[i:i+taille_groupe] for i in range(0, len(noms), taille_groupe)]

# Afficher les groupes
for i, groupe in enumerate(groupes, 1):
    print(f"Groupe {i}: {', '.join(groupe)}")