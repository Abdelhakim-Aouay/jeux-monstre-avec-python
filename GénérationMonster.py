import random

def generationMonster(nom):
    print("génération du monster :" +nom)
    tab = []
    tab.append(nom)
    tab.append(random.randint(5,20)) #PV
    tab.append(random.randint(3,8)) # la force
    tab.append(random.randint(0,5)) #armure
    print(tab)
    return tab


