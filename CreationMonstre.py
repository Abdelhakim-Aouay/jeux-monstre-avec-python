import GénérationMonster
monstre = []
def creationMonstre():
    print("La creation du monstre")
    nomMonstre = input("Enter le nom du monstre:")
    print("Nom du Monstre est: " + nomMonstre)
    monstre = GénérationMonster.generationMonster(nomMonstre)
    return monstre


