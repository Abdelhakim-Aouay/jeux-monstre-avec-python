def gestion_des_degats(ForceAttaquant, PVDefenseur, ArmureDefenseur):
    if ArmureDefenseur > ForceAttaquant:
        return PVDefenseur - 1
    else:
        PVDefenseur = PVDefenseur - (ForceAttaquant - ArmureDefenseur)
        print("le point de vie de defenseur est : ", PVDefenseur)
        return PVDefenseur
