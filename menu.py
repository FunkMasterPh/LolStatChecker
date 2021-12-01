

def printMenu(champ1, champ2):
    print(f"\n{champ1.getName()}\t\t\t\t{champ2.getName()}\n")
    print(f"Health:\t{champ1.getHp()}\t\t\tHealth:\t{champ2.getHp()}")
    print(f"Range:\t{champ1.getRange()}\t\t\tRange:\t{champ2.getRange()}")
    print(f"Mana:\t{champ1.getMana()}\t\t\tMana:\t{champ2.getMana()}")
    print(f"Damage:\t{champ1.getDmg()}\t\t\tDamage:\t{champ2.getDmg()}")
    print(f"Speed:\t{champ1.getMs()}\t\t\tSpeed:\t{champ2.getMs()}")
    print(f"Q CD:\t{champ1.getQCD()}\tQ CD:\t{champ2.getQCD()}")
    print(f"W CD:\t{champ1.getWCD()}\tW CD:\t{champ2.getWCD()}")
    print(f"E CD:\t{champ1.getECD()}\tE CD:\t{champ2.getECD()}")
    print(f"R CD:\t{champ1.getRCD()}\t\tR CD:\t{champ2.getRCD()}\n")