class Champ:
    def __init__(self, name, health, range, mana, dmg, movespeed, qCD, wCD, eCD, rCD):
        self.name = name
        self.health = health
        self.range = range
        self.mana = mana
        self.dmg = dmg
        self.movespeed = movespeed
        self.qCD = qCD
        self.wCD = wCD
        self.eCD = eCD
        self.rCD = rCD

    def getName(self):
        return self.name


    def getHp(self):
        return self.health

    def getRange(self):
        return self.range

    def getMana(self):
        return self.mana

    def getDmg(self):
        return self.dmg

    def getMs(self):
        return self.movespeed
    
    def getQCD(self):
        return self.qCD

    def getWCD(self):
        return self.wCD
    
    def getECD(self):
        return self.eCD

    def getRCD(self):
        return self.rCD
    