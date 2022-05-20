'''Enemy class'''

class Enemy:
    def __init__(self, hp: int, atk: int, affinity: str) -> None:
        self.hp = hp
        self.atk = atk
        self.affinity = affinity
    
    def get_hp(self):
        return self.hp

    def get_atk(self):
        return self.atk

    def get_affinity(self):
        return self.atk

    def set_hp(self, value):
        self.hp -= value

    def attack(self, target):
        target.set_hp(target.get_hp() - self.atk) #we can work on affinity when/e
