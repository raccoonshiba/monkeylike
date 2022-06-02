'''Enemy class'''

class Enemy:#contains all important information about enemy
    def __init__(self, hp: int, atk: int, affinity: str) -> None:# hp, atk, affinity
        self.hp = hp
        self.atk = atk
        self.affinity = affinity
    
    def getHp(self):# return hp
        return self.hp

    def getAtk(self):# return atk
        return self.atk

    def getAffinity(self):# return affinity
        return self.atk

    def setHp(self, value):# set hp
        self.hp = value

    def attack(self, target):# attack target
        target.set_hp(target.get_hp() - self.atk) #we can work on affinity when/e
