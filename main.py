import CreationMonstre,Creation_personnage,GestionCombat
import compteur_ennemi
Nbr_Kill = 0
print ("Jeu de combat")
print ("merci de saisir les données du peronnage")
pseudo = input("nom du personnage: ")
PV = int(input("point de vie pour le personnage: "))
force = int(input ("point de Force: "))
armure = int(input ("point d'armure : "))
personne1 = Creation_personnage.creationPersonnage(pseudo, PV, force, armure)
print("la personne créée :" ,personne1)

monstre1 = CreationMonstre.creationMonstre()
print("Le monstre créé est " ,monstre1)

GestionCombat.gestionCombat(personne1, monstre1)

if personne1[1] == 0 :
    print("vous etes mort, vous n'avez gagné aucun monstre")
else :
    Nbr_Kill = compteur_ennemi.compteur_ennemie_tué(Nbr_Kill)
    print('vous avez tué : ', Nbr_Kill)

while (personne1[1]>0):
    print("vous etes toujours en vie, on va vous créer un nouveau monstre")
    monstre2 = CreationMonstre.creationMonstre()
    print("Le monstre créé est " ,monstre2)
    GestionCombat.gestionCombat(personne1, monstre2)
    if monstre2[1]<=0 :
        Nbr_Kill=compteur_ennemi.compteur_ennemie_tué(Nbr_Kill)
        print('vous avez tué : ', Nbr_Kill)
print('vous êtes mort mais vous avez tué : ',Nbr_Kill)



fichier = open("toto.txt", "w")

pseudo = personne1[0]
fichier.write(pseudo)
fichier.write("  ,  ")

PV = str(personne1[1])
fichier.write(PV)
fichier.write(" ,  ")

force = str(personne1[2])
fichier.write(force)
fichier.write(" ,  ")

force = str(personne1[3])
fichier.write(force)
fichier.write(" ,  ")

fichier.close()

