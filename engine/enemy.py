'''Enemy class'''

class Enemy:
    def __init__(self, hp: int, atk: int, affinity: str) -> None:
        self.hp = hp
        self.atk = atk
        self.affinity = affinity
    
    def getHp(self):
        return self.hp

    def getAtk(self):
        return self.atk

    def getAffinity(self):
        return self.atk

    def setHp(self, value):
        self.hp -= value

    def attack(self, target):
        target.set_hp(target.get_hp() - self.atk) #we can work on affinity when/e
