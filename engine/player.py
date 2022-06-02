'''Player / Monster defined as characters'''
import pygame

class Player:# Player class
    def __init__(self):# hp, atk, defense, affinity
        self.hp = 10
        self.max_hp = 10
        self.xp = 1
        self.level = 1
        self.inventory = {
            'armour': {
                'stat': 1,
                'affinity': '' #we dont have to implement this idrc
            },
            'weapon': {
                'stat': 1,
                'affinity': '' #would be nice to implement this though since monkeytype (HAHA) matters more
            },
            'potion': 0 #integer for how much hp gets restored
        }

    def getHp(self):# return hp
        return self.hp

    def getMaxHp(self):# return max hp
        return self.max_hp()

    def getAtk(self):
        return self.inventory['weapon']['stat']

    def getDef(self):
        return self.inventory['armour']['stat']

    def getWeaponAffinity(self):
        return self.inventory['armour']['affinity']

    def usePotion(self):
        pass

    
    def setArmour(self, stat, affinity):
        self.inventory['armour']['stat'] = stat
        self.inventory['armour']['affinity'] = affinity

    def setWeapon(self, stat, affinity):
        self.inventory['weapon']['stat'] = stat
        self.inventory['weapon']['affinity'] = affinity

    def setPotion(self, stat):
        self.ivnentory['potion'] = stat