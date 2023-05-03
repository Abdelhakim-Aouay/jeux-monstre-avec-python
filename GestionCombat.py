import gestion_degat
import Creation_personnage
import CreationMonstre


def gestionCombat(personne, monstre):
    #CreationMonstre.creationMonstre()
    while personne[1] > 0 and monstre[1] > 0  :# tant que la personne est en
        attaquant = int(input("veuillez choisir l'attaquant:  1 pour personne ou 2 pour monstre"))
        if attaquant == 1: # la personne
            print("la personne attaque")
            monstre[1]= gestion_degat.gestion_des_degats(personne[2],monstre[1], monstre[3])

        elif attaquant == 2:
            print("le monstre attaque")
            #ForceAttaquant,PVDefenseur, ArmureDefenseur
            personne[1] = gestion_degat.gestion_des_degats(monstre[2], personne[1], personne[3])
        print("les points de vie restantes de la personne :" ,personne ) # affichage les points de vie du joueur
        print("les points de vie restantes du monstre :",monstre)  # affichage les points de vie du joueur
    return personne







